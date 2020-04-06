using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1updown
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Up:       // 判斷是否按鍵盤上鍵
                    label1.Text = "上";
                    break;
                case Keys.Down:      // 判斷是否按鍵盤下鍵
                    label1.Text = "下";

                    break;
                case Keys.Left:    // 判斷是否按鍵盤左鍵
                    label1.Text = "左";
                    break;
                case Keys.Right:   // 判斷是否按鍵盤右鍵
                    label1.Text = "右";
                    break;
                default:
                    label1.Text = "Form1_KeyDown你按了" + e.KeyCode.ToString() + "";
                    break;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.PageDown)
            {
                label1.Text = "PageDown";
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                label1.Text = "PageUp";
            }
            else if (e.KeyCode == Keys.Up)
            {
                label1.Text = "Up";
            }
            else if (e.KeyCode == Keys.Down)
            {
                label1.Text = "Down";
            }
            else if (e.KeyCode == Keys.Left)
            {
                label1.Text = "Left";
            }
            else if (e.KeyCode == Keys.Right)
            {
                label1.Text = "Right";
            }
            else if (e.KeyCode == Keys.NumPad8)
            {
                label1.Text = "NumPad8";
            }
            else if (e.KeyCode == Keys.NumPad9)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad9";
                }
                else
                {
                    label1.Text = "NumPad9";
                }
            }
            else if (e.KeyCode == Keys.NumPad2)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad2";
                }
                else
                {
                    label1.Text = "NumPad2";
                }
            }
            else if (e.KeyCode == Keys.NumPad1)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad1";
                }
                else
                {
                    label1.Text = "NumPad1";
                }
            }
            else if (e.KeyCode == Keys.NumPad4)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad4";
                }
                else
                {
                    label1.Text = "NumPad4";
                }
            }
            else if (e.KeyCode == Keys.NumPad7)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad7";
                }
                else
                {
                    label1.Text = "NumPad7";
                }
            }
            else if (e.KeyCode == Keys.NumPad6)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad6";
                }
                else
                {
                    label1.Text = "NumPad6";
                }
            }
            else if (e.KeyCode == Keys.NumPad3)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    label1.Text = "ctrl + NumPad3";
                }
                else
                {
                    label1.Text = "NumPad3";
                }
            }
            else if (e.KeyCode == Keys.NumPad5)
            {
                label1.Text = "NumPad5";
            }
            else if (e.KeyCode == Keys.Home)
            {
                label1.Text = "Home";
            }
            else if (e.KeyCode == Keys.End)
            {
                label1.Text = "End";
            }
            else if (e.KeyCode == Keys.Add)
            {
                label1.Text = "ADD";
            }
            else if (e.KeyCode == Keys.Subtract)
            {
                label1.Text = "Substract";
            }
            else if (e.KeyCode == Keys.X)
            {
                Application.Exit();
            }
            else if (e.KeyCode == Keys.F1)
            {
                label1.Text = "F1 : Help";
            }
            else if (e.KeyCode == Keys.F10)
            {
                label1.Text = "F10 : Setup";
            }
            else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
            {
                if (e.KeyCode == Keys.W)
                {
                }
                else if (e.KeyCode == Keys.H)
                {
                }
            }
            else if ((e.KeyCode == Keys.Return) || (e.KeyCode == Keys.Escape))
            {
            }
            else
            {
                label1.Text = "pictureBox1_KeyDown你按了" + e.KeyCode.ToString() + "";

            }




        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //pictureBox1.Focus();
            this.Focus();
        }


    }
}
