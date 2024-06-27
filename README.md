# YOLO_Dripping_Detection
 A repository used for detecting dripping during laser aided additive manufacturing.

 ### Installation:

```
pip install ultralytics

```

### Requirement:

Python Version 3.7 or higher

### Files contained:

1.  **YOLO-Train_dataset** - This folder contains the **images** folder and **labels** folder containing the images and their respective annotations.
2.  **YOLO-test** - This folder contains two folders **YOLO-test** and **YOLO-train.** The **YOLO-test folder** contains all the original images which is unfiltered and not prepped for the model to train on. The **YOLO-train folder** contains the images which is filtered through and prepped for training the model.
3.  **runs -** This folder is created by YOLOv8 and contains the weights and various results of the trained model.

### Documentation:

1.  Data includes 7 subfolders of their respective classes and three of them are grouped under the common label "Dripping"
2.  Sort through the mismatched images and put them in their respective class folders
3.  Annotate the images with bounding boxes of their respective class using [cvat.ai](http://cvat.ai) The classes are as follows: Dripping, Laser-Off, Lack of Fusion, Non-Defective, Overheating
4.  Export the annotation which reveals a folder containing text files with names matching that of their respective images
5.  Create a folder specifically for training and within this folder create two folders named "**images**" and "**labels**" **Note**: The names of "**images**" and "**labels**" must remain as such and should not be changed as it is used as such by YOLOv8
6.  Place all images required for training within the **images** folder and text files containing the annotations within the **labels** folder
7.  At the home directory, create a **config.yaml** file and input the following code:

```
# Input the respective paths according to your directory
path : path/to/training_dataset_folder
train : path/to/images_folder
val : path/to/images_folder

# Class names
nc : 5
names: ['Dripping', 'Laser-Off', 'Lack of Fusion', 'Non-Defective', 'Overheating']

```

8.  At the home directory, create a python and folder and input the following code:

```
# import YOLO from the ultralytics library
from ultralytics import YOLO

# Load a model
model= YOLO("yolov8n.yaml") # Using the Nano model

# Train the model
results = model.train(data="path/to/config.yaml", epochs=10) # Input path to config.yaml

```

9.  Run the model

### References:

1.  <https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide>
2.  <https://github.com/ultralytics/ultralytics>
