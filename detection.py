import cv2
import numpy as np
import time

# Load Haar Cascade for face detection
pengklasifikasiWajah = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize video capture from the webcam
videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("Kamera tidak dapat diakses")
    exit()

tombolQditekan = False
while not tombolQditekan:
    ret, kerangka = videoCam.read()

    if ret:
        abuAbu = cv2.cvtColor(kerangka, cv2.COLOR_BGR2GRAY)
        dafWajah = pengklasifikasiWajah.detectMultiScale(abuAbu, scaleFactor=1.3, minNeighbors=2)

        for (x, y, w, h) in dafWajah:
            cv2.rectangle(kerangka, (x, y), (x + w, y + h), (0, 255, 0), 2)

        teks = "Jumlah Wajah Terdeteksi = " + str(len(dafWajah))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(kerangka, teks, (10, 30), font, 1, (255, 0, 0), 2)

        cv2.imshow("Hasil", kerangka)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tombolQditekan = True
            break

videoCam.release()
cv2.destroyAllWindows()
