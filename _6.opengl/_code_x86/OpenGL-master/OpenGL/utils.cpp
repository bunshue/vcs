#include "utils.h"

// 加载文件方法
unsigned char* LoadFileContent(const char* filePath)
{
	unsigned char* fileContent = nullptr;
	/*
	// 该指针指向的内存空间存储文件内容

	// 打开文件
	FILE* pFile = fopen(filePath, "rb"); 

	//printf("打开文件 pFile : %p", pFile);

	// 如果打开文件成功
	if (pFile)
	{
		// 判定文件大小, 将文件指针从 "尾部" 开始移动
		// 移动 0 个字节
		// 成功返回 0 , 失败返回非 0
		fseek(pFile, 0, SEEK_END);

		// 获取文件指针位置 , 当前文件指针位于文件尾部
		// 当前的文件指针位置就是文件的字节长度
		int nLen = ftell(pFile);

		// 如果文件长度大于 0 , 才去读取文件
		if (nLen > 0) 
		{
			// 将文件指针 FILE* pFile 移到文件的开始位置
			rewind(pFile);

			// 为文件内容分配一块内存空间 , 即创建一个 nLen + 1 字节的数组
			// 多出一个字节 , 在字节末尾添加一个 '\0'
			fileContent = new unsigned char[nLen + 1];

			// 读取 pFile 指针指向的内存中的数据 
			// 读取的数据个数是 nLen 个 
			// 每个数据的大小是 sizeof(unsigned char) 字节 , 即 1 字节 
			// 将读取的数据存储到 fileContent 指向的内存中
			fread(fileContent, sizeof(unsigned char), nLen, pFile);

			// 最后第 nLen + 1 个元素 , 索引是 nLen , 设置为 '\0'
			fileContent[nLen] = '\0';
		}

		// 关闭文件
		fclose(pFile);
	}
		*/

	return fileContent;
}