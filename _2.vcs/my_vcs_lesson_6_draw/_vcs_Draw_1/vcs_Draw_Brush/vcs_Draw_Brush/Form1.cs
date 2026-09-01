using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;  // for HatchBrush, LinearGradientBrush

//使用TextureBrush類繪製圖像
/*
筆刷物件（單色S、圖案T、花紋H、漸層L）
SolidBrush / TextureBrush / HatchBrush / LinearGradientBrush / PathGradientBrush

單色筆刷
圖案筆刷    TextureBrush tb = new TextureBrush("bmp1.bmp");  // 建立以圖形物件當作圖案的筆刷
花紋筆刷    HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
漸層筆刷
*/

namespace vcs_Draw_Brush
{
    public partial class Form1 : Form
    {
        //以塗刷新增畫筆, 刮刮樂效果 ST
        Bitmap image;
        TextureBrush textureBrush;
        Pen p;
        int x, y;　// 紀錄上一個筆畫的起始點
        Graphics g2; // 畫布物件

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        bool flag_mouse_down = false;
        //以塗刷新增畫筆, 刮刮樂效果 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //以塗刷新增畫筆, 刮刮樂效果 ST
            image = new Bitmap(filename);
            textureBrush = new TextureBrush(image);
            p = new Pen(textureBrush, 40);
            //以塗刷新增畫筆, 刮刮樂效果 SP
        }

