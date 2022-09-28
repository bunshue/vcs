#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "sortingNetworks_common.h"

////////////////////////////////////////////////////////////////////////////////
// Validate sorted keys array (check for integrity and proper order)
////////////////////////////////////////////////////////////////////////////////
extern "C" uint validateSortedKeys(uint * resKey, uint * srcKey, uint batchSize, uint arrayLength, uint numValues, uint dir)
{
    uint* srcHist;
    uint* resHist;

    if (arrayLength < 2)
    {
        printf("validateSortedKeys(): arrayLength too short, exiting...\n");
        return 1;
    }

    printf("...inspecting keys array: ");

    srcHist = (uint*)malloc(numValues * sizeof(uint));
    resHist = (uint*)malloc(numValues * sizeof(uint));

    int flag = 1;

    for (uint j = 0; j < batchSize; j++, srcKey += arrayLength, resKey += arrayLength)
    {
        // Build histograms for keys arrays
        memset(srcHist, 0, numValues * sizeof(uint));
        memset(resHist, 0, numValues * sizeof(uint));

        for (uint i = 0; i < arrayLength; i++)
        {
            if (srcKey[i] < numValues && resKey[i] < numValues)
            {
                srcHist[srcKey[i]]++;
                resHist[resKey[i]]++;
            }
            else
            {
                flag = 0;
                break;
            }
        }

        if (!flag)
        {
            printf("***Set %u source/result key arrays are not limited properly***\n", j);
            goto brk;
        }

        // Compare the histograms
        for (uint i = 0; i < numValues; i++)
            if (srcHist[i] != resHist[i])
            {
                flag = 0;
                break;
            }

        if (!flag)
        {
            printf("***Set %u source/result keys histograms do not match***\n", j);
            goto brk;
        }

        if (dir) {
            // Ascending order
            for (uint i = 0; i < arrayLength - 1; i++)
                if (resKey[i + 1] < resKey[i])
                {
                    flag = 0;
                    break;
                }
        }
        else
        {
            // Descending order
            for (uint i = 0; i < arrayLength - 1; i++)
                if (resKey[i + 1] > resKey[i])
                {
                    flag = 0;
                    break;
                }
        }

        if (!flag)
        {
            printf("***Set %u result key array is not ordered properly***\n", j);
            goto brk;
        }
    }

brk:
    free(resHist);
    free(srcHist);

    if (flag) printf("OK\n");

    return flag;
}

extern "C" int validateValues(uint * resKey, uint * resVal, uint * srcKey, uint batchSize, uint arrayLength)
{
    int correctFlag = 1, stableFlag = 1;

    printf("...inspecting keys and values array: ");

    for (uint i = 0; i < batchSize;
        i++, resKey += arrayLength, resVal += arrayLength)
    {
        for (uint j = 0; j < arrayLength; j++)
        {
            if (resKey[j] != srcKey[resVal[j]]) correctFlag = 0;

            if ((j < arrayLength - 1) && (resKey[j] == resKey[j + 1]) && (resVal[j] > resVal[j + 1]))
                stableFlag = 0;
        }
    }

    printf(correctFlag ? "OK\n" : "***corrupted!!!***\n");
    printf(stableFlag ? "...stability property: stable!\n"
        : "...stability property: NOT stable\n");

    return correctFlag;
}
