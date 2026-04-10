from ultralytics import YOLO
import multiprocessing
import os

def train_model():
    # Force it to use the EXACT file in your folder
    # This prevents the library from looking for 'newer' versions online
    model_path = os.path.join(os.getcwd(), "yolo11s.pt")
    model = YOLO(model_path)

    model.train(
        data="<file path to data.yaml>",  # Absolute file path of data.yaml, that can be found in data set folder 
        epochs=100,
        imgsz=512,  # Image dimension
        device=0,   # This uses your GPU if available otherwise uses CPU to train the YOLO model on data set   
        batch=16,      
        workers=2,     
        plots=True,
        exist_ok=True # This tells YOLO to overwrite/ignore folder conflicts
    )

if __name__ == '__main__':
    multiprocessing.freeze_support() # Due to the lack of native folk() system file, this code can run endlessly causing system crash to prevent that freeze_support() function is used
    train_model()
