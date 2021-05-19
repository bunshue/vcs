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

namespace vcs_Draw3D
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        //展示板 DisplayBoard ST
        //高低展示板 (亂數上下呈現)
        DisplayBoard db;  // 展示板物件
        Random rd = new Random();
        int col = 20, row = 15;  // 展示板的 行列數目
        int[] values;  // 展示板 內 每行的高度
        int WW = 230, HH = 230;  // 展示板 的 寬高
        PointF pt = new PointF(10, 10); // 展示板物件 左上角的座標
        //展示板 DisplayBoard SP

        //展示板 DisplayBoard2 ST
        //高低展示板 (波浪上下呈現)
        DisplayBoard db2; // 展示板物件
        //Random rd = new Random();
        int col2 = 40, row2 = 40; // 展示板的 行列數目
        int[] values2; // 展示板 內 每行的高度
        double theta = 0;  // 徑度
        int WW2 = 230, HH2 = 230;  // 展示板 的 寬高
        //展示板 DisplayBoard2 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //展示板 DisplayBoard ST
            //高低展示板 (亂數上下呈現)
            // 新增 一個展示板物件
            db = new DisplayBoard(
                    new PointF(10, 10), // 展示板左上角的座標
                    WW, HH, // 展示板的寬高
                    col, row, // 展示板的 行列數目
                    0.5f, 0.5f);  // 小方塊間隙 與 小方塊寬高 的比例

            values = new int[col];
            for (int i = 0; i < values.Length; i++)
            {
                values[i] = 5;  // 預設每行的高度
            }

            db.Update(values); // 更新 展示板 每行的高度
            //展示板 DisplayBoard SP

            //展示板 DisplayBoard2 ST
            //高低展示板 (波浪上下呈現)
            // 新增 一個展示板物件
            db2 = new DisplayBoard(new PointF(10, 10),  // 展示板左上角的座標
                WW2, HH2,  // 展示板的寬高
                col2, row2,  // 展示板的 行列數目
                0.5f, 0.5f);  // 小方塊間隙 與 小方塊寬高 的比例

            values2 = new int[col2];
            db2.Update(values2);
            //展示板 DisplayBoard2 SP


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

            x_st = 1810;
            y_st = 80;
            dx = 120;
            dy = 50;

            richTextBox1.Location = new Point(x_st + dx * 0 - 250, y_st + dy * 12);
            richTextBox1.Size = new Size(340, 380);
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

        //展示板 DisplayBoard ST
        //高低展示板 (亂數上下呈現)
        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            db.Draw(e.Graphics);  // 繪出 展示板
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            double d;
            for (int i = 0; i < values.Length; i++)
            {
                d = rd.NextDouble(); // 以亂數當作機率
                if (d < 0.1)  // 有 0.1 的機率 第 i 行要增加
                {
                    values[i] = values[i] + 1;
                    if (values[i] > row)  // 超過 上標
                        values[i] = row;
                }
                else if (d > 0.9)  // 有 0.1 的機率 第 i 行要減少
                {
                    values[i] = values[i] - 1;
                    if (values[i] < 0)  // 低於 下標
                        values[i] = 0;
                }
            }

            db.Update(values);  // 更新 展示板 每行的高度
            this.pictureBox0.Invalidate();  // 要求 重畫

        }
        //展示板 DisplayBoard SP


        //展示板 DisplayBoard2 ST
        //高低展示板 (波浪上下呈現)
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            db2.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta = theta + 0.1;
            for (int i = 0; i < values2.Length; i++)
            {
                values2[i] = (int)((row2 / 2) * Math.Sin(theta + i * 0.1) + row2 / 2) + 1;
            }

            db2.Update(values2);
            this.pictureBox1.Invalidate();
        }

        //展示板 DisplayBoard2 SP


        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer4_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer5_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox6_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer6_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox7_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer7_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox8_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer8_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox9_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer9_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox10_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer10_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox11_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer11_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox12_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer12_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox13_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer13_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox14_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer14_Tick(object sender, EventArgs e)
        {
        }
    }
}
