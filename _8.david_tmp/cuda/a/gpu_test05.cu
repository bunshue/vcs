//����ʬ�d��

//�ˬd�ۤv��GPU�w��t�m

#include <stdio.h>

#include <iostream>

int main()
{
int dev = 0;
    cudaDeviceProp devProp;
    cudaGetDeviceProperties(&devProp, dev);
    std::cout << "�ϥ�GPU device " << dev << ": " << devProp.name << std::endl;
    std::cout << "SM���ƶq�G" << devProp.multiProcessorCount << std::endl;
    std::cout << "�C�ӽu�{�����@�ɤ��s�j�p�G" << devProp.sharedMemPerBlock / 1024.0 << " KB" << std::endl;
    std::cout << "�C�ӽu�{�����̤j�u�{�ơG" << devProp.maxThreadsPerBlock << std::endl;
    std::cout << "�C��EM���̤j�u�{�ơG" << devProp.maxThreadsPerMultiProcessor << std::endl;
    std::cout << "�C��EM���̤j�u�{���ơG" << devProp.maxThreadsPerMultiProcessor / 32 << std::endl;

}
