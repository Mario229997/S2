import cv2


def process_video(video_filepath):
    cap = cv2.VideoCapture(video_filepath)
    grabbed, frame = cap.read()

    while grabbed:
        grabbed, frame = cap.read()
        # do stuff with `frame` here
    cap.release()

    