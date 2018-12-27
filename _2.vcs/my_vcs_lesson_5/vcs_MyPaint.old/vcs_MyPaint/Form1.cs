using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_MyPaint
{
    public partial class Form1 : Form
    {
        Graphics g;                 // 繪圖區
        Pen pen;                    // 畫筆
        bool isMouseDown = false;   // 紀錄滑鼠是否被按下
        List<Point> points = new List<Point>(); // 紀錄滑鼠軌跡的陣列。        
        int width;
        int height;

        public Form1()
        {
            InitializeComponent();

            g = this.panel1.CreateGraphics(); // 取得繪圖區物件
            g.Clear(Color.Red);
            pen = new Pen(Color.Black, 3); // 設定畫筆為黑色、粗細為 3 點。
            g.DrawRectangle(pen, 50, 50, 100, 100);  //繪製100×100矩形
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDown = true; // 滑鼠被按下後設定旗標值。
            points.Add(e.Location); // 將點加入到 points 陣列當中。

        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown) // 如果滑鼠被按下
            {
                points.Add(e.Location); // 將點加入到 points 陣列當中。
                // 畫出上一點到此點的線段。
                //g.DrawLine(pen, points[points.Count - 2], points[points.Count - 1]);
                this.Invalidate();
            }

        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            points.Add(new Point(-1, -1)); // 滑鼠放開時，插入一個斷點 (-1,-1)，以代表前後兩點之間有斷開。
            isMouseDown = false; // 滑鼠已經沒有被按下了。

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            for (int i = 0; i < points.Count - 1; i++)
            {
                if (points[i].X >= 0 && points[i + 1].X >= 0)
                    g.DrawLine(pen, points[i], points[i + 1]);
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            width = int.Parse(tb_width.Text);
            height = int.Parse(tb_height.Text);

            richTextBox1.Text += "size of panel is " + panel1.Width.ToString() + " X " + panel1.Height.ToString() + "\n";
            richTextBox1.Text += "setup value is " + width.ToString() + " X " + height.ToString() + "\n";

            panel1.Width = width;
            panel1.Height = height;

            // 原始影像，顯示於pictureBox1
            Bitmap bmpOrg = new Bitmap("D:\\bear.jpg");
            this.panel1.BackgroundImage = bmpOrg;

            richTextBox1.Text += "size of panel is " + panel1.Width.ToString() + " X " + panel1.Height.ToString() + "\n";

            g.Clear(Color.Red);
            pen = new Pen(Color.Black, 3); // 設定畫筆為黑色、粗細為 3 點。
            g.DrawRectangle(pen, 50, 50, 100, 100);  //繪製100×100矩形

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bm = new Bitmap(width, height);
            panel1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));
            bm.Save(@"D:\aaaaaaa.jpg", ImageFormat.Jpeg);
            bm.Save(@"D:\aaaaaaa.bmp", ImageFormat.Bmp);
            bm.Save(@"D:\aaaaaaa.png", ImageFormat.Png);

        }
    }
}
