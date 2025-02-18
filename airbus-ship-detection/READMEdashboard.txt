The dashboard works on PyCharm by running the "main" file. Make sure you download the model and write the correct path to it when loading it (line 105). You can use any image you want, I've put a folder "DashboardImages", with some random test images downloaded directly from here: https://www.kaggle.com/competitions/airbus-ship-detection/data?select=test_v2 

Note that the model is trained only on images similar to the ones I've uploaded, so if you use complitely different images (such as a family having dinner) you will probably get some random ships detected since the model isn't trained that way.

Download the Whole DashboardStreamlit folder. When opening main.py, open it as a project inside that same folder (if asked).
