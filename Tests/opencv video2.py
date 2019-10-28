import cv2
import numpy as np

a="MPEG"
b='MP4V'

writer = cv2.VideoWriter("output.mp4",
cv2.VideoWriter_fourcc(*a), 100,(640,480))

for frame in range(1000):
    writer.write(np.random.randint(0, 255, (480,640,3)).astype('uint8'))

writer.release()
