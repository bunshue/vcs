using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_StackOrder
{
    public partial class Form1 : Form
    {
        private const int MOVE_TO_TOP_MOST = 0x00;
        private const int MOVE_TO_BUTTOM_MOST = 0x01;
        private const int MOVE_TO_TOP_ONE = 0x02;
        private const int MOVE_TO_BUTTON_ONE = 0x03;

        int move_status = 0;

        public Form1()
        {
            InitializeComponent();
        }

        void show_info(object sender)
        {
            Button btn = sender as Button;

            int index = btn.Parent.Controls.GetChildIndex(btn);
            richTextBox1.Text += "index = " + index.ToString() + "\n";

            richTextBox1.Text += "你按了\t" + btn.Name + " " + btn.Text + "\n";
            switch (move_status)
            {
                case MOVE_TO_TOP_MOST:
                    richTextBox1.Text += "到最上層\n";
                    btn.BringToFront();
                    break;
                case MOVE_TO_BUTTOM_MOST:
                    richTextBox1.Text += "到最下層\n";
                    btn.SendToBack();
                    break;
                case MOVE_TO_TOP_ONE:
                    richTextBox1.Text += "往上一層\n";
                    if (index > 0)
                    {
                        index--;
                        btn.Parent.Controls.SetChildIndex(btn, index);
                    }
                    break;
                case MOVE_TO_BUTTON_ONE:
                    richTextBox1.Text += "往下一層\n";
                    index++;
                    btn.Parent.Controls.SetChildIndex(btn, index);
                    break;
                default:
                    richTextBox1.Text += "XXXXXXX\n";
                    break;
            }


            richTextBox1.Text += "順序:\t" + button1.Parent.Controls.GetChildIndex(button1).ToString() + " " +
                button2.Parent.Controls.GetChildIndex(button2).ToString() + " " +
                button3.Parent.Controls.GetChildIndex(button3).ToString() + " " +
                button4.Parent.Controls.GetChildIndex(button4).ToString() + " " +
                button5.Parent.Controls.GetChildIndex(button5).ToString() + " " +
                button6.Parent.Controls.GetChildIndex(button6).ToString() + " " +
                button7.Parent.Controls.GetChildIndex(button7).ToString() + "\n";
        }


        private void button1_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_TOP_ONE;
            show_info(sender);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_TOP_MOST;
            show_info(sender);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_BUTTON_ONE;
            show_info(sender);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_TOP_MOST;
            show_info(sender);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_BUTTON_ONE;
            show_info(sender);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_BUTTOM_MOST;
            show_info(sender);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            move_status = MOVE_TO_BUTTOM_MOST;
            show_info(sender);

        }
    }
}
