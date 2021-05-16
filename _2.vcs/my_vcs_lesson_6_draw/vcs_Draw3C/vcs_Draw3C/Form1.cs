using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode
using System.Drawing.Text;      //for TextRenderingHint
using System.IO;                //for File

namespace vcs_Draw3C
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        //數字 8 雙扭線 (Lemniscate of Bernoulli) ST
        G2D_LemniscateOfBernoulli lob;

        int angle0 = 0; // 數字 8 曲線公式的參數值(角度 0 ~ 359)

        int cx0, cy0;  // 中心點
        int radius0; // 半徑
        //數字 8 雙扭線 (Lemniscate of Bernoulli) SP

        //Maurer Rose 玫瑰線 ST
        double rose_x0, rose_y0, rose_x1, rose_y1;
        float k_rose = 2;  // 係數
        float d_rose = 29; // 係數
        //Maurer Rose 玫瑰線 SP

        //picturebox11 蝴蝶曲線 Butterfly curve ST
        double butterfly_x0, butterfly_y0, butterfly_x1, butterfly_y1;  // 兩個點畫一直線
        int butterfly_n = 1;   // 畫幾圈 蝴蝶曲線
        //picturebox11 蝴蝶曲線 Butterfly curve SP

        //picturebox12 蝴蝶曲線 Butterfly curve ST
        G2D_Butterfly butterfly; // 蝴蝶物件
        int eX = 100;  // 蝴蝶 的目標點座標
        int eY = 100;
        //picturebox12 蝴蝶曲線 Butterfly curve SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //數字 8 雙扭線 (Lemniscate of Bernoulli) ST
            this.pictureBox1.ClientSize = new Size(250, 250);
            cx0 = this.pictureBox1.ClientSize.Width / 2;
            cy0 = this.pictureBox1.ClientSize.Height / 2;
            radius0 = (int)(Math.Min(cx0, cy0) * 2 * 0.3);

            lob = new G2D_LemniscateOfBernoulli(radius0);
            //數字 8 雙扭線 (Lemniscate of Bernoulli) SP

            //picturebox12 蝴蝶曲線 Butterfly curve ST
            butterfly = new G2D_Butterfly(3, 30);
            //picturebox12 蝴蝶曲線 Butterfly curve SP
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 20;
            dx = 160;
            dy = 50;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);

            x_st = 10;
            y_st = 10;
            dx = W + 70;
            dy = H + 45;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            label3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 30);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 60);
            numericUpDown1.Location = new Point(x_st + dx * 0 + 50, y_st + dy * 3 + 60);
            button1.Location = new Point(x_st + dx * 0 + 50 + 80, y_st + dy * 3 + 60);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 90);
            numericUpDown2.Location = new Point(x_st + dx * 0 + 50, y_st + dy * 3 + 90);

            x_st = 1810;
            y_st = 80;
            dx = 120;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0 - 300, y_st + dy * 12);
            richTextBox1.Size = new Size(400, 380);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();

        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        //數字 8 雙扭線 (Lemniscate of Bernoulli) ST

        // http://en.wikipedia.org/wiki/Lemniscate_of_Bernoulli

        // Converting between polar and Cartesian coordinates
        // x = r cos(θ)
        // y = r sin(θ)

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            lob.Draw(e.Graphics, cx0, cy0);

            PointF pt = lob.GetPos(angle0, cx0, cy0);
            e.Graphics.FillEllipse(Brushes.Red, pt.X - 10, pt.Y - 10, 20, 20);

        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            angle0++;
            angle0 %= 360;
            this.pictureBox0.Invalidate();
        }
        //數字 8 雙扭線 (Lemniscate of Bernoulli) SP

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {



        }

        //Maurer Rose 玫瑰線 ST

        // http://en.wikipedia.org/wiki/Maurer_rose
        //  Maurer rose was introduced by Peter M. Maurer in his article entitled A Rose is a Rose

        // (r, θ) = (a * sin(kθ), θ) where (θ = 0, d, 2d, 3d, ..., 360d)
        // Converting between polar and Cartesian coordinates
        // x = r cos(θ)
        // y = r sin(θ)

        private void pictureBox10_Paint(object sender, PaintEventArgs e)
        {
            // 畫布設定為較佳的輸出品質 
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            int Cx = this.pictureBox10.ClientSize.Width / 2;  // 中心點
            int Cy = this.pictureBox10.ClientSize.Height / 2;
            int a = (int)(Math.Min(Cx, Cy) * 0.9); // 半徑
            double r; // 極座標的 r
            double theta; // 極座標的θ

            for (int t = 0; t <= 360; t = t + 1)  // 361個點  = 360 條直線
            {
                rose_x0 = rose_x1; // 求該點之前 先存成為上個點
                rose_y0 = rose_y1;
                theta = t * d_rose * Math.PI / 180;
                r = a * Math.Sin(k_rose * theta);  // 極座標
                rose_x1 = r * Math.Cos(theta);  // 直角座標
                rose_y1 = r * Math.Sin(theta);
                if (t != 0)  // 第一個點不畫
                {
                    e.Graphics.DrawLine(Pens.Red, Cx + (float)rose_x0, Cy - (float)rose_y0, Cx + (float)rose_x1, Cy - (float)rose_y1);
                }
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            k_rose = (int)numericUpDown1.Value;
            this.pictureBox10.Invalidate();
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            d_rose = (int)numericUpDown2.Value;
            this.pictureBox10.Invalidate();
        }

        private void timer10_Tick(object sender, EventArgs e)
        {
            k_rose++;
            if (k_rose > (int)numericUpDown1.Maximum)
            {
                k_rose = (int)numericUpDown1.Minimum;
            }
            numericUpDown1.Value = (decimal)k_rose;
            this.pictureBox10.Invalidate();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer10.Enabled = !timer10.Enabled;
            if (timer10.Enabled)
                button1.Text = "停止";
            else
                button1.Text = "K 自動增加";

        }
        //Maurer Rose 玫瑰線 SP


        //蝴蝶曲線 Butterfly curve ST
        // http://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)

        private void pictureBox11_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒設定 -- 畫布設定為較佳的輸出品質 
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            int Cx = this.pictureBox11.ClientSize.Width / 2;  // 中心點
            int Cy = this.pictureBox11.ClientSize.Height / 2;
            double d = Math.Min(this.pictureBox11.ClientSize.Width, this.pictureBox11.ClientSize.Height) / 8.0;  // 半徑

            double t;  // 極座標的θ
            double r;  // 極座標的 r
            for (int k = 0; k <= 360 * butterfly_n; k++)
            {
                butterfly_x0 = butterfly_x1;  // 先儲存 成為上個點
                butterfly_y0 = butterfly_y1;

                // 計算該點 (極座標)
                t = k * Math.PI / 180;
                r = d * (Math.Pow(Math.E, Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5));

                // 轉成直角座標
                butterfly_x1 = r * Math.Sin(t);
                butterfly_y1 = r * Math.Cos(t);

                if (t != 0)  // 第一個點不畫
                {
                    e.Graphics.DrawLine(Pens.Red, Cx + (float)butterfly_x0, Cy - (float)butterfly_y0, Cx + (float)butterfly_x1, Cy - (float)butterfly_y1);
                }
            }
            e.Graphics.DrawString(butterfly_n.ToString(), new Font("標楷體", 20), Brushes.Navy, 10, pictureBox11.Height - 30);
        }

        private void timer11_Tick(object sender, EventArgs e)
        {
            butterfly_n++;
            if (butterfly_n >= 12)
                butterfly_n = 1;

            this.pictureBox11.Invalidate();
        }

        //蝴蝶曲線 Butterfly curve SP

        //picturebox12 蝴蝶曲線 Butterfly curve ST
        // http://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)

        private void pictureBox12_MouseDown(object sender, MouseEventArgs e)
        {
            eX = e.X;
            eY = e.Y;
            this.pictureBox12.Invalidate();
        }

        private void pictureBox12_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.FillEllipse(Brushes.Red, eX - 5, eY - 5, 10, 10); // 畫出 目標點

            butterfly.Draw(e.Graphics);  // 畫出 蝴蝶圖案
        }

        private void timer12_Tick(object sender, EventArgs e)
        {
            butterfly.Update(eX, eY);
            this.pictureBox12.Invalidate();
        }

        //picturebox12 蝴蝶曲線 Butterfly curve SP


    }
}
