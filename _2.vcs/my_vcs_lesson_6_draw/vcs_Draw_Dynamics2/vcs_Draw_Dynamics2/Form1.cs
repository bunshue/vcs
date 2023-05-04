using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for DashStyle

namespace vcs_Draw_Dynamics2
{
    public partial class Form1 : Form
    {
        Image img = Image.FromFile(@"C:\______test_files\__pic\_angry_bird\angry_bird.jpg");
        int W = 0;
        int H = 0;
        int x_st = 0;
        int y_st = 0;
        int t = 0;
        int angle = 45;
        int draw_angle = 45;
        double g = 0.5;
        int v = 18;
        int r = 300;

        public Form1()
        {
            InitializeComponent();
            W = img.Width*4/3;
            H = img.Height*4/3;
            x_st = W / 2;
            y_st = H / 2;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Size = new System.Drawing.Size(W, H);
            pictureBox1.Image = img;
            pictureBox2.Size = new System.Drawing.Size(W, 30);
            pictureBox2.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y + H);
            richTextBox1.Size = new Size(W, 190);
            richTextBox1.Location = new Point(pictureBox1.Location.X, pictureBox1.Location.Y + H + 40);


            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件
            angle = trackBar1.Value;
            v = trackBar2.Value;
            lb_angle.Text = trackBar1.Value.ToString();
            lb_speed.Text = trackBar2.Value.ToString();
            lb_mass.Text = "質量 " + 10 + " 公斤";
            lb_v0.Text = "初速度 " + trackBar2.Value.ToString() + " m/s";
            lb_energy.Text = "能量 " + ((10 * trackBar2.Value * trackBar2.Value) / 2).ToString() + " 焦耳";
            lb_total_power.Text = "總能量 " + 10000 + " 焦耳";
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space)
            {
                label1.Text = "Space";
            }
            else if (e.KeyCode == Keys.PageDown)
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
                y_st -= 20;
            }
            else if (e.KeyCode == Keys.Down)
            {
                label1.Text = "Down";
                y_st += 20;
            }
            else if (e.KeyCode == Keys.Left)
            {
                label1.Text = "Left";
                x_st -= 20;
            }
            else if (e.KeyCode == Keys.Right)
            {
                label1.Text = "Right";
                x_st += 20;
            }
            else if (e.KeyCode == Keys.X)
            {
                Application.Exit();
            }
            else
            {
                label1.Text = "你按了" + e.KeyCode.ToString();
            }
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {

        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            x_st = e.X;
            y_st = e.Y;
            this.pictureBox1.Invalidate();
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

        private void DrawFillCircle(PaintEventArgs e, int center_x, int center_y, int radius, Color c)
        {
            SolidBrush newBrush = new SolidBrush(c);

            // Fill the circle
            e.Graphics.FillEllipse(newBrush, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            newBrush.Dispose();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int x_st;
            int y_st;


            SolidBrush redBrush = new SolidBrush(Color.Red);
            //e.Graphics.DrawRectangle(new Pen(Color.Red, 1), x_st - sw / 2, y_st - sh / 2, sw, sh);


            x_st = (int)(v * Math.Cos(angle * Math.PI / 180) * t);  //s = vt
            //y_st = (int)(v * Math.Sin(angle * Math.PI / 180) * t - (1 / 2) * g * t * t);  //s = vt - 1/2*g*t^2;
            //y_st = (int)(v * Math.Sin(angle * Math.PI / 180) * t*100 - (g * t * t) / 2);  //s = vt - 1/2*g*t^2;
            y_st = (int)(v * Math.Sin(angle * Math.PI / 180) * t - (g * t * t) / 2);  //s = vt - 1/2*g*t^2;

            if (y_st < 0)
            {
                timer1.Enabled = false;
                //button1_Click(sender, e);
            }

            //richTextBox1.Text += "t = " + t.ToString() + ", x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";

            //dy = (int)(r * Math.Sin(i * Math.PI / 180));

            //e.Graphics.FillEllipse(redBrush, x, H - y, 20, 20);
            //e.Graphics.FillEllipse(redBrush, x_st, H-y_st, 20, 20);

            //private void DrawCircle(PaintEventArgs e, int center_x, int center_y, int radius, int linewidth, Color c)
            DrawCircle(e, x_st, H - y_st, 15, 2, Color.Red);
            DrawFillCircle(e, x_st, H - y_st, 15, Color.Red);

            Point p1 = new Point();
            Point p2 = new Point();

            p1.X = 0;
            p1.Y = H - 0;
            p2.X = (int)(r * Math.Cos(draw_angle * Math.PI / 180));
            p2.Y = H - (int)(r * Math.Sin(draw_angle * Math.PI / 180));

            Pen p = new Pen(Color.Red, 2);
            p.DashStyle = DashStyle.Dot;
            e.Graphics.DrawLine(p, p1, p2);

            int dw = 0;
            int dh = 20;
            int max = trackBar2.Maximum;
            int min = trackBar2.Minimum;

            dw = pictureBox1.Width * (trackBar2.Value - trackBar2.Minimum + 1) / (trackBar2.Maximum - trackBar2.Minimum + 1);
            //richTextBox1.Text += "max = " + max.ToString() + ", min = " + min.ToString() + "\n";

            //SolidBrush newBrush = new SolidBrush(c);
            //e.Graphics.FillRectangle(new SolidBrush(Color.Red), 0, H - dh, dw, dh);
            
            label1.Text = t.ToString();
            this.pictureBox2.Invalidate();
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            int dw = 0;
            int dh = 20;
            int max = trackBar2.Maximum;
            int min = trackBar2.Minimum;

            dw = pictureBox1.Width * (trackBar2.Value - trackBar2.Minimum + 1) / (trackBar2.Maximum - trackBar2.Minimum + 1);
            //richTextBox1.Text += "max = " + max.ToString() + ", min = " + min.ToString() + "\n";

            //SolidBrush newBrush = new SolidBrush(c);
            e.Graphics.FillRectangle(new SolidBrush(Color.Red), 0, 0, dw, pictureBox2.Size.Height);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
            t += 1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            t = 0;
            angle = trackBar1.Value;
            v = trackBar2.Value;
            timer1.Enabled = true;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            draw_angle = trackBar1.Value;
            lb_angle.Text = trackBar1.Value.ToString();
            this.Invalidate();
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            lb_speed.Text = trackBar2.Value.ToString();
            this.Invalidate();
        }

        /*
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            int sx = x_st - sw / 2;
            int sy = y_st - sh / 2;

            Rectangle srcRect = new Rectangle(sx, sy, sw, sh);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;

            Image img = Image.FromFile("c:\\______test_files1\\picture1.jpg");

            //Bitmap bitmap = new Bitmap(srcRect.Width, srcRect.Height);
            //             貼上位置x,貼上位置y,貼上大小W,貼上大小H
            //g.DrawImage(img, x_st, y_st, W * 10 / 10, H * 10 / 10);

            // 準備貼上的位置與放大縮小量,以平行四邊形(parallelogram)的左上點右上點左下點表示
            int x_st2 = pictureBox2.Width / 2 - sw / 2;
            int y_st2 = pictureBox2.Height / 2 - sh / 2;
            label1.Text = "x_st2 = " + x_st2.ToString() + ", y_st2 = " + y_st2.ToString();

            Point ulCorner = new Point(x_st2, y_st2);
            Point urCorner = new Point(x_st2 + sw * 3, y_st2);
            Point llCorner = new Point(x_st2, y_st2 + sh * 3);

            Point[] destRect1 = { ulCorner, urCorner, llCorner };

            //擷取部分圖片貼上
            //            貼上位置與大小,擷取部分圖片位置與大小,單位

            e.Graphics.DrawImage(img, destRect1, srcRect, units);

        */



            /*
                //擷取部分圖片貼上
                //            貼上位置與大小,擷取部分圖片位置與大小,單位
                g.DrawImage(img, destRect1, srcRect, units);

            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);

                bitmap.Save("test.jpg", ImageFormat.Jpeg);
             */


        //}

    }
}
