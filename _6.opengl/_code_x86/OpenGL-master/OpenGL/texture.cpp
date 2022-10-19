#include "texture.h"
#include "utils.h"

// 注意参数中的引用数据类型
// 在该函数中 , 要修改该引用数据类型 , 并将其当做返回值返回
unsigned char* DecodeBMP(unsigned char* bmpFileData, int& width, int& height)
{
	// 判定该文件是否是 bmp 文件 
	// bmp 图像文件前两个字节是 0x4D42 
	// 注意这里先将 unsigned char* bmpFileData 指针强转为 unsigned short* 类型指针
	// 然后使用 * 符号取值该地址中的 short* 指针指向的内容 
	// 就是文件的前两个字节
	if (0x4D42 == *((unsigned short*)bmpFileData)) 
	{
		// 像素数据偏移地址是从第 10 个字节开始 ( 从 0 开始计数 )
		// 宽度是 10 , 11 字节
		// 高度是 12 , 13 字节 

	}
	unsigned char* zzzz = nullptr;

	return zzzz;
}

// 实现纹理初始化方法
void Texture::Init(const char* imagePath) 
{
	// 从硬盘加载纹理文件到内存中
	// 纹理图片数据放在 imageFileContent 指针指向的内存中
	unsigned char* imageFileContent = LoadFileContent(imagePath);

	// 定义解码图片的宽高
	int width = 0; 
	int height = 0;

	// 
	//unsigned char* pixelData = DecodeBMP(imageFileContent, width, height);

	// 生成 OpenGL 纹理


}