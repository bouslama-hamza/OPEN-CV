import cv2 as cv

#read images using imread method
img = cv.imread('Image/4.png')
cv.imshow('Neural', img)
cv.waitKey(0)

#read vedio using frame and true method
capture = cv.VideoCapture('video/VID_20210429_063454.mp4')
while True:
    istrue , frame = capture.read()
    cv.imshow('Vedio' , frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
