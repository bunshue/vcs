#include "texture.h"
#include "utils.h"

// ע������е�������������
// �ڸú����� , Ҫ�޸ĸ������������� , �����䵱������ֵ����
unsigned char* DecodeBMP(unsigned char* bmpFileData, int& width, int& height)
{
	// �ж����ļ��Ƿ��� bmp �ļ� 
	// bmp ͼ���ļ�ǰ�����ֽ��� 0x4D42 
	// ע�������Ƚ� unsigned char* bmpFileData ָ��ǿתΪ unsigned short* ����ָ��
	// Ȼ��ʹ�� * ����ȡֵ�õ�ַ�е� short* ָ��ָ������� 
	// �����ļ���ǰ�����ֽ�
	if (0x4D42 == *((unsigned short*)bmpFileData)) 
	{
		// ��������ƫ�Ƶ�ַ�Ǵӵ� 10 ���ֽڿ�ʼ ( �� 0 ��ʼ���� )
		// ����� 10 , 11 �ֽ�
		// �߶��� 12 , 13 �ֽ� 

	}
	unsigned char* zzzz = nullptr;

	return zzzz;
}

// ʵ�������ʼ������
void Texture::Init(const char* imagePath) 
{
	// ��Ӳ�̼��������ļ����ڴ���
	// ����ͼƬ���ݷ��� imageFileContent ָ��ָ����ڴ���
	unsigned char* imageFileContent = LoadFileContent(imagePath);

	// �������ͼƬ�Ŀ��
	int width = 0; 
	int height = 0;

	// 
	//unsigned char* pixelData = DecodeBMP(imageFileContent, width, height);

	// ���� OpenGL ����


}