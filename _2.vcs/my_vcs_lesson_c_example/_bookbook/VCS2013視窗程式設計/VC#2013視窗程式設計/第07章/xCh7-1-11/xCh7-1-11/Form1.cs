using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh7_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 初始化ColorDialog
            colorDialog1.AllowFullOpen = false;
            colorDialog1.FullOpen = false;
            colorDialog1.ShowHelp = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 初始化色彩
            colorDialog1.Color = textBox1.ForeColor;

            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.ForeColor = colorDialog1.Color;
                textBox1.Text = "完成前景色(ForeColor)的設定";
            }
            else
                textBox1.Text = "[取消]前景色(ForeColor)的設定";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 初始化色彩
            colorDialog1.Color = textBox1.BackColor;

            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.BackColor = colorDialog1.Color;
                textBox1.Text = "完成背景色(BackColor)的設定";
            }
            else
                textBox1.Text = "[取消]背景色(BackColor)的設定";
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            colorDialog1.AllowFullOpen = checkBox1.Checked;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            colorDialog1.FullOpen = checkBox2.Checked;
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            colorDialog1.ShowHelp = checkBox3.Checked;
        }
    }
}
