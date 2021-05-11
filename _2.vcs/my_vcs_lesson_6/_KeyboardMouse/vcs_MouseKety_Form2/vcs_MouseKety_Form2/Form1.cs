using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//C# 透過Win32控制滑鼠 mouse_event

namespace vcs_MouseKety_Form2
{
    public partial class Form1 : Form
    {
        Point mousePos; // 記錄滑鼠的位置

        [System.Runtime.InteropServices.DllImport("user32")]
        //[DllImport("user32")]
        private static extern int mouse_event(int dwFlags, int dx, int dy, int cButtons, int dwExtraInfo);
        const int MOUSEEVENTF_ABSOLUTE = 0x8000;
        const int MOUSEEVENTF_MOVE = 0x0001;        //移動鼠標
        const int MOUSEEVENTF_WHEEL = 0x0800;       //移動滾輪
        const int MOUSEEVENTF_HWHEEL = 0x01000;     //移動H滾輪
        const int MOUSEEVENTF_LEFTDOWN = 0x0002;    //左鍵按下
        const int MOUSEEVENTF_LEFTUP = 0x0004;      //左鍵放開
        const int MOUSEEVENTF_MIDDLEDOWN = 0x0020;  //中鍵按下
        const int MOUSEEVENTF_MIDDLEUP = 0x0040;    //中鍵放開
        const int MOUSEEVENTF_RIGHTDOWN = 0x0008;   //右鍵按下
        const int MOUSEEVENTF_RIGHTUP = 0x0010;     //右鍵放開
        const int MOUSEEVENTF_XDOWN = 0x0080;       //X鍵按下
        const int MOUSEEVENTF_XUP = 0x1000;         //X鍵放開

        public Form1()
        {
            InitializeComponent();
            label0.Text = "在Form上按方向鍵控制鼠標";
            label1.Text = "在Form上按滑鼠各按鍵";
            label2.Text = "按X離開";
            label3.Text = "";
            label4.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 加入滾輪事件、指定事件處理函數
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);
        }

        // 滾輪事件處理函數
        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0) // 滾輪往前
            {
                richTextBox1.Text += "滾輪往上 ";
            }
            else if (e.Delta < 0) // 滾輪往後
            {
                richTextBox1.Text += "滾輪往下 ";
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {

        }

        // 滑鼠按下事件
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄滑鼠的位置

            if (e.Button == MouseButtons.Left)
            {
                richTextBox1.Text += "滑鼠左鍵\t";
                label3.Text = "MouseButtons.Left 你按了滑鼠左鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.Middle)
            {
                richTextBox1.Text += "滑鼠中鍵\t";
                label3.Text = "MouseButtons.Middle 你按了滑鼠中鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.Right)
            {
                richTextBox1.Text += "滑鼠右鍵\t";
                label3.Text = "MouseButtons.Right 你按了滑鼠右鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, 20, 0, 0);
            }
            else if (e.Button == MouseButtons.XButton1)
            {
                richTextBox1.Text += "滑鼠上一頁\t";
                label3.Text = "MouseButtons.XButton1 你按了滑鼠上一頁";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.XButton2)
            {
                richTextBox1.Text += "滑鼠下一頁\t";
                label3.Text = "MouseButtons.XButton2 你按了滑鼠下一頁";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }

            String s = "";
            switch (e.Button)
            {
                case System.Windows.Forms.MouseButtons.Left: s = "左鍵"; break;
                case System.Windows.Forms.MouseButtons.Middle: s = "中間鍵"; break;
                case System.Windows.Forms.MouseButtons.Right: s = "右鍵"; break;
            }
            label4.Text = String.Format("按了{0}於 X：{1}, Y：{2}", s, e.X, e.Y);

            /*
            說明：利用switch來判斷e.Button按下的是那個按鍵
            需要注意的是，判讀的值在System.Windows.Forms.MouseButtons 裡對應
            */

        }

        // 滑鼠移動事件
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄滑鼠的位置
            this.Text = e.Location.ToString();
        }

        // 滑鼠放開事件
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "放開\n";
        }
    }
}


