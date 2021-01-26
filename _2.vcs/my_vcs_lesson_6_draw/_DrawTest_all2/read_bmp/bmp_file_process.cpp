#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
using namespace std;
#define MAXPIX 384*260

int main()
{
    BITMAPFILEHEADER FileHeader;    //宣告BMP檔案標頭
    BITMAPINFOHEADER InfoHeader;    //宣告BMP資訊標頭
    FILE *fp;                       //讀取檔案FILE
    FILE *fpw;                      //寫入檔案FILE
    int ImageX, ImageY;             //圖檔內容寬高
    RGBTRIPLE rgb;
    RGBTRIPLE color[MAXPIX];
    
    /** ##### 讀取圖檔 #####  */
    fp = fopen("in.bmp", "rb");                    //開啟檔案
    fpw = fopen("out.bmp", "wb");
    if (!fp) printf("in.bmp檔案開啟失敗...\n");         //確認開啟檔案是否成功
    if (!fpw) printf("out.bmp檔案開啟失敗...\n");

    fread(&FileHeader, sizeof(BITMAPFILEHEADER), 1, fp);    //1.陣列or結構的指標 2.陣列or結構的大小
    fread(&InfoHeader, sizeof(BITMAPINFOHEADER), 1, fp);    //3.陣列的元素數量，如果是結構就等同 1 個陣列元素 4.指向結構 FILE 的指標

    /**< 資訊正確測試 */
//    cout << "bfType：" << FileHeader.bfType << endl << "bfSize：" << FileHeader.bfSize << endl
//    << "bfReserved1：" << FileHeader.bfReserved1 << endl << "bfReserved2：" << FileHeader.bfReserved2 << endl
//    << "bfOffBits：" << FileHeader.bfOffBits << endl ;

    ImageX = InfoHeader.biWidth;        // 取得寬高
    ImageY = InfoHeader.biHeight;

    for(int i=0; i<ImageY; i++ )        //逐列掃描
    {
        for(int j=0; j<ImageX; j++ )    //逐行掃描
        {
          fread(&rgb, sizeof(RGBTRIPLE), 1, fp);        //將每格的pixel BGR 寫入 color matrix 中
          color[i*ImageX+j].rgbtBlue=rgb.rgbtBlue;
          color[i*ImageX+j].rgbtGreen=rgb.rgbtGreen;
          color[i*ImageX+j].rgbtRed=rgb.rgbtRed;
        }
    }
    fclose(fp);     //檔案fp讀取完成，關閉

    /** ##### 輸出圖檔 ##### */
    fwrite(&FileHeader, sizeof(BITMAPFILEHEADER), 1, fpw); //輸出檔案
  fwrite(&InfoHeader, sizeof(BITMAPINFOHEADER), 1, fpw);

    for(int i=0; i<ImageY; i++ )        //逐列掃描
    {
        for(int j=0; j<ImageX; j++ )    //逐行掃描
        {
            rgb.rgbtBlue=color[i*ImageX+j].rgbtBlue;
            rgb.rgbtGreen=color[i*ImageX+j].rgbtGreen;
            rgb.rgbtRed=color[i*ImageX+j].rgbtRed;
            fwrite(&rgb, sizeof(RGBTRIPLE), 1, fpw);        // 將 color matrix 寫入輸出圖檔中
        }
    }
	fclose(fpw);

    return 0;
}
