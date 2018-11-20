import os
import cv2

im_list = os.listdir(".\sample-images")

for image in im_list:
    # print("sample-images/%s" %(image))
    img = cv2.imread("sample-images/%s" %(image), 0)
    resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imshow("IMG", resized_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    #cv2.imwrite("sample-images/resized/%s" %(image), resized_img)
    ''' Key step to resize is above'''
