import cv2
import torch
from ultralytics import YOLO
import time

def main():

    # 1. Check if CUDA (GPU) is available
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"🚀 Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        print("⚠️ GPU not found, falling back to CPU. Check your drivers!")

    # 2. Load the model and move it to the device
    model = YOLO(r"<File path to best.pt>").to(device) # Enter the file path to best.pt that can be found in ...\runs\detect\train\weights\best.pt
 
    # 3. Open the video
    video_path = r"<videos file path to test>.mp4"
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():

        success, frame = cap.read()
        if not success:
            break

        if frame is None or frame.size == 0:
            print("Warning: Received an empty frame. Skipping this iteration...")
            continue # Skip to the next loop iteration

        # 4. Run inference with Half Precision (FP16) 

        frame = frame[65:795, 695:1225] # try to keep the frame of video as concise as area of Area for better results 

        results = model.predict(
            source=frame, 
            device=device, 
            half=True, 
            imgsz=512, 
            conf=0.4, 
            verbose=False
        )

        # 5. Visualize
        annotated_frame = results[0].plot()

        img = cv2.resize(annotated_frame, (0, 0), fx=0.8, fy=0.8) # Resize for better display

        cv2.imshow("Clash Royole", img)
        
        if cv2.waitKey(1) & 0xFF == ord(' '): # It can pause and resume the detection for analysis of mAP@
            cv2.imshow("Clash Royole", img)
            cv2.waitKey(0)
                
       # 6. End
        if cv2.waitKey(1) & 0xFF == ord('q'): # It will end the programe when pressed 'q'
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
