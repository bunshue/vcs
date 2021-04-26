using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_05_Array
{
    class BubbleSort
    {
        /// <summary>
        /// 冒泡排序
        /// </summary>
        public void Sort(int[] list)
        {
            int i, j, temp;
            bool done = false;
            j = 1;
            while ((j < list.Length) && (!done))//判斷長度
            {
                done = true;
                for (i = 0; i < list.Length - j; i++)
                {
                    if (list[i] > list[i + 1])
                    {
                        done = false;
                        temp = list[i];
                        list[i] = list[i + 1];//交換數據
                        list[i + 1] = temp;
                    }
                }
                j++;
            }
        }
    }
}

