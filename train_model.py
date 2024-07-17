from ultralytics import YOLO

# Load a model
model= YOLO("yolov8n.yaml") 

# Use the model
results = model.train(data="C:/Users/jeeva/OneDrive/Documents/YOLO/config.yaml", epochs=100) 