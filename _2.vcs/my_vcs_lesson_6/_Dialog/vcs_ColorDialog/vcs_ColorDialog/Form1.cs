using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ColorDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            colorDialog1.Color = richTextBox1.BackColor;    //顏色對話框的預設顏色
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.BackColor = colorDialog1.Color;
                button1.BackColor = colorDialog1.Color;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = true;  //可以使用該對話框定義自定義顏色
            colorDialog1.AnyColor = true;      			//顯示基本顏色集中可用的所有顏色
            colorDialog1.FullOpen = true;      //創建自定義顏色的控件在對話框打開時是可見的
            colorDialog1.SolidColorOnly = false;			//不限制只選擇純色
            if (colorDialog1.ShowDialog() == DialogResult.OK)   //彈出對話框
            {
                richTextBox1.SelectionBackColor = colorDialog1.Color;
            }
        }
    }
}
