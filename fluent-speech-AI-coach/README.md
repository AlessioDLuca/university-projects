# 🎤 Fluent Speech AI Coach  

## 📃 Project Overview  
The **Fluent Speech AI Coach** is an **AI-powered pronunciation and fluency evaluation tool** designed to help users improve their speech clarity. It allows users to **record their speech**, compare it against a **reference audio**, and receive feedback on **pronunciation, fluency, and pause management** using **deep learning models**.

The project is built using **Streamlit**, leveraging **Whisper for speech-to-text transcription**, **Silero VAD for voice activity detection**, and **FastDTW for pronunciation evaluation**.

---

## 🔍 Features  
- **Generate reference audio** from a text input.
- **Record speech** and process it (removing silence & noise).
- **Transcribe speech** using OpenAI's **Whisper**.
- **Evaluate pronunciation, fluency, and pauses**.
- **Streamlit dashboard** for easy interaction.

---

## 🛠️ How to Run  
### **1️⃣ Setup the Environment**  
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### **2️⃣ Run the Streamlit App**  
```bash
streamlit run app.py
```

- **Note**: The generated audio files are saved in the same folder as `app.py`.
- **Legacy Notebook**: `LearningBot.ipynb` is an older version of the app, included to show project progression.

---

## 📊 Evaluation Metrics  
### 🎧 **Pronunciation Analysis**  
- Uses **Dynamic Time Warping (DTW)** to compare recorded speech to reference audio.
- **Feedback categories**:
  - 🌟 **Excellent**: Near-perfect pronunciation.
  - 👍 **Great**: Minor mispronunciations.
  - 👌 **Good**: Some inaccuracies.
  - ⚠️ **Needs improvement**: Noticeable pronunciation issues.
  - ❌ **Unclear pronunciation**: Significant errors.

### ⏳ **Fluency Analysis**  
- Measures **Words Per Minute (WPM)** and compares it to the reference speed.
- Suggests **adjustments** for optimal speaking pace.
- **Feedback categories**:
  - ✅ **Perfect**: Ideal pace.
  - 👍 **Almost perfect**: Slight adjustments needed.
  - ⚠️ **Suboptimal pace**: Work on speed.
  - ❌ **Too fast or too slow**: Major improvements required.

### 🎤 **Pause Management**  
- Evaluates **pause frequency and duration**.
- **Feedback categories**:
  - 🌟 **Excellent**: Well-distributed pauses.
  - 👍 **Good**: Minor issues.
  - 👌 **Acceptable**: Needs slight improvements.
  - ⚠️ **Unnatural pauses**: Disrupts speech flow.
  - ❌ **Incorrect pauses**: Needs major corrections.

### 📊 **Overall Score**  
- Weighted combination of **Pronunciation (40%)**, **Fluency (35%)**, and **Pauses (25%)**.
- Final evaluation:
  - 🌟 **Excellent**: Very natural speech.
  - 👍 **Good**: Room for improvement.
  - 👌 **Sufficient**: Can be improved.
  - ❌ **Needs improvement**: Requires further training.

---

## 🎨 Future Work  
- **Enhance pronunciation analysis** using phoneme-based models.
- **Improve fluency detection** with real-time feedback.
- **Expand language support** beyond **English and Italian**.

---
