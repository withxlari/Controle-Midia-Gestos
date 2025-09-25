import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

finger_tips = [4, 8, 12, 16, 20]  # Polegar, indicador, médio, anelar, mindinho
finger_pips = [3, 6, 10, 14, 18]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rbg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rbg)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)


             # Verifica cada dedo
            for tip, pip in zip(finger_tips, finger_pips):
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
                    cv2.putText(frame, f"Dedo {tip} esticado", (10, 30 + tip*15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                
    cv2.imshow("Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    