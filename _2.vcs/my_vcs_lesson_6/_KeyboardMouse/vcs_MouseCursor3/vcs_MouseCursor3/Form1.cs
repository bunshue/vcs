using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseCursor3
{
    public partial class Form1 : Form
    {
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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
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

        //隱藏滑鼠鼠標 ST
        //重寫API函數
        [System.Runtime.InteropServices.DllImport("user32.dll", EntryPoint = "ShowCursor")]
        public extern static bool ShowCursor(bool bShow);

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Text = "按Alt+F4離開程式";
            ShowCursor(false);  //隱藏滑鼠鼠標


            //ShowCursor(true);  //顯示滑鼠鼠標
        }
        //隱藏滑鼠鼠標 SP

        //限制滑鼠只能在本表單上移動 ST
        bool flag_limit_mouse_activity_area = false;
        private void button2_Click(object sender, EventArgs e)
        {
            if (flag_limit_mouse_activity_area == false)
            {
                flag_limit_mouse_activity_area = true;
                button2.Text = "解除";

                this.Cursor = new Cursor(Cursor.Current.Handle);//创建Cursor对象
                Cursor.Position = new Point(Cursor.Position.X, Cursor.Position.Y);//设置鼠标位置
                Cursor.Clip = new Rectangle(this.Location, this.Size);//设置鼠标的活动区域
            }
            else
            {
                flag_limit_mouse_activity_area = false;
                button2.Text = "限制滑鼠只能在本表單上移動";

                Screen[] screens = Screen.AllScreens;//获取显示的数组
                this.Cursor = new Cursor(Cursor.Current.Handle);//创建Cursor对象
                Cursor.Clip = screens[0].Bounds;//接触对鼠标活动区域的限制
            }

        }
        //限制滑鼠只能在本表單上移動 SP
    }
}
