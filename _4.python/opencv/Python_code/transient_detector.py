import os
from pathlib import Path
import cv2 as cv

PAD = 5  # 設定要忽略鄰近影像邊緣多少距離的像素數

def find_transient(image, diff_image, pad): 
    """尋找並標出星空中移動的瞬變""" 
    transient = False
    height, width = diff_image.shape 
    cv.rectangle(image, (PAD, PAD), (width - PAD, height - PAD), 255, 1) 
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(diff_image) 
    if pad < maxLoc[0] < width - pad and pad < maxLoc[1] < height - pad: 
        cv.circle(image, maxLoc, 10, 255, 0) 
        transient = True 
    return transient, maxLoc

def main():
    night1_files = sorted(os.listdir('night_1_registered_transients'))
    night2_files = sorted(os.listdir('night_2'))             
    path1 = Path.cwd() / 'night_1_registered_transients'
    path2 = Path.cwd() / 'night_2'
    path3 = Path.cwd() / 'night_1_2_transients'
     
    for i, _ in enumerate(night1_files[:-1]):  # 用切片語法取出影像，會略過最後一張，也就是負片影像
        print('aaaaaaaaaa')
        filename1 = str(path1 / night1_files[i])
        filename2 = str(path2 / night2_files[i])
        print(filename1)
        print(filename2)

        if os.path.exists(filename1) == True:
            print(filename1, '存在')
        else:
            print(filename1, '不存在')

        if os.path.exists(filename2) == True:
            print(filename2, '存在')
        else:
            print(filename2, '不存在')
        
        img1 = cv.imread(filename1, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread(filename2, cv.IMREAD_GRAYSCALE)

        #cv.imshow('Peony', img1)  #顯示圖片

        #filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
        filename = 'C:/_git/vcs/1_bright_transient_left_registered.png'
        
        img1 = cv.imread(filename, cv.IMREAD_GRAYSCALE)
        img2 = cv.imread(filename, cv.IMREAD_GRAYSCALE)

        cv.imshow('Peony', img1)  #顯示圖片

        print(img1.shape)
        print(img2.shape)

        continue


        # 比較並顯示差異影像
        diff_imgs1_2 = cv.absdiff(img1, img2)
        cv.imshow('Difference', diff_imgs1_2)
        cv.waitKey(2000)
        cv.destroyAllWindows()

        # 複製一份影像副本，偵測及標示瞬變
        temp = diff_imgs1_2.copy()
        transient1, transient_loc1 = find_transient(img1, temp, PAD)

        # 畫圓蓋掉最亮點
        cv.circle(temp, transient_loc1, 10, 0, -1)

        # 偵測及標示瞬變       
        transient2, _ = find_transient(img1, temp, PAD)

        if transient1 or transient2:
            print('\nTRANSIENT DETECTED between {} and {}\n'
                  .format(night1_files[i], night2_files[i]))
            font = cv.FONT_HERSHEY_COMPLEX_SMALL
            cv.putText(img1, night1_files[i], (10, 25),
                       font, 1, (255, 255, 255), 1, cv.LINE_AA)
            cv.putText(img1, night2_files[i], (10, 55),
                       font, 1, (255, 255, 255), 1, cv.LINE_AA)

            blended = cv.addWeighted(img1, 1, diff_imgs1_2, 1, 0)
            cv.imshow('Surveyed', blended)
            cv.waitKey(2500)
            cv.destroyAllWindows()

            out_filename = '{}_DECTECTED.png'.format(
                night1_files[i][:-4])
            cv.imwrite(str(path3/out_filename), blended)  # 會覆寫既有檔案！

        else:
            print('\nNo transient detected between {} and {}\n'
                  .format(night1_files[i], night2_files[i]))

if __name__ == '__main__':
    main()
