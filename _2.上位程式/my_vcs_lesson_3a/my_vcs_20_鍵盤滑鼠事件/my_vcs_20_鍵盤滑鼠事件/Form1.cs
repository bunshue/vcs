using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_20_鍵盤滑鼠事件
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label10.Text = "";
            label12.Text = "";
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            label2.Text = "KeyDown";
            label12.Text = "KeyDown, 按鍵是：" + e.KeyCode;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            label3.Text = "KeyPress, 按鍵是：" + e.KeyChar;
        }

        private void textBox1_KeyUp(object sender, KeyEventArgs e)
        {
            label2.Text = "KeyUp";
        }

        private void textBox1_DoubleClick(object sender, EventArgs e)
        {
            label4.Text = "DoubleClick";

        }

        private void textBox1_Click(object sender, EventArgs e)
        {
            label4.Text = "Click";

        }

        private void textBox1_MouseHover(object sender, EventArgs e)
        {
            label6.Text = "MouseHover";

        }

        private void textBox1_MouseEnter(object sender, EventArgs e)
        {
            label5.Text = "MouseEnter";

        }

        private void textBox1_MouseLeave(object sender, EventArgs e)
        {
            label5.Text = "MouseLeave";
            label6.Text = "";
            label8.Text = "";

        }

        private void textBox1_MouseDown(object sender, MouseEventArgs e)
        {
            label7.Text = "MouseDown";

        }

        private void textBox1_MouseUp(object sender, MouseEventArgs e)
        {
            label7.Text = "MouseUp";

        }

        private void textBox1_MouseMove(object sender, MouseEventArgs e)
        {
            label8.Text = "MouseMove";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label10.Text = "";

        }

        private void textBox1_DragDrop(object sender, DragEventArgs e)
        {
            label9.Text = "DragDrop";

        }

        private void textBox1_DragEnter(object sender, DragEventArgs e)
        {
            label9.Text = "DragEnter";
        }

        private void textBox1_DragLeave(object sender, EventArgs e)
        {
            label10.Text = "DragLeave";

        }

        private void textBox1_DragOver(object sender, DragEventArgs e)
        {
            label10.Text = "DragOver";

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            label11.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;
            this.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;
        }

    }
}
