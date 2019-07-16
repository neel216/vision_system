import cv2
import  numpy as np
import serial
import time


try:
    ser = serial.Serial("COM3", 9600)
    time.sleep(2)


    ser.write("left".encode())
    from_ard = ser.read(ser.inWaiting())
    print(from_ard.decode())


except:
    face_cascade = cv2.CascadeClassifier("haarcascade_face.xml")
    #eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

    listy = []

    cam = cv2.VideoCapture(0)

    print("Press 'q' to close webcam window.")

    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

        height, width, channels = frame.shape
        imgCenterX = int(width/2)
        imgCenterY = int(height/2)
        cv2.rectangle(frame, (imgCenterX - 2, imgCenterY - 2), (imgCenterX + 2, imgCenterY + 2), (0, 0, 255), 3)

        txtStart_left = (10, 40)
        txtStart_right = (width - 100, 40)
        txtFont = cv2.FONT_HERSHEY_DUPLEX
        txtScale = 1
        txtColor = (255, 0, 255)
        txtType = 2

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x , y , w , h) in faces:
            midX = int(w / 2)
            midY = int(h / 2)
            centerX = x + midX
            centerY = y + midY

            cv2.rectangle(frame, (x,y), (x + w , y + h), (255 , 0 , 0), 2)
            cv2.rectangle(frame, (centerX - 2 , centerY - 2), (centerX + 2 , centerY + 2), (0 , 255 , 0), 3)

            xDistance = centerX - imgCenterX
            yDistance = imgCenterY - centerY
            cv2.putText(frame, "[" + str(xDistance) + ", " + str(yDistance) + "]", txtStart_left, txtFont, txtScale, txtColor, txtType)
            cv2.putText(frame, "[" + str(w) + "]", txtStart_right, txtFont, txtScale, txtColor, txtType)
            
            if (len(listy) < 200):
                listy.append(w)
            

    #        roi_gray = gray[y:y + h, x:x + w]
    #        roi_color = frame[y:y + h , x:x + w]
    #        eyes = eye_cascade.detectMultiScale(roi_gray)
    #        for (ex , ey , ew , eh) in eyes:
    #            cv2.rectangle(roi_color , (ex , ey) , (ex + ew , ey + eh) , (0 , 255, 0), 2)

        cv2.imshow('img' , frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cam.release()
    cv2.destroyAllWindows()

    summ = 0
    count = 0
    for i in listy:
        summ += listy[i]
        count += 1
    print(summ/count)