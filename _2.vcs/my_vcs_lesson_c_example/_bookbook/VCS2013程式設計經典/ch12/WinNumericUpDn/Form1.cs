using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinNumericUpDn
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 宣告engNum陣列，用來存放數字的英文單字
        // "one"索引0, "two"索引1...其它以此類推
        string[] engNum = new string[] { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" };
       
        // === 表單載入時執行

        private void Form1_Load(object sender, EventArgs e)
        {
            numericUpDown1.Minimum = 1;  // 數字上下鈕最小值為1
            numericUpDown1.Maximum = 10; // 數字上下鈕最小值為10
        }
        // ===  當數字上下按鈕的值改變時會執行
        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            // 將數字上下鈕的值減1即取得engNum陣列的索引 
            int n = int.Parse(numericUpDown1.Value.ToString()) - 1;
            // 在lblShow標籤上顯示數字上下鈕對應的英文單字
            lblShow.Text = "英文：" + engNum[n];  
        }
    }
}
