import cv2
import requests as requestes
import numpy as np 

url = 'http://192.168.29.184:8080//shot.jpg'
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow("test")

img_counter = 0

while True:
    img_resp= requestes.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    im =  cv2.imdecode(img_arr, -1)
    #ret, frame = cam.read()
    cv2.imshow("test",im )
    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, im)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()