#include "utils.h"

// �[������k
unsigned char* LoadFileContent(const char* filePath)
{
	unsigned char* fileContent = nullptr;
	/*
	// �ӫ��w���V�����s�Ŷ��s�x��󤺮e

	// ���}���
	FILE* pFile = fopen(filePath, "rb");

	//printf("���}��� pFile : %p", pFile);

	// �p�G���}��󦨥\
	if (pFile)
	{
		// �P�w���j�p, �N�����w�q "����" �}�l����
		// ���� 0 �Ӧr�`
		// ���\��^ 0 , ���Ѫ�^�D 0
		fseek(pFile, 0, SEEK_END);

		// ��������w��m , ��e�����w��������
		// ��e�������w��m�N�O��󪺦r�`����
		int nLen = ftell(pFile);

		// �p�G�����פj�� 0 , �~�hŪ�����
		if (nLen > 0)
		{
			// �N�����w FILE* pFile �����󪺶}�l��m
			rewind(pFile);

			// ����󤺮e���t�@�����s�Ŷ� , �Y�Ыؤ@�� nLen + 1 �r�`���Ʋ�
			// �h�X�@�Ӧr�` , �b�r�`�����K�[�@�� '\0'
			fileContent = new unsigned char[nLen + 1];

			// Ū�� pFile ���w���V�����s�����ƾ�
			// Ū�����ƾڭӼƬO nLen ��
			// �C�Ӽƾڪ��j�p�O sizeof(unsigned char) �r�` , �Y 1 �r�`
			// �NŪ�����ƾڦs�x�� fileContent ���V�����s��
			fread(fileContent, sizeof(unsigned char), nLen, pFile);

			// �̫�� nLen + 1 �Ӥ��� , ���ެO nLen , �]�m�� '\0'
			fileContent[nLen] = '\0';
		}

		// �������
		fclose(pFile);
	}
		*/

	return fileContent;
}