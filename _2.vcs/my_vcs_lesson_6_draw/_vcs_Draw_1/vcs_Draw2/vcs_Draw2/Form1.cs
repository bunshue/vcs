using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;
using System.Drawing.Drawing2D; //for CompositingQuality
using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_Draw2
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        //SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);

            if (radioButton1.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(0, 0);

                SolidBrush sb = new SolidBrush(Color.Gold);
                p = new Pen(sb, 10);
                richTextBox1.Text += "SolidBrush\n";
            }
            else if (radioButton2.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                TextureBrush tb = new TextureBrush(new Bitmap(@"C:\______test_files\picture1.jpg"));
                p = new Pen(tb, 10);
                richTextBox1.Text += "TextureBrush\n";
            }
            else if (radioButton3.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
                p = new Pen(hb, 10);
                richTextBox1.Text += "HatchBrush\n";
            }
            else if (radioButton4.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
                LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
                p = new Pen(lgb, 10);
                richTextBox1.Text += "LinearGradientBrush\n";
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int width = 600;
            int height = 600;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            pictureBox_pen.Size = new Size(width / 2, height / 2);
            pictureBox_pen.Location = new Point(900, 0);

            panel_word.Size = new Size(width * 3, 250);
            panel_word.Location = new Point(0, height + 200);

            this.pictureBox_pen.Controls.Add(groupBox2);
            this.pictureBox_pen.Controls.Add(groupBox3);
            this.pictureBox_pen.Controls.Add(groupBox4);
            this.pictureBox_pen.Controls.Add(groupBox5);
            groupBox2.BringToFront();
            groupBox3.BringToFront();
            groupBox4.BringToFront();
            groupBox5.BringToFront();

            int W;
            int H;
            int w;
            int h;

            //上
            W = pictureBox_pen.Size.Width;
            H = pictureBox_pen.Size.Height;
            w = groupBox5.Size.Width;
            h = groupBox5.Size.Height;
            x_st = (W - w) / 2;
            y_st = 10;
            groupBox5.Location = new Point(x_st, y_st);

            //下
            W = pictureBox_pen.Size.Width;
            H = pictureBox_pen.Size.Height;
            w = groupBox3.Size.Width;
            h = groupBox3.Size.Height;
            x_st = (W - w) / 2;
            y_st = H - h - 10;
            groupBox3.Location = new Point(x_st, y_st);

            //左
            W = pictureBox_pen.Size.Width;
            H = pictureBox_pen.Size.Height;
            w = groupBox2.Size.Width;
            h = groupBox2.Size.Height;
            x_st = 10;
            y_st = (H - h) / 2;
            groupBox2.Location = new Point(x_st, y_st);

            //右
            W = pictureBox_pen.Size.Width;
            H = pictureBox_pen.Size.Height;
            w = groupBox4.Size.Width;
            h = groupBox4.Size.Height;
            x_st = W - w - 10;
            y_st = (H - h) / 2;
            groupBox4.Location = new Point(x_st, y_st);

            //button
            x_st = 1300;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button24.Location = new Point(x_st + dx * 4, y_st + dy * 4);

            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button28.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button29.Location = new Point(x_st + dx * 4, y_st + dy * 5);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button34.Location = new Point(x_st + dx * 4, y_st + dy * 6);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            bt_save.Location = new Point(x_st + dx * 3, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 9 + 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width + 240, this.Height - richTextBox1.Location.Y - 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //pictureBox1.Location = new Point(10, 10);

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

        private void button0_Click(object sender, EventArgs e)
        {
            int width = 780;
            int height = 600;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            g.Clear(Color.Pink);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int x_st = 50;
            int y_st = 50;
            int w = 200;
            int dx = w + 50;
            int dy = 45;

            g.DrawRectangle(new Pen(Color.Lime, 5), x_st, y_st, w, dy * 11);

            Font f = new Font("標楷體", 13, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Blue);

            //LineCap線條屬性
            Pen p = new Pen(Color.Red, 20);

            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("------ (預設)", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.AnchorMask;
            p.EndCap = LineCap.AnchorMask;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("AnchorMask 指定遮罩，用來檢查線條端點是否為錨點端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.ArrowAnchor;
            p.EndCap = LineCap.ArrowAnchor;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("ArrowAnchor 指定箭頭形狀的錨點端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.Custom;
            p.EndCap = LineCap.Custom;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Custom 指定自訂的線條端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.DiamondAnchor;
            p.EndCap = LineCap.DiamondAnchor;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("DiamondAnchor 指定鑽石形錨點端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.Flat;
            p.EndCap = LineCap.Flat;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Flat 指定扁平線條端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.NoAnchor;
            p.EndCap = LineCap.NoAnchor;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("NoAnchor 不指定錨點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.Round;
            p.EndCap = LineCap.Round;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Round 指定圓形線條端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.RoundAnchor;
            p.EndCap = LineCap.RoundAnchor;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("RoundAnchor 指定圓形錨點端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.Square;
            p.EndCap = LineCap.Square;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Square 指定方形線條端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.SquareAnchor;
            p.EndCap = LineCap.SquareAnchor;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("SquareAnchor 指定方形錨點線條端點", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.StartCap = LineCap.Triangle;
            p.EndCap = LineCap.Triangle;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Triangle 指定三角形線條端點", f, sb, new PointF(x_st + dx, y_st));


            x_st = 50;
            y_st = 50;
            //w = 200;
            //dx = w + 50;
            dy = 45;

            g.DrawRectangle(new Pen(Color.Green, 1), x_st, y_st, w, dy * 11);

            pictureBox1.Image = bitmap1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int width = 780;
            int height = 600;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            g.Clear(Color.Pink);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int x_st = 50;
            int y_st = 50;
            int w = 200;
            int dx = w + 50;
            int dy = 45;

            g.DrawRectangle(new Pen(Color.Lime, 5), x_st, y_st, w, dy * 11);

            Font f = new Font("標楷體", 13, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Blue);

            //LineCap線條屬性

            using (Pen p = new Pen(Color.Blue, 20))
            {
                LineCap[] caps = (LineCap[])Enum.GetValues(typeof(LineCap));
                foreach (LineCap cap in caps)
                {
                    p.StartCap = cap;
                    p.EndCap = cap;
                    g.DrawLine(p, x_st, y_st, x_st + w, y_st);

                    g.DrawString(cap.ToString(), Font, Brushes.Black, new PointF(x_st + dx, y_st));
                    y_st += dy;
                }
            }
            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int width = 780;
            int height = 950;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            g.Clear(Color.Pink);

            int x_st = 50;
            int y_st = 50;
            int w = 200;
            int dx = w + 50;
            int dy = 45;

            g.DrawRectangle(new Pen(Color.Lime, 5), x_st, y_st, w, dy * 6);

            Font f = new Font("標楷體", 13, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Blue);

            //LineCap線條屬性
            Pen p = new Pen(Color.Red, 10);

            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("------ (預設)", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.DashStyle = DashStyle.Solid;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Solid 指定實線", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.DashStyle = DashStyle.Dash;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Dash 指定含有虛線的線條", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.DashStyle = DashStyle.Dot;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Dot 指定含有點的線條", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.DashStyle = DashStyle.DashDot;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("DashDot 指定含有「虛線-點」之重複花紋的線條", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.DashStyle = DashStyle.DashDotDot;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("DashDotDot 指定含有「虛線-點-點」之重複花紋的線條", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            p.DashStyle = DashStyle.Custom;
            g.DrawLine(p, x_st, y_st, x_st + w, y_st);
            g.DrawString("Custom 指定使用者定義的自訂虛線樣式", f, sb, new PointF(x_st + dx, y_st));

            y_st += dy;
            float[] dashValues = { 5, 2, 15, 4 };
            Pen p2 = new Pen(Color.Black, 5);
            p2.DashPattern = dashValues;
            g.DrawLine(p2, x_st, y_st, x_st + w * 3, y_st);
            g.DrawString("指定使用者定義的DashPattern", f, sb, new PointF(x_st + dx, y_st + 10));

            Bitmap bmp = new Bitmap(vcs_Draw2.Properties.Resources.DashPattern);
            int ww = bmp.Width;
            int hh = bmp.Height;

            //richTextBox1.Text += "pic w = " + ww.ToString() + "\n";
            //richTextBox1.Text += "pic h = " + hh.ToString() + "\n";

            Rectangle srcRect = new Rectangle(0, 0, ww, hh);
            Rectangle destRect = new Rectangle(50, y_st + 50, ww / 2, hh / 2);
            GraphicsUnit units = GraphicsUnit.Pixel;

            g.DrawImage(bmp, destRect, srcRect, units);

            x_st = 50;
            y_st = 50;
            //w = 200;
            //dx = w + 50;
            dy = 45;

            g.DrawRectangle(new Pen(Color.Green, 1), x_st, y_st, w, dy * 6);



            int y = 650;
            int x1 = 65;
            int x2 = 600;
            using (Pen dashed_pen = new Pen(Brushes.Red, 5))
            {
                dashed_pen.DashStyle = DashStyle.Custom;

                dashed_pen.DashPattern = new float[] { 3, 1 };
                g.DrawString("3, 1", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 5, 1, 5, 5 };
                g.DrawString("5, 1, 5, 5", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 5, 1 };
                g.DrawString("5, 1", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 1, 3 };
                g.DrawString("1, 3", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;

                dashed_pen.DashPattern = new float[] { 3, 1, 1, 1 };
                g.DrawString("3, 1, 1, 1", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, x1, y, x2, y);
                y += 20;
            }


            y = 800;
            using (Pen dashed_pen = new Pen(Color.Green, 15))
            {
                dashed_pen.DashStyle = DashStyle.Dash;

                dashed_pen.DashCap = DashCap.Flat;
                g.DrawString("Flat", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, 100, y, 600, y);
                y += 40;

                dashed_pen.DashCap = DashCap.Round;
                g.DrawString("Round", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, 100, y, 600, y);
                y += 40;

                dashed_pen.DashCap = DashCap.Triangle;
                g.DrawString("Triangle", this.Font, Brushes.Black, 10, y - 8);
                g.DrawLine(dashed_pen, 100, y, 600, y);
                y += 40;
            }

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
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
            Image myImage = Image.FromFile(@"C:\______test_files\bear.jpg");
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

        private void button4_Click(object sender, EventArgs e)
        {
            int width = 780;
            int height = 600;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            g.Clear(Color.Pink);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            int x_st = 50;
            int y_st = 50;
            int w = 200;
            int dx = w + 50;
            int dy = 45;

            g.DrawRectangle(new Pen(Color.Lime, 5), x_st, y_st, w, dy * 10);

            Font f = new Font("標楷體", 13, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Blue);

            using (Pen dashed_pen = new Pen(Color.Blue, 2))
            {
                for (int i = 0; i < 2; i++)
                {
                    y_st += dy;
                    dashed_pen.DashStyle = DashStyle.Dash;
                    g.DrawString("Dash", f, sb, x_st + dx, y_st);
                    g.DrawLine(dashed_pen, x_st, y_st, x_st + w, y_st);


                    y_st += dy;
                    dashed_pen.DashStyle = DashStyle.DashDot;
                    g.DrawString("DashDot", f, sb, x_st + dx, y_st);
                    g.DrawLine(dashed_pen, x_st, y_st, x_st + w, y_st);

                    y_st += dy;
                    dashed_pen.DashStyle = DashStyle.DashDotDot;
                    g.DrawString("DashDotDot", f, sb, x_st + dx, y_st);
                    g.DrawLine(dashed_pen, x_st, y_st, x_st + w, y_st);

                    y_st += dy;
                    dashed_pen.DashStyle = DashStyle.Dot;
                    g.DrawString("Dot", f, sb, x_st + dx, y_st);
                    g.DrawLine(dashed_pen, x_st, y_st, x_st + w, y_st);

                    y_st += dy;
                    dashed_pen.Width = 10;
                }
            }

            x_st = 50;
            y_st = 50;
            dy = 45;

            g.DrawRectangle(new Pen(Color.Green, 1), x_st, y_st, w, dy * 10);
            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //先畫 button5
            Graphics buttonGraphics = button5.CreateGraphics();
            Pen p = new Pen(Color.ForestGreen, 4.0F);
            p.DashStyle = DashStyle.DashDotDot;

            Rectangle theRectangle = button5.ClientRectangle;
            theRectangle.Inflate(-2, -2);
            buttonGraphics.DrawRectangle(p, theRectangle);
            buttonGraphics.DrawRectangle(p, 10, 10, button5.Width - 20, button5.Height - 20);
            buttonGraphics.Dispose();
            p.Dispose();

            //再畫 richTextBox1
            buttonGraphics = richTextBox1.CreateGraphics();
            p = new Pen(Color.ForestGreen, 4.0F);
            p.DashStyle = DashStyle.DashDotDot;

            theRectangle = richTextBox1.ClientRectangle;
            theRectangle.Inflate(-2, -2);
            buttonGraphics.DrawRectangle(p, theRectangle);
            buttonGraphics.DrawRectangle(p, 10, 10, richTextBox1.Width - 20, richTextBox1.Height - 20);
            buttonGraphics.Dispose();
            p.Dispose();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用不透明和半透明筆刷繪製

            string filename = @"C:\______test_files\picture1.jpg";

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);

            //g.DrawImage(bitmap1, 50, 50, bitmap1.Width, bitmap1.Height);

            SolidBrush opaqueBrush = new SolidBrush(Color.FromArgb(255, 0, 0, 255));
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 0, 255));

            g.FillEllipse(opaqueBrush, 35, 45, 145, 130);
            g.FillEllipse(semiTransBrush, 186, 45, 145, 130);

            g.CompositingQuality = CompositingQuality.GammaCorrected;   //指定要在合成期間使用的品質等級。
            g.FillEllipse(semiTransBrush, 140, 190, 186, 130);

            pictureBox1.Image = bitmap1;
            pictureBox1.Location = new Point(50, 50);


        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";


            //使用不透明和半透明筆刷繪製

            bitmap1 = new Bitmap(filename);
            g = Graphics.FromImage(bitmap1);

            //g.DrawImage(bitmap1, 50, 50, bitmap1.Width, bitmap1.Height);

            /*
            SolidBrush opaqueBrush = new SolidBrush(Color.FromArgb(255, 0, 0, 255));
            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(60, 0, 0, 255));

            g.FillEllipse(opaqueBrush, 35, 45, 145, 130);
            g.FillEllipse(semiTransBrush, 186, 45, 145, 130);

            g.CompositingQuality = CompositingQuality.GammaCorrected;   //指定要在合成期間使用的品質等級。
            g.FillEllipse(semiTransBrush, 140, 190, 186, 130);
            */


            g.DrawString("牡丹亭", new Font("標楷體", 30), new SolidBrush(Color.Blue), new PointF(20, 20));
            g.DrawString("牡丹亭", new Font("標楷體", 30), new SolidBrush(Color.FromArgb(60, 0, 0, 255)), new PointF(20, 220));

            pictureBox1.Image = bitmap1;
            pictureBox1.Location = new Point(50, 50);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //畫筆的樣式
            int x_st = 50;
            int y_st = 50;
            int dw = 300;
            int dy = 60;

            Graphics g = pictureBox1.CreateGraphics();

            Pen p1 = new Pen(Color.Black, 3);  // 紅色畫筆 粗細為 1
            Pen p2 = new Pen(Color.Red, 10); // 紅色畫筆 粗細為 10

            p1.DashStyle = DashStyle.Dash; //虛線
            g.DrawLine(p1, x_st, y_st + dy * 0, x_st + dw, y_st + dy * 0);

            p1.DashStyle = DashStyle.DashDot; // 虛線-點線
            g.DrawLine(p1, x_st, y_st + dy * 1, x_st + dw, y_st + dy * 1);

            p1.DashStyle = DashStyle.DashDotDot; // 虛線-點-點線
            g.DrawLine(p1, x_st, y_st + dy * 2, x_st + dw, y_st + dy * 2);

            p1.DashStyle = DashStyle.Dot; //點線
            g.DrawLine(p1, x_st, y_st + dy * 3, x_st + dw, y_st + dy * 3);

            p2.DashStyle = DashStyle.Solid; //實線
            g.DrawLine(p2, x_st, y_st + dy * 4, x_st + dw, y_st + dy * 4);
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        //HatchStyles ST
        private void button12_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.Visible = true;
            flowLayoutPanel1.Location = new Point(0, 0);
            flowLayoutPanel1.Size = new Size(960, 640 + 200);
            flowLayoutPanel1.BackColor = Color.Pink;

            // Display the names and samples of the HatchStyle values.
            // Get a list of the HatchStyles.
            foreach (HatchStyle hatch_style in Enum.GetValues(typeof(HatchStyle)))
            {
                DisplayHatchStyle(hatch_style);
            }
        }

        // Return a list of an enumerated type's values.
        private List<T> GetEnumValues<T>()
        {
            // Get the type's Type information.
            Type t_type = typeof(T);

            // Enumerate the Enum's fields.
            FieldInfo[] field_infos = t_type.GetFields();

            // Loop over the fields.
            List<T> results = new List<T>();
            foreach (FieldInfo field_info in field_infos)
            {
                // See if this is a literal value (set at compile time).
                if (field_info.IsLiteral)
                {
                    // Add it.
                    T value = (T)field_info.GetValue(null);
                    results.Add(value);
                }
            }
            return results;
        }

        // Display a sample of the HatchStyle.
        private void DisplayHatchStyle(HatchStyle hatch_style)
        {
            const int WID = 150;
            const int HGT = 50;
            const int BM_WID = WID;
            const int BM_HGT = 32;

            // Make a Panel to hold the sample and its label.
            Panel pan = new Panel();
            pan.Size = new Size(WID, HGT);
            flowLayoutPanel1.Controls.Add(pan);

            // Display the cursor's name in a Label.
            Label lbl = new Label();
            lbl.AutoSize = false;
            lbl.Text = hatch_style.ToString();
            lbl.Size = new Size(WID, 13);
            lbl.TextAlign = ContentAlignment.MiddleCenter;
            lbl.Location = new Point(0, 0);
            pan.Controls.Add(lbl);

            // Draw the cursor onto a Bitmap.
            Bitmap bm = new Bitmap(BM_WID, BM_HGT);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                using (HatchBrush br = new HatchBrush(hatch_style, Color.Black, Color.White))
                {
                    gr.FillRectangle(br, 0, 0, BM_WID, BM_HGT);
                }
            }

            // Display the Bitmap in a PictureBox.
            PictureBox pic = new PictureBox();
            pic.Location = new Point((WID - BM_WID) / 2, 15);
            pic.BorderStyle = BorderStyle.Fixed3D;
            pic.ClientSize = new Size(BM_WID, BM_HGT);
            pic.Image = bm;
            pan.Controls.Add(pic);
        }
        //HatchStyles SP

        private void button13_Click(object sender, EventArgs e)
        {
            //直線的開端與末端帽緣樣式
            int x_st = 50;
            int y_st = 50;
            int dw = 300;
            int dy = 60;
            int dd = 50;

            Graphics g = pictureBox1.CreateGraphics();

            Pen p1 = new Pen(Color.Black, 10);  // 黑色畫筆 粗細為 10

            p1.StartCap = LineCap.Flat; // 扁平線條端點。開端
            p1.EndCap = LineCap.Flat; // 扁平線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 0, x_st + dw, y_st + dy * 0);
            g.DrawString("LineCap.Flat", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 0);

            p1.StartCap = LineCap.Square; // 方形線條端點。開端
            p1.EndCap = LineCap.Square; // 方形線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 1, x_st + dw, y_st + dy * 1);
            g.DrawString("LineCap.Square", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 1);

            p1.StartCap = LineCap.Round; // 圓形線條端點。開端
            p1.EndCap = LineCap.Round; // 圓形線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 2, x_st + dw, y_st + dy * 2);
            g.DrawString("LineCap.Round", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 2);

            p1.StartCap = LineCap.Triangle; // 三角形線條端點。開端
            p1.EndCap = LineCap.Triangle; // 三角形線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 3, x_st + dw, y_st + dy * 3);
            g.DrawString("LineCap.Triangle", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 3);

            p1.StartCap = LineCap.SquareAnchor; // 方形錨點線條端點。開端
            p1.EndCap = LineCap.SquareAnchor; // 方形錨點線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 4, x_st + dw, y_st + dy * 4);
            g.DrawString("LineCap.SquareAnchor", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 4);

            p1.StartCap = LineCap.RoundAnchor; // 圓形錨點線條端點。開端
            p1.EndCap = LineCap.RoundAnchor; // 圓形錨點線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 5, x_st + dw, y_st + dy * 5);
            g.DrawString("LineCap.RoundAnchor", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 5);

            p1.StartCap = LineCap.DiamondAnchor; // 鑽石形線條端點。開端
            p1.EndCap = LineCap.DiamondAnchor; // 鑽石形線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 6, x_st + dw, y_st + dy * 6);
            g.DrawString("LineCap.DiamondAnchor", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 6);

            p1.StartCap = LineCap.ArrowAnchor; // 箭頭形狀線條端點。開端
            p1.EndCap = LineCap.ArrowAnchor; // 箭頭形狀線條端點。末端
            g.DrawLine(p1, x_st, y_st + dy * 7, x_st + dw, y_st + dy * 7);
            g.DrawString("LineCap.ArrowAnchor", this.Font, Brushes.Black, x_st + dw + dd, y_st + dy * 7);
        }

        private void button14_Click(object sender, EventArgs e)
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

        private void button15_Click(object sender, EventArgs e)
        {
            int x_st = 10;
            int y_st = 10;
            int w = 100;
            int h = 200;
            int dx = 130;

            //g.DrawRectangle(new Pen(Color.Lime, 5), x_st, y_st, w, dy * 6);

            Font f = new Font("標楷體", 20, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Blue);

            // Create a new pen.
            Pen p = new Pen(Color.Red);
            p.Width = 10;

            // Set the LineJoin property.
            p.LineJoin = LineJoin.Miter;
            // Draw a rectangle.
            g.DrawRectangle(p, new Rectangle(x_st, y_st, w, h));
            g.DrawString("Miter", f, sb, new PointF(x_st, y_st + h + 10));

            // Set the LineJoin property.
            p.LineJoin = LineJoin.Bevel;
            // Draw a rectangle.
            x_st += dx;
            g.DrawRectangle(p, new Rectangle(x_st, y_st, w, h));
            g.DrawString("Bevel", f, sb, new PointF(x_st, y_st + h + 10));

            // Set the LineJoin property.
            p.LineJoin = LineJoin.Round;
            // Draw a rectangle.
            x_st += dx;
            g.DrawRectangle(p, new Rectangle(x_st, y_st, w, h));
            g.DrawString("Round", f, sb, new PointF(x_st, y_st + h + 10));

            // Set the LineJoin property.
            p.LineJoin = LineJoin.MiterClipped;
            // Draw a rectangle.
            x_st += dx;
            g.DrawRectangle(p, new Rectangle(x_st, y_st, w, h));
            g.DrawString("MiterClipped", f, sb, new PointF(x_st, y_st + h + 10));

            string mesg = "Miter : 指定斜接接合。這會產生尖角或銳角，取決於斜接的長度是否超過斜接限制。\nBevel : 指定斜面接合。這會產生對角\nRound : 指定圓形接合。這會在直線之間產生平滑且圓的弧形。\nMiterClipped : 指定斜接接合。這會產生尖角或斜面角，取決於斜接的長度是否超過斜接限制。";
            x_st = 10;
            f = new Font("標楷體", 10, FontStyle.Bold);
            g.DrawString(mesg, f, sb, new PointF(0, y_st + h + 70));

        }

        private void DrawXY()//画X轴Y轴
        {
            int width = 600;
            int height = 600;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);
            bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            //Graphics g = this.pictureBox1.CreateGraphics();
            System.Drawing.Point px1 = new System.Drawing.Point(0, this.pictureBox1.Height);
            System.Drawing.Point px2 = new System.Drawing.Point(this.pictureBox1.Width, this.pictureBox1.Height);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(0, this.pictureBox1.Height);
            System.Drawing.Point py2 = new System.Drawing.Point(0, 0);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            pictureBox1.Image = bitmap1;
            pictureBox1.Refresh();
            //g.Dispose();
        }

        private void DrawXLine()    //画X轴平行线
        {
            //Graphics g = this.pictureBox1.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                Point px1 = new Point(0, this.pictureBox1.Height - i * 50);
                Point px2 = new Point(this.pictureBox1.Width, this.pictureBox1.Height - i * 50);
                g.DrawLine(new Pen(Brushes.Black, 1), px1, px2);
            }
            //g.Dispose();
            //pictureBox1.Refresh();
        }
        private void DrawYLine()    //画X轴刻度
        {
            //Graphics g = this.pictureBox1.CreateGraphics();
            for (int i = 1; i < 9; i++)
            {
                System.Drawing.Point py1 = new System.Drawing.Point(100 * i, this.pictureBox1.Height - 5);
                System.Drawing.Point py2 = new System.Drawing.Point(100 * i, this.pictureBox1.Height);
                g.DrawLine(new Pen(Brushes.Red, 1), py1, py2);
            }
            //pictureBox1.Refresh();
            //g.Dispose();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //畫XY軸
            DrawXY();
            pictureBox1.Image = bitmap1;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //畫X軸線
            DrawXLine();
            pictureBox1.Image = bitmap1;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //畫X軸刻度
            DrawYLine();
            pictureBox1.Image = bitmap1;
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //DrawHeart

            DrawGrid();

            richTextBox1.Text += "DrawHeart\n";

            int center_x;
            int center_y;
            int radius;
            int linewidth;
            Color c;

            center_x = 100;
            center_y = 100;
            radius = 100;
            linewidth = 10;
            c = Color.Red;

            p = new Pen(c, linewidth);
            g.DrawArc(p, center_x - radius / 1, center_y - radius / 1, radius / 1, radius / 1, 180, 180);
            g.DrawArc(p, center_x, center_y - radius / 1, radius / 1, radius / 1, 180, 180);


            Point[] pt = new Point[3];    //一維陣列內有3個Point

            pt[0].X = 0;
            pt[0].Y = radius / 2;

            pt[1].X = radius;
            pt[1].Y = radius + radius * 2 / 3;

            pt[2].X = radius * 2;
            pt[2].Y = radius / 2;
            g.DrawLines(new Pen(Brushes.Red, linewidth), pt);



        }

        private void button23_Click(object sender, EventArgs e)
        {
            //DrawPicture
            //在指定位置畫上一圖
            // Create image.
            Image newImage = Image.FromFile(@"C:\______test_files\__pic\_cat\cat2.png");
            //Image newImage = Resource1.doraemon;

            // Create coordinates for upper-left corner of image.
            int x = 200;
            int y = 200;

            // Draw image to screen.
            g.DrawImage(newImage, x, y);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            DrawGrid();
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

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                SolidBrush sb = new SolidBrush(Color.Gold);
                p = new Pen(sb, 10);
                richTextBox1.Text += "SolidBrush\n";
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                TextureBrush tb = new TextureBrush(new Bitmap(@"C:\______test_files\picture1.jpg"));
                p = new Pen(tb, 10);
                richTextBox1.Text += "TextureBrush\n";
            }
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton3.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
                p = new Pen(hb, 10);
                richTextBox1.Text += "HatchBrush\n";
            }
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton4.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

                Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
                LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
                p = new Pen(lgb, 10);
                richTextBox1.Text += "LinearGradientBrush\n";
            }
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void open_new_file()
        {
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        private void DrawGrid()
        {
            int i;
            p = new Pen(Color.Navy, 1);
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        //畫筆的設定
        Pen pen = new Pen(Color.Red, 1);
        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            RadioButton radioButton = (RadioButton)sender;
            if (radioButton.Checked == false)
                return;

            // 顏色選項
            if (radioButton == rb_color1)
                pen.Color = Color.Red;
            else if (radioButton == rb_color2)
                pen.Color = Color.Green;
            else if (radioButton == rb_color3)
                pen.Color = Color.Blue;

            // 粗細選項
            else if (radioButton == rb_width1)
                pen.Width = 1;
            else if (radioButton == rb_width2)
                pen.Width = 5;
            else if (radioButton == rb_width3)
                pen.Width = 10;

            // 樣式選項
            else if (radioButton == rb_style1)
                pen.DashStyle = DashStyle.Solid; //實線
            else if (radioButton == rb_style2)
                pen.DashStyle = DashStyle.Dash; //虛線
            else if (radioButton == rb_style3)
                pen.DashStyle = DashStyle.Dot; //點線

            // 端點樣式選項
            else if (radioButton == rb_cap1)
                pen.EndCap = LineCap.Flat; // 扁平線條端點
            else if (radioButton == rb_cap2)
                pen.EndCap = LineCap.RoundAnchor; //圓形錨點端點
            else if (radioButton == rb_cap3)
                pen.EndCap = LineCap.SquareAnchor; //方形錨點線條端點

            this.pictureBox_pen.Invalidate();
        }

        private void pictureBox_pen_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawLine(pen, 20, 20, this.pictureBox_pen.ClientSize.Width - 20, this.pictureBox_pen.ClientSize.Height - 20);
        }

        int size = 1;
        private void timer1_Tick(object sender, EventArgs e)
        {
            size++;
            if (size > 6)
                size = 1;

            Graphics g = panel_word.CreateGraphics();//建立控制元件的Graphics類
            g.Clear(Color.White);//以指定的顏色清除控制元件背景
            Brush Var_Back = Brushes.Black;//設定畫刷
            FontFamily Var_FontFamily = new FontFamily("標楷體");//設定字體樣式
            string Var_Str = "海納百川，有容乃大；壁立千仞，無欲則剛。";//設定字串

            //SizeF Var_Size = g.MeasureString(Var_Str, Var_Font);//取得字串的大小
            //int Var_X = (panel_word.Width - Convert.ToInt32(Var_Size.Width)) / 2;//設定平移的X座標
            //int Var_Y = (panel_word.Height - Convert.ToInt32(Var_Size.Height)) / 2;////設定平移的Y座標

            GraphicsPath Var_Path = new GraphicsPath();//實例化GraphicsPath對像
            Var_Path.AddString(Var_Str, Var_FontFamily, (int)FontStyle.Regular, 50, new Point(0, 0), new StringFormat());//在路徑中新增文字
            PointF[] Var_PointS = Var_Path.PathPoints;//取得路徑中的點
            Byte[] Car_Types = Var_Path.PathTypes;//取得對應點的類型

            //Matrix Var_Matrix = new Matrix(Convert.ToSingle(textBox1.Text), 0.0F, 0.0F, Convert.ToSingle(textBox1.Text), 0.0F, 0.0F);//設定仿射矩陣
            Matrix Var_Matrix = new Matrix((float)size, 0.0F, 0.0F, (float)size, 0.0F, 0.0F);//設定仿射矩陣
            Var_Matrix.TransformPoints(Var_PointS);
            GraphicsPath Var_New_Path = new GraphicsPath(Var_PointS, Car_Types);
            g.FillPath(Var_Back, Var_New_Path);
        }
    }
}

