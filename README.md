# Clash-Royale-Computer-Vision-Bot

# 🛡️ Project Argus: Neural Game Automation
> Teaching AI to play Clash Royale through real-time object detection and tactical actuation.

Project Argus is an end-to-end computer vision agent developed to automate strategic decision-making in mobile gaming environments. This project focuses on high-speed troop detection, coordinate translation, and automated deployment logic.

# 🛡️ Project Argus: Neural Game Automation
> Teaching AI to play Clash Royale through real-time object detection and tactical actuation.

Project Argus is an end-to-end computer vision agent developed to automate strategic decision-making in mobile gaming environments. This project focuses on high-speed troop detection, coordinate translation, and automated deployment logic.

### 🎥 Demo
![Project Demo](demo.gif)


### 🧠 Core Architecture
- **The Eye (Vision):** A custom-trained **YOLOv11** model capable of identifying 26 unique troop classes in real-time.
- **The Muscle (Actuator):** A Python-based automation layer that translates detected object coordinates into precise emulator inputs.
- **The Pipeline:** Integrates PyTorch for inference and OpenCV for frame-by-frame image processing.

### 📊 Dataset & Training
The model was trained on a curated dataset to ensure robustness against varying background noise and deployment animations.
- **Platform:** [Roboflow Universe](https://universe.roboflow.com/srijan-80rmd/cr_dataset/6)
- **Volume:** 508 annotated frames (270 base images + data augmentation)
- **Classes:** 26 distinct unit archetypes.

### 🛠️ Tech Stack
- **Languages:** Python 3.13
- **ML Frameworks:** Ultralytics (YOLOv11), PyTorch
- **Vision:** OpenCV
- **Tools:** Roboflow (Data Management), Git

### 🚀 Getting Started
1. Clone the repository: `git clone https://github.com/Gonenza9090/Clash-Royale-Computer-Vision-Bot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the agent: `python src/main.py`

### Results
    Metric   	        Value
1.  mAP50	            0.986
2.  mAP50-95	        0.769
3.  Validation        set	16 images, 125 object instances
4.  Model	            YOLO11s (9.4M parameters), trained for 100 epochs at 512 pixels
5.  Inference speed	  5.8 ms per image (plus 0.5 ms preprocessing and 1.0 ms postprocessing), measured on the validation set with an RTX 4050 Laptop GPU

### 📖 Notes on use

This is an educational project. Automating a game can break its terms of service, so do not run it on a live or ranked account. It is not affiliated with Supercell, and the game and its artwork belong to their owners.

### 🔗 About

*Built by Srijan Kumar Samrat as a self-taught computer vision project*
*Developed during a self-directed gap year to explore the intersection of Machine Learning and Robotics.*

