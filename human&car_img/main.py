import cv2

# 加载人体检测模型
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# 加载车辆检测模型
car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

# 加载测试图像
img = cv2.imread('test.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人体
humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

# 检测车辆
cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# 标注人体识别框
for (x,y,w,h) in humans:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    cv2.putText(img, 'Human', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

# 标注车辆识别框
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 显示结果图像
#cv2.imshow('result',img)

#保存图像
cv2.imwrite('output.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
