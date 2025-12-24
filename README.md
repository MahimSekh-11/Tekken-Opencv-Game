# Tekken-Opencv-Game

⚙️ Full Setup Guide (VS Code – Step by Step)
✅ Step 1: Install Python

Download Python from
👉 https://www.python.org/downloads/

During installation:

✔️ Check Add Python to PATH

✅ Step 2: Open Project in VS Code

Open VS Code

Click File → Open File

Select your project file:

epoch-tekken-opencv.py

✅ Step 3: Create Virtual Environment (Recommended)

Open VS Code terminal:
Create virtual environment:
```
python -m venv myvenv
```
Activate virtual environment:
▶ Windows
```
myvenv\Scripts\activate
```
▶ macOS / Linux
```
source myvenv/bin/activate
```
You should see:

(myvenv)

✅ Step 4: Upgrade pip
```
python -m pip install --upgrade pip
```
✅ Step 5: Install Required Modules
```
pip install opencv-python mediapipe pyautogui
```
If mediapipe fails:
```
pip install mediapipe --no-cache-dir
```
▶️ Running the Project
Type on vscode terminal
```
  python epoch-tekken-opencv.py
```
📷 Your webcam will open
🦴 Pose landmarks will appear
🕹️ Gestures will trigger keyboard keys

⛔ Stopping the Program
Option 1:

Press Q on keyboard

Option 2:

Click terminal and press:
```
  Ctrl + C
```

### 🎮 Game Setup (Browser)

1. Open a **side window**
2. Visit:
   https://tekkengameplay.com/tekken-mobile.html#google_vignette
3. Click on **Play**
4. Keep the game window active while running the Python script

🔧 Gesture Logic Explained
🥊 Punch Detection
If wrist distance from shoulder > threshold → Z key

🛡️ Defence Detection
If both wrists near nose & above nose → C key

🧪 Threshold Customization

You can tune sensitivity:

PUNCH_THRESHOLD = 70
DEFENCE_THRESHOLD = 60

🧑‍💻 Author

Mahim Ali Sekh
Machine Learning & Computer Vision Enthusiast

📧 Email: mahimsekh02@gmail.com

🔗 LinkedIn: https://linkedin.com/in/mahim-ali-sekh-6194b

⭐ Support
If you found this project useful:

⭐ Star the repository
🍴 Fork it

🛠️ Improve it
