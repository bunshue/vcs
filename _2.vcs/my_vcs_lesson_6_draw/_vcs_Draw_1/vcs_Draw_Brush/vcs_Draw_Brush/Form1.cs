using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for HatchBrush, LinearGradientBrush

namespace vcs_Draw_Brush
{
    public partial class Form1 : Form
    {
        Color color_st = Color.White;
        Color color_sp = Color.Green;

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

            color_st = pictureBox_gradient_color_st.BackColor;
            color_sp = pictureBox_gradient_color_sp.BackColor;
            draw_gradient_color();
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
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            x_st = 10;
            y_st = 10;
            dx = W + 30;
            groupBox0.Size = new Size(W + 20, H * 10 + 150);
            groupBox1.Size = new Size(W + 20, H * 10 + 150);
            groupBox2.Size = new Size(W + 20, H * 10 + 150);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 8);


            pictureBox2.Size = new Size(305, 400);
            pictureBox2.Location = new Point(x_st + dx * 7, y_st + dy * 0 + 50);
            label1.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            richTextBox1.Size = new Size(550, 550);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 7);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Name = "bt_exit";
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //使用TextureBrush類繪製圖像

            string filename = @"C:\_git\vcs\_1.data\______test_files1\_icon\唐.ico";

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

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";  //使用一張背景圖

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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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
            Graphics g = this.pictureBox1.CreateGraphics();
            Rectangle rect = new Rectangle(10, 10, 50, 50);//定義矩形,參數為起點橫縱坐標以及其長和寬

            //用圖片填充
            TextureBrush b2 = new TextureBrush(Image.FromFile(@"C:\_git\vcs\_1.data\______test_files1\picture1.jpg"));
            rect.Location = new Point(10, 70);//更改這個矩形的起點坐標
            rect.Width = 200;//更改這個矩形的寬來
            rect.Height = 200;//更改這個矩形的高
            g.FillRectangle(b2, rect);

            //用漸變色填充
            rect.Location = new Point(10, 290);
            LinearGradientBrush b3 = new LinearGradientBrush(rect, Color.Yellow, Color.Black, LinearGradientMode.Horizontal);
            g.FillRectangle(b3, rect);
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


        private void button10_Click(object sender, EventArgs e)
        {
            //使用 LinearGradientBrush 0

            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);

            //漸層色
            LinearGradientBrush lgBrush = new LinearGradientBrush(new Point(0, 0), new Point(220, 100), Color.Yellow, Color.Green);
            g.FillEllipse(lgBrush, 20, 20, 200, 100);
            g.DrawString("群曜醫電", new Font("標楷體", 40, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline), lgBrush, 10, 200);

            pictureBox1.Image = bitmap1;



        }

        private void button11_Click(object sender, EventArgs e)
        {
            //使用 LinearGradientBrush 1
            UseHorizontalLinearGradients1();
        }

        void UseHorizontalLinearGradients1()
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            Rectangle r = new Rectangle(10, 10, 100, 100);

            LinearGradientBrush theBrush = null;
            int yOffSet = 10;

            Array obj = Enum.GetValues(typeof(LinearGradientMode));

            for (int x = 0; x < obj.Length; x++)
            {
                LinearGradientMode temp = (LinearGradientMode)obj.GetValue(x);
                theBrush = new LinearGradientBrush(r, Color.Red, Color.Blue, temp);

                g.DrawString(temp.ToString(), new Font("Times New Roman", 10), new SolidBrush(Color.Black), 0, yOffSet);

                g.FillRectangle(theBrush, 120, yOffSet, 200, 50);
                yOffSet += 80;
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //使用 LinearGradientBrush 2
            UseHorizontalLinearGradients2();
        }

        public void UseHorizontalLinearGradients2()
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            LinearGradientBrush linGrBrush = new LinearGradientBrush(
               new Point(0, 10),
               new Point(200, 10),
               Color.FromArgb(255, 255, 0, 0),   // Opaque red
               Color.FromArgb(255, 0, 0, 255));  // Opaque blue

            Pen pen = new Pen(linGrBrush);

            g.DrawLine(pen, 0, 10, 200, 10);
            g.FillEllipse(linGrBrush, 0, 30, 200, 100);
            g.FillRectangle(linGrBrush, 0, 155, 500, 30);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //使用 LinearGradientBrush 3

            //實現顏色漸變效果 
            Bitmap bitmap1 = new Bitmap(300, 200);
            Graphics g = Graphics.FromImage(bitmap1);

            g.Clear(Color.BlueViolet);
            g.DrawString("漸變圖形", new Font("黑體", 30, FontStyle.Italic), new SolidBrush(Color.White), new PointF(2, 2));
            g.FillRectangle(new System.Drawing.Drawing2D.LinearGradientBrush(new Point(0, 0), new Point(300, 200), Color.FromArgb(0, 0, 0, 0), Color.FromArgb(255, 255, 255, 255)), 0, 0, 100, 50);
            g.Dispose();

            pictureBox1.Image = bitmap1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //漸層色1

            Graphics g = this.pictureBox1.CreateGraphics();

            LinearGradientBrush lgb = new LinearGradientBrush(new Point(0, 0), new Point(0, 400), Color.Red, Color.Green);
            g.FillRectangle(lgb, 0, 0, 400, 400);

            //另法
            LinearGradientBrush brush = new LinearGradientBrush(this.ClientRectangle, Color.White, Color.Red, LinearGradientMode.Horizontal);
            brush.SetSigmaBellShape(0.5f);
            //Graphics g = this.CreateGraphics();
            g.FillRectangle(brush, 50, 150, 300, 100);
            Font f = new Font("Times New Roman", 60);
            g.DrawString("文字漸層色", f, brush, 1, 1);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //漸層色2

            //漸層色 3種

            Bitmap bitmap1 = new Bitmap(600, 600);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //漸層色1
            // Define a brush with two points and their colors.
            using (LinearGradientBrush br = new LinearGradientBrush(new Point(10, 10), new Point(140, 50), Color.Red, Color.White))
            {
                g.FillRectangle(br, 10, 10, 125, 50);
                g.DrawRectangle(Pens.Black, 10, 10, 125, 50);
            }

            // Define a brush with a Rectangle, colors, and gradient mode.
            Rectangle rect = new Rectangle(145, 10, 125, 50);
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Blue, Color.White, LinearGradientMode.ForwardDiagonal))
            {
                g.FillRectangle(br, rect);
                g.DrawRectangle(Pens.Black, rect);
            }

            // Define a gradient with more than 2 colors.
            rect = new Rectangle(10, 70, 260, 50);
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Blue, Color.White, 0f))
            {
                // Create a ColorBlend object. Note that you
                // must initialize it before you save it in the
                // brush's InterpolationColors property.
                ColorBlend colorBlend = new ColorBlend();
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
                br.InterpolationColors = colorBlend;

                g.FillRectangle(br, rect);
                g.DrawRectangle(Pens.Black, rect);
            }

            //漸層色2
            //用漸變色填充
            //LinearGradientBrush：使用沿漸變混合的兩種顏色進行繪制
            rect = new Rectangle(0, 0, 500, 100);//定義矩形,參數為起點橫縱坐標以及其長和寬
            rect.Location = new Point(50, 300);
            LinearGradientBrush b = new LinearGradientBrush(rect, Color.Red, Color.Black, LinearGradientMode.Horizontal);
            g.FillRectangle(b, rect);

            //漸層色3
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 30 + i, 500, 30 + i);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //漸層色3

            //LinearGradientBrush線形漸層塗刷

            Graphics g = pictureBox1.CreateGraphics();

            LinearGradientBrush lbrush = new LinearGradientBrush(
       new Point(0, 0),  // 開始的位置
       new Point(400, 200),// 結束的位置
       Color.White, // 第一種顏色
       Color.Blue); // 第二種顏色

            g.FillRectangle(lbrush, 0, 0, 400, 200);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //漸層色4
            //PathGradientBrush 路徑漸層塗刷

            Graphics g = pictureBox1.CreateGraphics();

            Point[] pt = new Point[3];  // 路徑
            pt[0] = new Point(0, 0);
            pt[1] = new Point(200, 200);
            pt[2] = new Point(400, 0);
            PathGradientBrush lbrush = new PathGradientBrush(pt);  // 中央顏色 
            lbrush.CenterColor = Color.Blue;
            Color[] colorArray = new Color[] { Color.Red, Color.Green, Color.Yellow };
            lbrush.SurroundColors = colorArray; // 路徑中點的顏色
            g.FillRectangle(lbrush, 0, 0, 400, 200);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //LinearGradientBrush

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            g.Clear(Color.White);

            Rectangle rect = new Rectangle(100, 100, 400, 200);

            Font f = new Font("標楷體", 20, FontStyle.Bold);


            //梯度刷
            LinearGradientBrush lgb = new LinearGradientBrush(new Rectangle(0, 0, 100, 100), Color.Teal, Color.Snow, 2f, true);
            g.DrawString("群曜醫電", f, lgb, 0, 0);


            g.FillRectangle(lgb, 0, 100, 200, 200);
        }

        private void button19_Click(object sender, EventArgs e)
        {

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

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        //以塗刷新增畫筆, 刮刮樂效果 ST

        Bitmap image;
        TextureBrush textureBrush;
        Pen p;
        int x, y;　// 紀錄上一個筆畫的起始點
        Graphics g2; // 畫布物件

        string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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

        private void pictureBox_gradient_color_st_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color_st = colorDialog1.Color;
                pictureBox_gradient_color_st.BackColor = color_st;
                draw_gradient_color();
            }
        }

        private void pictureBox_gradient_color_sp_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color_sp = colorDialog1.Color;
                pictureBox_gradient_color_sp.BackColor = color_sp;
                draw_gradient_color();
            }
        }

        void draw_gradient_color()
        {
            int W = pictureBox_gradient_color.ClientSize.Width;
            int H = pictureBox_gradient_color.ClientSize.Height;

            Bitmap bitmap1 = new Bitmap(W, H);

            int i;
            int j;

            byte r_st = color_st.R;
            byte g_st = color_st.G;
            byte b_st = color_st.B;

            byte r_sp = color_sp.R;
            byte g_sp = color_sp.G;
            byte b_sp = color_sp.B;

            int r_diff = r_sp - r_st;
            int g_diff = g_sp - g_st;
            int b_diff = b_sp - b_st;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, r_st + i * r_diff / W, g_st + i * g_diff / W, b_st + i * b_diff / W));
                }
            }
            pictureBox_gradient_color.Image = bitmap1;
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            GradientColor(e);
        }

        //抽取成一個方法實現漸變色,在Paint中引用
        private void GradientColor(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Color FColor = Color.Red;
            Color TColor = Color.Green;

            Brush b = new LinearGradientBrush(this.panel1.ClientRectangle, FColor, TColor, LinearGradientMode.Horizontal);

            g.FillRectangle(b, this.panel1.ClientRectangle);

            /*
             * Horizontal = 0　　　　　　摘要:指定從左到右的漸變。
             * 
             * Vertical = 1　　　　　　　摘要: 指定從上到下的漸變。
             * 
             * ForwardDiagonal = 2　　  摘要:指定從左上到右下的漸變。
             * 
             * BackwardDiagonal = 3　　 摘要:指定從右上到左下的漸變。
             */
        }
    }
}
