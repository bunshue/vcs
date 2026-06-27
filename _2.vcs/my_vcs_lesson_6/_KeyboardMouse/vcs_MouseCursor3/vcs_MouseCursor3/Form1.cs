using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_MouseCursor3
{
    public partial class Form1 : Form
    {
        [DllImport("user32")]
        private static extern int mouse_event(int dwFlags, int dx, int dy, int cButtons, int dwExtraInfo);
        //可以設置鼠標指針絕對的位置，而且可以以相對坐標來設置。另外，該函數還可以模擬鼠標左右鍵點擊、鼠標滾輪操作等

        const int MOUSEEVENTF_MOVE = 0x0001;
        const int MOUSEEVENTF_LEFTDOWN = 0X0002;
        const int MOUSEEVENTF_LEFTUP = 0X0004;
        const int MOUSEEVENTF_RIGHTDOWN = 0X0008;
        const int MOUSEEVENTF_RIGHTUP = 0X0010;
        const int MOUSEEVENTF_MIDDLEDOWN = 0X0020;
        const int MOUSEEVENTF_MIDDLEUP = 0X0040;
        const int MOUSEEVENTF_ABSOLUTE = 0X8000;

        enum MouseEventFlag : uint
        {
            Move = 0x0001,
            LeftDown = 0x0002,
            LeftUp = 0x0004,
            RightDown = 0x0008,
            RightUp = 0x0010,
            MiddleDown = 0x0020,
            MiddleUp = 0x0040,
            XDown = 0x0080,
            XUp = 0x0100,
            Wheel = 0x0800,
            VirtualDesk = 0x4000,
            Absolute = 0x8000
        }

        [DllImport("user32.dll")]
        static extern bool SetCursorPos(int X, int Y);
        //該函數可以改變鼠標指針的位置。其中X，Y是相對於屏幕左上角的絕對位置。

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            //this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            //this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Down)
            {
                this.Text = "下";
                mouse_event(MOUSEEVENTF_MOVE, 0, 20, 0, 0);
            }
            else if (e.KeyCode == Keys.Up)
            {
                this.Text = "上";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.KeyCode == Keys.Left)
            {
                this.Text = "左";
                mouse_event(MOUSEEVENTF_MOVE, -20, 0, 0, 0);
            }
            else if (e.KeyCode == Keys.Right)
            {
                this.Text = "右";
                mouse_event(MOUSEEVENTF_MOVE, 20, 0, 0, 0);
            }
            else
            {
                this.Text = "其他按鍵";
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "A";
            if (e.Button == MouseButtons.Right)
            {
                this.Text = "滑鼠右鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, 20, 0, 0);
            }
            else if (e.Button == MouseButtons.Left)
            {
                this.Text = "滑鼠左鍵";
                mouse_event(MOUSEEVENTF_MOVE, 0, -20, 0, 0);
            }
            else if (e.Button == MouseButtons.Middle)
            {
                this.Text = "滑鼠中鍵";
                mouse_event(MOUSEEVENTF_MOVE, -20, 0, 0, 0);
            }
            else
            {
                this.Text = "滑鼠 其他 鍵";
            }
        }

    }
}
