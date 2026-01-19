using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for HatchBrush, LinearGradientBrush

//使用TextureBrush類繪製圖像

namespace vcs_Draw_Brush
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen pen;
        //SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //以塗刷新增畫筆, 刮刮樂效果 ST
            image = new Bitmap(filename);
            textureBrush = new TextureBrush(image);
            p = new Pen(textureBrush, 40);
            //以塗刷新增畫筆, 刮刮樂效果 SP


            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            pen = new Pen(Color.Red, 3);

            if (radioButton1.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                pen = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(0, 0);

                SolidBrush sb = new SolidBrush(Color.Gold);
                pen = new Pen(sb, 10);
                richTextBox1.Text += "SolidBrush\n";
            }
            else if (radioButton2.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                pen = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                TextureBrush tb = new TextureBrush(new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg"));
                pen = new Pen(tb, 10);
                richTextBox1.Text += "TextureBrush\n";
            }
            else if (radioButton3.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                pen = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
                pen = new Pen(hb, 10);
                richTextBox1.Text += "HatchBrush\n";
            }
            else if (radioButton4.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                pen = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
                LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
                pen = new Pen(lgb, 10);
                richTextBox1.Text += "LinearGradientBrush\n";
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int W = 160;
            int H = 60;

            //button
            x_st = 10;
            y_st = 20;
            dx = W + 10;
            dy = H + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);

            x_st = 10;
            y_st = 10;
            dx = W + 30;
            groupBox0.Size = new Size(W + 20, H * 3 + 110);
            groupBox1.Size = new Size(W + 20, H * 4);
            groupBox2.Size = new Size(W + 20, H * 2 + 110);
            groupBox3.Size = new Size(W + 20, H * 4);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 5 - 50);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 4);

            pictureBox1.Size = new Size(750, 620);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_pictureBox1_clear.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_pictureBox1_clear.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_pictureBox1_clear.Size.Height);

            panel1.Size = new Size(750, 50);
            panel1.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            pictureBox2.Size = new Size(305, 400);
            pictureBox2.Location = new Point(x_st + dx * 6, y_st + dy * 0 + 30);
            label1.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            richTextBox1.Size = new Size(305, 240);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 7 - 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 20;
            y_st = 20;
            dx = 50;
            dy = 30;
            radioButton1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            radioButton2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            radioButton3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            radioButton4.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_draw1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_draw2.Location = new Point(x_st + dx * 0, y_st + dy * 5 + 20);

            this.Size = new Size(1500, 740);
            this.Text = "vcs_Draw_Brush";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_pictureBox1_clear_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            draw_TextureBrush();
        }

        public void draw_TextureBrush()
        {
            SetStyle(ControlStyles.Opaque, true);

            //用圖像創建畫筆,來繪制圖像
            //用圖片當筆刷用
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_背景圖\background.jpg";  //使用一張背景圖
            Bitmap bitmap0 = new Bitmap(filename);
            int W = bitmap0.Width;
            int H = bitmap0.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            TextureBrush tb = new TextureBrush(bitmap0);//用圖片做成的筆刷
            //TextureBrush tb = new TextureBrush(bitmap0, new Rectangle(0, 0, bitmap0.Width, bitmap0.Height));

            //建立新影像圖片
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);//清空背景色

            g.FillRectangle(tb, new Rectangle(0, 0, W, H));

            g.FillRectangle(Brushes.White, 0, 130, 640, 220);

            //用圖像創建畫筆,來繪制圖像
            Pen pen = new Pen(tb, 10);
            g.DrawRectangle(pen, new Rectangle(0 + 20, 130 + 20, 640 - 40, 220 - 40));

            //用圖像繪製文字
            Font f = new Font("標楷體", 60, FontStyle.Bold);
            //Font f = new Font("標楷體", 60, FontStyle.Bold | FontStyle.Italic);
            g.DrawString("天階夜色涼如水\n坐看牽牛織女星", f, tb, 10, 150);

            int cx = 650;
            int cy = 450;
            int R = 100;
            g.FillRectangle(Brushes.Yellow, new Rectangle(cx - R / 2, cy - R / 2, R, R));
            g.FillEllipse(tb, new Rectangle(cx - R / 2, cy - R / 2, R, R));

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";  //使用一張背景圖
            bitmap0 = new Bitmap(filename);
            TextureBrush tb2 = new TextureBrush(bitmap0);
            Rectangle rect = new Rectangle(50, 70, 150, 150);//定義矩形,參數為起點橫縱坐標以及其長和寬
            g.FillRectangle(tb2, rect);

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //TextureBrush 有圖形的塗刷

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);
            TextureBrush textureBrush = new TextureBrush(bmp);

            Graphics g = pictureBox1.CreateGraphics();


            TextureBrush tb = new TextureBrush(bmp);  // 使用的影像
            g.FillEllipse(tb, 0, 0, 305, 400); //塗刷填滿橢圓形區域
            g.DrawEllipse(Pens.Black, 0, 0, 305, 400);  //畫出橢圓形外框

            richTextBox1.Text += "------------------------------\n";  // 30個

            Rectangle rect = new Rectangle(150, 150, 80, 80);
            tb = new TextureBrush(bmp, rect);  // 使用的影像
            g.FillEllipse(tb, 320, 20, 400, 200); //塗刷填滿橢圓形區域
            g.DrawEllipse(Pens.Black, 320, 20, 400, 200);  //畫出橢圓形外框

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();

            int x_st = 0;
            int y_st = 0;
            int w = 300;
            int h = 50;
            int dy = h + 5;
            Rectangle rect = new Rectangle(x_st, y_st, w, h);

            //(紋理刷)
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            TextureBrush textureBrush = new TextureBrush(new Bitmap(filename));

            //對原圖(x_st,y_st) w, h 抓一塊出來放在(x_st,y_st)
            rect = new Rectangle(x_st, y_st, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷1", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st));
            rect = new Rectangle(x_st, y_st + dy, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷2", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st + dy));
            rect = new Rectangle(x_st, y_st + dy * 2, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷3", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st + dy * 2));
            rect = new Rectangle(x_st, y_st + dy * 3, w, h);
            g.FillRectangle(textureBrush, rect);       //(紋理刷)
            g.DrawString("紋理刷4", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st + dy * 3));

            //實心刷
            SolidBrush sb1 = new SolidBrush(Color.DarkOrchid);
            SolidBrush sb2 = new SolidBrush(Color.Aquamarine);
            SolidBrush sb3 = new SolidBrush(Color.DarkOrange);
            rect = new Rectangle(x_st, y_st + dy * 4, w, h);
            g.FillRectangle(sb1, rect);　        // (實心刷)
            g.DrawString("實心刷1", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 4));
            rect = new Rectangle(x_st, y_st + dy * 5, w, h);
            g.FillRectangle(sb2, rect);　        // (實心刷)
            g.DrawString("實心刷2", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 5));
            rect = new Rectangle(x_st, y_st + dy * 6, w, h);
            g.FillRectangle(sb3, rect);　        // (實心刷)
            g.DrawString("實心刷3", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 6));

            //陰影刷
            HatchBrush hb1 = new HatchBrush(HatchStyle.DiagonalCross,
            Color.DarkOrange, Color.Aquamarine);
            HatchBrush hb2 = new HatchBrush(HatchStyle.DarkVertical,
            Color.DarkOrange, Color.Aquamarine);
            HatchBrush hb3 = new HatchBrush(HatchStyle.LargeConfetti,
            Color.DarkOrange, Color.Aquamarine);
            rect = new Rectangle(x_st, y_st + dy * 8, w, h);
            g.FillRectangle(hb1, rect);             //(陰影刷)
            g.DrawString("陰影刷1", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 8));
            rect = new Rectangle(x_st, y_st + dy * 9, w, h);
            g.FillRectangle(hb2, rect);             //(陰影刷)
            g.DrawString("陰影刷2", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 9));
            rect = new Rectangle(x_st, y_st + dy * 10, w, h);
            g.FillRectangle(hb3, rect);             //(陰影刷)
            g.DrawString("陰影刷3", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 10));
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //LinearGradientBrush線形漸層塗刷, 線性梯度刷

            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);

            int x_st = 20;
            int y_st = 20;
            int w = 200;
            int h = 150;
            int dx = w + 20;

            LinearGradientBrush lgb = new LinearGradientBrush(
                new Point(x_st + w * 0, y_st + 0),  // 開始的位置
                new Point(x_st + w * 1, y_st + h),// 結束的位置
                Color.Red, // 第一種顏色
                Color.Green); // 第二種顏色
            g.FillRectangle(lgb, x_st + 0, y_st + 0, w, h);

            lgb = new LinearGradientBrush(
                new Point(x_st + w * 1, y_st + h),  // 開始的位置
                new Point(x_st + w * 2, y_st + 0),// 結束的位置
                Color.Green, // 第一種顏色
                Color.Blue); // 第二種顏色
            g.FillRectangle(lgb, x_st + w * 1, y_st + 0, w, h);

            lgb = new LinearGradientBrush(
                new Point(x_st + w * 2, y_st + 0),  // 開始的位置
                new Point(x_st + w * 3, y_st + h),// 結束的位置
                Color.Blue, // 第一種顏色
                Color.Yellow); // 第二種顏色
            g.FillRectangle(lgb, x_st + w * 2, y_st + 0, w, h);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //線性梯度刷的4種模式
            Font f = new Font("標楷體", 12, FontStyle.Bold);
            x_st = 20;
            y_st = 220;
            w = 150;
            h = 150;
            dx = w + 20;
            Rectangle rect = new Rectangle(x_st, y_st, w, h);
            lgb = new LinearGradientBrush(rect, Color.Red, Color.Green, LinearGradientMode.Horizontal);
            g.FillRectangle(lgb, rect);
            g.DrawString("從左至右的漸層", f, new SolidBrush(Color.Red), x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st += dx;
            rect = new Rectangle(x_st, y_st, w, h);
            lgb = new LinearGradientBrush(rect, Color.Red, Color.Green, LinearGradientMode.Vertical);
            g.FillRectangle(lgb, rect);
            g.DrawString("從上至下的漸層", f, new SolidBrush(Color.Red), x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st += dx;
            rect = new Rectangle(x_st, y_st, w, h);
            lgb = new LinearGradientBrush(rect, Color.Red, Color.Green, LinearGradientMode.ForwardDiagonal);
            g.FillRectangle(lgb, rect);
            g.DrawString("從左上至右下的漸層", f, new SolidBrush(Color.Red), x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st += dx;
            rect = new Rectangle(x_st, y_st, w, h);
            lgb = new LinearGradientBrush(rect, Color.Red, Color.Green, LinearGradientMode.BackwardDiagonal);
            g.FillRectangle(lgb, rect);
            g.DrawString("從右上至左下的漸層", f, new SolidBrush(Color.Red), x_st, y_st - 30);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //用圖像繪製文字
            x_st = 20;
            y_st = 380;
            w = 150;
            h = 150;

            //線性梯度刷, 加上轉彎角度
            rect = new Rectangle(x_st, y_st, w, h);
            lgb = new LinearGradientBrush(rect, Color.Red, Color.Green, 45f, true);
            g.FillRectangle(lgb, x_st, y_st, w, h);

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 10;
            y_st = 10;
            w = 130;
            h = 40;
            //建立漸層色畫筆
            LinearGradientBrush br1 = new LinearGradientBrush(
                new Point(x_st, y_st),// 開始的位置
                new Point(x_st + w, y_st + h),// 結束的位置
                Color.Red,// 第一種顏色
                Color.Green);// 第二種顏色

            g.FillRectangle(br1, 10, 10, 125, 50);
            g.DrawRectangle(Pens.Black, 10, 10, 125, 50);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //建立漸層色畫筆, 使用Rectangle才可以使用LinearGradientMode
            x_st = 145;
            y_st = 10;
            w = 125;
            h = 50;
            rect = new Rectangle(x_st, y_st, w, h);
            LinearGradientBrush br2 = new LinearGradientBrush(
                rect,
                Color.Blue,
                Color.White,
                LinearGradientMode.ForwardDiagonal);
            g.FillRectangle(br2, rect);
            g.DrawRectangle(Pens.Black, rect);


            //-----------------------------------------------

            //線性梯度刷

            x_st = 250;
            y_st = 450;
            w = 405;
            h = 55;

            //建立漸層色畫筆
            lgb = new LinearGradientBrush(
                new Point(x_st, y_st),// 開始的位置
                new Point(x_st + w, y_st + h),// 結束的位置
                Color.Red,// 第一種顏色
                Color.Green);// 第二種顏色

            //用圖像繪製文字
            f = new Font("標楷體", 40, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline);
            g.DrawString("天階夜色涼如水", f, lgb, x_st, y_st);

            //畫漸層色
            g.FillRectangle(lgb, x_st, y_st, w, h);
            g.DrawRectangle(Pens.Red, x_st, y_st, w, h);//邊框

            y_st += 100;
            Pen pen = new Pen(lgb, 30);
            g.DrawLine(pen, x_st + 0, y_st + 10, x_st + 405, y_st + 10);

            pictureBox1.Image = bitmap1;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //彩虹漸層色

            Bitmap bitmap1 = new Bitmap(600, 600);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            int x_st = 10;
            int y_st = 440;
            int w = 700;
            int h = 100;

            Rectangle rect = new Rectangle(x_st, y_st, w, h);
            LinearGradientBrush br3 = new LinearGradientBrush(rect, Color.Blue, Color.White, 0f);

            ColorBlend colorBlend = new ColorBlend();//建立一個混色物件
            colorBlend.Colors = new Color[] 
                {
                    Color.Red,
                    Color.Orange,
                    Color.Yellow,
                    Color.Lime,
                    Color.Blue,
                    Color.Indigo,
                    Color.Violet,
                };
            colorBlend.Positions = new float[]
                {
                    0f, 1/6f, 2/6f, 3/6f, 4/6f, 5/6f, 1f
                };
            br3.InterpolationColors = colorBlend;//設定混色物件

            g.FillRectangle(br3, rect);
            g.DrawRectangle(Pens.Black, rect);//外框

            //3030

            //PathGradientBrush 路徑漸層塗刷

            x_st = 10;
            y_st = 10;

            Point[] pts = new Point[4];  // 路徑
            pts[0] = new Point(x_st + 200, y_st + 0);
            pts[1] = new Point(x_st + 300, y_st + 170);
            pts[2] = new Point(x_st + 200, y_st + 170 + 170);
            pts[3] = new Point(x_st + 100, y_st + 170);
            PathGradientBrush lbrush = new PathGradientBrush(pts);  // 中央顏色 
            lbrush.CenterColor = Color.Blue;
            Color[] colorArray = new Color[] { Color.Red, Color.Green, Color.Blue, Color.Yellow };
            lbrush.SurroundColors = colorArray; // 路徑中點的顏色
            g.FillRectangle(lbrush, x_st + 0, y_st + 0, 400, 400);
            g.DrawRectangle(Pens.Red, x_st + 0, y_st + 0, 400, 400);

            pictureBox1.Image = bitmap1;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //彩色曲線

            Bitmap bitmap1 = new Bitmap(600, 600);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.SmoothingMode = SmoothingMode.AntiAlias;

            Point[] ColorPoints = null;

            Random rand = new Random();
            ColorPoints = new Point[20];
            for (int i = 0; i < ColorPoints.Length; i++)
            {
                ColorPoints[i] = new Point(i * 15, rand.Next(5, 110));
            }

            RectangleF world_rect = new RectangleF(0, 0, 100, 100);
            RectangleF device_rect = new RectangleF(5, 5,
                pictureBox1.ClientSize.Width - 10,
                pictureBox1.ClientSize.Height - 10);
            SetTransformation(g, world_rect, device_rect, false, true);

            // Draw the axes.
            using (Pen pen = new Pen(Color.Black, 0))
            {
                for (int y = 10; y < 100; y += 10)
                    g.DrawLine(pen, -2, y, 2, y);
                g.DrawLine(pen, 0, 0, 0, 100);

                for (int x = 10; x < 100; x += 10)
                    g.DrawLine(pen, x, -2, x, 2);
                g.DrawLine(pen, 0, 0, 100, 0);
            }

            // Make a brush for the curve.
            using (LinearGradientBrush brush =
                new LinearGradientBrush(world_rect,
                    Color.Red, Color.Blue, 270))
            {
                ColorBlend blend = new ColorBlend();
                blend.Colors = new Color[]
                {
                    Color.Red, Color.Red,
                    Color.Orange, Color.Orange,
                    Color.Yellow, Color.Yellow,
                    Color.Green, Color.Green,
                    Color.Blue, Color.Blue,
                };
                blend.Positions =
                    new float[]
                    {
                        0.0f, 0.2f,
                        0.2f, 0.4f,
                        0.4f, 0.6f, 
                        0.6f, 0.8f,
                        0.8f, 1.0f,
                    };
                brush.InterpolationColors = blend;

                // Make a thick pen defined by the brush.
                using (Pen pen = new Pen(brush, 3))
                {
                    pen.LineJoin = LineJoin.Bevel;

                    // Draw the curve.
                    rand = new Random();

                    g.DrawCurve(pen, ColorPoints);     //曲線

                    //g.DrawLines(pen, ColorPoints);     //直線

                    //// Draw a vertical line on the edge to show the colors.
                    //g.DrawLine(pen, 100, 0, 100, 100);
                }
            }
            pictureBox1.Image = bitmap1;
        }

        // Map from world coordinates to device coordinates.
        private void SetTransformation(Graphics gr, RectangleF world_rect, RectangleF device_rect, bool invert_x, bool invert_y)
        {
            PointF[] device_points =
            {
                new PointF(device_rect.Left, device_rect.Top),      // Upper left.
                new PointF(device_rect.Right, device_rect.Top),     // Upper right.
                new PointF(device_rect.Left, device_rect.Bottom),   // Lower left.
            };

            if (invert_x)
            {
                device_points[0].X = device_rect.Right;
                device_points[1].X = device_rect.Left;
                device_points[2].X = device_rect.Right;
            }
            if (invert_y)
            {
                device_points[0].Y = device_rect.Bottom;
                device_points[1].Y = device_rect.Bottom;
                device_points[2].Y = device_rect.Top;
            }

            gr.Transform = new Matrix(world_rect, device_points);
        }


        private void button20_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            //條紋
            HatchBrush hBrush = new HatchBrush(HatchStyle.DarkHorizontal, Color.Gold);
            using (Pen p = new Pen(hBrush, 30))
            {
                g.DrawLine(p, 10, 30, 200, 200);
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        //以塗刷新增畫筆, 刮刮樂效果 ST

        Bitmap image;
        TextureBrush textureBrush;
        Pen p;
        int x, y;　// 紀錄上一個筆畫的起始點
        Graphics g2; // 畫布物件

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            Brush b = new LinearGradientBrush(this.panel1.ClientRectangle, Color.Red, Color.Green, LinearGradientMode.Horizontal);

            e.Graphics.FillRectangle(b, this.panel1.ClientRectangle);

            /*
             * Horizontal = 0　　　　從左到右的漸變
             * Vertical = 1　　　　　從上到下的漸變
             * ForwardDiagonal = 2　 從左上到右下的漸變
             * BackwardDiagonal = 3　從右上到左下的漸變
             */
        }

        private void bt_draw1_Click(object sender, EventArgs e)
        {
            //p = new Pen(Color.Red, 5);
            int width, height;
            width = pictureBox1.ClientSize.Width;
            height = pictureBox1.ClientSize.Height;
            g.Clear(Color.LightGreen);
            g.DrawRectangle(p, 0, 0, width - 1, height - 1);
        }

        private void bt_draw2_Click(object sender, EventArgs e)
        {
            //g.Clear(Color.LightGreen);
            p.Width = 10;
            for (int i = 0; i <= pictureBox1.Width; i = i + 36)
            {
                g.DrawLine(p, i, 0, i, pictureBox1.Height);
                p.Width += 2;
            }
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                SolidBrush sb = new SolidBrush(Color.Gold);
                p = new Pen(sb, 10);
                richTextBox1.Text += "SolidBrush\n";
            }
            else if (radioButton2.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                TextureBrush tb = new TextureBrush(new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg"));
                p = new Pen(tb, 10);
                richTextBox1.Text += "TextureBrush\n";
            }
            else if (radioButton3.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
                p = new Pen(hb, 10);
                richTextBox1.Text += "HatchBrush\n";
            }
            else if (radioButton4.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                //pictureBox1.Location = new Point(50, 50);

                Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
                LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
                p = new Pen(lgb, 10);
                richTextBox1.Text += "LinearGradientBrush\n";
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


//Font f = new Font("黑體", 30, FontStyle.Italic);
//lgb.SetSigmaBellShape(0.5f);
/*
            Array obj = Enum.GetValues(typeof(LinearGradientMode));

            for (int x = 0; x < obj.Length; x++)
            {
                LinearGradientMode temp = (LinearGradientMode)obj.GetValue(x);
                richTextBox1.Text += temp.ToString() + "\n";
            }
*/

//LinearGradientBrush：使用沿漸變混合的兩種顏色進行繪制

//Graphics g = pictureBox1.CreateGraphics();

//                    Brush menu_brush = new LinearGradientBrush(e.Bounds, Color.Red, Color.Black, 90);

