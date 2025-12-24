import cv2
import mediapipe as mp
import pyautogui

# Mediapipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Webcam
cap = cv2.VideoCapture(0)
FRAME_WIDTH, FRAME_HEIGHT = 580, 900

# Thresholds
PUNCH_THRESHOLD = 70
DEFENCE_THRESHOLD = 60

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    if result.pose_landmarks:
        lm = result.pose_landmarks.landmark
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Coordinates
        wrist_rx = int(lm[mp_pose.PoseLandmark.RIGHT_WRIST].x * w)
        wrist_lx = int(lm[mp_pose.PoseLandmark.LEFT_WRIST].x * w)
        wrist_ry = int(lm[mp_pose.PoseLandmark.RIGHT_WRIST].y * h)
        wrist_ly = int(lm[mp_pose.PoseLandmark.LEFT_WRIST].y * h)

        shoulder_rx = int(lm[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * w)
        shoulder_lx = int(lm[mp_pose.PoseLandmark.LEFT_SHOULDER].x * w)

        nose_x = int(lm[mp_pose.PoseLandmark.NOSE].x * w)
        nose_y = int(lm[mp_pose.PoseLandmark.NOSE].y * h)

        # ---- DEFENCE ----
        if (abs(wrist_rx - nose_x) < DEFENCE_THRESHOLD and
            abs(wrist_lx - nose_x) < DEFENCE_THRESHOLD and
            wrist_ry < nose_y and wrist_ly < nose_y):

            pyautogui.press('c')
            cv2.putText(frame, "DEFENCE", (30, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 0, 0), 3)

        # ---- PUNCH ----
        if (abs(wrist_rx - shoulder_rx) > PUNCH_THRESHOLD or
            abs(wrist_lx - shoulder_lx) > PUNCH_THRESHOLD):

            pyautogui.press('z')
            cv2.putText(frame, "PUNCH", (30, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3)

    cv2.imshow("Motion Control", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()