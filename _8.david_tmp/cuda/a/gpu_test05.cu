//蝴膀κ絛ㄒ

//浪琩GPU祑ン皌竚

#include <stdio.h>

#include <iostream>

int main()
{
int dev = 0;
    cudaDeviceProp devProp;
    cudaGetDeviceProperties(&devProp, dev);
    std::cout << "ㄏノGPU device " << dev << ": " << devProp.name << std::endl;
    std::cout << "SM计秖" << devProp.multiProcessorCount << std::endl;
    std::cout << "–絬祘遏ㄉず" << devProp.sharedMemPerBlock / 1024.0 << " KB" << std::endl;
    std::cout << "–絬祘遏程絬祘计" << devProp.maxThreadsPerBlock << std::endl;
    std::cout << "–EM程絬祘计" << devProp.maxThreadsPerMultiProcessor << std::endl;
    std::cout << "–EM程絬祘计" << devProp.maxThreadsPerMultiProcessor / 32 << std::endl;

}
