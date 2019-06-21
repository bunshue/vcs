using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_MouseKeyboard
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label10.Text = "";
            g = this.CreateGraphics();
        }

        Graphics g;
        int need_clear = 0;
        int timer_cnt = 0;
        int mouse_down_position_x = 0;
        int mouse_down_position_y = 0;
        int mouse_up_position_x = 0;
        int mouse_up_position_y = 0;
        int flag_mouse_down = 0;

        private void timer1_Tick(object sender, EventArgs e)
        {
            label1.Text = "目前滑鼠在整個桌面的位置: " + "x:" + System.Windows.Forms.Cursor.Position.X + " y:" + System.Windows.Forms.Cursor.Position.Y;

            label11.Text = "目前滑鼠在整個桌面的位置: " + "x:" + Control.MousePosition.X + " y:" + Control.MousePosition.Y;

            Point pt = new Point(System.Windows.Forms.Cursor.Position.X, System.Windows.Forms.Cursor.Position.Y);

            //Color cl = GetColor(pt);	//創建Point對象, 使用Color結構獲取顏色
            //panel1.BackColor = cl;

            if ((label2.Text != "") && (need_clear == 0))
            {
                need_clear = 1;
                timer_cnt = 0;
            }
            if (timer_cnt == 20)
            {
                label2.Text = "";
                label3.Text = "";
                label4.Text = "";
                label5.Text = "";
                label6.Text = "";
                label7.Text = "";
                label8.Text = "";
                need_clear = 0;
            }
            timer_cnt++;
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            label2.Text = "MouseClick";
            label3.Text = "MouseClick";
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            label2.Text = "MouseDoubleClick";
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {

            flag_mouse_down = 1;
            mouse_down_position_x = e.X;
            mouse_down_position_y = e.Y;
        }

        private void Form1_MouseEnter(object sender, EventArgs e)
        {
        }

        private void Form1_MouseHover(object sender, EventArgs e)
        {
        }

        private void Form1_MouseLeave(object sender, EventArgs e)
        {
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            label10.Text = "目前滑鼠在這個表單的位置: " + "x:" + e.X + " y:" + e.Y;

            Point pt = new Point(e.X, e.Y);

            //Color cl = GetColor(pt);	//創建Point對象, 使用Color結構獲取顏色
            //panel2.BackColor = cl;

            label2.Text = "MouseMove ";

            if (flag_mouse_down == 1)
            {
                //g.DrawRectangle(new Pen(Color.Black), new Rectangle(mouse_down_position_x, mouse_down_position_y, e.X - mouse_down_position_x, e.Y - mouse_down_position_y));

            
            }


        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 0;
            mouse_up_position_x = e.X;
            mouse_up_position_y = e.Y;

            label2.Text = "MouseUp\t" + e.X + " : " + e.Y;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(mouse_down_position_x, mouse_down_position_y, mouse_up_position_x - mouse_down_position_x, mouse_up_position_y - mouse_down_position_y));
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            label2.Text = "Click";
            label3.Text = "Click";
            label4.Text = "Click";
        }

        [DllImport("user32")]
        static extern bool SetCursorPos(int X, int Y);
        int xx = 1920 / 2;
        int yy = 1080 / 2;
        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            label2.Text = "DoubleClick";
            label3.Text = "DoubleClick";
            label4.Text = "DoubleClick";

            label5.Text = "移動滑鼠鼠標";
            //自動 移動滑鼠
            SetCursorPos(xx, yy);  //把滑鼠移到 (xx,yy) 的位置
        }
    }
}
