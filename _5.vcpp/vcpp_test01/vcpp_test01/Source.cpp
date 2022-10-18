
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctime>

#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <vector>

#include <iostream>

using namespace std;

const char* program_name = "測試程式的名稱";

inline bool IsAppBuiltAs64() { return sizeof(void*) == 8; }

void test_write_binary_file()
{
    //將資料寫成檔案

    /*
        char* reference_file = NULL;
    void* imageData = malloc(mesh_width * mesh_height * sizeof(float));

    sdkDumpBin2(imageData, mesh_width * mesh_height * sizeof(float), "simpleGL.bin");
    */


}

#ifndef FOPEN
#define FOPEN(fHandle,filename,mode) fopen_s(&fHandle, filename, mode)
#endif
void sdkDumpBin2(void* data, unsigned int bytes, const char* filename)
{
    printf("sdkDumpBin2, filename : %s\n", filename);
    FILE* fp;
    FOPEN(fp, filename, "wb");
    fwrite(data, bytes, 1, fp);
    fflush(fp);
    fclose(fp);
}

////////////////////////////////////////////////////////////////////////////////
// Helper function, returning uniformly distributed
// random float in [low, high] range
////////////////////////////////////////////////////////////////////////////////
float RandFloat(float low, float high)
{
    float t = (float)rand() / (float)RAND_MAX;
    return (1.0f - t) * low + t * high;
}

int main()
{
    cout << "歡迎使用C++！\n";
    printf("將資料寫成檔案\n");

    printf("[%s]\n", program_name);

    test_write_binary_file();


    printf("製作random資料\n");
    float h_StockPrice[10];
    int i;
    for (i = 0; i < 10; i++)
    {
        h_StockPrice[i] = RandFloat(5.0f, 30.0f);
    }

    for (i = 0; i < 10; i++)
    {
        printf("%f ", h_StockPrice[i]);
    }
    printf("\n");



    printf("Pointer測試\n");

    int* p;
    int aaa[10];

    p = &aaa[0];
    printf("p1 = %p\n", p);
    p = aaa;
    printf("p2 = %p\n", p);

    for (i = 0; i < 10; i++)
    {
        aaa[i] = i * i;
        printf("i = %d, aaa[%d] = %d, addr of aaa[%d] is %p\n", i, i, aaa[i], i, &aaa[i]);
    }
    for (i = 0; i < 10; i++)
    {
        printf("index %d, addr is %p, value is %d\n", i, p + i, *(p + i));
    }


    //System("pause");
    //getchar();//或system("pause");

    char k1 = '5';
    int k2 = atoi(&k1);
    printf("k1 = %c\n", k1);
    printf("k2 = %d\n", k2);

    //char* k3 = "FF";
    //int k4 = atoi(k3);
    //printf("k3 = %s\n", k3);
    //printf("k4 = %d\n", k4);

    /*
    printf("sprintf 測試\n");

    char fps[256];
    sprintf(fps, "Cuda GL Interop (VBO): %3.1f fps (Max 100Hz)", 12.345);
    //glutSetWindowTitle(fps);
    printf("%s\n", fps);
    */

    printf("使用 srand 製作random資料\n");

    srand((unsigned int)time(NULL));

    float rr = 0;
    for (i = 0; i < 10; i++)
    {
        rr = (float)rand() / (float)RAND_MAX;
        //rr = (float)rand();
        printf("%f ", rr);
    }
    printf("\n");

    bool os_type = IsAppBuiltAs64();
    if (os_type == true)
    {
        printf("Built as a 64-bit target\n");
    }
    else
    {
        printf("Built NOT as a 64-bit target\n");
    }

    

    return 0;
}

