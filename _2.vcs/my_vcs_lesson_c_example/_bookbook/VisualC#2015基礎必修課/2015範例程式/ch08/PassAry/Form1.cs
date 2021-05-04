using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PassAry
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            int[] myArray = new int[] { 10, 30, 20, 40, 50 };
            label1.Text = "排序前: ";
            label2.Text = "排序後: ";
            // 顯示排序前的每個陣列元素資料
            for (int i = 0; i <= myArray.GetUpperBound(0); i++)
            {
                label1.Text += myArray[i] + ",  ";
            }
            // 呼叫BubbleSort進行由小到大排序，傳遞的參數為myArray陣列
            BubbleSort(ref myArray);
            // 顯示排序後的每個陣列元素資料
            for (int i = 0; i <= myArray.GetUpperBound(0); i++)
            {
                label2.Text += myArray[i] + ",  ";
            }
        }
        //氣泡排序法
        private void BubbleSort(ref int[] vArray)
        {
            int i, j, temp;
            for (i = vArray.GetUpperBound(0); i > 0; i--)  // 第幾輪Pass
            {
                for (j = 0; j < i; j++)
                {
                    if (vArray[j] > vArray[j + 1])
                    {
                        temp = vArray[j];  // 兩陣列元素內容互換
                        vArray[j] = vArray[j + 1];
                        vArray[j + 1] = temp;
                    }
                }
            }
        }
    }
}
