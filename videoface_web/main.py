import cv2

# 加载Haar特征分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 打开网页在线视频
cap = cv2.VideoCapture('https://ymd.dlod.link/?u=https%3A%2F%2Fredirector.googlevideo.com%2Fvideoplayback%3Fexpire%3D1680018280%26ei%3DCLciZMPHKP2ZsfIPlaqomAU%26ip%3D209.141.37.75%26id%3Do-AMOLdzT_Cl1vnlrKG6jow7vC19A0H0oLLNdkuwe8Bn9f%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DIP%26mm%3D31%252C26%26mn%3Dsn-a5meknzk%252Csn-q4flrnee%26ms%3Dau%252Conr%26mv%3Dm%26mvi%3D2%26pl%3D24%26gcr%3Dus%26initcwndbps%3D522500%26spc%3D99c5CT5hRl0hqdTpK5hvRUemC1XKQ6LKBC3C91EJIuLJvf01vf9afaiFbRzqPIg%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DZoTkjuwKk1VsfdFb2qFw2GkM%26cnr%3D14%26ratebypass%3Dyes%26dur%3D382.154%26lmt%3D1665432225462235%26mt%3D1679996475%26fvip%3D4%26fexp%3D24007246%26c%3DWEB%26txp%3D5538434%26n%3DNkbDXziIRWIh7w%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cspc%252Cvprv%252Cmime%252Cns%252Ccnr%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAKbzQ1UcD8rPks-1ETSQT7MxeNp_kSXR9azL1b4M5j4sAiAbQdoPH5OSsgWCB6Jrv22t7xkPc2LQDSnHTPsU66J4Sw%253D%253D%26sig%3DAOq0QJ8wRgIhAIrC6Rb-JAngHlBziVos8xM5lLb48EUzq_Ni0Isur9o2AiEAsDfDZH3Dd5NSrVgq-Cmm8pIyaKmPSB2lq-SDOpht7NU%253D%26range%3D0-&s=WmExp3XOEvL45wr-f888unW6wOCDH0EGg_WS2nWkiD4')

# 持续循环直到按下“q”键停止
while True:
    # 读取视频流
    ret, frame = cap.read()

    # 将帧转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

    # 在检测到的人脸周围画一个白色的框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

    # 显示视频流
    cv2.imshow('Video Stream', frame)

    # 按下“q”键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放视频流并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
