import cv2

#导入Haar特征分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

#导入画面
cam = cv2.VideoCapture(701)#701

while True:
    #截取视频流
    ret, frame = cam.read()

    #每一帧转为灰度图像
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #检测
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 7, minSize=(80, 80))
    humans = human_cascade.detectMultiScale(gray_img, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
        #cv2.textput

    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    #显示视频流
    cv2.imshow('detect human', frame)

    #如果按下“q”停止识别
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#释放窗口
cam.release()
cv2.destoryAllWindow()