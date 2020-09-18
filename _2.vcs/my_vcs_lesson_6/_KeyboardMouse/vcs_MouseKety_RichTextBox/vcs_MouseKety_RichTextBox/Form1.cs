using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MouseKety_RichTextBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            label2.Text = "KeyDown";
            label3.Text = "KeyDown, 按鍵是：" + e.KeyCode;
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

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            label3.Text = "KeyPress, 按鍵是：" + e.KeyChar;
        }

        private void richTextBox1_KeyUp(object sender, KeyEventArgs e)
        {
            label4.Text = "KeyUp";
        }
    }
}
