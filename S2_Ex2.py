import cv2
import numpy as np
import matplotlib.pyplot as plt


def process_video(video_filepath):
    cap = cv2.VideoCapture(video_filepath)
    grabbed, frame = cap.read()

    count = 0
    while grabbed:
        grabbed, frame = cap.read()                             # read every frame of the video
        frame_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)      # convert the frame from rgb to yuv
        frame_hist = np.histogram(frame_yuv)                    # compute histogram of the yuv frame
        fig = plt.plot(frame_hist)                              # plot histogram
        cv2.imwrite("Histograms_Ex2/frame%d.jpg" % count, fig)  # save each plot into Histograms_Ex2 folder
        plt.close(fig)
        count += 1
    cap.release()


input_video = 'BBB_11.mp4'
process_video(input_video)
