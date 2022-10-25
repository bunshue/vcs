#include <assert.h>
#include "convolutionFFT2D_common.h"

////////////////////////////////////////////////////////////////////////////////
// Reference straightforward CPU convolution
////////////////////////////////////////////////////////////////////////////////
extern "C" void convolutionClampToBorderCPU(float* h_Result, float* h_Data, float* h_Kernel, int dataH,
    int dataW, int kernelH, int kernelW, int kernelY, int kernelX)
{
    for (int y = 0; y < dataH; y++)
        for (int x = 0; x < dataW; x++)
        {
            double sum = 0;

            for (int ky = -(kernelH - kernelY - 1); ky <= kernelY; ky++)
                for (int kx = -(kernelW - kernelX - 1); kx <= kernelX; kx++)
                {
                    int dy = y + ky;
                    int dx = x + kx;

                    if (dy < 0)
                    {
                        dy = 0;
                    }

                    if (dx < 0)
                    {
                        dx = 0;
                    }

                    if (dy >= dataH)
                    {
                        dy = dataH - 1;
                    }

                    if (dx >= dataW)
                    {
                        dx = dataW - 1;
                    }

                    sum += h_Data[dy * dataW + dx] * h_Kernel[(kernelY - ky) * kernelW + (kernelX - kx)];
                }

            h_Result[y * dataW + x] = (float)sum;
        }
}
