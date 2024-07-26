from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load the trained YOLOv8 model
model = YOLO('C:/Users/uidp9675/Documents/GitHub/YOLOv8_Dripping_Detection/runs/detect/train2/weights/last.pt')

# Function to run inference on a single image
def predict_and_visualize(image_path):
    # Load image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for displaying with matplotlib
    
    # Perform inference
    results = model(image_rgb)

    # Plot the image with detections
    for result in results:
        #Plot method in YOLOv8
        plt.figure(figsize=(10, 10))
        plt.imshow(result.plot())
        plt.axis('off')
        plt.show()


# Test on a new image
predict_and_visualize('C:/Users/uidp9675/Documents/GitHub/YOLOv8_Dripping_Detection/YOLO-Train_dataset/YOLO-Train_dataset/images/Exp_April_13_5_2.jpg')
