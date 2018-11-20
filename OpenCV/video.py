import cv2 , time

video = cv2.VideoCapture(0)
while(True):
    check, frame = video.read()
    #print(check) # This is a  boolean if image is successfully captured
    #print(frame) # This is an image file
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capture", gray)
    key = cv2.waitKey(1)
    if (key == ord('q')):
        break
cv2.destroyAllWindows

video.release()
