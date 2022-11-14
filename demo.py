from donkeycar.vehicle import Vehicle
from cvcam import CvCam, CvImageDisplay


V = Vehicle()




cam = CvCam()
V.add(cam, outputs=["camera/image"], threaded=True)

disp = CvImageDisplay()
V.add(disp, inputs=["camera/image"])



V.start()