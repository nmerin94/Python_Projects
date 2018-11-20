import cv2 , time, pandas
from datetime import datetime
import os

def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
                os.makedirs(dir)

df =  pandas.DataFrame(columns = ["Start", "Stop"])
times = []

first_frame = None
video = cv2.VideoCapture(0)
for i in range(1,20):
    check, frame = video.read()
status_list = [None, None]
while(True):
    status = 0
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)  # Gaussian Blur is used to smooth the image for better accuracy

    if(first_frame is None):   # To capture the first frame with no object
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)


    (_,cntrs,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntrs:
        if cv2.contourArea(contour) < 1000 :
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)

    # Creating a datetime list to store the times when object appeared and disappeared

    if(status_list[-1] == 1 and status_list[-2] == 0):
        times.append(datetime.now())
    elif(status_list[-1] == 0 and status_list[-2] == 1):
        times.append(datetime.now())

    cv2.imshow("Capture", gray)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    if (key == ord('q')):

        # Appending Datetime if the moving object is still in the vicinity

        if(status == 1):
            times.append(datetime.now())

        break
    status_list = status_list[-2:]  # If the script runs for too long, the list will grow


#print(status_list) # Has the motion status
#print(times)  # has the time when object appeared and dissappeared

for i in range(0, len(times), 2):   # The loop runs for length/2 times to capture the motion
    df = df.append({"Start" : times[i], "Stop" : times[i+1]}, ignore_index = True)

d = datetime.now().strftime("%Y_%m_%d_%H_%M")

assure_path_exists("csv\\Times_%s.csv" %(d))
df.to_csv("csv\\Times_%s.csv" %(d))
cv2.destroyAllWindows
video.release()
