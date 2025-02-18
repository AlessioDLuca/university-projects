README

The notebook works both in colab and kaggle. If you want to run the notebook on colab, make sure you run the "Kaggle function to run on colab", since it was imported from kaggle. Also it is recomended to run the Notebook on kaggle, when doing so, make sure that after importing the notebook you have the Airbus Ship Detection Challenge in the input cell on the right of the screen, since from there we will import the images and csv file. link to the challenge: https://www.kaggle.com/competitions/airbus-ship-detection

The Data Processing part works complitely using cpu, however the Segmentation part requires GPU for faster training and validation of the model. To access GPU on kaggle just create and verify your account.

To use exactly the model that I used in the dashboard, download the model weights "ResNet101.pth" inside the "DashboardStreamlit" folder, and run the cell under the model definition, this way you can also skip the train and validation section, which also allows you to run everything without GPU.