import streamlit as st
from audio_recorder_streamlit import audio_recorder
import librosa
import numpy as np
from gtts import gTTS
import soundfile as sf
import torch
import os
import whisper
import difflib

# Additional imports for evaluation functions
from fastdtw import fastdtw
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(page_title="Fluent Speech Coach", layout="wide")
st.title("Fluent Speech Coach")
st.write(
    "This dashboard allows you to generate reference audio from text, record your version, process it (removing initial/final silence), transcribe it using Whisper, and evaluate your reading in terms of pronunciation, fluency, and pause management."
)

# ---------------------------
# Language Selection
# ---------------------------
language = st.selectbox("Select language", options=["English", "Italian"])
lang_code = "en" if language == "English" else "it"

# ---------------------------
# Text Input & Reference Audio Creation
# ---------------------------
original_text = st.text_area("Enter the text you want to read: (CTRL+Enter to save text)")

if original_text:
    # Create a styled HTML box for the text
    text_box = f"""
    <div style="
        border: 3px solid black;
        padding: 15px;
        width: 80%;
        max-height: 200px;
        overflow-y: auto;
        background-color: white;
        font-family: Arial, sans-serif;
        font-size: 16px;
        color: black;
        line-height: 1.5;
        text-align: justify;
        ">
        {original_text}
    </div>
    """
    st.markdown("**📖 Text to read:**")
    st.markdown(text_box, unsafe_allow_html=True)

    # Generate the reference audio using gTTS
    tts = gTTS(text=original_text, lang=lang_code, slow=False)
    reference_file = "reference.wav"
    tts.save(reference_file)
    st.success("🎵 Reference audio created!")

    # Display the reference audio player
    with open(reference_file, "rb") as f:
        reference_audio_bytes = f.read()
    st.markdown("**🎵 Listen to the reference audio:**")
    st.audio(reference_audio_bytes, format="audio/wav")


# ---------------------------
# Record Your Voice with audio_recorder_streamlit
# ---------------------------
st.markdown("**🎙️ Record your version:**")
st.info("Click the 🎙️ to start and to finish recording.")

audio_bytes = audio_recorder(
    text="Click to record",
    pause_threshold=10.0,
)

