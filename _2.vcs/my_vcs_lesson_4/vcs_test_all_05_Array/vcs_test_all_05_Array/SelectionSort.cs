using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_05_Array
{
    class SelectionSort
    {
        private int min;
        /// <summary>
        /// 選擇排序
        /// </summary>
        public void Sort(int[] list)
        {
            for (int i = 0; i < list.Length - 1; i++)
            {
                min = i;
                for (int j = i + 1; j < list.Length; j++)
                {
                    if (list[j] < list[min])
                        min = j;
                }
                int t = list[min];
                list[min] = list[i];
                list[i] = t;
            }
        }
    }
}
