#include "utils.h"

// 加載文件方法
unsigned char* LoadFileContent(const char* filePath)
{
	unsigned char* fileContent = nullptr;
	/*
	// 該指針指向的內存空間存儲文件內容

	// 打開文件
	FILE* pFile = fopen(filePath, "rb");

	//printf("打開文件 pFile : %p", pFile);

	// 如果打開文件成功
	if (pFile)
	{
		// 判定文件大小, 將文件指針從 "尾部" 開始移動
		// 移動 0 個字節
		// 成功返回 0 , 失敗返回非 0
		fseek(pFile, 0, SEEK_END);

		// 獲取文件指針位置 , 當前文件指針位於文件尾部
		// 當前的文件指針位置就是文件的字節長度
		int nLen = ftell(pFile);

		// 如果文件長度大於 0 , 才去讀取文件
		if (nLen > 0)
		{
			// 將文件指針 FILE* pFile 移到文件的開始位置
			rewind(pFile);

			// 為文件內容分配一塊內存空間 , 即創建一個 nLen + 1 字節的數組
			// 多出一個字節 , 在字節末尾添加一個 '\0'
			fileContent = new unsigned char[nLen + 1];

			// 讀取 pFile 指針指向的內存中的數據
			// 讀取的數據個數是 nLen 個
			// 每個數據的大小是 sizeof(unsigned char) 字節 , 即 1 字節
			// 將讀取的數據存儲到 fileContent 指向的內存中
			fread(fileContent, sizeof(unsigned char), nLen, pFile);

			// 最後第 nLen + 1 個元素 , 索引是 nLen , 設置為 '\0'
			fileContent[nLen] = '\0';
		}

		// 關閉文件
		fclose(pFile);
	}
		*/

	return fileContent;
}