if audio_bytes is not None:
    st.audio(audio_bytes, format="audio/wav")
    st.success("Audio recorded successfully!")

    # Save the recorded audio to a file for processing
    student_file = "student.wav"
    with open(student_file, "wb") as f:
        f.write(audio_bytes)

    # ---------------------------
    # Load Silero VAD Model
    # ---------------------------
    st.info("Loading Silero VAD model...")

    @st.cache_resource(show_spinner=False)
    def load_silero_model():
        model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                                      model='silero_vad',
                                      source='github')
        return model, utils

    model_vad, utils = load_silero_model()
    get_speech_timestamps, _, _, _, _ = utils

    # ---------------------------
    # Audio Processing Functions
    # ---------------------------
    def get_speech_segment(audio, sr):
        """Use Silero VAD to detect the beginning and end of speech."""
        audio_tensor = torch.tensor(audio, dtype=torch.float32)
        speech_timestamps = get_speech_timestamps(audio_tensor, model_vad, sampling_rate=sr)
        if not speech_timestamps:
            return audio  # Return the original audio if no speech is detected
        start_sample = speech_timestamps[0]['start']
        end_sample = speech_timestamps[-1]['end']
        return audio[start_sample:end_sample]

    def trim_silence(input_file, output_file='student_processed_vad.wav'):
        """Remove initial and final silence using librosa and Silero VAD."""
        audio, sr = librosa.load(input_file, sr=16000)
        audio_trimmed, _ = librosa.effects.trim(audio, top_db=25)
        audio_final = get_speech_segment(audio_trimmed, sr)
        sf.write(output_file, audio_final, sr)
        return output_file

    # Process the recorded audio
    processed_file = trim_silence(student_file)
    st.markdown("**🎵 Processed audio (without initial/final silence):**")
    with open(processed_file, "rb") as f:
        processed_audio_bytes = f.read()
    st.audio(processed_audio_bytes, format="audio/wav")

    # ---------------------------
    # Load Whisper Model
    # ---------------------------
    st.info("Loading Whisper model...")

    @st.cache_resource(show_spinner=False)
    def load_whisper_model():
        MODEL_SIZE = "small"  # Change to "medium" or "large" for higher accuracy if needed
        model = whisper.load_model(MODEL_SIZE)
        return model, MODEL_SIZE

    MODEL, MODEL_SIZE = load_whisper_model()
    st.success(f"Whisper model '{MODEL_SIZE}' loaded successfully!")

    # ---------------------------
    # Define Transcription Function using Whisper
    # ---------------------------
    def transcribe_audio(file_audio):
        st.info("Transcribing audio...")
        # Load the audio using librosa
        audio_data, sr = librosa.load(file_audio, sr=16000)
        # Pass the raw audio (as a NumPy array) to the model
        result = MODEL.transcribe(audio_data, language=lang_code)
        return result['text']

    # Transcribe the processed audio
    st.markdown("**🎯 Transcription with Whisper...**")
    transcribed_text = transcribe_audio(processed_file)
    st.markdown("=" * 50)
    st.markdown(f"**Original Text:** {original_text}")
    st.markdown(f"**Transcribed Text:** {transcribed_text}")
    st.markdown("=" * 50)

    # Calculate the transcription accuracy percentage
    precision = difflib.SequenceMatcher(
        None,
        original_text.lower().strip(),
        transcribed_text.lower().strip()
    ).ratio() * 100
    st.markdown(f"**📊 Reading Accuracy:** {precision:.1f}%")

    # If accuracy is below 90%, do not proceed further
    if precision < 90:
        st.error("❌ Your reading is not accurate enough. Please try reading more clearly.")
        st.stop()

    # ---------------------------
    # Evaluation Functions
    # ---------------------------

    # 1. Pronunciation Evaluation
    def calculate_pronunciation(reference_audio, student_audio):
        ref_audio, sr_ref = librosa.load(reference_audio, sr=16000)
        stu_audio, sr_stu = librosa.load(student_audio, sr=16000)

        ref_mfcc = librosa.feature.mfcc(y=ref_audio, sr=sr_ref, n_mfcc=13).T
        stu_mfcc = librosa.feature.mfcc(y=stu_audio, sr=sr_stu, n_mfcc=13).T

        scaler = StandardScaler()
        ref_mfcc_norm = scaler.fit_transform(ref_mfcc)
        stu_mfcc_norm = scaler.transform(stu_mfcc)

        distance, path = fastdtw(ref_mfcc_norm, stu_mfcc_norm, dist=euclidean)
        normalized_distance = distance / len(path)

        if normalized_distance < 4.5:
            pronunciation_score = 5
            feedback = "🌟 Excellent! Perfect pronunciation!"
        elif normalized_distance < 5:
            pronunciation_score = 4
            feedback = "👍 Great pronunciation, only minor imperfections."
        elif normalized_distance < 5.5:
            pronunciation_score = 3
            feedback = "👌 Good pronunciation, but there are some inaccuracies."
        elif normalized_distance < 6:
            pronunciation_score = 2
            feedback = "⚠️ Acceptable pronunciation, but improvements are needed."
        else:
            pronunciation_score = 1
            feedback = "❌ Unclear pronunciation, needs significant work."

        return pronunciation_score, feedback, distance, normalized_distance


    def analyze_fluency(student_audio, original_text, reference_audio):
        # Load the reference audio and compute its duration and WPM
        ref_audio, sr_ref = librosa.load(reference_audio, sr=16000)
        ref_duration = librosa.get_duration(y=ref_audio, sr=sr_ref)
        total_words = len(original_text.split())
        ref_wpm = (total_words / ref_duration) * 60
        ref_wpm_rounded = round(ref_wpm)

        # Load the student's audio and compute its duration and WPM
        stu_audio, sr_stu = librosa.load(student_audio, sr=16000)
        stu_duration = librosa.get_duration(y=stu_audio, sr=sr_stu)
        stu_wpm = (total_words / stu_duration) * 60
        stu_wpm_rounded = round(stu_wpm)

        # Calculate the time difference (in seconds) between the reference and student durations
        time_adjustment = ref_duration - stu_duration

        if stu_wpm < ref_wpm:
            speed_feedback = "Too slow."
            adjustment_text = f"💡 You should speed up by about {abs(time_adjustment):.1f} s."
        else:
            speed_feedback = "Too fast."
            adjustment_text = f"💡 You should slow down by about {abs(time_adjustment):.1f} s."

        # Define evaluation thresholds based on the reference WPM
        perfect_lower = ref_wpm * 0.9
        perfect_upper = ref_wpm * 1.1
        almost_lower = ref_wpm * 0.85
        almost_upper = ref_wpm * 1.15
        acceptable_lower = ref_wpm * 0.8
        acceptable_upper = ref_wpm * 1.2
        suboptimal_lower = ref_wpm * 0.75
        suboptimal_upper = ref_wpm * 1.25

        if perfect_lower <= stu_wpm <= perfect_upper:
            fluency_score = 5
            feedback = f"✅ Perfect! Ideal pace ({stu_wpm_rounded} WPM)."
            adjustment_text = "No adjustment needed."
        elif (almost_lower <= stu_wpm < perfect_lower) or (perfect_upper < stu_wpm <= almost_upper):
            fluency_score = 4
            feedback = f"👍 Almost perfect ({stu_wpm_rounded} WPM). Minor adjustments needed."
        elif (acceptable_lower <= stu_wpm < almost_lower) or (almost_upper < stu_wpm <= acceptable_upper):
            fluency_score = 3
            feedback = f"👌 Acceptable ({stu_wpm_rounded} WPM). Consider slight adjustments."
        elif (suboptimal_lower <= stu_wpm < acceptable_lower) or (acceptable_upper < stu_wpm <= suboptimal_upper):
            fluency_score = 2
            feedback = f"⚠️ Suboptimal pace ({stu_wpm_rounded} WPM). Work on your pace."
        else:
            fluency_score = 1
            feedback = f"❌ {speed_feedback} ({stu_wpm_rounded} WPM)."

        return fluency_score, feedback, round(ref_wpm), stu_wpm_rounded, adjustment_text


    # 3. Pause Analysis
    def analyze_pauses(reference_audio, student_audio):
        ref_audio, sr_ref = librosa.load(reference_audio, sr=16000)
        stu_audio, sr_stu = librosa.load(student_audio, sr=16000)

        ref_intervals = librosa.effects.split(ref_audio, top_db=30)
        stu_intervals = librosa.effects.split(stu_audio, top_db=30)

        num_pauses_ref = len(ref_intervals) - 1
        num_pauses_student = len(stu_intervals) - 1

        pause_durations_ref = [(ref_intervals[i+1][0] - ref_intervals[i][1]) / sr_ref for i in range(num_pauses_ref)]
        pause_durations_student = [(stu_intervals[i+1][0] - stu_intervals[i][1]) / sr_stu for i in range(num_pauses_student)]

        avg_pause_ref = np.mean(pause_durations_ref) if pause_durations_ref else 0
        avg_pause_student = np.mean(pause_durations_student) if pause_durations_student else 0

        pause_diff = abs(num_pauses_ref - num_pauses_student)
        pause_duration_diff = abs(avg_pause_ref - avg_pause_student)

        if pause_diff <= 1 and pause_duration_diff < 0.3:
            pause_score = 5
            feedback = "🌟 Excellent rhythm! Natural and well-distributed pauses."
        elif pause_diff <= 2 and pause_duration_diff < 0.4:
            pause_score = 4
            feedback = "👍 Good rhythm, with minor differences in pauses."
        elif pause_diff <= 3 and pause_duration_diff < 0.6:
            pause_score = 3
            feedback = "👌 Acceptable rhythm, room for improvement."
        elif pause_diff <= 4 and pause_duration_diff < 0.8:
            pause_score = 2
            feedback = "⚠️ Unnatural pauses, improvement needed."
        else:
            pause_score = 1
            feedback = "❌ Incorrect pauses, needs review."

        return pause_score, feedback, num_pauses_ref, num_pauses_student, pause_diff, avg_pause_ref, avg_pause_student, pause_duration_diff

    # 4. Overall Evaluation
    def calculate_overall_score(pron_score, fluency_score, pause_score):
        WEIGHT_PRON = 0.40
        WEIGHT_FLUENCY = 0.35
        WEIGHT_PAUSES = 0.25

        overall_score = (
            (pron_score * WEIGHT_PRON) +
            (fluency_score * WEIGHT_FLUENCY) +
            (pause_score * WEIGHT_PAUSES)
        )

        if overall_score >= 4.5:
            final_evaluation = "🌟 Excellent! Very clear and natural speech."
        elif overall_score >= 3.5:
            final_evaluation = "👍 Good level, with room for improvement."
        elif overall_score >= 2.5:
            final_evaluation = "👌 Sufficient, but can be improved."
        else:
            final_evaluation = "❌ Needs improvement."

        return overall_score, final_evaluation

    # ---------------------------
    # Display Evaluation Results (in tables)
    # ---------------------------
    st.markdown("## Detailed Speech Evaluation")

    ### 1. Pronunciation
    pron_score, pron_feedback, dtw_value, normalized_value = calculate_pronunciation(reference_file, processed_file)
    pronunciation_table = f"""
    | Metric                          | Value                          |
    |---------------------------------|--------------------------------|
    | DTW Distance                    | {dtw_value:.2f}                |
    | Normalized Distance per Frame   | {normalized_value:.2f}         |
    | **Pronunciation Score**         | **{pron_score}/5**             |
    | Feedback                        | {pron_feedback}                |
    """
    st.markdown("### Pronunciation Evaluation")
    st.markdown(pronunciation_table)

    ### 2. Fluency
    fluency_score, fluency_feedback, ref_wpm, wpm_actual, adjustment_text = analyze_fluency(processed_file,
                                                                                            original_text,
                                                                                            reference_file)

    fluency_table = f"""
    | Metric                    | Value                                      |
    |---------------------------|--------------------------------------------|
    | Reference Speed (WPM)     | {ref_wpm} WPM                              |
    | Actual Speed (WPM)        | {wpm_actual} WPM                           |
    | Fluency Feedback          | {fluency_feedback}                         |
    | **Fluency Score**         | **{fluency_score}/5**                      |
    | Adjustment                | {adjustment_text}                          |
    """

    st.markdown("### Fluency Evaluation")
    st.markdown(fluency_table)

    ### 3. Pause Analysis
    pause_score, pause_feedback, num_pauses_ref, num_pauses_student, pause_diff, avg_pause_ref, avg_pause_student, pause_duration_diff = analyze_pauses(reference_file, processed_file)
    pause_table = f"""
    | Metric                                        | Value                           |
    |-----------------------------------------------|---------------------------------|
    | Number of Pauses (Reference)                  | {num_pauses_ref}                |
    | Number of Pauses (Student)                    | {num_pauses_student}            |
    | Difference in Number of Pauses                | {pause_diff}                   |
    | Average Pause Duration (Reference)            | {avg_pause_ref:.2f} s            |
    | Average Pause Duration (Student)              | {avg_pause_student:.2f} s        |
    | Difference in Average Pause Duration          | {pause_duration_diff:.2f} s       |
    | **Pause Management Score**                    | **{pause_score}/5**             |
    | Pause Feedback                                | {pause_feedback}                |
    """
    st.markdown("### Pause Analysis")
    st.markdown(pause_table)

    ### 4. Overall Evaluation
    overall_score, overall_feedback = calculate_overall_score(pron_score, fluency_score, pause_score)
    overall_table = f"""
    | Metric                    | Value                           |
    |---------------------------|---------------------------------|
    | **Overall Score**         | **{overall_score:.2f}/5**        |
    | Overall Feedback          | {overall_feedback}              |
    """
    st.markdown("### Overall Evaluation")
    st.markdown(overall_table)
