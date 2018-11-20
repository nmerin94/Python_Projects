import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#print(type(face_cascade))

img = cv2.imread("photo.jpg")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5)

for x, y, w, h in faces :
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
#print(faces)
#print(type(faces))

cv2.imshow("Detect",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
