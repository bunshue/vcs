using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_05_Mouse
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = "";
            label2.Text = "";
        }

        bool flag_mouse_down = false;
        int mouse_down_position_x = 0;
        int mouse_down_position_y = 0;
        int mouse_up_position_x = 0;
        int mouse_up_position_y = 0;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Down ";
            //label1.Text = "";
            //label2.Text = "";
            flag_mouse_down = true;
            mouse_down_position_x = e.X;
            mouse_down_position_y = e.Y;
            label9.Text = "MouseDown   (" + e.X.ToString() + ", " + e.Y + ")";

            if (e.Button == MouseButtons.Left)
                label12.Text = "你按了滑鼠左鍵";
            else if (e.Button == MouseButtons.Right)
                label12.Text = "你按了滑鼠右鍵";
            else if (e.Button == MouseButtons.Middle)
                label12.Text = "你按了滑鼠中鍵";
            else if (e.Button == MouseButtons.XButton1)
                label12.Text = "你按了滑鼠XButton1";
            else if (e.Button == MouseButtons.XButton2)
                label12.Text = "你按了滑鼠XButton2";
            else if (e.Button == MouseButtons.None)
                label12.Text = "你按了滑鼠None";
            else
                label12.Text = "你按了滑鼠其他鍵";








        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            label8.Text = "MouseMove";
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            mouse_up_position_x = e.X;
            mouse_up_position_y = e.Y;
            if (mouse_up_position_x > mouse_down_position_x)
            {
                richTextBox1.Text += "Right ";
                label1.Text = "滑鼠向右";
            }
            else
            {
                richTextBox1.Text += "Left ";
                label1.Text = "滑鼠向左";
            }

            if (mouse_up_position_y > mouse_down_position_y)
            {
                richTextBox1.Text += "Down ";
                label2.Text = "滑鼠向下";
            }
            else
            {
                richTextBox1.Text += "Up ";
                label2.Text = "滑鼠向上";
            }
            label9.Text = "MouseUp";
        }

        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += e.Delta.ToString() + " ";
            if (e.Delta < 0)
                label11.Text = "滾輪向下";
            else
                label11.Text = "滾輪向上";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            label5.Text = "按了Click";
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            label5.Text = "按了DoubleClick";
        }

        private void pictureBox1_MouseEnter(object sender, EventArgs e)
        {
            label6.Text = "MouseEnter";
        }

        private void pictureBox1_MouseHover(object sender, EventArgs e)
        {
            label7.Text = "MouseHover";
        }

        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {
            label6.Text = "MouseLeave";
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            label4.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;
            this.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;

            //label10.Text = "目前滑鼠在這個表單的位置: " + "x:" + e.X + " y:" + e.Y;
        }
    }
}
