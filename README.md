# ImageRecognition_CV
## Image recognition implemented through OpenCV library using a cascaded classifier model based on Haar features
## 基于Haar特征的级联分类器模型通过opencv库实现图像识别

### 算法实现主要框架：

1.加载官OpenCV官方提供的相应的基于Haar特征的级联分类器模型  
`xxx_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_xxx.xml')`

2.加载原图像  
`img|video = cv2.imread('文件绝对路径')`

3.转换为灰度图像  
`gray_img = cv2.cvtColor(img, cv2.COLORBGR2GRAY)`

4.检测物体  
`xxx = xxx_cascade.detectMultiscale(gray, 1.1, 5, minSize = (50, 50))`

5.标注识别框  
```
for (x, y, w, h) in xxxs:
    cv2.rectangle(img, (x, y), (x+w, y+h ), (255, 255, 255), 2)
    注释识别框cv2.putText()
```

6.显示图像结果  
`cv2.imshow('result', img)`

(6.1).保存图像结果  
`cv2.imwrite('output.jpg', img)`

7.释放窗口及资源  
```
cv2.waitKey(0)  
cv2.destoryAllWindows()
```
