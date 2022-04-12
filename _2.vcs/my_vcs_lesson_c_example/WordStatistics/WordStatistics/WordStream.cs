// --------------------------------------------------------------------------------------------------------------------
// <copyright file="WordStatistics.cs" company="yada">
//   Copyright (c) yada Corporation. All rights reserved.
// </copyright>
// change by qugang 2015.4.18
// 单词枚举器:算法从开始找字符，如果不是字符，则返回从pos 到end 的单词
// --------------------------------------------------------------------------------------------------------------------
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WordStatistics
{
    /// <summary>
    /// 单词枚举器
    /// </summary>
    public class WordStream : IEnumerable
    {
        private char[] buffer;
        public WordStream(char[] buffer)
        {
            this.buffer = buffer;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return (IEnumerator)GetEnumerator();
        }

        public WordStreamEnum GetEnumerator()
        {
            return new WordStreamEnum(this.buffer);
        }


    }

    public class WordStreamEnum : IEnumerator
    {
        private char[] buffer;
        int pos = 0;
        int endCount = 0;
        int index = -1;

        public WordStreamEnum(char[] buffer)
        {
            this.buffer = buffer;
        }

        public bool MoveNext()
        {
            while (index < buffer.Length - 1)
            {
                index++;
                char buff = buffer[index];
                if ((buff >= 'a' && buff <= 'z') || (buff >= 'A' && buff <= 'Z'))
                {
                    if (endCount == 0)
                    {
                        pos = index;
                        endCount++;
                    }
                    else
                    {
                        endCount++;
                    }
                }
                else
                {
                    if (endCount != 0)
                        return true;
                }
                if (buff == '\0')
                {
                    return false;
                }
            }
            return false;
        }

        public object Current
        {
            get
            {
                int tempInt = endCount;
                endCount = 0;
                return new string(buffer, pos, tempInt);
            }
        }

        public void Reset()
        {
            index = -1;
        }
    }

}
