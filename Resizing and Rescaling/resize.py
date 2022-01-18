import cv2 as cv

#create a method to change pictures or videos size
def change_size(frame , scale = .2):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width , height)

    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

#read and resize image size
img = cv.imread('Image/4.png')
change_it = change_size(img)
cv.imshow('Neural', change_it)
cv.waitKey(0)

#read and change vedio and frame size
capture = cv.VideoCapture('video/VID_20210429_063454.mp4')
while True:
    istrue , frame = capture.read()
    frame_resized = change_size(frame)
    cv.imshow('Vedio' , frame)
    cv.imshow('Vedio Resized' , frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

