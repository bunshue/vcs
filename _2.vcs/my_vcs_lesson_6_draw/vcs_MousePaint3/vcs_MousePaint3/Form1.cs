using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint3
{
    public partial class Form1 : Form
    {
        float angleEarth = 0;  // 地球的旋轉角度
        float angleMoon = 0;   // 月球的旋轉角度

        float deltaEarth = 1;  // 地球旋轉角度的遞增值
        float deltaMoon = 12;  // 月球旋轉角度的遞增值

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        Bitmap bitmap1; // Bitmap 影像
        Point MousePos = new Point(); //滑鼠位置

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;

            pictureBox0.BackColor = Color.Black;
            bitmap1 = (Bitmap)Bitmap.FromFile(filename);
        }

        void show_item_location()
        {
            int W = 460;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "太陽、地球、與月亮 (↑↓←→空白鍵)";
            label1.Text = "扭曲的影像";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";

            this.Size = new Size(1740, 940);
            this.Text = "vcs_MousePaint3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出 太陽
            e.Graphics.TranslateTransform(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height / 2);
            e.Graphics.FillEllipse(Brushes.Crimson, -100, -100, 200, 200);

            // 繪出 地球
            e.Graphics.RotateTransform(angleEarth);
            e.Graphics.TranslateTransform(200, 0);
            e.Graphics.FillEllipse(Brushes.Cyan, -20, -20, 40, 40);

            // 繪出 月球
            e.Graphics.RotateTransform(angleMoon);
            e.Graphics.TranslateTransform(40, 0);
            e.Graphics.FillEllipse(Brushes.PaleGreen, -5, -5, 10, 10);
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                Cursor = Cursors.Hand;
                MousePos = e.Location; // 記錄滑鼠位置
                this.pictureBox1.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                MousePos = e.Location; // 記錄滑鼠位置
                this.pictureBox1.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            Cursor = Cursors.Default;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.pictureBox1.ClientSize.Height / 2;

            Point[] pt = new Point[3];  // 三個點座標 定義一個平形四邊形
            pt[0] = new Point(MousePos.X - bitmap1.Width / 2, MousePos.Y); // 左上
            pt[1] = new Point(MousePos.X + bitmap1.Width / 2, MousePos.Y); // 右上
            pt[2] = new Point(Cx - bitmap1.Width / 2, Cy + bitmap1.Height / 2); // 左下

            e.Graphics.DrawImage(bitmap1, pt); // 呈現原圖
        }

        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            angleEarth += deltaEarth; // 地球的旋轉角度 累進
            angleEarth %= 360;

            angleMoon += deltaMoon; // 月球的旋轉角度 累進
            angleMoon %= 360;
            this.pictureBox0.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Up)
            {
                deltaEarth += 1;
            }
            else if (e.KeyData == Keys.Down)
            {
                deltaEarth -= 1;
                if (deltaEarth < 1)
                {
                    deltaEarth = 1;
                }
            }

            if (e.KeyData == Keys.Right)
            {
                deltaMoon += 1;
            }
            else if (e.KeyData == Keys.Left)
            {
                deltaMoon -= 1;
                if (deltaMoon < 1)
                {
                    deltaMoon = 1;
                }
            }

            if (e.KeyData == Keys.Space)
            {
                deltaEarth = 1;
                deltaMoon = 12;
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/
