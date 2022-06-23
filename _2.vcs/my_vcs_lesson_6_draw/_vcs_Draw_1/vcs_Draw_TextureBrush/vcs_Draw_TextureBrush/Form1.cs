using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for HatchBrush, LinearGradientBrush

namespace vcs_Draw_TextureBrush
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            image = new Bitmap(filename);
            textureBrush = new TextureBrush(image);
            p = new Pen(textureBrush, 40);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //使用TextureBrush類繪製圖像

            string filename = @"C:\______test_files\_icon\唐.ico";

            Image theimage;
            Image smallimage;

            SetStyle(ControlStyles.Opaque, true);
            //Bounds = new Rectangle(0, 0, 600, 600);
            theimage = new Bitmap(filename);
            smallimage = new Bitmap(theimage, new Size(theimage.Width / 2, theimage.Height / 2));

            Graphics g = this.pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, this.pictureBox1.ClientRectangle);

            Brush brush = new TextureBrush(smallimage, new Rectangle(0, 0, smallimage.Width, smallimage.Height));
            //用圖像創建畫筆,來繪制圖像
            g.FillEllipse(brush, new Rectangle(0, 200, 200, 200));
            //用圖像創建剛筆,來繪制圖像
            Pen pen = new Pen(brush, 40);
            g.DrawRectangle(pen, new Rectangle(250, 200, 200, 200));
            //用圖像繪製文本
            Font font = new Font("Times New Roman", 60, FontStyle.Bold | FontStyle.Italic);
            g.DrawString("Hello Image !!", font, brush, new Rectangle(0, 0, 500, font.Height));

            brush.Dispose();
            font.Dispose();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            draw_TextureBrush();
        }

        public void draw_TextureBrush()
        {
            int W = 305;
            int H = 400;

            string filename = @"C:\______test_files\picture1.jpg";  //使用一張背景圖

            Bitmap _bitmap = new Bitmap(filename);
            TextureBrush tb = new TextureBrush(_bitmap);

            Font f = new Font("Arial", 60, FontStyle.Bold);
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            //清空背景色  
            g.Clear(Color.White);
            //繪制驗證碼  

            g.DrawString("牡丹亭", f, tb, 0, 150);
            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //TextureBrush 有圖形的塗刷1

            Graphics g = pictureBox1.CreateGraphics();

            Bitmap bmp = new Bitmap(Properties.Resources.Butterfly);
            TextureBrush Mybrush = new TextureBrush(bmp);  // 使用的影像
            g.FillEllipse(Mybrush, 20, 20, 400, 200); //塗刷填滿橢圓形區域
            g.DrawEllipse(Pens.Black, 20, 20, 400, 200);  //畫出橢圓形外框
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //TextureBrush 有圖形的塗刷2

            Graphics g = pictureBox1.CreateGraphics();

            Bitmap bmp = new Bitmap(Properties.Resources.Butterfly);
            Rectangle rect = new Rectangle(0, 0, 50, 50);
            TextureBrush Mybrush = new TextureBrush(bmp, rect);  // 使用的影像
            g.FillEllipse(Mybrush, 20, 20, 400, 200); //塗刷填滿橢圓形區域
            g.DrawEllipse(Pens.Black, 20, 20, 400, 200);  //畫出橢圓形外框
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(720, 900);

            Graphics g = pictureBox1.CreateGraphics();

            int x_st = 0;
            int y_st = 0;
            int w = 300;
            int h = 50;
            int dy = h + 10;
            Rectangle rect = new Rectangle(x_st, y_st, w, h);

            //(紋理刷)
            string filename = @"C:\______test_files\picture1.jpg";
            TextureBrush textureBrush = new TextureBrush(new Bitmap(filename));

            //對原圖(x_st,y_st) w, h 抓一塊出來放在(x_st,y_st)
            rect = new Rectangle(x_st, y_st, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st));
            rect = new Rectangle(x_st, y_st + dy, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st + dy));
            rect = new Rectangle(x_st, y_st + dy * 2, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st + dy * 2));
            rect = new Rectangle(x_st, y_st + dy * 3, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st + dy * 3));

            //實心刷
            SolidBrush sb1 = new SolidBrush(Color.DarkOrchid);
            SolidBrush sb2 = new SolidBrush(Color.Aquamarine);
            SolidBrush sb3 = new SolidBrush(Color.DarkOrange);
            rect = new Rectangle(x_st, y_st + dy * 4, w, h);
            g.FillRectangle(sb1, rect);　        // (實心刷)
            g.DrawString("實心刷", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 4));
            rect = new Rectangle(x_st, y_st + dy * 5, w, h);
            g.FillRectangle(sb2, rect);　        // (實心刷)
            g.DrawString("實心刷", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 5));
            rect = new Rectangle(x_st, y_st + dy * 6, w, h);
            g.FillRectangle(sb3, rect);　        // (實心刷)
            g.DrawString("實心刷", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 6));

            //梯度刷
            LinearGradientBrush lgb = new LinearGradientBrush(rect,
            Color.DarkOrange, Color.Aquamarine,
            LinearGradientMode.BackwardDiagonal);
            rect = new Rectangle(x_st, y_st + dy * 7, w, h);
            g.FillRectangle(lgb, rect);            //(梯度刷)
            g.DrawString("梯度刷", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(x_st + w + 10, y_st + dy * 7));

            //陰影刷
            HatchBrush hb1 = new HatchBrush(HatchStyle.DiagonalCross,
            Color.DarkOrange, Color.Aquamarine);
            HatchBrush hb2 = new HatchBrush(HatchStyle.DarkVertical,
            Color.DarkOrange, Color.Aquamarine);
            HatchBrush hb3 = new HatchBrush(HatchStyle.LargeConfetti,
            Color.DarkOrange, Color.Aquamarine);
            rect = new Rectangle(x_st, y_st + dy * 8, w, h);
            g.FillRectangle(hb1, rect);             //(陰影刷)
            g.DrawString("陰影刷", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 8));
            rect = new Rectangle(x_st, y_st + dy * 9, w, h);
            g.FillRectangle(hb2, rect);             //(陰影刷)
            g.DrawString("陰影刷", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 9));
            rect = new Rectangle(x_st, y_st + dy * 10, w, h);
            g.FillRectangle(hb3, rect);             //(陰影刷)
            g.DrawString("陰影刷", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 10));

            x_st = w + 150;

            LinearGradientBrush linGrBrush = new LinearGradientBrush(
   new Point(0, 10),
   new Point(200, 10),
   Color.FromArgb(255, 255, 0, 0),   // Opaque red
   Color.FromArgb(255, 0, 0, 255));  // Opaque blue

            Pen pen = new Pen(linGrBrush, 10);

            g.DrawLine(pen, x_st, 10, x_st + 200, 10);
            g.FillEllipse(linGrBrush, x_st, 30, 200, 100);
            g.FillRectangle(linGrBrush, x_st, 155, 450, 30);

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

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


        //以塗刷新增畫筆, 刮刮樂效果 ST

        Bitmap image;
        TextureBrush textureBrush;
        Pen p;
        int x, y;　// 紀錄上一個筆畫的起始點
        Graphics g2; // 畫布物件

        string filename = @"C:\______test_files\picture1.jpg";
        bool flag_mouse_down = false;

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            x = e.X; // 紀錄筆畫的起始點
            y = e.Y;
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                if (e.Button == MouseButtons.Left) // 滑鼠的左鍵
                {
                    g2 = this.pictureBox2.CreateGraphics();
                    g2.DrawLine(p, x, y, e.X, e.Y);　// 寫到　buffer

                    x = e.X; // 結束點 就是 下一次的 開始點
                    y = e.Y;
                }
            }
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }
        //以塗刷新增畫筆, 刮刮樂效果 SP
    }
}

