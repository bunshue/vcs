using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseKety_Form2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label0.Text = "在Form上按方向鍵控制鼠標";
            label1.Text = "在Form上按滑鼠各按鍵";
            label2.Text = "按X離開";
            label3.Text = "";
        }

        [System.Runtime.InteropServices.DllImport("user32")]
        private static extern int mouse_event(int dwFlags, int dx, int dy, int cButtons, int dwExtraInfo);
        const int MOUSEEVENTF_MOVE = 0x0001;
        const int MOUSEEVENTF_LEFTDOWN = 0X0002;
        const int MOUSEEVENTF_LEFTUP = 0X0004;
        const int MOUSEEVENTF_RIGHTDOWN = 0X0008;
        const int MOUSEEVENTF_RIGHTUP = 0X0010;
        const int MOUSEEVENTF_MIDDLEDOWN = 0X0020;
        const int MOUSEEVENTF_MIDDLEUP = 0X0040;
        const int MOUSEEVENTF_ABSOLUTE = 0X8000;

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Down)
            {
                label3.Text = "鼠標向下移動";
                mouse_event(MOUSEEVENTF_MOVE, 0, 20, 0, 0);
            }
            else if (e.KeyCode == Keys.Up)
            {
                label3.Text = "鼠標向上移動";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.KeyCode == Keys.Left)
            {
                label3.Text = "鼠標向左移動";
                mouse_event(MOUSEEVENTF_MOVE, -20, 0, 0, 0);
            }
            else if (e.KeyCode == Keys.Right)
            {
                label3.Text = "鼠標向右移動";
                mouse_event(MOUSEEVENTF_MOVE, 20, 0, 0, 0);
            }
            else if (e.KeyCode == Keys.X)
            {
                label3.Text = "離開";
                Application.Exit();
            }
            else
            {
                label3.Text = "你按了" + e.KeyCode + "\n";
            }

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                label3.Text = "MouseButtons.Right 你按了滑鼠右鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, 20, 0, 0);
            }
            else if (e.Button == MouseButtons.Left)
            {
                label3.Text = "MouseButtons.Left 你按了滑鼠左鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.Middle)
            {
                label3.Text = "MouseButtons.Middle 你按了滑鼠中鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.XButton1)
            {
                label3.Text = "MouseButtons.XButton1 你按了滑鼠上一頁";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.XButton2)
            {
                label3.Text = "MouseButtons.XButton2 你按了滑鼠下一頁";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }

        }
    }
}
