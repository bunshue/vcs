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

        float x_st = 0;
        float y_st = 0;
        double drop_sec = 0;

        float x_st0 = 445;
        float y_st0 = 170;
        float y_sp0 = 170 + 460;    //降落距離 460

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

            x_st = x_st0;
            y_st = y_st0;
        }

        void show_item_location()
        {
            int xx;
            int yy;
            int dx;
            int dy;

            xx = 50;
            yy = 50;
            dx = 0;
            dy = 0;

            pictureBox1.Size = new Size(700, 700);
            pictureBox1.Location = new Point(xx + dx * 0, yy + dy * 1);

            this.ClientSize = new Size(1200, 800);
            //this.Location = new Point(xx + dx * 0, yy + dy * 1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

            //Pen p = new Pen(Color.Red, 10);
            //e.Graphics.DrawLine(p, 480, y_st0, 480, y_st0 + 480);
            //e.Graphics.FillEllipse(new SolidBrush(Color.Red), x_st, y_st0, 20, 20);

            if (dropdown_status == false)
                return;

            SolidBrush newBrush = new SolidBrush(Color.Red);

            if (y_st <= y_sp0)
            {
                e.Graphics.FillEllipse(newBrush, x_st, y_st, 20, 20);
                e.Graphics.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, 20, 20);
                richTextBox1.Text += "t = " + drop_sec.ToString() + "\t" + (y_st - y_st0).ToString("n3") + "\n";

                drop_sec += one_step_second;
                y_st = y_st0 + (float)(g * drop_sec * drop_sec * 1 / 2) * 10;   //1公尺 10點
                //int y_st2 = (int)Math.Round(y_st);
                richTextBox1.Text += "t = " + drop_sec.ToString("n3") + "\t" + (y_st - y_st0).ToString("n3") + "\n";
            }
            else
            {
                y_st = y_sp0;

                e.Graphics.FillEllipse(newBrush, x_st, y_st, 20, 20);
                e.Graphics.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, 20, 20);

                richTextBox1.Text += "測試結束\n";

                button1.Text = "ST";
                timer1.Enabled = false;
                dropdown_status = false;

                x_st = x_st0;
                y_st = y_st0;
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

            x_st = x_st0;
            y_st = y_st0;
            drop_sec = 0;
        }

    }
}

