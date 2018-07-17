import cv2

# path はここにAnaconda3\Library\etc\haarcascades
# 場所遠いけど../../

# 潮顔　綾の号
# 

# 顔認識用
face_cascade_path = './library/haarcascade_frontalface_default.xml'

#face_cascade_path = './library/haarcascade_profileface.xml'
# 目認識用
eye_cascade_path =  './library/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)

count = 0

for i in range(1, 81):
    src = cv2.imread('./data/yosuke/sample ('+str(i)+').jpg')

    # 試しに表示
    # cv2.imshow("loaded", src)
    # キーを待つ
    # cv2.waitKey(0)

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(src_gray)

    # detectMultiScaleは顔認識したx,yの位置と，高さと幅が出る
    # rectangle 左上の角の座標、右下の角の座標、色、枠線の太さ
    '''
    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
        目を認識する場合
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2) 
    '''

    # cv2.imwrite('data/opencv_face_detect_rectangle.jpg', src)
    # print(faces)

    # 切り出し
    for rect in faces:
        count += 1
        #cv2.imwrite('demo.jpg', image[rect])
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        
        # img[y: y + h, x: x + w] 
        cv2.imwrite('./redata/koyanagi_' + str(i+1+count) + '.png', src[y:y+h, x:x+w])