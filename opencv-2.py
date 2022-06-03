import cv2
print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    cv2.imshow('my grayframe',grayFrame)
    cv2.moveWindow('my grayframe',640,480)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
