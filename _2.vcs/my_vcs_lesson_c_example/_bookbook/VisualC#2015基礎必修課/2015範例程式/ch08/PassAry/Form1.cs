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
            //傳一個陣列給函數 做 氣泡排序法
            int[] myArray = new int[] { 33, 25, 16, 78, 12 };
            richTextBox1.Text += "排序前: \n";
            // 顯示排序前的每個陣列元素資料
            for (int i = 0; i <= myArray.GetUpperBound(0); i++)
            {
                richTextBox1.Text += myArray[i] + ",  ";
            }
            richTextBox1.Text += "\n";

            // 呼叫BubbleSort進行由小到大排序，傳遞的參數為myArray陣列
            BubbleSort(ref myArray);

            richTextBox1.Text += "排序後: \n";
            // 顯示排序後的每個陣列元素資料
            for (int i = 0; i <= myArray.GetUpperBound(0); i++)
            {
                richTextBox1.Text += myArray[i] + ",  ";
            }
            richTextBox1.Text += "\n";
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
