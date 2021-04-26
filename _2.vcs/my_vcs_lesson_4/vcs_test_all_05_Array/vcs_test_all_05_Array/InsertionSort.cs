using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_05_Array
{
    class InsertionSort
    {
        /// <summary>
        /// 插入排序
        /// </summary>
        public void Sort(int[] list)
        {
            for (int i = 1; i < list.Length; i++)
            {
                int t = list[i];
                int j = i;
                while ((j > 0) && (list[j - 1] > t))
                {
                    list[j] = list[j - 1];
                    --j;
                }
                list[j] = t;
            }
        }
    }
}
