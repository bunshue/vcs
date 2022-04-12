using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_01_Math
{
    class Transform
    {
        internal string TenToBinary(long value)//將十進制轉換為二進制
        {
            return Convert.ToString(value, 2);
        }
        internal string TenToEight(long value)//將十進制轉換為八進制
        {
            return Convert.ToString(value, 8);
        }
        internal string TenToSixteen(long value)//將十進制轉換為十六進制
        {
            return Convert.ToString(value, 16);
        }
        internal string BinaryToEight(long value)//將二進制轉換為八進制
        {
            return Convert.ToString(Convert.ToInt64(value.ToString(), 2), 8);
        }
        internal string BinaryToTen(long value)//將二進制轉換為十進制
        {
            return Convert.ToInt64(value.ToString(), 2).ToString();
        }
        internal string BinaryToSixteen(long value)//將二進制轉換為十六進制
        {
            return Convert.ToString(Convert.ToInt64(value.ToString(), 2), 16);
        }
        internal string EightToBinary(long value)//將八進制轉換為二進制
        {
            return Convert.ToString(Convert.ToInt64(value.ToString(), 8), 2);
        }
        internal string EightToTen(long value)//將八進制轉換為十進制
        {
            return Convert.ToInt64(value.ToString(), 8).ToString();
        }
        internal string EightToSixteen(long value)//將八進制轉換為十六進制
        {
            return Convert.ToString(Convert.ToInt64(value.ToString(), 8), 16);
        }
        internal string SixteenToBinary(string value)//將十六進制轉換為二進制
        {
            return Convert.ToString(Convert.ToInt64(value, 16), 2);
        }
        internal string SixteenToEight(string value)//將十六進制轉換為八進制
        {
            return Convert.ToString(Convert.ToInt64(value, 16), 8);
        }
        internal string SixteenToTen(string value)//將十六進制轉換為十進制
        {
            return Convert.ToUInt64(value, 16).ToString();
        }
    }
}
