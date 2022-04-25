import cv2
def take_snapshot():
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(True):
        #switch on the camera and read the frames
        ret,frame=videoCaptureObject.read()
        #storing the image
        cv2.imwrite("newImage.jpg",frame)
        result=False

    #switch off the camera    
    videoCaptureObject.release()

    #close all the windows that were open during the process
    cv2.destroyAllWindows()

take_snapshot() 