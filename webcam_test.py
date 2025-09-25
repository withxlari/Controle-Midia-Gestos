import cv2

# Inicializa a captura de video (0 = webcam padrão)
cap = cv2.VideoCapture(0) # Abre a webcam padrão. Se tiver outra webcam, trocar por 0 por 1.

while True:
    # Captura frame a frame
    ret, frame = cap.read()

    # Mostra o frame em uma janela
    cv2.imshow("Webcam", frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha a janela
cap.release()
cv2.destroyAllWindows()
