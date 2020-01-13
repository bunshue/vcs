using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawMove
{
    public partial class Form1 : Form
    {
        string filename = "C:\\______test_files\\picture1.jpg";

        Bitmap bitmap1;
        Bitmap bitmap_tmp;
        Bitmap bitmap_old;

        bool isRunning1 = false;
        bool isRunning2 = false;
        bool isRunning3 = false;
        bool isRunning4 = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            //pictureBox1.Image = Image.FromFile(filename);


            bitmap1 = new Bitmap(filename);
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";
            bitmap_old = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning1 == false)
            {
                isRunning1 = true;
                timer1.Enabled = true;
                richTextBox1.Text += "ST\n";
            }
            else
            {
                isRunning1 = false;
                timer1.Enabled = false;
                richTextBox1.Text += "SP\n";
            }
        }

        int x_st = 0;
        int y_st = 200;

        private void timer1_Tick(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);

            Graphics g = Graphics.FromImage(bitmap1);

            if (x_st < 300)
            {
                x_st += 5;
                //y_st += 10;
                //y_st = 200 + 200 * (int)(Math.Sin((Math.PI * x_st / 180)));
                y_st = 200 + (int)(100 * (Math.Sin((Math.PI * x_st / 180))));
            }
            else
            {
                x_st = 0;
                //y_st = 0;
            }
            int ww = 10;
            int hh = 10;

            //g.DrawRectangle(new Pen(Color.Red, 1), x_st, y_st, ww, hh);
            //g.DrawEllipse(new Pen(Color.Red, 1), x_st, y_st, ww, hh);
            //g.FillEllipse(new Brush(Color.Red), x_st, y_st, ww, hh);
            g.FillEllipse(new SolidBrush(Color.Red), x_st, y_st, ww, hh);

            pictureBox1.Image = bitmap1;


            //bitmap1 = new Bitmap(filename);
            //bitmap_old = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            bitmap_old = new Bitmap(filename);
            pictureBox1.Image = bitmap_old;

        }

        private void timer_focus_Tick(object sender, EventArgs e)
        {
            if (pictureBox1.Focused == false)
            {
                richTextBox1.Text += "F ";
                pictureBox1.Focus();
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning2 == false)
            {
                isRunning2 = true;
                timer2.Enabled = true;
                richTextBox1.Text += "ST\n";
            }
            else
            {
                isRunning2 = false;
                timer2.Enabled = false;
                richTextBox1.Text += "SP\n";
            }

        }

        int step = 1;
        int xx = 0;
        int yy = 0;
        int ww = 0;
        int hh = 0;
        int thick = 10;
        int add = 10;
        int round = 0;

        private void timer2_Tick(object sender, EventArgs e)
        {
            //bitmap1 = new Bitmap(filename);

            ww = bitmap1.Width;
            hh = bitmap1.Height;

            Graphics g = Graphics.FromImage(bitmap1);

            if (step == 1)
            {
                if (xx < (ww - thick - add))
                {
                    xx += add;
                }
                else
                {
                    xx = ww - thick - 1;
                    step = 2;
                }
            }
            else if (step == 2)
            {
                if (yy < (hh - thick - add))
                {
                    yy += add;
                }
                else
                {
                    yy = hh - thick - 1;
                    step = 3;
                }
            }
            else if (step == 3)
            {
                if (xx > add)
                {
                    xx -= add;
                }
                else
                {
                    xx = 0;
                    step = 4;
                }
            }
            else if (step == 4)
            {
                if (yy > add)
                {
                    yy -= add;
                }
                else
                {
                    yy = 0;
                    step = 1;
                    round++;
                    //bitmap1 = new Bitmap(filename);
                }
            }

            if ((round % 2) == 0)
                g.FillRectangle(new SolidBrush(Color.Red), xx, yy, thick, thick);
            else
                g.FillRectangle(new SolidBrush(Color.White), xx, yy, thick, thick);

            //g.FillEllipse(new SolidBrush(Color.Red), xx, yy, 3, 3);

            pictureBox1.Image = bitmap1;


            //bitmap1 = new Bitmap(filename);
            //bitmap_old = new Bitmap(filename);
            //pictureBox1.Image = bitmap1;

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件

        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {

            if ((e.KeyCode == Keys.PageDown) || (e.KeyCode == Keys.Space))
            {
                richTextBox1.Text += "下一首\n";
            }
            else if (e.KeyCode == Keys.PageUp)
            {
                richTextBox1.Text += "上一首\n";
            }
            else if (e.KeyCode == Keys.Up)
            {
                richTextBox1.Text += "Up\n";
            }
            else if (e.KeyCode == Keys.Down)
            {
                richTextBox1.Text += "Down\n";
            }
            else if (e.KeyCode == Keys.NumPad8)
            {
                richTextBox1.Text += "Up\n";
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                }
                else
                {
                }
            }
            else if (e.KeyCode == Keys.NumPad9)
            {
                richTextBox1.Text += "Up-Right\n";
            }
            else if (e.KeyCode == Keys.NumPad2)
            {
                richTextBox1.Text += "Down\n";
            }
            else if (e.KeyCode == Keys.NumPad1)
            {
                richTextBox1.Text += "Down-Left\n";
            }
            else if (e.KeyCode == Keys.NumPad4)
            {
                richTextBox1.Text += "Left\n";
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                }
                else
                {
                }
            }
            else if (e.KeyCode == Keys.NumPad7)
            {
                richTextBox1.Text += "Up-Left\n";

                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                }
                else
                {
                }
            }
            else if (e.KeyCode == Keys.NumPad6)
            {
                richTextBox1.Text += "Right\n";
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                }
                else
                {
                }
            }
            else if (e.KeyCode == Keys.NumPad3)
            {
                richTextBox1.Text += "Down-Right\n";
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                }
            }
            else if (e.KeyCode == Keys.NumPad5)
            {
                richTextBox1.Text += "Center\n";
            }
            else if (e.KeyCode == Keys.Home)
            {
                richTextBox1.Text += "Home\n";
            }
            else if (e.KeyCode == Keys.End)
            {
                richTextBox1.Text += "End\n";
            }
            else if (e.KeyCode == Keys.Add)
            {
            }
            else if (e.KeyCode == Keys.Subtract)
            {
            }
            else if (e.KeyCode == Keys.X)
            {
            }
            else if (e.KeyCode == Keys.F1)
            {
                richTextBox1.Text += "F1 : Help\n";
            }
            else if (e.KeyCode == Keys.F10)
            {
                richTextBox1.Text += "F10 : Setup\n";
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
                richTextBox1.Text += "你按了" + e.KeyCode.ToString() + "\n";

            }






        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int tt = 0;
        int xx2 = 0;
        int yy2 = 0;
        double gg = 9.8;

        private void button6_Click(object sender, EventArgs e)
        {
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }

            if (isRunning3 == false)
            {
                isRunning3 = true;
                timer3.Enabled = true;
                richTextBox1.Text += "ST\n";
                tt = 0;
                xx2 = 0;
                yy2 = 0;
            }
            else
            {
                isRunning3 = false;
                timer3.Enabled = false;
                richTextBox1.Text += "SP\n";
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

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


        Bitmap bmp;
        Graphics g;
        Pen p;
        int t;

        int WIDTH = 720, HEIGHT = 300, AMPLITUDE = 150;

        private void button7_Click(object sender, EventArgs e)
        {
            /*
            if (bitmap1 == null)
            {
                richTextBox1.Text += "未開啟圖片\n";
                return;
            }
            */

            if (isRunning4 == false)
            {
                isRunning4 = true;
                timer4.Enabled = true;
                richTextBox1.Text += "ST\n";
                //create Bitmap
                bmp = null;
                bmp = new Bitmap(pictureBox1.Size.Width, pictureBox1.Size.Height);

                //background color
                //this.BackColor = Color.Black;

                //center
                //cx = WIDTH / 2;
                //cy = HEIGHT / 2;

                //initial degree of HAND
                //u = 0;

                //timer1.Enabled = true;
                pictureBox1.Image = null;
                t = 0;
                DrawXY();
                DrawYLine();


                //timer1.Enabled = true;



            }
            else
            {
                isRunning4 = false;
                timer4.Enabled = false;
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

        private void timer4_Tick(object sender, EventArgs e)
        {
            //pen
            p = new Pen(Color.Green, 1f);

            //graphics
            g = Graphics.FromImage(bmp);

            int xx;
            int yy;

            xx = t;
            yy = HEIGHT - (int)(AMPLITUDE * Math.Sin(Math.PI * t / 180)) - AMPLITUDE;


            g.DrawEllipse(new Pen(Color.Red, 1f), xx, yy, 1, 1);

            //load bitmap in picturebox1
            pictureBox1.Image = bmp;


            //dispose
            p.Dispose();
            g.Dispose();

            t += 3;
            if (t >= 720)
                timer1.Enabled = false;

        }


    }
}