        void show_item_location()
        {
            //button
            int W = 200;
            int H = 60;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            groupBox0.Size = new Size(W, H * 6 + 10);
            groupBox1.Size = new Size(W, H * 6 + 10);
            groupBox2.Size = new Size(W, H * 6 + 10);
            groupBox3.Size = new Size(W, H * 6 + 10);
            groupBox4.Size = new Size(W, H * 6 + 10);
            pictureBox3.Size = new Size(W, W);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 6 - 10);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 6 - 10);
            groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 6 - 10);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            pictureBox1.Size = new Size(830, 780);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_pictureBox1_clear.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_pictureBox1_clear.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_pictureBox1_clear.Size.Height);

            pictureBox2.Size = new Size(305, 400);
            pictureBox2.Location = new Point(x_st + dx * 7, y_st + dy * 0 + 30);
            label1.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            richTextBox1.Size = new Size(305, 340);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 7 - 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            y_st = 20;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            this.Size = new Size(1810, 840);
            this.Text = "vcs_Draw_Brush";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_pictureBox1_clear_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
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
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "TextureBrush 有圖形的塗刷\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);
            TextureBrush tb = new TextureBrush(bmp);  // 使用的影像

            g.FillRectangle(tb, 0, 30, 305, 30);

            g.FillRectangle(tb, 0, 90, 305, 30);

            g.FillRectangle(tb, 0, 150, 305, 30);

            g.FillRectangle(tb, 0, 210, 305, 30);

            g.FillRectangle(tb, 0, 270, 305, 30);

            g.FillRectangle(tb, 0, 330, 305, 30);

            g.FillRectangle(tb, 0, 390, 305, 30);




            //g.FillRectangle(tb, 0, 0, 305, 400);

            //g.FillEllipse(tb, 0, 0, 305, 400); //塗刷填滿橢圓形區域
            g.DrawEllipse(Pens.Black, 0, 0, 305, 400);  //畫出橢圓形外框

            richTextBox1.Text += "------------------------------\n";  // 30個

            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_animals\animals2.jpg";
            bmp = new Bitmap(filename);
            Rectangle rect = new Rectangle(399, 209, 140, 140);
            tb = new TextureBrush(bmp, rect);  // 使用的影像
            //g.FillEllipse(tb, 320, 20, 400, 200); //塗刷填滿橢圓形區域
            //g.FillRectangle(tb, 320, 230, 400, 200); //塗刷填滿橢圓形區域

            g.FillRectangle(tb, 0, 0, 140 * 3, 140 * 3); //塗刷填滿橢圓形區域

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "";

            int x_st = 0;
            int y_st = 0;
            int w = 300;
            int h = 50;
            int dy = h + 5;
            Rectangle rect = new Rectangle(x_st, y_st, w, h);

            //(紋理刷)
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            TextureBrush tb = new TextureBrush(new Bitmap(filename));

            //對原圖(x_st,y_st) w, h 抓一塊出來放在(x_st,y_st)
            rect = new Rectangle(x_st, y_st, w, h);
            g.FillRectangle(tb, rect);       //(紋理刷)
            g.DrawString("紋理刷1", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(x_st + w + 10, y_st));

            //3030

            x_st = 180;
            y_st = 50;
            dy = 140;
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            int pen_width = 25;

            Pen p = new Pen(Color.Red, 10);     //default pen

            //------------------------------  # 30個

            //用圖片填滿筆刷
            richTextBox1.Text += "TextureBrush 圖案筆\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            tb = new TextureBrush(new Bitmap(filename));
            p = new Pen(tb, pen_width);
            y_st += dy;
            g.DrawRectangle(p, x_st, y_st, 200, 50);
            g.DrawLine(p, x_st, y_st + 100, x_st + 200, y_st + 100);
            g.FillEllipse(tb, x_st + 250, y_st, 200, 100);
            g.DrawString("圖案筆", new Font("標楷體", 32), new SolidBrush(Color.Black), new PointF(x_st - 160, y_st));

            //------------------------------  # 30個

            //旋轉顯示圖像

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            float MyAngle = 30f;//旋转的角度
            tb = new TextureBrush(bitmap1);//实例化TextureBrush类
            tb.RotateTransform(MyAngle);//以指定角度旋转图像
            g.FillRectangle(tb, 0, 400, 300, 300);//绘制旋转后的图像

            //------------------------------  # 30個

            //紋理效果, 使用圖像填充文字線條
            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_背景圖\background.jpg";  //使用一張背景圖
            //用圖片填滿筆刷
            tb = new TextureBrush(Image.FromFile(filename));
            g.DrawString("紋理效果, 使用圖像填充文字線條", new Font("標楷體", 40), tb, new PointF(x_st + 450, y_st));


        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "";

            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_ic\ic1.jpg";
            TextureBrush textureBrush1;
            Image img = Image.FromFile(pic_filename);
            g.DrawImage(img, 100, 100);

            textureBrush1 = new TextureBrush(img, WrapMode.TileFlipXY);
            int W = this.Size.Width;
            int H = this.Size.Height;
            //g.FillRectangle(textureBrush1, 0, 0, this.Size.Width, this.Size.Height);
            //g.FillRectangle(textureBrush1, W * 4 / 5, H * 4 / 5, W / 5, H / 5);

            g.FillRectangle(textureBrush1, W * 2 / 3, H * 2 / 3, W / 3, H / 3);

            //------------------------------------------------------------  # 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            TextureBrush textureBrush2;
            Rectangle sR, dR;
            img = Image.FromFile(filename);
            //g.DrawImage(img, 10, 10);

            sR = new Rectangle(100, 100, 100, 100);//來源矩形
            dR = new Rectangle(W * 1 / 3 - 50, H * 2 / 3 - 100, W / 3, H / 3);//目標矩形

            textureBrush2 = new TextureBrush(img, WrapMode.TileFlipXY);
            g.DrawImage(img, dR, sR, GraphicsUnit.Pixel);

        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

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

            //------------------------------  # 30個

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

        //------------------------------------------------------------  # 60個

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
            RectangleF device_rect = new RectangleF(5, 5, pictureBox1.ClientSize.Width - 10, pictureBox1.ClientSize.Height - 10);
            SetTransformation(g, world_rect, device_rect, false, true);

            // Draw the axes.
            Pen pen = new Pen(Color.Black, 0);
            for (int y = 10; y < 100; y += 10)
            {
                g.DrawLine(pen, -2, y, 2, y);
            }
            g.DrawLine(pen, 0, 0, 0, 100);

            for (int x = 10; x < 100; x += 10)
            {
                g.DrawLine(pen, x, -2, x, 2);
            }
            g.DrawLine(pen, 0, 0, 100, 0);

            // Make a brush for the curve.
            LinearGradientBrush brush = new LinearGradientBrush(world_rect, Color.Red, Color.Blue, 270);
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
            pen = new Pen(brush, 3);
            pen.LineJoin = LineJoin.Bevel;

            // Draw the curve.
            rand = new Random();

            g.DrawCurve(pen, ColorPoints);     //曲線

            //g.DrawLines(pen, ColorPoints);     //直線

            //// Draw a vertical line on the edge to show the colors.
            //g.DrawLine(pen, 100, 0, 100, 100);
            pictureBox1.Image = bitmap1;
        }

        // Map from world coordinates to device coordinates.
        private void SetTransformation(Graphics g, RectangleF world_rect, RectangleF device_rect, bool invert_x, bool invert_y)
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

            g.Transform = new Matrix(world_rect, device_points);  // 設定仿射矩陣, 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "LinearGradientBrush 漸層筆\n";

            //LinearGradientBrush 建立漸層筆刷, 使用沿漸變混合的兩種顏色進行繪制
            //LinearGradientBrush 漸層筆刷變數 = new LinearGradientBrush(漸層矩形區域, 前景顏色, 背景顏色, 漸層傾斜角度);

            int W = 400;
            int H = 200;
            int x_st = 100;
            int y_st = 100;
            int x_sp = 100 + W;
            int y_sp = y_st;
            Rectangle rect1 = new Rectangle(x_st, y_st, W, H);

            LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Red, Color.Green, 0f);

            Pen p = new Pen(lgb, 200);
            g.DrawLine(p, x_st - 50, y_st, x_sp + 50, y_sp);

            //lgb.SetSigmaBellShape(0.5f);

            Array obj = Enum.GetValues(typeof(LinearGradientMode));

            for (int x = 0; x < obj.Length; x++)
            {
                LinearGradientMode temp = (LinearGradientMode)obj.GetValue(x);
                richTextBox1.Text += temp.ToString() + "\n";
            }

            //------------------------------------------------------------  # 60個

            Rectangle rect = new Rectangle(50, 300, 600, 50);
            Brush b = new LinearGradientBrush(rect, Color.Red, Color.Green, LinearGradientMode.Horizontal);
            g.FillRectangle(b, rect);

            /*
            Horizontal = 0　　　　從左到右的漸變
            Vertical = 1　　　　　從上到下的漸變
            ForwardDiagonal = 2　 從左上到右下的漸變
            BackwardDiagonal = 3　從右上到左下的漸變
            */

            //------------------------------------------------------------  # 60個

            x_st = 100;
            y_st = 400;

            Font f_index = new Font("Arial", 80, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.FromArgb(128, 255, 0, 0));

            g.DrawString("5", f_index, sb, new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, 100, 100);

            Rectangle R2;
            LinearGradientBrush lgb2;

            R2 = new Rectangle(x_st + 20, y_st + 50, 80, 80);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            R2 = new Rectangle(x_st + 120, y_st + 70, 50, 50);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            R2 = new Rectangle(x_st + 190, y_st + 85, 30, 30);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            //3030

            x_st = 180;
            y_st = 50;
            int dy = 140;
            //W = pictureBox1.ClientSize.Width;
            //H = pictureBox1.ClientSize.Height;
            int pen_width = 25;

            p = new Pen(Color.Red, 10);     //default pen
            rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
            lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
            p = new Pen(lgb, pen_width);
            y_st += dy * 4;
            g.DrawRectangle(p, x_st, y_st, 200, 50);
            g.DrawLine(p, x_st, y_st + 100, x_st + 200, y_st + 100);
            g.FillEllipse(lgb, x_st + 250, y_st, 200, 100);
            g.DrawString("漸層筆", new Font("標楷體", 32), new SolidBrush(Color.Black), new PointF(x_st - 160, y_st));
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {


        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "HatchBrush 花紋筆刷\n";

            /*
            HatchBrush		建立花紋筆刷
            HatchBrush 花紋筆刷變數 = new HatchBrush(花紋筆刷, 前景顏色, 背景顏色);
            HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
            Pen p = new Pen(hb, 10);
            */

            int x_st = 0;
            int y_st = 0;
            int w = 300;
            int h = 50;
            int dy = h + 5;
            Rectangle rect = new Rectangle(x_st, y_st, w, h);

            //花紋筆刷
            HatchBrush hb1 = new HatchBrush(HatchStyle.DiagonalCross, Color.DarkOrange, Color.Aquamarine);
            HatchBrush hb2 = new HatchBrush(HatchStyle.DarkVertical, Color.DarkOrange, Color.Aquamarine);
            HatchBrush hb3 = new HatchBrush(HatchStyle.LargeConfetti, Color.DarkOrange, Color.Aquamarine);
            rect = new Rectangle(x_st, y_st + dy * 1, w, h);
            g.FillRectangle(hb1, rect);

            g.DrawString("花紋筆刷1", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 1));

            rect = new Rectangle(x_st, y_st + dy * 2, w, h);
            g.FillRectangle(hb2, rect);
            g.DrawString("花紋筆刷2", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 2));

            rect = new Rectangle(x_st, y_st + dy * 3, w, h);
            g.FillRectangle(hb3, rect);
            g.DrawString("花紋筆刷3", new Font("標楷體", 20), new SolidBrush(Color.Purple), new PointF(x_st + w + 10, y_st + dy * 3));

            //------------------------------------------------------------  # 60個

            int pen_width = 25;
            richTextBox1.Text += "HatchBrush 花紋筆\n";
            HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
            p = new Pen(hb, pen_width);
            y_st += dy;
            y_st += 200;
            g.DrawRectangle(p, x_st, y_st, 200, 50);
            g.DrawLine(p, x_st, y_st + 100, x_st + 200, y_st + 100);
            g.FillEllipse(hb, x_st + 250, y_st, 200, 100);
            g.DrawString("花紋筆", new Font("標楷體", 32), new SolidBrush(Color.Black), new PointF(x_st - 160, y_st));

            //------------------------------------------------------------  # 60個

            //條紋
            hb = new HatchBrush(HatchStyle.DarkHorizontal, Color.Gold);
            p = new Pen(hb, pen_width);
            g.DrawLine(p, 100, 400, 400, 500);

            //------------------------------------------------------------  # 60個

            Font f_index = new Font("Arial", 80, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.FromArgb(128, 255, 0, 0));

            HatchBrush hatchBrush1;
            Single p1, p2, p3;
            x_st = 500;
            y_st = 0;

            g.DrawString("3", f_index, sb, new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, 100, 100);

            p1 = 180;
            p2 = 125;
            p3 = 160;

            hatchBrush1 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.White, Color.Red);
            g.FillRectangle(hatchBrush1, x_st + 70, y_st + 250 - p1, 30, p1);

            hatchBrush1 = new HatchBrush(HatchStyle.DarkUpwardDiagonal, Color.White, Color.Blue);
            g.FillRectangle(hatchBrush1, x_st + 120, y_st + 250 - p2, 30, p2);

            hatchBrush1 = new HatchBrush(HatchStyle.DiagonalCross, Color.White, Color.Green);
            g.FillRectangle(hatchBrush1, x_st + 170, y_st + 250 - p3, 30, p3);

            g.DrawLine(new Pen(Color.Black, 2), new Point(x_st + 10, y_st + 250), new Point(x_st + 280, y_st + 250));


            x_st = 500;
            y_st = 300;

            g.DrawString("4", f_index, sb, new PointF(x_st, y_st));
            g.DrawRectangle(Pens.Red, x_st, y_st, 100, 100);

            HatchBrush hatchBrush2 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.Black, Color.Red);
            Font f = new Font("Arial", 25, FontStyle.Bold);
            g.DrawString("Visual Studio", f, hatchBrush2, new PointF(x_st + 20, y_st + 10));
            hatchBrush2 = new HatchBrush(HatchStyle.DarkUpwardDiagonal, Color.Black, Color.Blue);

            f = new Font("Garamond", 16, FontStyle.Strikeout);
            g.DrawString("Visual Studio I love it.", f, hatchBrush2, new PointF(x_st + 10, y_st + 60));
            hatchBrush2 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.Black, Color.Green);

            f = new Font("Broadway", 22, FontStyle.Underline);
            g.DrawString(".NET Framework", f, hatchBrush2, new PointF(x_st + 30, y_st + 100));
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "";

            //pbox的背景圖案
            //表單的背景圖案 法二  // Tile the image.

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_背景圖\bg1.png";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            Bitmap bmp = new Bitmap(filename);
            TextureBrush brush = new TextureBrush(bmp);
            g.FillRectangle(brush, this.pictureBox1.ClientRectangle);

            //把一張小圖畫出來
            g.DrawRectangle(Pens.Blue, bmp.Width, bmp.Height, bmp.Width, bmp.Height);
        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
            //HatchBrush 有樣式的塗刷

            int x_st = 10;
            int y_st = 10;
            int w = 100;
            int dx = w + 20;
            int dy = w + 50;
            //int dd = 50;

            Graphics g = pictureBox1.CreateGraphics();

            HatchBrush myBrush1 = new HatchBrush(HatchStyle.Cross, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush1, x_st + dx * 0, y_st + dy * 0, w, w);
            g.DrawString("Cross", Font, Brushes.Black, x_st + dx * 0, y_st + dy * 0 + w + 10);

            HatchBrush myBrush2 = new HatchBrush(HatchStyle.DarkVertical, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush2, x_st + dx * 1, y_st + dy * 0, w, w);
            g.DrawString("DarkVertical", Font, Brushes.Black, x_st + dx * 1, y_st + dy * 0 + w + 10);

            HatchBrush myBrush3 = new HatchBrush(HatchStyle.DarkHorizontal, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush3, x_st + dx * 2, y_st + dy * 0, w, w);
            g.DrawString("DarkHorizontal", Font, Brushes.Black, x_st + dx * 2, y_st + dy * 0 + w + 10);

            HatchBrush myBrush4 = new HatchBrush(HatchStyle.DiagonalCross, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush4, x_st + dx * 3, y_st + dy * 0, w, w);
            g.DrawString("DiagonalCross", Font, Brushes.Black, x_st + dx * 3, y_st + dy * 0 + w + 10);

            HatchBrush myBrush5 = new HatchBrush(HatchStyle.Divot, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush5, x_st + dx * 4, y_st + dy * 0, w, w);
            g.DrawString("Divot", Font, Brushes.Black, x_st + dx * 4, y_st + dy * 0 + w + 10);

            HatchBrush myBrush6 = new HatchBrush(HatchStyle.Horizontal, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush6, x_st + dx * 0, y_st + dy * 1, w, w);
            g.DrawString("Horizontal", Font, Brushes.Black, x_st + dx * 0, y_st + dy * 1 + w + 10);

            HatchBrush myBrush7 = new HatchBrush(HatchStyle.Vertical, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush7, x_st + dx * 1, y_st + dy * 1, w, w);
            g.DrawString("Vertical", Font, Brushes.Black, x_st + dx * 1, y_st + dy * 1 + w + 10);

            HatchBrush myBrush8 = new HatchBrush(HatchStyle.Plaid, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush8, x_st + dx * 2, y_st + dy * 1, w, w);
            g.DrawString("Plaid", Font, Brushes.Black, x_st + dx * 2, y_st + dy * 1 + w + 10);

            HatchBrush myBrush9 = new HatchBrush(HatchStyle.Percent50, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush9, x_st + dx * 3, y_st + dy * 1, w, w);
            g.DrawString("Percent50", Font, Brushes.Black, x_st + dx * 3, y_st + dy * 1 + w + 10);

            HatchBrush myBrush10 = new HatchBrush(HatchStyle.Shingle, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush10, x_st + dx * 4, y_st + dy * 1, w, w);
            g.DrawString("Shingle", Font, Brushes.Black, x_st + dx * 4, y_st + dy * 1 + w + 10);

            HatchBrush myBrush11 = new HatchBrush(HatchStyle.SolidDiamond, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush11, x_st + dx * 0, y_st + dy * 2, w, w);
            g.DrawString("SolidDiamond", Font, Brushes.Black, x_st + dx * 0, y_st + dy * 2 + w + 10);

            HatchBrush myBrush12 = new HatchBrush(HatchStyle.Trellis, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush12, x_st + dx * 1, y_st + dy * 2, w, w);
            g.DrawString("Trellis", Font, Brushes.Black, x_st + dx * 1, y_st + dy * 2 + w + 10);

            HatchBrush myBrush13 = new HatchBrush(HatchStyle.Wave, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush13, x_st + dx * 2, y_st + dy * 2, w, w);
            g.DrawString("Wave", Font, Brushes.Black, x_st + dx * 2, y_st + dy * 2 + w + 10);

            HatchBrush myBrush14 = new HatchBrush(HatchStyle.Weave, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush14, x_st + dx * 3, y_st + dy * 2, w, w);
            g.DrawString("Weave", Font, Brushes.Black, x_st + dx * 3, y_st + dy * 2 + w + 10);

            HatchBrush myBrush15 = new HatchBrush(HatchStyle.SmallGrid, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush15, x_st + dx * 4, y_st + dy * 2, w, w);
            g.DrawString("SmallGrid", Font, Brushes.Black, x_st + dx * 4, y_st + dy * 2 + w + 10);

            HatchBrush myBrush16 = new HatchBrush(HatchStyle.ZigZag, Color.Yellow, Color.Blue);
            g.FillEllipse(myBrush16, x_st + dx * 0, y_st + dy * 3, w, w);
            g.DrawString("ZigZag", Font, Brushes.Black, x_st + dx * 0, y_st + dy * 3 + w + 10);
        }

        //------------------------------------------------------------  # 60個

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button30_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "SolidBrush 單色筆\n";

            int x_st = 180;
            int y_st = 50;
            int dy = 140;
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            int pen_width = 25;
            Pen p = new Pen(Color.Red, 10);     //default pen
            SolidBrush sb = new SolidBrush(Color.Gold);
            p = new Pen(sb, pen_width);
            g.DrawRectangle(p, x_st, y_st, 200, 50);
            g.DrawLine(p, x_st, y_st + 100, x_st + 200, y_st + 100);
            g.FillEllipse(sb, x_st + 250, y_st, 200, 100);
            g.DrawString("單色筆", new Font("標楷體", 32), new SolidBrush(Color.Black), new PointF(x_st - 160, y_st));

            int w = 300;
            int h = 50;

            //實心刷
            SolidBrush sb1 = new SolidBrush(Color.DarkOrchid);
            SolidBrush sb2 = new SolidBrush(Color.Aquamarine);
            SolidBrush sb3 = new SolidBrush(Color.DarkOrange);
            Rectangle rect = new Rectangle(x_st, y_st + dy * 1, w, h);
            g.FillRectangle(sb1, rect);　        // (實心刷)
            g.DrawString("實心刷1", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(x_st + w + 10, y_st + dy * 1));
        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        private void button34_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(pictureBox1.BackColor);

            richTextBox1.Text += "新進 mix\n";



            //純色筆刷
            SolidBrush sb = new SolidBrush(Color.LightGreen);
            g.FillEllipse(sb, 50, 50, 300, 100);

            //規劃筆刷
            HatchBrush hb = new HatchBrush(HatchStyle.Vertical, Color.Blue, Color.Green);
            g.FillEllipse(hb, 50, 150, 200, 100);

            hb = new HatchBrush(HatchStyle.Cross, Color.Blue, Color.Green);
            g.FillEllipse(hb, 250, 150, 200, 100);

            hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Green);
            g.FillEllipse(hb, 450, 150, 200, 100);

            //紋理筆刷
            Image myImage = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\bear.jpg");
            TextureBrush tb = new TextureBrush(myImage);
            g.FillEllipse(tb, 50, 250, 300, 100);


            //漸層筆刷
            Rectangle r;
            LinearGradientBrush lgb;

            r = new Rectangle(50, 350, 300, 100);
            lgb = new LinearGradientBrush(
               r,
               Color.Blue,
               Color.Green,
               LinearGradientMode.Horizontal);
            g.FillEllipse(lgb, r);


            r = new Rectangle(50, 450, 300, 100);
            lgb = new LinearGradientBrush(
               r,
               Color.Blue,
               Color.Green,
               LinearGradientMode.BackwardDiagonal);
            g.FillEllipse(lgb, r);

        }

        //------------------------------------------------------------  # 60個

        private void button40_Click(object sender, EventArgs e)
        {

        }

        private void button41_Click(object sender, EventArgs e)
        {

        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        //以塗刷新增畫筆, 刮刮樂效果 ST

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

        //------------------------------------------------------------  # 60個

        int heart_type = 0;

        private void timer3_Tick(object sender, EventArgs e)
        {
            this.pictureBox3.Invalidate();
            heart_type++;
            if (heart_type > 4)
            {
                heart_type = 0;
            }
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            //GraphicsPath - FillPath() 心形

            GraphicsPath gp = new GraphicsPath();
            int Cx = this.pictureBox3.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.pictureBox3.ClientSize.Height / 2;

            int D = 20;    // 每格 寬
            int x = Cx;    // 心臟的起始點
            int y = Cy - 2 * D;

            //心臟右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };
            gp.AddCurve(pt, 0.6f);

            //心臟左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);


            if (heart_type == 0)
            {
                //空心
            }
            else if (heart_type == 1)   //單色塗刷
            {
                e.Graphics.FillPath(Brushes.Red, gp); // 填滿形狀區域 //SolidBrush - Red
            }
            else if (heart_type == 2)   //樣式塗刷一
            {
                HatchBrush myBrush1 = new HatchBrush(HatchStyle.DiagonalCross, Color.Yellow, Color.Blue);   //HatchBrush - DiagonalCross
                e.Graphics.FillPath(myBrush1, gp); //填滿形狀區域
            }
            else if (heart_type == 3)   //樣式塗刷二
            {
                HatchBrush myBrush2 = new HatchBrush(HatchStyle.SolidDiamond, Color.Yellow, Color.Blue);    //HatchBrush - SolidDiamond
                e.Graphics.FillPath(myBrush2, gp); //填滿形狀區域
            }
            else if (heart_type == 4)   //使用圖形塗刷
            {
                Bitmap bm = new Bitmap(Properties.Resources.Butterfly);
                TextureBrush myBrush3 = new TextureBrush(bm);  // 圖形塗刷  //TextureBrush
                e.Graphics.FillPath(myBrush3, gp); //填滿形狀區域
            }
            e.Graphics.DrawPath(Pens.Black, gp); //繪出圖形軌跡
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


/*

HatchBrush myBrush1 = new HatchBrush(HatchStyle.Cross, Color.Red);
e.Graphics.FillEllipse(myBrush1, 0 - D, 0 - D, 2 * D, 2 * D); //畫出旋轉的圓點 

*/



/*
FillRegion

TextureBrush newBrush = new TextureBrush(myPic);
g.FillRegion(newBrush, new Region(PaintPath));

*/


