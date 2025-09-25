# test_env.py - teste rápido de import

try:
    import cv2
    import mediapipe as mp
    import pyautogui
    import numpy as np

    print("Imports OK")
    print("cv2:", cv2.__version__)
    # mediapipe tem versão em mp.__version__ em muitas instalações
    print("mediapipe:", getattr(mp, "__version__", "version info not available"))
    print("numpy:", np.__version__)
except Exception as e:
    print("Erro durante imports:", e)
    