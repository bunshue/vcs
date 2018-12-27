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
            label1.Text = "目前滑鼠位置: " + "x:" + System.Windows.Forms.Cursor.Position.X + " y:" + System.Windows.Forms.Cursor.Position.Y + "\n";
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
            label3.Text = "KeyDown";
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.A:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        label7.Text = "Ctrl + A";
                    }
                    else if ((Control.ModifierKeys & Keys.Alt) == Keys.Alt)
                    {
                        label7.Text = "Alt + A";
                    }
                    else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                    {
                        label7.Text = "Shift + A";
                    }
                    else
                    {
                        label7.Text = "A";
                    }
                    break;
                case Keys.Up:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        label7.Text = "Ctrl + 上";
                    }
                    else
                    {
                        label7.Text = "上";
                    }
                    this.Refresh();
                    break;
                case Keys.Down:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        label7.Text = "Ctrl + 下";
                    }
                    else
                    {
                        label7.Text = "下";
                    }
                    this.Refresh();
                    break;
                case Keys.Left:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        label7.Text = "Ctrl + 左";
                    }
                    else
                    {
                        label7.Text = "左";
                    }
                    break;
                case Keys.Right:
                    if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                    {
                        label7.Text = "Ctrl + 右";
                    }
                    else
                    {
                        label7.Text = "右";
                    }
                    break;
                case Keys.Add:
                    label7.Text = "+";
                    break;
                case Keys.Subtract:
                    label7.Text = "-";
                    break;
                case Keys.PageUp:
                    label7.Text = "PageUp";
                    break;
                case Keys.PageDown:
                    label7.Text = "PageDown";
                    break;
                case Keys.X:
                    label7.Text = "X";
                    Application.Exit();
                    break;
                default:
                    //label7.Text = "KeyCode: " + e.KeyCode.ToString();
                    label7.Text = e.KeyCode.ToString();
                    break;
            }
            if (e.Alt == true)
            {
                label8.Text = "Alt + ";
                //if (e.KeyCode == Keys.D)
                  //  label7.Text = "Alt + D";
            }
            if (e.Control == true)
            {
                label8.Text = "Ctrl + ";
                //if (e.KeyCode == Keys.D)
                  //  label7.Text = "Ctrl + D";
            }
            if (e.Shift == true)
            {
                label8.Text = "Shift + ";
                /*
                if (e.KeyCode == Keys.D)
                {
                    label7.Text = "Shift + D";
                    e.Handled = true;   //已處理此事件
                }
                */
            }

        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            label3.Text = "KeyPress";
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            label3.Text = "KeyUp";
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            label2.Text = "MouseDoubleClick";
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            label2.Text = "MouseDown\t" + e.X + " : " + e.Y;

            flag_mouse_down = 1;
            mouse_down_position_x = e.X;
            mouse_down_position_y = e.Y;

            if (e.Button == MouseButtons.Left)
                label6.Text = "你按了滑鼠左鍵";
            else if (e.Button == MouseButtons.Right)
                label6.Text = "你按了滑鼠右鍵";
            else if (e.Button == MouseButtons.Middle)
                label6.Text = "你按了滑鼠中鍵";
            else if (e.Button == MouseButtons.XButton1)
                label6.Text = "你按了滑鼠XButton1";
            else if (e.Button == MouseButtons.XButton2)
                label6.Text = "你按了滑鼠XButton2";
            else if (e.Button == MouseButtons.None)
                label6.Text = "你按了滑鼠None";
            else
                label6.Text = "你按了滑鼠其他鍵";
        }

        private void Form1_MouseEnter(object sender, EventArgs e)
        {
            label2.Text = "MouseEnter";
        }

        private void Form1_MouseHover(object sender, EventArgs e)
        {
            label2.Text = "MouseHover";
        }

        private void Form1_MouseLeave(object sender, EventArgs e)
        {
            label2.Text = "MouseLeave";
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            label2.Text = "MouseMove " + e.X + " : " + e.Y;

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
