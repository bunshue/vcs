import cv2

filename1 = 'penguin3.jpg'
filename2 = 'penguin4.jpg'
output_filename = 'penguin_all.jpg'
filenames = [filename1, filename2]

filename1 = 'SF1.jpg'
filename2 = 'SF2.jpg'
filename3 = 'SF3.jpg'
filename4 = 'SF4.jpg'
output_filename = 'SF_all.jpg'
filenames = [filename1, filename2, filename3, filename4]

img_arr = []
for filename in filenames:
    image = cv2.imread(filename)
    img_arr.append(image)
    
stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(img_arr)
if status == cv2.Stitcher_OK:
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', pano)
    cv2.imwrite(output_filename, pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('done')
else:
    print('error: {}'.format(status))
