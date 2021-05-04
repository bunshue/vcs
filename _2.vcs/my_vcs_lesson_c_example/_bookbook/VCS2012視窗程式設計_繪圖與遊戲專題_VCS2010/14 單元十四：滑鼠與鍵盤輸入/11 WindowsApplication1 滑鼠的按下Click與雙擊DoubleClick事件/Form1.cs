/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 滑鼠按下事件
        private void panel1_MouseClick(object sender, MouseEventArgs e)
        {
            panel1.BackColor = Color.Black;
        }

        // 滑鼠雙擊事件
        private void panel2_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            panel2.BackColor = Color.Black;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            panel1.BackColor = panel2.BackColor = Color.Pink; // Reset
        }
    }
}