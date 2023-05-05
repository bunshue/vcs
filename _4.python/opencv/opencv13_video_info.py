import cv2
filename = 'C:/_git/vcs/_1.data/______test_files1/_video/鹿港.mp4'

video = cv2.VideoCapture(filename);

fps = video.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

print("data video.get(cv2.CAP_PROP_FPS) : {0}".format(video.get(cv2.CAP_PROP_FPS)))
print("data video.get(cv2.CAP_PROP_POS_MSEC) : {0}".format(video.get(cv2.CAP_PROP_POS_MSEC)))#Current position of the video file in milliseconds.
print("data video.get(cv2.CAP_PROP_POS_FRAMES) : {0}".format(video.get(cv2.CAP_PROP_POS_FRAMES)))#0-based index of the frame to be decoded/captured next.
print("data video.get(cv2.CAP_PROP_POS_AVI_RATIO) : {0}".format(video.get(cv2.CAP_PROP_POS_AVI_RATIO)))#Relative position of the video file: 0=start of the film, 1=end of the film.
print("data video.get(cv2.CAP_PROP_FRAME_WIDTH) : {0}".format(video.get(cv2.CAP_PROP_FRAME_WIDTH)))#Width of the frames in the video stream.
print("data video.get(cv2.CAP_PROP_FRAME_HEIGHT) : {0}".format(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))#Height of the frames in the video stream.
print("data video.get(cv2.CAP_PROP_FPS) : {0}".format(video.get(cv2.CAP_PROP_FPS)))#Frame rate.
print("data video.get(cv2.CAP_PROP_FOURCC) : {0}".format(video.get(cv2.CAP_PROP_FOURCC)))#4-character code of codec. see VideoWriter::fourcc .
print("data video.get(cv2.CAP_PROP_FRAME_COUNT) : {0}".format(video.get(cv2.CAP_PROP_FRAME_COUNT)))#Number of frames in the video file.
print("data video.get(cv2.CAP_PROP_FORMAT) : {0}".format(video.get(cv2.CAP_PROP_FORMAT)))#Format of the Mat objects returned by VideoCapture::retrieve().
print("data video.get(cv2.CAP_PROP_MODE) : {0}".format(video.get(cv2.CAP_PROP_MODE)))#Backend-specific value indicating the current capture mode.
print("data video.get(cv2.CAP_PROP_BRIGHTNESS) : {0}".format(video.get(cv2.CAP_PROP_BRIGHTNESS)))#Brightness of the image (only for cameras).
print("data video.get(cv2.CAP_PROP_CONTRAST) : {0}".format(video.get(cv2.CAP_PROP_CONTRAST)))#Contrast of the image (only for cameras).
print("data video.get(cv2.CAP_PROP_SATURATION) : {0}".format(video.get(cv2.CAP_PROP_SATURATION)))#Saturation of the image (only for cameras).
print("data video.get(cv2.CAP_PROP_HUE) : {0}".format(video.get(cv2.CAP_PROP_HUE)))#Hue of the image (only for cameras).
print("data video.get(cv2.CAP_PROP_GAIN) : {0}".format(video.get(cv2.CAP_PROP_GAIN)))#Gain of the image (only for cameras).
print("data video.get(cv2.CAP_PROP_EXPOSURE) : {0}".format(video.get(cv2.CAP_PROP_EXPOSURE)))#Exposure (only for cameras).
print("data video.get(cv2.CAP_PROP_CONVERT_RGB) : {0}".format(video.get(cv2.CAP_PROP_CONVERT_RGB)))#Boolean flags indicating whether images should be converted to RGB.
print("data video.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U) : {0}".format(video.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U)))#Currently unsupported.
print("data video.get(cv2.CAP_PROP_RECTIFICATION) : {0}".format(video.get(cv2.CAP_PROP_RECTIFICATION)))#Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently).
print("data video.get(cv2.CAP_PROP_MONOCHROME) : {0}".format(video.get(cv2.CAP_PROP_MONOCHROME)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_SHARPNESS) : {0}".format(video.get(cv2.CAP_PROP_SHARPNESS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_AUTO_EXPOSURE) : {0}".format(video.get(cv2.CAP_PROP_AUTO_EXPOSURE)))#DC1394: exposure control done by camera, user can adjust reference level using this feature.
print("data video.get(cv2.CAP_PROP_GAMMA) : {0}".format(video.get(cv2.CAP_PROP_GAMMA)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_TEMPERATURE) : {0}".format(video.get(cv2.CAP_PROP_TEMPERATURE)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_TRIGGER) : {0}".format(video.get(cv2.CAP_PROP_TRIGGER)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_TRIGGER_DELAY) : {0}".format(video.get(cv2.CAP_PROP_TRIGGER_DELAY)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V) : {0}".format(video.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_ZOOM) : {0}".format(video.get(cv2.CAP_PROP_ZOOM)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_FOCUS) : {0}".format(video.get(cv2.CAP_PROP_FOCUS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_GUID) : {0}".format(video.get(cv2.CAP_PROP_GUID)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_ISO_SPEED) : {0}".format(video.get(cv2.CAP_PROP_ISO_SPEED)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_BACKLIGHT) : {0}".format(video.get(cv2.CAP_PROP_BACKLIGHT)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_PAN) : {0}".format(video.get(cv2.CAP_PROP_PAN)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_TILT) : {0}".format(video.get(cv2.CAP_PROP_TILT)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_ROLL) : {0}".format(video.get(cv2.CAP_PROP_ROLL)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_IRIS) : {0}".format(video.get(cv2.CAP_PROP_IRIS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_SETTINGS) : {0}".format(video.get(cv2.CAP_PROP_SETTINGS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
print("data video.get(cv2.CAP_PROP_BUFFERSIZE) : {0}".format(video.get(cv2.CAP_PROP_BUFFERSIZE)))#Pop up video/camera filter dialog (note: only supported by DSHOW backend currently. Property value is ignored)
print("data video.get(cv2.CAP_PROP_AUTOFOCUS) : {0}".format(video.get(cv2.CAP_PROP_AUTOFOCUS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx

video.release();

