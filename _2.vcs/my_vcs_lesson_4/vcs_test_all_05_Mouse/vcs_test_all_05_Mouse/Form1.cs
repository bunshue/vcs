using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_test_all_05_Mouse
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            g = this.pictureBox1.CreateGraphics();

            label1.Text = "";
            label2.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label11.Text = "滾輪";
            label12.Text = "";
            label14.Text = "";
        }

        Graphics g;
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
            label14.Text = "";


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
            if (flag_mouse_down == true)
            {
                //g.DrawRectangle(new Pen(Color.Black), new Rectangle(mouse_down_position_x, mouse_down_position_y, e.X - mouse_down_position_x, e.Y - mouse_down_position_y));
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            mouse_up_position_x = e.X;
            mouse_up_position_y = e.Y;

            label14.Text = "MouseUp   (" + e.X.ToString() + ", " + e.Y + ") 畫矩形";
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(mouse_down_position_x, mouse_down_position_y, mouse_up_position_x - mouse_down_position_x, mouse_up_position_y - mouse_down_position_y));


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
            label4.Text = "目前滑鼠在Form1上的位置：" + e.X + " : " + e.Y;
            this.Text   = "目前滑鼠在Form1上的位置：" + e.X + " : " + e.Y;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label13.Text = "目前滑鼠在整個桌面的位置：" + System.Windows.Forms.Cursor.Position.X + " : " + System.Windows.Forms.Cursor.Position.Y;
            //下同
            //label13.Text = "目前滑鼠在整個桌面的位置: " + Control.MousePosition.X + " : " + Control.MousePosition.Y;

        }

        private void delay(int delay)
        {
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < delay; j++)
                System.Threading.Thread.Sleep(1);
        }

        //移動滑鼠鼠標
        [DllImport("user32")]
        static extern bool SetCursorPos(int X, int Y);

        int screenWidth = Screen.PrimaryScreen.Bounds.Width;
        int screenHeight = Screen.PrimaryScreen.Bounds.Height;

        private void button2_Click(object sender, EventArgs e)
        {
            //移動滑鼠鼠標
            int xx = screenWidth / 2;
            int yy = screenHeight / 2;
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy - 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx + 100, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy + 100);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx - 100, yy);  //把滑鼠移到 (xx,yy) 的位置
            delay(300);
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (SystemInformation.MousePresent)  // 是否安裝滑鼠
                richTextBox1.Text += "是否安裝滑鼠 : 是\n";
            else
                richTextBox1.Text += "是否安裝滑鼠 : 否\n";

            // 滑鼠按鈕的數目
            richTextBox1.Text += "滑鼠按鈕的數目 : " + SystemInformation.MouseButtons.ToString() + "\n";

            if (SystemInformation.MouseWheelPresent) // 滑鼠是否有滾輪
                richTextBox1.Text += "滑鼠是否有滾輪 : 是\n";
            else
                richTextBox1.Text += "滑鼠是否有滾輪 : 否\n";

            // 滑鼠速度 (1 ~ 20)
            richTextBox1.Text += "滑鼠速度 (1 ~ 20) : " + SystemInformation.MouseSpeed.ToString() + "\n";

        }
    }
}
