using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int i;  // 宣告一個區域整數變數
            i = Convert.ToInt32(label1.Text); //將字串轉換成為整數
            i = i + 1; // 遞增
            label1.Text = i.ToString();//將整數轉換成為字串
            // label1.Text = Convert.ToString(i); // 也可以這樣 將 整數轉為 字串
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            label1.Text = "0";
        }
    }
}
