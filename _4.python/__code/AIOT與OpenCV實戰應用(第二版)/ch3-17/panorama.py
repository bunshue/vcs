import cv2

filename1 = 'penguin1.jpg'
filename2 = 'penguin2.jpg'

filenames = [filename1, filename2]

img_arr = []
for filename in filenames:
    image = cv2.imread(filename)
    img_arr.append(image)
    
stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(img_arr)
if status == cv2.Stitcher_OK:
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', pano)
    cv2.imwrite('final.jpg', pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('done')
else:
    print('error: {}'.format(status))
