video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

import cv2

cap = cv2.VideoCapture(video_filename)

while True:
    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    
    if cv2.waitKey(100) == 27:
        cv2.destroyAllWindows()
        break

