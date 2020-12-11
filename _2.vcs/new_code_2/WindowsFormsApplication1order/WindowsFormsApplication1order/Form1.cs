using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1order
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

            richTextBox1.Text += "你按了\t" + btn.Text + "\n";
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
                    break;
                case MOVE_TO_BUTTON_ONE:
                    richTextBox1.Text += "往下一層\n";
                    break;
                default:
                    richTextBox1.Text += "XXXXXXX\n";
                    break;
            }
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
