import pyautogui
import cv2
import numpy as np
import time

# Specify video resolution (adjust as needed)
resolution = (1920, 1080)

# Specify video codec (XVID in this case)
codec = cv2.VideoWriter_fourcc(*"mp4v")

# Specify output file name
filename = "Recording.mp4"

# Specify frames per second (FPS)
fps = 7.0

# Create a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution,)

# Optional: Create an empty window for real-time display
# cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Live", 480, 270)

# Start recording
i=0
min=float(input("Enter the length of your video:(in sec.)"))
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    # cv2.imshow("Live", frame)
    # if cv2.waitKey(1) == ord("q"):
    if i==min*7:
        break
    i=i+1
    time.sleep(1/7)

# Release the writer and close all windows
out.release()
cv2.destroyAllWindows()
