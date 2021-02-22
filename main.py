import pyvirtualcam
import numpy as np
#imports

with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:  #for any other webcams such as 1080p or 60FPS, change the values
    while True:
        frame = np.zeros((cam.height, cam.width, 4), np.uint8)  #creates a shape called frame which sets to your webcam and has a 4 input for RGBA colour
        frame[:,:] = (34, 34, 34, 1)  #setting an RGBA colour to 34, 34, 34, 1
        cam.send(frame)  #sets camera to our frame
        cam.sleep_until_next_frame()  #wait till next frame
