from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
results = model.track(source= 'http://127.0.0.1:5000/video',stream =True, show= True, tracker="bytetrack.yaml")
for r in results:
    # boxes = r.boxes  # Boxes object for bbox outputs
    # masks = r.masks  # Masks object for segment masks outputs
    # probs = r.probs  # Class probabilities for classification outputs
    # print(boxes, masks, probs)
    pass