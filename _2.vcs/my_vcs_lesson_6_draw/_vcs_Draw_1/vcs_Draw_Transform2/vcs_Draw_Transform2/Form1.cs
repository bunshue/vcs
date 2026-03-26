using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; // for HatchBrush, Matrix, MatrixOrder

namespace vcs_Draw_Transform2
{
    public partial class Form1 : Form
    {
        //Bitmap bm = Properties.Resources.Butterfly;
        Bitmap bitmap0;
        float theta0 = 0; // 旋轉角度

        HatchBrush myBrush1 = new HatchBrush(HatchStyle.Cross, Color.Red);
        float theta1 = 0; // 旋轉角度

        float xScale = 1; // X 軸縮放倍數

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            bitmap0 = (Bitmap)Bitmap.FromFile(filename);
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
            bt_plus.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_minus.Location = new Point(x_st + dx * 2 + 60, y_st + dy * 0);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "旋轉矩陣 - 在固定點自轉";
            label1.Text = "旋轉矩陣 - 繞固定點公轉";
            label2.Text = "縮放矩陣 - X 軸放大縮小";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";

            this.Size = new Size(1740, 940);
            this.Text = "vcs_Draw_Transform2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            theta0 = theta0 + 2;  // 旋轉角度 遞增
            this.pictureBox0.Invalidate();
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            //視窗客戶區正中心點
            int Cx = this.pictureBox0.ClientSize.Width / 2;
            int Cy = this.pictureBox0.ClientSize.Height / 2;

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣

            Matrix mtx = new Matrix(); // 轉換矩陣
            mtx.Translate(-bitmap0.Width / 2, -bitmap0.Height / 2, MatrixOrder.Append);  // 先將圖形的中心點平移到原點
            mtx.Rotate(theta0, MatrixOrder.Append);  // 乘上 旋轉矩陣
            mtx.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = mtx;
            e.Graphics.DrawImage(bitmap0, 0, 0); // 繪出圖形
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta1 = theta1 + 1; // 旋轉角度 遞增
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            //視窗客戶區正中心點
            int Cx = this.pictureBox1.ClientSize.Width / 2;
            int Cy = this.pictureBox1.ClientSize.Height / 2;
            int D = 20; // 球本身的半徑
            int D2 = 100; // 球旋轉的半徑

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣
            e.Graphics.FillEllipse(Brushes.Gray, Cx - D, Cy - D, 2 * D, 2 * D); //畫出正中心圓點 
            e.Graphics.DrawEllipse(Pens.Silver, Cx - D2, Cy - D2, 2 * D2, 2 * D2); //畫出軌道

            Matrix mtx = new Matrix(); // 轉換矩陣
            mtx.Translate(D2, 0, MatrixOrder.Append);  // 先平移到 旋轉的半徑邊緣
            mtx.Rotate(theta1, MatrixOrder.Append);  // 乘上 旋轉矩陣
            mtx.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = mtx;  // 畫布的矩陣 = 矩陣 A
            e.Graphics.FillEllipse(myBrush1, 0 - D, 0 - D, 2 * D, 2 * D); //畫出旋轉的圓點 
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            xScale = xScale + 0.1f;
            this.pictureBox2.Invalidate();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            xScale = xScale - 0.1f;
            if (xScale <= 0.1f)
            {
                xScale = 0.1f;
            }
            this.pictureBox2.Invalidate();
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            //視窗客戶區正中心點
            int Cx = this.pictureBox2.ClientSize.Width / 2;
            int Cy = this.pictureBox2.ClientSize.Height / 2;
            int D = 100; // 球本身的半徑

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣
            e.Graphics.DrawEllipse(Pens.Silver, Cx - D, Cy - D, 2 * D, 2 * D); //畫出開始的圓

            Matrix mtx = new Matrix(); // 轉換矩陣
            mtx.Scale(xScale, 1, MatrixOrder.Append);  // 乘上 縮放矩陣
            mtx.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = mtx;  // 畫布的矩陣 = 矩陣 A
            e.Graphics.DrawEllipse(Pens.Red, 0 - D, 0 - D, 2 * D, 2 * D); //畫出縮放後的圓 
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
