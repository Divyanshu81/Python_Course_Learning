import cv2
import time
import os
from threading import Thread
from glob import glob
from sendemail import send_email


video = cv2.VideoCapture(0)  # 1 for external web device
time.sleep(1)
first_frame = None

count = 1
status_list = [0]


def clean_folder():
    filepaths = glob("images/*.png")
    for file in filepaths:
        os.remove(file)

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21,21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 80, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow("My Video ", dil_frame)
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0),3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png",frame)
            count += 1
            all_file = glob("/images/*.png")
            index = len(all_file)//2 +1
            image_with_object = f"images/{index}.png"
    status_list.append(status)
    status_list = status_list[-2:]
    print(status_list)
    if status_list[0] > status_list[1]:
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True
        email_thread.start()
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

clean_thread.start()
video.release()
