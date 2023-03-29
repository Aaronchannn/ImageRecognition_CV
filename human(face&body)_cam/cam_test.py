import cv2

i = 0
while True:
  cap = cv2.VideoCapture(i)#700
  if cap.isOpened():  # 当摄像头为开启状态时打印索引位置
    print(i)
  if cv2.waitKey(5)==ord('q'):  # 按 q 退出
    break
  i = i+1
cap.release()