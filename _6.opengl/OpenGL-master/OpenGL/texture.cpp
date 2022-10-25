//#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "texture.h"
#include "utils.h"

// �`�N�ѼƤ����ޥμƾ�����
// �b�Ө�Ƥ� , �n�ק�Ӥޥμƾ����� , �ñN�����^�Ȫ�^
unsigned char* DecodeBMP(unsigned char* bmpFileData, int& width, int& height)
{
	unsigned char* ret;

	ret = (unsigned char*)malloc(sizeof(unsigned char));

	// �P�w�Ӥ��O�_�O bmp ��� 
	// bmp �Ϲ����e��Ӧr�`�O 0x4D42 
	// �`�N�o�̥��N unsigned char* bmpFileData ���w�j�ର unsigned short* �������w
	// �M��ϥ� * �Ÿ����ȸӦa�}���� short* ���w���V�����e 
	// �N�O��󪺫e��Ӧr�`
	if (0x4D42 == *((unsigned short*)bmpFileData))
	{
		// �����ƾڰ����a�}�O�q�� 10 �Ӧr�`�}�l ( �q 0 �}�l�p�� )
		// �e�׬O 10 , 11 �r�`
		// ���׬O 12 , 13 �r�` 

	}
	ret = 0;

	return ret;
}

// ��{���z��l�Ƥ�k
void Texture::Init(const char* imagePath)
{
	// �q�w�L�[�����z���줺�s��
	// ���z�Ϥ��ƾک�b imageFileContent ���w���V�����s��
	unsigned char* imageFileContent = LoadFileContent(imagePath);

	// �w�q�ѽX�Ϥ����e��
	int width = 0;
	int height = 0;

	// 
	unsigned char* pixelData = DecodeBMP(imageFileContent, width, height);

	// �ͦ� OpenGL ���z


}