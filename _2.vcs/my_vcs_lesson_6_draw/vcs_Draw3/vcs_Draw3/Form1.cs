using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_Draw3
{
    public partial class Form1 : Form
    {
        Graphics g1;
        Graphics g2;
        Pen p;
        //SolidBrush sb;
        //Bitmap bitmap1;
        Bitmap bitmap2;
        Bitmap bitmap3;

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            //pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            g1 = panel1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g1.Clear(Color.Red);             //useless??
            panel1.BackColor = Color.Pink;

        }


        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 800;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        bool isRunning1 = false;
        bool isRunning2 = false;
        bool isRunning3 = false;
        bool isRunning4 = false;

        string filename = "C:\\______test_files\\picture1.jpg";
        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            //pictureBox2.Image = Image.FromFile(filename);

            bitmap3 = new Bitmap(filename);
            richTextBox1.Text += "W = " + bitmap3.Width.ToString() + " H = " + bitmap3.Height.ToString() + "\n";
            pictureBox2.Size = bitmap3.Size;
            pictureBox2.Image = bitmap3;
            pictureBox2.Location = new Point(400, 300);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning1 == false)
            {
                isRunning1 = true;
                timer4.Enabled = true;
                richTextBox1.Text += "ST\n";
            }
            else
            {
                isRunning1 = false;
                timer4.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        int tt = 0;
        int xx2 = 0;
        int yy2 = 0;
        double gg = 9.8;
        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning3 == false)
            {
                isRunning3 = true;
                timer6.Enabled = true;
                richTextBox1.Text += "ST\n";
                tt = 0;
                xx2 = 0;
                yy2 = 0;
            }
            else
            {
                isRunning3 = false;
                timer6.Enabled = false;
                richTextBox1.Text += "SP\n";
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap_old;
            bitmap_old = new Bitmap(filename);
            pictureBox2.Image = bitmap_old;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning2 == false)
            {
                isRunning2 = true;
                timer5.Enabled = true;
                richTextBox1.Text += "ST\n";
            }
            else
            {
                isRunning2 = false;
                timer5.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning2 == false)
            {
                isRunning2 = true;
                timer8.Enabled = true;
                richTextBox1.Text += "ST\n";
                round8 = 0;
            }
            else
            {
                isRunning2 = false;
                timer8.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        Bitmap bmp;
        Graphics g;
        Pen p4;
        int t;

        //int WIDTH = 720;
        int HEIGHT = 300;
        int AMPLITUDE = 150;

        private void button6_Click(object sender, EventArgs e)
        {
            /*
            if (bitmap3 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }
             */

            if (isRunning4 == false)
            {
                isRunning4 = true;
                timer7.Enabled = true;
                richTextBox1.Text += "ST\n";

                pictureBox2.Width = 640;
                pictureBox2.Height = 480;
                pictureBox2.Location = new Point(400, 300);

                //create Bitmap
                bmp = null;
                bmp = new Bitmap(pictureBox2.Size.Width, pictureBox2.Size.Height);

                //background color
                //this.BackColor = Color.Black;

                //center
                //cx = WIDTH / 2;
                //cy = HEIGHT / 2;

                //initial degree of HAND
                //u = 0;

                //timer1.Enabled = true;
                pictureBox2.Image = null;
                t = 0;
                DrawXY();
                DrawYLine();

                //timer1.Enabled = true;
            }
            else
            {
                isRunning4 = false;
                timer7.Enabled = false;
                richTextBox1.Text += "SP\n";
            }
        }

        private void DrawXY()//画X轴Y轴
        {
            //graphics
            g = Graphics.FromImage(bmp);
            System.Drawing.Point px1 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.pictureBox1.Width * 90 / 100, this.pictureBox1.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.pictureBox1.Width * 10 / 100, this.pictureBox1.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        private void DrawYLine()    //画X轴刻度
        {
            //graphics
            g = Graphics.FromImage(bmp);
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.pictureBox1.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.pictureBox1.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            g.Dispose();
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }


        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        double degree = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int r = 150;
            int x;
            int y;
            degree += 0.1;
            x = r + (int)(r * Math.Cos(degree * Math.PI / 180));
            y = r + (int)(r * Math.Sin(degree * Math.PI / 180));

            g1.Clear(Color.Pink);

            Point point1a = new Point(r, r);
            Point point2a = new Point(x, y);
            g1.DrawLine(p, point1a, point2a);     // Draw line to screen.


        }

        int cnt = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            cnt++;

            if ((cnt % 4) == 0)
            {
                p0.BackColor = Color.Blue;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 1)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Blue;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 2)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Blue;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 3)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Blue;
            }
        }


        int x_st = 0;
        int y_st = 0;
        int xx = 0;
        int yy = 0;
        int step = 60;
        Pen pen = new Pen(Color.Blue, 30);

        private void timer3_Tick(object sender, EventArgs e)
        {
            int w = pictureBox1.Width;
            int h = pictureBox1.Height;
            //richTextBox1.Text += "w = " + w.ToString() + " h = " + h.ToString() + "\n";
            if ((xx < (w - 1)) && (yy == 0))
            {
                if (xx == 0)
                {
                    if (pen.Color == Color.Red)
                        pen.Color = Color.Blue;
                    else
                        pen.Color = Color.Red;
                }

                //richTextBox1.Text += "1";
                if (xx < (w - step))
                    xx += step;
                else
                    xx = w - 1;
            }
            else if ((yy < (h - 1)) && (xx == (w - 1)))
            {
                //richTextBox1.Text += "2";
                if (yy < (h - step))
                    yy += step;
                else
                    yy = h - 1;
            }
            else if ((xx > 0) && (yy == (h - 1)))
            {
                //richTextBox1.Text += "3";
                if (xx > step)
                    xx -= step;
                else
                    xx = 0;
            }
            else if ((yy > 0) && (xx == 0))
            {
                //richTextBox1.Text += "4";
                if (yy > step)
                    yy -= step;
                else
                    yy = 0;
            }
            else
            {
                richTextBox1.Text += "xxxxxx\n";
            }

            if (pen.Color == Color.Red)
                pen.Color = Color.Blue;
            else
                pen.Color = Color.Red;


            //richTextBox1.Text += "\t(" + x_st.ToString() + "," + y_st.ToString() + ")-" + "(" + xx.ToString() + "," + yy.ToString() + ")" + "\n";

            g2.DrawLine(pen, x_st, y_st, xx, yy);
            x_st = xx;
            y_st = yy;

            pictureBox1.Image = bitmap2;


        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                //新建圖檔, 初始化畫布
                bitmap2 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
                g2 = Graphics.FromImage(bitmap2);
                g2.Clear(Color.White);
                pictureBox1.Image = bitmap2;

                timer3.Enabled = true;
                pictureBox1.Location = new Point(10, 350);
                pictureBox1.Size = new Size(300, 200);
            }
            else
            {
                timer3.Enabled = false;

            }

        }

        int x_st4 = 0;
        int y_st4 = 200;

        private void timer4_Tick(object sender, EventArgs e)
        {
            bitmap3 = new Bitmap(filename);

            Graphics g = Graphics.FromImage(bitmap3);

            if (x_st4 < 300)
            {
                x_st4 += 5;
                //y_st4 += 10;
                //y_st4 = 200 + 200 * (int)(Math.Sin((Math.PI * x_st4 / 180)));
                y_st4 = 200 + (int)(100 * (Math.Sin((Math.PI * x_st4 / 180))));
            }
            else
            {
                x_st4 = 0;
                //y_st4 = 0;
            }
            int ww = 10;
            int hh = 10;

            //g.DrawRectangle(new Pen(Color.Red, 1), x_st4, y_st4, ww, hh);
            //g.DrawEllipse(new Pen(Color.Red, 1), x_st4, y_st4, ww, hh);
            //g.FillEllipse(new Brush(Color.Red), x_st4, y_st4, ww, hh);
            g.FillEllipse(new SolidBrush(Color.Red), x_st4, y_st4, ww, hh);

            pictureBox2.Image = bitmap3;


            //bitmap1 = new Bitmap(filename);
            //bitmap_old = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;


        }

        int step3 = 1;
        int xx3 = 0;
        int yy3 = 0;
        int ww = 0;
        int hh = 0;
        int thick5 = 10;
        int add = 10;
        int round = 0;

        private void timer5_Tick(object sender, EventArgs e)
        {
            //bitmap1 = new Bitmap(filename);

            ww = bitmap3.Width;
            hh = bitmap3.Height;

            Graphics g = Graphics.FromImage(bitmap3);

            if (step3 == 1)
            {
                if (xx3 < (ww - thick5 - add))
                {
                    xx3 += add;
                }
                else
                {
                    xx3 = ww - thick5 - 1;
                    step3 = 2;
                }
            }
            else if (step3 == 2)
            {
                if (yy3 < (hh - thick5 - add))
                {
                    yy3 += add;
                }
                else
                {
                    yy3 = hh - thick5 - 1;
                    step3 = 3;
                }
            }
            else if (step3 == 3)
            {
                if (xx3 > add)
                {
                    xx3 -= add;
                }
                else
                {
                    xx3 = 0;
                    step3 = 4;
                }
            }
            else if (step3 == 4)
            {
                if (yy3 > add)
                {
                    yy3 -= add;
                }
                else
                {
                    yy3 = 0;
                    step3 = 1;
                    round++;
                    //bitmap1 = new Bitmap(filename);
                }
            }

            if ((round % 2) == 0)
                g.FillRectangle(new SolidBrush(Color.Red), xx3, yy3, thick5, thick5);
            else
                g.FillRectangle(new SolidBrush(Color.White), xx3, yy3, thick5, thick5);

            //g.FillEllipse(new SolidBrush(Color.Red), xx3, yy3, 3, 3);

            pictureBox2.Image = bitmap3;


            //bitmap1 = new Bitmap(filename);
            //bitmap_old = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;



        }

        int step8 = 1;
        int step8_old = -1;
        int round8 = 0;
        int W;
        int H;
        int w;
        int h;
        //int ratio = 7;

        int x_st8 = 0;
        int y_st8 = 0;
        int count = 0;
        int count_old = 0;

        private void timer8_Tick(object sender, EventArgs e)
        {
            W = bitmap3.Width;
            H = bitmap3.Height;

            w = 25;
            h = 25;

            //richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + " w = " + w.ToString() + " h = " + h.ToString() + "\n";
            
            Graphics g = Graphics.FromImage(bitmap3);

            g.FillRectangle(new SolidBrush(Color.Red), 0, 0, w, h);

            if (step8 == 1)
            {
                //if (x_st8 < (W - w * (round8 + 2)))
                if ((x_st8 + w) < (W -w * round8-w))
                {
                    x_st8 = x_st8 + w;
                    richTextBox1.Text += "U ";
                }
                else
                {
                    x_st8 = W - w * round8 - w;
                    step8 = 2;
                    richTextBox1.Text += "u ";
                }
                //richTextBox1.Text += x_st8.ToString() + " ";
                count++;
            }
            else if (step8 == 2)
            {
                if ((y_st8 + h) < (H - h * round8-h))
                {
                    y_st8 = y_st8 + h;
                    richTextBox1.Text += "R ";
                }
                else
                {
                    //y_st8 = H - h * (round8 + 1) - 1;
                    y_st8 = H - h * round8 - h;
                    step8 = 3;
                    richTextBox1.Text += "r ";
                }
                //richTextBox1.Text += y_st8.ToString() + " ";
                count++;
            }
            else if (step8 == 3)
            {
                //if ((x_st8 - w * round8) > w)
                if ((x_st8 - w)> (w* round8))
                {
                    x_st8 -= w;
                    richTextBox1.Text += "D ";
                }
                else
                {
                    x_st8 = w * round8;
                    step8 = 4;
                    richTextBox1.Text += "d ";
                }
                //richTextBox1.Text += x_st8.ToString() + " ";
                count++;
            }
            else if (step8 == 4)
            {
                if ((y_st8 - h) > (h * round8))
                {
                    y_st8 -= h;
                    richTextBox1.Text += "L ";
                }
                else
                {
                    step8 = 1;
                    round8++;
                    x_st8 = w * round8;
                    y_st8 = h * round8;
                }
                //richTextBox1.Text += y_st8.ToString() + " ";
                count++;
            }

            if (step8_old != step8)
            {
                step8_old = step8;
                richTextBox1.Text += "\nstep = " + step8.ToString() + "\t";

                richTextBox1.Text += "count = " + count.ToString() + " ";
                if (count > 1)
                {
                    if ((count - count_old) == 1)
                    {
                        timer8.Enabled = false;
                        return;
                    }
                    else
                    {
                        count_old = count;
                    }
                }


                //count = 0;
            }

            if (step8 == 1)
            {
                g.FillRectangle(new SolidBrush(Color.Red), x_st8, y_st8, w, h);
            }
            else if (step8 == 2)
            {
                g.FillRectangle(new SolidBrush(Color.Green), x_st8, y_st8, w, h);
            }
            else if (step8 == 3)
            {
                g.FillRectangle(new SolidBrush(Color.Blue), x_st8, y_st8, w, h);
                //richTextBox1.Text += "(" + x_st8.ToString() + "," + y_st8.ToString() + ") ";
            }
            else if (step8 == 4)
            {
                g.FillRectangle(new SolidBrush(Color.Cyan), x_st8, y_st8, w, h);
            }


            richTextBox1.Text += "(" + x_st8.ToString() + "," + y_st8.ToString() + ") ";

            pictureBox2.Image = bitmap3;

        }

        private void timer6_Tick(object sender, EventArgs e)
        {
            bitmap3 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap3);
            pictureBox2.Image = bitmap3;

            /*
            xx += 2;
            yy += 2;
            //g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);

            //g.DrawEllipse(new Pen(Color.Red, 3), xx, yy, 20, 20);
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(xx, yy, 20, 20));

            if (xx >= 300)
                yy -= 4;

            if (xx >= 600)
                timer1.Enabled = false;
            */

            tt++;
            xx2 = tt * 30;
            yy2 = (int)(gg * tt * tt / 2);
            //g.DrawLine(new Pen(Color.Red, 1), x_st, y_st + awb_block * i, x_st + search_size - 1, y_st + awb_block * i);

            //g.DrawEllipse(new Pen(Color.Red, 3), xx, yy, 20, 20);
            g.FillEllipse(new SolidBrush(Color.Red), new Rectangle(xx2, yy2, 20, 20));

            if (xx2 >= 200)
                yy2 -= 4;

            if (xx2 >= 800)
            {
                tt = 0;
                xx2 = 0;
                yy2 = 0;

            }

        }

        private void timer7_Tick(object sender, EventArgs e)
        {
            //pen
            p4 = new Pen(Color.Green, 1f);

            //graphics
            g = Graphics.FromImage(bmp);

            int xx;
            int yy;

            xx = t;
            yy = HEIGHT - (int)(AMPLITUDE * Math.Sin(Math.PI * t / 180)) - AMPLITUDE;


            g.DrawEllipse(new Pen(Color.Red, 1f), xx, yy, 1, 1);

            //load bitmap in picturebox1
            pictureBox2.Image = bmp;


            //dispose
            p4.Dispose();
            g.Dispose();

            t += 3;
            if (t >= 720)
                timer1.Enabled = false;


        }




    }
}
