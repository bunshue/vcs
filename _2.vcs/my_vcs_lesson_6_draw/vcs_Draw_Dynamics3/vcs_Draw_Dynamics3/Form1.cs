using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Dynamics3
{
    public partial class Form1 : Form
    {
        bool dropdown_status = false;


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //bool angry_bird_move_status = false;

            //timer1.Enabled = !timer1.Enabled;
            if (button1.Text == "ST")
            {
                button1.Text = "SP";
                timer1.Enabled = true;
                dropdown_status = true;

            }
            else
            {
                button1.Text = "ST";
                timer1.Enabled = false;
                dropdown_status = false;

            }


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        float x_st = 20;
        float y_st = 0;
        float drop_sec = 0;
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if (dropdown_status == false)
                return;
            

            if (y_st <= (pictureBox1.Height - 50))
            {
                e.Graphics.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, 20, 20);
                //richTextBox1.Text += "t = " + drop_sec.ToString() + "\t" + y_st.ToString() + "\n";

                drop_sec += 0.2f;
                y_st = (float)(10 * drop_sec * drop_sec * 1 / 2);
                //int y_st2 = (int)Math.Round(y_st);
                richTextBox1.Text += "t = " + drop_sec.ToString() + "\t" + y_st.ToString("n2") + "\n";


                //c = (int)Math.Round(result);
                //richTextBox1.Text += "四捨五入c = " + c.ToString() + "\n";
                /*
                double pi = Math.PI;
                richTextBox1.Text += "小數點下2位\t" + pi.ToString("n2") + "\n";
                richTextBox1.Text += "小數點下4位\t" + pi.ToString("n4") + "\t四捨五入\n";
                richTextBox1.Text += "小數點下5位\t" + pi.ToString("n5") + "\n";
                richTextBox1.Text += "小數點下10位\t" + pi.ToString("n10") + "\n";
                richTextBox1.Text += "小數點下15位\t" + pi.ToString("n15") + "\n";
                */



            }
            else
            {
                button1.Text = "ST";
                timer1.Enabled = false;
            }
        }
    }
}
