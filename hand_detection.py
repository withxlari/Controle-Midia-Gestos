import cv2
import mediapipe as mp

# Inicializa o MediaPipe Hands:

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    # Converte a imagem para RGB (MediaPipe exige):
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processa a imagem e detecta mãos:
    results = hands.process(img_rgb)

    # Se detecta mãos
    if results.multi_hand_landmarks:  # Retorna uma lista de mãos detectadas e seus 21 pontos-chave.
        for hand_landmarks in results.multi_hand_landmarks:
            # Desenha os pontos e conexões na imagem
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)  # Desenha os pontos na tela junto com linhas conectando os dedos.

    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()