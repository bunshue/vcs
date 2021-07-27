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

        double one_step_second = 0.2;
        int g = 10;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "H = " + pictureBox1.Height.ToString() + "\n";
            one_step_second = ((double)trackBar1.Value) / 10;
            richTextBox1.Text += "每步 " + one_step_second.ToString() + " 秒\n";


        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 50;
            y_st = 50;
            dx = 0;
            dy = 0;

            pictureBox1.Size = new Size(700, 700);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);


            this.ClientSize = new Size(1200, 800);
            //this.Location = new Point(x_st + dx * 0, y_st + dy * 1);

        }


        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "ST")
            {
                richTextBox1.Text += "每步 " + one_step_second.ToString() + " 秒\n";
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
        double drop_sec = 0;

        float x_st0 = 445;
        float y_st0 = 170;

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            GraphicsUnit units = GraphicsUnit.Pixel;

            Bitmap bmp;

            bmp = new Bitmap("..//..//Leaning_Tower_of_Pisa.jpg");

            int w = bmp.Width;
            int h = bmp.Height;

            //richTextBox1.Text += "W = " + bmp.Width.ToString() + ", H = " + bmp.Height.ToString() + "\n";

            int ww = w * 7 / 10;
            int hh = h * 7 / 10;

            Rectangle destRect1 = new Rectangle(0, 0, ww, hh);

            e.Graphics.DrawImage(bmp, destRect1, 0, 0, w, h, units);

            Pen p = new Pen(Color.Red, 10);
            e.Graphics.DrawLine(p, 480, 150, 480, 500 + 150);

            e.Graphics.FillEllipse(new SolidBrush(Color.Red), x_st0, y_st0, 20, 20);

            if (dropdown_status == false)
                return;

            if (y_st <= (pictureBox1.Height - 100))
            {

                SolidBrush newBrush = new SolidBrush(Color.Red);

                e.Graphics.FillEllipse(newBrush, 450, y_st, 20, 20);


                e.Graphics.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, 20, 20);
                //richTextBox1.Text += "t = " + drop_sec.ToString() + "\t" + y_st.ToString() + "\n";

                drop_sec += one_step_second;
                y_st = (float)(g * drop_sec * drop_sec * 1 / 2);
                //int y_st2 = (int)Math.Round(y_st);
                richTextBox1.Text += "t = " + drop_sec.ToString("n3") + "\t" + y_st.ToString("n3") + "\n";


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
                richTextBox1.Text += "測試結束\n";

                button1.Text = "ST";
                timer1.Enabled = false;
                dropdown_status = false;

                x_st = 20;
                y_st = 0;
                drop_sec = 0;

            }
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            one_step_second = ((double)trackBar1.Value) / 10;
            richTextBox1.Text += "每步 " + one_step_second.ToString() + " 秒\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            button1.Text = "ST";
            timer1.Enabled = false;
            dropdown_status = false;

            x_st = 20;
            y_st = 0;
            drop_sec = 0;
        }

        private void DrawCircle(PaintEventArgs e, int center_x, int center_y, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);

            // Draw the circle
            e.Graphics.DrawEllipse(p, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            p.Dispose();
        }


    }
}
