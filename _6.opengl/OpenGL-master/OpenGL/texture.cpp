//#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "texture.h"
#include "utils.h"

// 注意參數中的引用數據類型
// 在該函數中 , 要修改該引用數據類型 , 並將其當做返回值返回
unsigned char* DecodeBMP(unsigned char* bmpFileData, int& width, int& height)
{
	unsigned char* ret;

	ret = (unsigned char*)malloc(sizeof(unsigned char));

	// 判定該文件是否是 bmp 文件 
	// bmp 圖像文件前兩個字節是 0x4D42 
	// 注意這裡先將 unsigned char* bmpFileData 指針強轉為 unsigned short* 類型指針
	// 然後使用 * 符號取值該地址中的 short* 指針指向的內容 
	// 就是文件的前兩個字節
	if (0x4D42 == *((unsigned short*)bmpFileData))
	{
		// 像素數據偏移地址是從第 10 個字節開始 ( 從 0 開始計數 )
		// 寬度是 10 , 11 字節
		// 高度是 12 , 13 字節 

	}
	ret = 0;

	return ret;
}

// 實現紋理初始化方法
void Texture::Init(const char* imagePath)
{
	// 從硬盤加載紋理文件到內存中
	// 紋理圖片數據放在 imageFileContent 指針指向的內存中
	unsigned char* imageFileContent = LoadFileContent(imagePath);

	// 定義解碼圖片的寬高
	int width = 0;
	int height = 0;

	// 
	unsigned char* pixelData = DecodeBMP(imageFileContent, width, height);

	// 生成 OpenGL 紋理


}