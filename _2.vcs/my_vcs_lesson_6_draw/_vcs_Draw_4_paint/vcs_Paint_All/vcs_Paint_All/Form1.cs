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
// 小畫家大全

namespace vcs_Paint_All
{
    public partial class Form1 : Form
    {
        //picture0
        private bool flag_MouseDown0 = false;
        private List<Point> Points = new List<Point>();
        //picture0

        //picture1 ST
        Bitmap bmp1;
        Pen p1;
        float x1;
        float y1;
        //picture1 SP

        //picture2 ST
        Graphics g2;                 // 繪圖區
        Pen pen2;                    // 畫筆
        bool flag_MouseDown2 = false;   // 紀錄滑鼠是否被按下
        List<Point> points2 = new List<Point>(); // 紀錄滑鼠軌跡的陣列。
        //picture2 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;

            //picture1 ST
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            bmp1 = new Bitmap(W, H);
            pictureBox1.BackColor = Color.White;
            p1 = new Pen(Color.Black, 2);  //指定畫筆的顏色與粗細
            //picture1 SP

            //picture2 ST
            g2 = this.pictureBox2.CreateGraphics(); // 取得繪圖區物件
            pen2 = new Pen(Color.Black, 3); // 設定畫筆為黑色、粗細為 3 點。
            //picture2 SP
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
            label0.Text = "";
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear1.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_clear1.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_clear1.Size.Height);
            this.Size = new Size(1740, 940);
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

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            Graphics g = Graphics.FromImage(bmp1);
            g.Clear(Color.White);    // 清除畫布，背景為白色
            pictureBox1.Image = bmp1;
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            flag_MouseDown0 = true;
            Points = new List<Point>();
            Points.Add(e.Location);
            Refresh();
        }

        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
            if (!flag_MouseDown0)
            {
                return;
            }

            if (Points.Count > 0)
            {
                Point last_point = Points[Points.Count - 1];
                if ((last_point.X != e.X) || (last_point.Y != e.Y))
                {
                    Points.Add(e.Location);
                }
            }
            else
            {
                Points.Add(e.Location);
            }
            Refresh();
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
            flag_MouseDown0 = false;
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            if (Points.Count > 1)
            {
                e.Graphics.DrawLines(Pens.Black, Points.ToArray());
            }
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            x1 = e.X;
            y1 = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //宣告畫布的來源是bmp1圖案物件
            Graphics g = Graphics.FromImage(bmp1);
            //如果按下滑鼠左鍵時
            if (e.Button == MouseButtons.Left)
            {
                //隨指標移動不斷在畫布上(圖案物件)畫短點直線
                g.DrawLine(p1, x1, y1, e.X, e.Y);
                //用圖片方塊pictureBox1來顯示畫布(圖案物件)的內容
                pictureBox1.Image = bmp1;
                x1 = e.X;
                y1 = e.Y;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            flag_MouseDown2 = true; // 滑鼠被按下後設定旗標值。
            points2.Add(e.Location); // 將點加入到 points2 陣列當中。
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_MouseDown2) // 如果滑鼠被按下
            {
                points2.Add(e.Location); // 將點加入到 points2 陣列當中。
                // 畫出上一點到此點的線段。
                g2.DrawLine(pen2, points2[points2.Count - 2], points2[points2.Count - 1]);
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            points2.Add(new Point(-1, -1)); // 滑鼠放開時，插入一個斷點 (-1,-1)，以代表前後兩點之間有斷開。
            flag_MouseDown2 = false; // 滑鼠已經沒有被按下了。

        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個
