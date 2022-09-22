#include <stdio.h>
#include <iostream>
using namespace std;

const char* program_name = "測試程式的名稱";

void test_write_binary_file()
{
    //將資料寫成檔案

    /*
        char* reference_file = NULL;
    void* imageData = malloc(mesh_width * mesh_height * sizeof(float));

    sdkDumpBin2(imageData, mesh_width * mesh_height * sizeof(float), "simpleGL.bin");
    */


}

/*
void sdkDumpBin2(void* data, unsigned int bytes, const char* filename)
{
    printf("sdkDumpBin2, filename : %s\n", filename);
    FILE* fp;
    FOPEN(fp, filename, "wb");
    fwrite(data, bytes, 1, fp);
    fflush(fp);
    fclose(fp);
}
*/


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



    return 0;
}

