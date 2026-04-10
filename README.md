# Clash-Royale-Computer-Vision-Bot

# 🛡️ Project Argus: Neural Game Automation
> Teaching AI to play Clash Royale through real-time object detection and tactical actuation.

Project Argus is an end-to-end computer vision agent developed to automate strategic decision-making in mobile gaming environments. This project focuses on high-speed troop detection, coordinate translation, and automated deployment logic.

# 🛡️ Project Argus: Neural Game Automation
> Teaching AI to play Clash Royale through real-time object detection and tactical actuation.

Project Argus is an end-to-end computer vision agent developed to automate strategic decision-making in mobile gaming environments. This project focuses on high-speed troop detection, coordinate translation, and automated deployment logic.

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
- **Languages:** Python 3.11
- **ML Frameworks:** Ultralytics (YOLOv11), PyTorch
- **Vision:** OpenCV
- **Tools:** Roboflow (Data Management), Git

### 🚀 Getting Started
1. Clone the repository: `git clone https://github.com/Gonenza9090/Clash-Royale-Computer-Vision-Bot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the agent: `python src/main.py`

---
*Developed during a self-directed gap year to explore the intersection of Machine Learning and Robotics.*

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

---
*Developed during a self-directed gap year to explore the intersection of Machine Learning and Robotics.*
