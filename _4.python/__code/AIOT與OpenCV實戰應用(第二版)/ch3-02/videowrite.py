import cv2

ESC = 27
cap = cv2.VideoCapture(0)
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 400
HEIGHT = int(WIDTH / ratio)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('video.mp4', fourcc, 30, (WIDTH, HEIGHT))

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

    # 影像大小必須與設定一致，否則會輸出失敗
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ESC: 
        cv2.destroyAllWindows()
        break
