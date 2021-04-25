import cv2,time    #time library provide delay
face_cascad=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)   #start web cam

while True:
    check,frame=video.read()
    print(check)        #boolean variable show weather web take
    print(frame)        #numpy method to show matric of image
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascad.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)
    for x, y, w, h in faces:
        frame= cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 230, 0), 5)

    cv2.imshow("capturing",frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()   #used to stop camera
cv2.destroyWindow()
