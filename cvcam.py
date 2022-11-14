import cv2
import time

class CvCam(object):

    def __init__(self) -> None:
        # initialize video capture
        self.cap = cv2.VideoCapture(0)
        # initialize frame
        self.frame = None
        self.running = True

    def poll(self):
        ret, self.frame = self.cap.read()


    def update(self):
        while(self.running):
            self.poll()

    def run_threaded(self):
        return self.frame

    def run(self):
        self.poll()
        return self.frame

    def shutdown(self):
        self.cap.release()
        self.running = False

class CvImageDisplay(object):

    def run(self, image):
        cv2.imshow('frame', image)
        cv2.waitKey(1)

    def shutdown(self):
        cv2.destroyAllWindows()