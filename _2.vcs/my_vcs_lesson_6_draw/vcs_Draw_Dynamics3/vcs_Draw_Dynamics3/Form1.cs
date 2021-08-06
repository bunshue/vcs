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
        bool transverse_direction = false;

        double one_step_second = 0.2;
        int g = 10;

        float x_st = 0;
        float y_st = 0;
        double drop_sec = 0;

        float x_st0 = 445;
        float y_st0 = 170;
        float y_sp0 = 170 + 460;    //降落距離 460

        List<float[]> pts = new List<float[]>();    //二維List for float

        int ball_size_width0 = 40;
        int ball_size_height0 = 40;

        int ball_size_width = 40;
        int ball_size_height = 40;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            x_st = x_st0;
            y_st = y_st0;

            richTextBox1.Text += "H = " + pictureBox1.Height.ToString() + "\n";
            one_step_second = ((double)trackBar1.Value) / 10;
            richTextBox1.Text += "每步 " + one_step_second.ToString() + " 秒\n";

            trackBar1_Scroll(sender, e);
            rb_bird_CheckedChanged(sender, e);
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

            richTextBox1.Size = new Size(374, 490);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "自由落體")
            {
                richTextBox1.Text += "每步 " + one_step_second.ToString() + " 秒\n";
                button1.Text = "暫停";
                timer1.Enabled = true;
                dropdown_status = true;
                pts.Clear();
            }
            else
            {
                button1.Text = "自由落體";
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

            Bitmap bmp_pisa;

            bmp_pisa = new Bitmap(@"C:\_git\vcs\_2.vcs\______test_files\_AB\Leaning_Tower_of_Pisa.jpg");

            int picture_width = bmp_pisa.Width;
            int picture_height = bmp_pisa.Height;

            //richTextBox1.Text += "W = " + bmp_pisa.Width.ToString() + ", H = " + bmp_pisa.Height.ToString() + "\n";

            int w = picture_width * 7 / 10;
            int h = picture_height * 7 / 10;

            Rectangle destRect1 = new Rectangle(0, 0, w, h);

            e.Graphics.DrawImage(bmp_pisa, destRect1, 0, 0, picture_width, picture_height, units);

            //Pen p = new Pen(Color.Red, 10);
            //e.Graphics.DrawLine(p, 480, y_st0, 480, y_st0 + 480);
            //e.Graphics.FillEllipse(new SolidBrush(Color.Red), x_st, y_st0, ball_size_width, ball_size_height);

            if (dropdown_status == false)
                return;

            SolidBrush newBrush = new SolidBrush(Color.Red);
            int point_width = 10;
            int len;
            int i;

            int ww = ball_size_width;
            int hh = ball_size_height;

            Bitmap bmp;

            if (rb1.Checked == true)
                bmp = new Bitmap(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_red.jpg");
            else if (rb2.Checked == true)
                bmp = new Bitmap(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_yellow.jpg");
            else if (rb3.Checked == true)
                bmp = new Bitmap(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_blue.jpg");
            else if (rb4.Checked == true)
                bmp = new Bitmap(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_black.jpg");
            else
                bmp = new Bitmap(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_red.jpg");

            bmp.MakeTransparent(Color.White); ;  //MakeTransparent 用法, bmp2 去背景, 可以多重去背, 連續寫即可

            //DrawFillCircle(e, x_st + ww / 2, H - y_st - hh / 2, 15, Color.Blue);

            //Rectangle destRect1 = new Rectangle(x_st - ww / 2, H - y_st - hh / 2, ww, hh);

            ww = hh * bmp.Width / bmp.Height;   //符合比例
            //e.Graphics.DrawImage(bmp, destRect1a, 0, 0, bmp.Width, bmp.Height, units);
            //e.Graphics.FillRectangle(new SolidBrush(Color.Red), x_st - ww / 2, H - y_st - hh / 2, ww, hh);

            //richTextBox1.Text += "ww = " + ww.ToString() + ", hh = " + hh.ToString() + "\n";

            if (y_st <= y_sp0)
            {
                //e.Graphics.FillEllipse(newBrush, x_st, y_st, ball_size_width, ball_size_height);
                //e.Graphics.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, ball_size_width, ball_size_height);

                Rectangle destRect1a = new Rectangle((int)x_st, (int)y_st, ww, hh);
                e.Graphics.DrawImage(bmp, destRect1a, 0, 0, bmp.Width, bmp.Height, units);

                pts.Add(new float[] { (float)drop_sec, x_st, y_st });

                len = pts.Count;
                if (len > 0)
                {
                    for (i = 0; i < len; i++)
                    {
                        e.Graphics.FillEllipse(new SolidBrush(Color.DarkGreen), pts[i][1] + ball_size_width / 2 - point_width / 2, pts[i][2] + ball_size_height / 2 - point_width / 2, 10, 10);
                    }
                }
                richTextBox1.Text += "t = " + drop_sec.ToString() + "\t" + (y_st - y_st0).ToString("n3") + "\n";

                drop_sec += one_step_second;
                if (transverse_direction == true)
                {
                    x_st = x_st0 + (float)(60 * drop_sec);
                }
                y_st = y_st0 + (float)(g * drop_sec * drop_sec * 1 / 2) * 10;   //1公尺 10點
                //int y_st2 = (int)Math.Round(y_st);
                richTextBox1.Text += "t = " + drop_sec.ToString("n3") + "\t" + (y_st - y_st0).ToString("n3") + "\n";
            }
            else
            {
                y_st = y_sp0;

                if (transverse_direction == true)
                {
                    x_st = x_st0 + (float)(60 * Math.Sqrt(2 * 46 / 10.0));
                }

                //e.Graphics.FillEllipse(newBrush, x_st, y_st, ball_size_width, ball_size_height);
                //e.Graphics.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, ball_size_width, ball_size_height);

                Rectangle destRect1a = new Rectangle((int)x_st, (int)y_st, ww, hh);
                e.Graphics.DrawImage(bmp, destRect1a, 0, 0, bmp.Width, bmp.Height, units);

                pts.Add(new float[] { (float)drop_sec, x_st, y_st });
                len = pts.Count;
                if (len > 0)
                {
                    for (i = 0; i < len; i++)
                    {
                        e.Graphics.FillEllipse(new SolidBrush(Color.DarkGreen), pts[i][1] + ball_size_width / 2 - point_width / 2, pts[i][2] + ball_size_height / 2 - point_width / 2, 10, 10);
                    }
                }

                richTextBox1.Text += "測試結束\n";

                richTextBox1.Text += "已在 : " + Math.Sqrt(2 * 46 / 10.0) + " 秒時墜地\n";

                button1.Text = "自由落體";
                transverse_direction = false;
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

            lb_interval.Text = "每步 " + one_step_second.ToString() + " 秒";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            button1.Text = "自由落體";
            transverse_direction = false;
            timer1.Enabled = false;
            dropdown_status = false;

            x_st = x_st0;
            y_st = y_st0;
            drop_sec = 0;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int i;

            int len = pts.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";

            for (i = 0; i < pts.Count; i++)
            {
                //richTextBox1.Text += pts[i][0].ToString() + "\t" + pts[i][1].ToString() + "\n";
                richTextBox1.Text += pts[i][0].ToString() + "\t" + pts[i][1].ToString() + "\t" + pts[i][2].ToString() + "\n";
            }
        }

        float mass = 1;
        int use_bird_kind = 0;

        private void rb_bird_CheckedChanged(object sender, EventArgs e)
        {
            if (rb1.Checked == true)
            {
                richTextBox1.Text += "改用 紅鳥 1 Kg\n";
                pictureBox_bird.Image = Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_red.jpg");
                mass = 1;
                use_bird_kind = 0;
            }
            else if (rb2.Checked == true)
            {
                richTextBox1.Text += "改用 黃鳥 0.6 Kg\n";
                pictureBox_bird.Image = Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_yellow.jpg");
                mass = 0.6f;
                use_bird_kind = 1;
            }
            else if (rb3.Checked == true)
            {
                richTextBox1.Text += "改用 藍鳥 0.3 Kg\n";
                pictureBox_bird.Image = Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_blue.jpg");
                mass = 0.3f;
                use_bird_kind = 2;
            }
            else if (rb4.Checked == true)
            {
                richTextBox1.Text += "改用 炸彈鳥 2 Kg\n";
                pictureBox_bird.Image = Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_black.jpg");
                mass = 2;
                use_bird_kind = 3;
            }
            else
            {
                richTextBox1.Text += "改用 紅鳥 1 Kg\n";
                pictureBox_bird.Image = Image.FromFile(@"C:\_git\vcs\_2.vcs\______test_files\_AB\AB_red.jpg");
                use_bird_kind = 0;
            }
            ball_size_width = (int)((float)ball_size_width0 * mass);
            ball_size_height = (int)((float)ball_size_height0 * mass);
            this.pictureBox1.Invalidate();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //橫拋
            if (button1.Text == "自由落體")
            {
                richTextBox1.Text += "每步 " + one_step_second.ToString() + " 秒\n";
                button1.Text = "暫停";
                transverse_direction = true;
                timer1.Enabled = true;
                dropdown_status = true;
                pts.Clear();
            }
            else
            {
                button1.Text = "自由落體";
                transverse_direction = false;
                timer1.Enabled = false;
                dropdown_status = false;
            }


        }
    }
}

