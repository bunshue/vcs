using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_2_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 多行編輯按鈕的事件處理程序
        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Multiline = true;
            textBox1.ScrollBars = ScrollBars.Vertical;
            textBox1.AcceptsReturn = true;

            Size aSize = new Size(200, 150);
            textBox1.Size = aSize;

            textBox1.Focus();
        }

        // 取得文字按鈕的事件處理程序
        private void button2_Click(object sender, EventArgs e)
        {
            int i = 0;
            foreach (string line in textBox1.Lines)
            {
                i++;
            }
            textBox2.Text = "共有 " + i + " 列文字：" + textBox1.Text;

            textBox2.ReadOnly = true;
            textBox2.Enabled = false;
        }
    }
}
