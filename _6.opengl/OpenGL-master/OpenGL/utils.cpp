#include "utils.h"

// �����ļ�����
unsigned char* LoadFileContent(const char* filePath)
{
	unsigned char* fileContent = nullptr;
	/*
	// ��ָ��ָ����ڴ�ռ�洢�ļ�����

	// ���ļ�
	FILE* pFile = fopen(filePath, "rb"); 

	//printf("���ļ� pFile : %p", pFile);

	// ������ļ��ɹ�
	if (pFile)
	{
		// �ж��ļ���С, ���ļ�ָ��� "β��" ��ʼ�ƶ�
		// �ƶ� 0 ���ֽ�
		// �ɹ����� 0 , ʧ�ܷ��ط� 0
		fseek(pFile, 0, SEEK_END);

		// ��ȡ�ļ�ָ��λ�� , ��ǰ�ļ�ָ��λ���ļ�β��
		// ��ǰ���ļ�ָ��λ�þ����ļ����ֽڳ���
		int nLen = ftell(pFile);

		// ����ļ����ȴ��� 0 , ��ȥ��ȡ�ļ�
		if (nLen > 0) 
		{
			// ���ļ�ָ�� FILE* pFile �Ƶ��ļ��Ŀ�ʼλ��
			rewind(pFile);

			// Ϊ�ļ����ݷ���һ���ڴ�ռ� , ������һ�� nLen + 1 �ֽڵ�����
			// ���һ���ֽ� , ���ֽ�ĩβ���һ�� '\0'
			fileContent = new unsigned char[nLen + 1];

			// ��ȡ pFile ָ��ָ����ڴ��е����� 
			// ��ȡ�����ݸ����� nLen �� 
			// ÿ�����ݵĴ�С�� sizeof(unsigned char) �ֽ� , �� 1 �ֽ� 
			// ����ȡ�����ݴ洢�� fileContent ָ����ڴ���
			fread(fileContent, sizeof(unsigned char), nLen, pFile);

			// ���� nLen + 1 ��Ԫ�� , ������ nLen , ����Ϊ '\0'
			fileContent[nLen] = '\0';
		}

		// �ر��ļ�
		fclose(pFile);
	}
		*/

	return fileContent;
}