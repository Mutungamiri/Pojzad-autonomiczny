from datetime import datetime
import cv2
import imutils

now = datetime.now()
current_time = now.strftime("%d-%m-%y_%H:%M:%S")
print("Current Time =", current_time)


cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('your_video.avi', fourcc, 20.0, size)
video_name = "test_videos/" + current_time + ".avi"
out = cv2.VideoWriter(video_name, fourcc, 20.0, size)

while(True):
    _, frame = cap.read()
    frame = imutils.rotate(frame, 180)
    # cv2.imshow('Recording...', frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# I should rotate the video now...
