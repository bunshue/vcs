using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality

using System.Drawing.Imaging;   //for ImageFormat


namespace vcs_Draw9_Example
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.Red);             //useless??
            pictureBox1.BackColor = Color.Pink;
            show_item_location();

            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.BackColor = Color.Pink;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 850;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            cb_manual.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            cb_snake.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            cb_magnifying.Location = new Point(x_st + dx * 2, y_st + dy * 7 + dy / 2);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            button22.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
        }

        void show_item_location2()
        {
            pictureBox2.Visible = false;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            this.Size = new Size(1700, 900);
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1250;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            cb_manual.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            cb_snake.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            cb_magnifying.Location = new Point(x_st + dx * 2, y_st + dy * 7 + dy / 2);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            button22.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //Bitmap bmp;
            //SolidBrush brush;
            //Pen pen;

            float ratio_x, ratio_y;
            float w, h;
            float x0, x1, y0, y1;

            //----畫筆顏色----
            p = new Pen(Color.Black);
            sb = new SolidBrush(p.Color);
            //----取得picturebox寬度與高度----
            w = pictureBox1.Width;
            h = pictureBox1.Height;
            //----是否有上一次的圖片，如果有就清除----
            if (pictureBox1.Image != null)
                pictureBox1.Image = null;
            //if (bitmap1 != null)
            //  bitmap1.Dispose();
            //----轉換使用者輸入的資料----
            x0 = (float)10;
            y0 = (float)10;
            x1 = (float)-5;
            y1 = (float)-9;
            //----計算放大倍率----
            ratio_x = (w - 50) / 20;
            ratio_y = (h - 50) / 20;
            //----開新的Bitmap----
            bitmap1 = new Bitmap((int)w, (int)h);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);
            //----清除Bitmap為某顏色----
            g.Clear(Color.White);
            //----更改原點位置----
            g.TranslateTransform(pictureBox1.Width / 2, pictureBox1.Height / 2);
            //----畫坐標軸----
            g.DrawLine(p, -1000, 0, 1000, 0);//x軸
            g.DrawLine(p, 0, -1000, 0, 1000);//y軸
            g.DrawString("X", this.Font, sb, w / 2 - 20, 20);
            g.DrawString("Y", this.Font, sb, 20, -h / 2);
            g.DrawLine(p, w / 2, 0, w / 2 - 10, 5);//x軸箭頭
            g.DrawLine(p, w / 2, 0, w / 2 - 10, -5);
            g.DrawLine(p, 0, -h / 2, 5, -h / 2 + 10);//y軸箭頭
            g.DrawLine(p, 0, -h / 2, -5, -h / 2 + 10);
            for (int i = -10; i <= 10; i++)//畫X Y軸座標位置
            {
                g.DrawLine(p, i * ratio_x, -5, i * ratio_x, 5);
                g.DrawString(i.ToString().PadLeft(2, ' '), this.Font, sb, i * ratio_x - 9, 10);
                g.DrawLine(p, -5, i * ratio_y, 5, i * ratio_y);
                if (i != 0)
                    g.DrawString(i.ToString(), this.Font, sb, 15, i * ratio_y - 8);
            }
            //----換顏色----
            p = new Pen(Color.Red);
            sb = new SolidBrush(p.Color);
            //----畫線----
            g.DrawLine(p, x0 * ratio_x, -y0 * ratio_y, x1 * ratio_x, -y1 * ratio_y);
            //----畫兩點----
            g.FillEllipse(sb, new RectangleF(x0 * ratio_x - 2.5f, -y0 * ratio_y - 2.5f, 5, 5));
            g.FillEllipse(sb, new RectangleF(x1 * ratio_x - 2.5f, -y1 * ratio_y - 2.5f, 5, 5));
            //----釋放Graphics資源----
            //g.Dispose();
            //----將Bitmap顯示在Picture上
            pictureBox1.Image = bitmap1;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int center_x = 300;
            int center_y = 300;
            int radius = 200;
            DrawPacman(center_x, center_y, radius);
        }

        private void DrawPacman(int center_x, int center_y, int radius)
        {
            // Create a Graphics object for the Control.
            //Graphics g = pictureBox1.CreateGraphics();

            // Create a new brush.
            Brush brush = new SolidBrush(Color.Blue);

            try
            {
                g.FillPie(brush, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2), 320, -280);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

            //Dispose of the brush.
            brush.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //同心圓
            g.DrawString("這是一組同心圓", this.Font, Brushes.Black, 10, 20);
            Pen p1 = new Pen(Color.Red);
            Pen p2 = new Pen(Color.Purple);
            Pen p3 = new Pen(Color.Blue);
            Pen p4 = new Pen(Color.Green);
            g.DrawEllipse(p1, 120 - 80, 120 - 80, 80 * 2, 80 * 2);
            g.DrawEllipse(p2, 120 - 60, 120 - 60, 60 * 2, 60 * 2);
            g.DrawEllipse(p3, 120 - 40, 120 - 40, 40 * 2, 40 * 2);
            g.DrawEllipse(p4, 120 - 20, 120 - 20, 20 * 2, 20 * 2);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 50 + i, 500, 50 + i);
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Pen pen = new Pen(Color.Black, 8);
            pen.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(pen, 50, 400, 50, 100);  //畫出X軸及y軸
            g.DrawLine(pen, 50, 400, 350, 400);

            pen = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            //pp.DashStyle = DashStyle.Dot; //DashStyle設定線條 點
            //pp.StartCap = LineCap.RoundAnchor; //設定為圓頭

            pen.EndCap = LineCap.ArrowAnchor;

            //gg.DrawLine(pp, 50, 50, 250, 250);//只畫一條
            g.DrawLines(pen, new Point[]
            {//一次畫好多條
            new Point(70,350),
            new Point(100,280),
            new Point(120,300),
            new Point(200,220),
            new Point(250,260),
            new Point(340,150)
            }
            );
        }

        private void button5_Click(object sender, EventArgs e)
        {
            draw_grid();
        }

        public void draw_grid()
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

        private void button6_Click(object sender, EventArgs e)
        {
            Brush bb = new SolidBrush(Color.Orange);
            g.FillRectangle(bb, 70, 70, 200, 100);  //畫出一個填滿的方框

            Pen pp = new Pen(Color.Black, 4);
            g.DrawRectangle(pp, 70, 70, 200, 100);
            //在同樣起點畫出黑色的長方型線，即實現加外框            

            Random rr = new Random();
            Brush db;
            for (int i = 1; i <= 7; i++)
            {
                db = new SolidBrush(Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256)));
                //Color.FromArgb() 可以設定3原色，這裡3原色的代碼是亂數產生的

                g.FillRectangle(db, 70 + (i * 40), 70 + (i * 40), 200, 100);
                //畫布上畫出方框，每次位置的X及Y值都加70，以實現往右下角移動
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(640, 480);

            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);
            sb = new SolidBrush(Color.Navy);

            int i;
            var random = new Random();

            /*
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[10];
            var stringChars2 = new char[11];
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if (i < 2)
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            richTextBox1.Text += "相機序號1：" + finalString1 + "\n";

            for (int i = 0; i < stringChars2.Length; i++)
            {
                stringChars2[i] = chars2[random.Next(chars2.Length)];
            }
            var finalString2 = new String(stringChars2);
            richTextBox1.Text += "相機序號2：" + finalString2 + "\n";
            */

            int N = 10;
            int[] x = new int[N];
            int[] y = new int[N];

            int[,] position = new int[N, 2];	//建立一個二維陣列

            int w = pictureBox1.Width;
            int h = pictureBox1.Height;

            int cx = 100;
            int cy = 100;
            int r = 30;

            for (i = 0; i < N; i++)
            {
                position[i, 0] = random.Next(w - 2 * r) + r;  //x1, x2, x3.....
                position[i, 1] = random.Next(h - 2 * r) + r;  //y1, y2, y3.....
            }
            richTextBox1.Text += "每個點的位置\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += position[i, 0].ToString() + "\t" + position[i, 1].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < N; i++)
            {
                x[i] = i;
                y[i] = random.Next(N);
                /*
                do
                {
                    y[i] = random.Next(N);
                }
                while (x[i] == y[i]);
                */
            }
            richTextBox1.Text += "\n";


            richTextBox1.Text += "x array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += x[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "y array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";


            Point pointa;
            Point pointb;
            for (i = 0; i < N; i++)
            {
                pointa = new Point(position[x[i], 0], position[x[i], 1]);
                pointb = new Point(position[y[i], 0], position[y[i], 1]);
                g.DrawLine(p, pointa, pointb);     // Draw line to screen.
            }

            for (i = 0; i < N; i++)
            {
                cx = position[i, 0];
                cy = position[i, 1];

                //richTextBox1.Text += position[i, 0].ToString() + "\t" + position[i, 1].ToString() + "\n";
                //richTextBox1.Text += "(" + (cx - r).ToString() + ", " + (cy - r).ToString() + ") - (" + (cx + r).ToString() + ", " + (cy + r).ToString() + ")\n";
                //g.FillEllipse(sb, cx - r, cy - r, r * 2, r * 2);
                FillCircle(g, sb, cx, cy, r);

                //g.DrawEllipse(new Pen(Color.Red, 3), cx - r, cy - r, r * 2, r * 2);
                DrawCircle(g, p, cx, cy, r);
            }
            pictureBox1.Image = bitmap1;
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        void FillCircle(Graphics g, SolidBrush sb, int cx, int cy, int r)
        {
            g.FillEllipse(sb, cx - r, cy - r, r * 2, r * 2);
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            int W = 340;
            int H = 543;
            int x_st;
            int y_st;
            int w;
            int h;
            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(W + 50, H + 50);  //改變圖框大小
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            sb = new SolidBrush(Color.Red);
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, 0, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(0, H - h, w, h));
            w = 30; h = 6; g.FillRectangle(sb, new Rectangle(W - w, H - h, w, h));

            x_st = 0; y_st = 6 + 205; w = 10; h = 88; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));
            x_st = W - 10; y_st = 6 + 66; w = 10; h = 205; g.DrawRectangle(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h));

            Font f;
            f = new Font("Times New Roman", 14);
            sb = new SolidBrush(Color.Black);
            g.DrawString("205", f, sb, new PointF(0, 205 / 2));
            g.DrawString("268", f, sb, new PointF(0, 573 - 6 - 268 + 268 / 2));
            g.DrawString("66", f, sb, new PointF(W - 30, 66 / 2));
            g.DrawString("290", f, sb, new PointF(W - 40, 573 - 6 - 290 + 290 / 2));

            Pen pen = new Pen(Color.Black, 5);
            pen.StartCap = LineCap.ArrowAnchor;
            pen.EndCap = LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(pen, 0, H + 10, W, H + 10);
            g.DrawLine(pen, W + 10, 0, W + 10, H);
            g.DrawString("340", f, sb, new PointF(W / 2, H + 15));
            g.DrawString("573", f, sb, new PointF(W + 15, H / 2));

            int dw = 152;
            int dh = 78;

            x_st = (W - dw) / 2;
            y_st = (H - dh) / 2;
            g.DrawRectangle(new Pen(Color.Black), new Rectangle(x_st, y_st, dw, dh));


            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, W, H));
            p = new Pen(Color.Black, 1);
            g.DrawLine(p, 0, 0, W, H);
            g.DrawLine(p, W, 0, 0, H);

            pictureBox1.Image = bitmap1;

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {
            draw_audit_picture(1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            draw_audit_picture(2);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            draw_audit_picture(3);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            draw_audit_picture(4);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            draw_audit_picture(5);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            draw_audit_picture(6);
        }

        void draw_audit_picture(int draw_case)
        {
            int title_size1 = 50;
            int title_size2 = 40;
            int title_size3 = 40;
            int H = 100;
            int h = 10;
            int width = 440;
            int height = h + title_size1 + title_size2 + h + H + h + title_size3 + h + H + h;

            Pen ArrowPen;
            Pen redPen = new Pen(Color.Red, 3);
            Pen greenPen = new Pen(Color.Green, 3);
            Pen blackPen = new Pen(Color.Black, 3);

            pictureBox1.Width = width;
            pictureBox1.Height = height;

            if (bitmap1 == null)
                bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.White);

            /*
            //debug
            Pen debug = new Pen(Color.Green, 1);
            g.DrawRectangle(debug, 0, 0, width - 1, h - 1); //h
            g.DrawRectangle(debug, 0, h, width - 1, title_size1 - 1);   //title_size1
            g.DrawRectangle(debug, 0, h + title_size1, width - 1, title_size2 - 1);   //title_size2
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h, width - 1, H - 1);   //H
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h, width - 1, title_size3 - 1); //title_size3
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3, width - 1, h - 1);   //h
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3 + h, width - 1, H - 1);   //H
            g.DrawRectangle(debug, 0, h + title_size1 + title_size2 + h + H + h + title_size3 + h + H, width - 1, h - 1);   //h
            */

            g.DrawRectangle(p, 0, 0, width - 1, height - 1);

            int x_st = 0;
            int y_st = 0;
            int x_sp = 0;
            int y_sp = 0;
            int offset = 10;

            int h_st = height;

            int[] x_data = new int[21];
            int[] y_data = new int[21];
            Point point0;
            Point point1;
            Point point2;
            Point point3;
            Point point4;
            Point point5;
            Point point6;
            Point point7;
            Point point8;
            Point point9;
            Point point10;
            Point point11;
            Point point12;
            Point point13;
            Point point14;
            Point point15;
            Point point16;
            Point point17;
            Point point18;
            Point point19;
            Point point20;

            int dx = 22;
            y_st = h + H + h + title_size3 + h;

            if ((draw_case == 1) || (draw_case == 2))
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;
                x_data[5] = dx * 5; y_data[5] = y_st;
                x_data[6] = dx * 6; y_data[6] = y_st;
                x_data[7] = dx * 7; y_data[7] = y_st;
                x_data[8] = dx * 8; y_data[8] = y_st;
                x_data[9] = dx * 9; y_data[9] = y_st;

                x_data[10] = dx * 10; y_data[10] = y_st;
                y_st += H;
                x_data[11] = dx * 10; y_data[11] = y_st;

                x_data[12] = dx * 11; y_data[12] = y_st;
                y_st -= H;
                x_data[13] = dx * 11; y_data[13] = y_st;

                x_data[14] = dx * 12; y_data[14] = y_st;
                y_st += H;
                x_data[15] = dx * 12; y_data[15] = y_st;

                x_data[16] = dx * 13; y_data[16] = y_st;
                y_st -= H;
                x_data[17] = dx * 13; y_data[17] = y_st;

                x_data[18] = dx * 14; y_data[18] = y_st;
                y_st += H;
                x_data[19] = dx * 14; y_data[19] = y_st;

                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線

                y_st = h;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;
                x_data[5] = dx * 5; y_data[5] = y_st;
                x_data[6] = dx * 6; y_data[6] = y_st;
                x_data[7] = dx * 7; y_data[7] = y_st;
                x_data[8] = dx * 8; y_data[8] = y_st;
                x_data[9] = dx * 9; y_data[9] = y_st;

                x_data[10] = dx * 10; y_data[10] = y_st;
                y_st += H;
                x_data[11] = dx * 10; y_data[11] = y_st;

                x_data[12] = dx * 11; y_data[12] = y_st;
                y_st -= H;
                x_data[13] = dx * 11; y_data[13] = y_st;

                x_data[14] = dx * 12; y_data[14] = y_st;
                y_st += H;
                x_data[15] = dx * 12; y_data[15] = y_st;

                x_data[16] = dx * 13; y_data[16] = y_st;
                y_st -= H;
                x_data[17] = dx * 13; y_data[17] = y_st;

                x_data[18] = dx * 14; y_data[18] = y_st;
                y_st += H;
                x_data[19] = dx * 14; y_data[19] = y_st;

                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints2 = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(redPen, curvePoints2);   //畫直線
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 8; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 8; y_data[8] = y_st;

                x_data[9] = dx * 8; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 18; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線




                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線
            }
            else if (draw_case == 5)
            {
                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 7; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 7; y_data[8] = y_st;

                x_data[9] = dx * 7; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 17; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 17; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線


                y_st = h;


                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 8; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 8; y_data[8] = y_st;

                x_data[9] = dx * 8; y_data[9] = y_st;
                x_data[10] = dx * 10; y_data[10] = y_st;
                x_data[11] = dx * 11; y_data[11] = y_st;
                x_data[12] = dx * 12; y_data[12] = y_st;
                x_data[13] = dx * 13; y_data[13] = y_st;
                x_data[14] = dx * 14; y_data[14] = y_st;

                x_data[15] = dx * 15; y_data[15] = y_st;
                y_st += H;
                x_data[16] = dx * 15; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                y_st -= H;
                x_data[18] = dx * 18; y_data[18] = y_st;

                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints2 = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(redPen, curvePoints2);   //畫直線






                /*
                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線
                */


            }
            else if (draw_case == 6)
            {

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 1; y_data[1] = y_st;
                x_data[2] = dx * 2; y_data[2] = y_st;
                x_data[3] = dx * 3; y_data[3] = y_st;
                x_data[4] = dx * 4; y_data[4] = y_st;

                x_data[5] = dx * 5; y_data[5] = y_st;
                y_st += H;
                x_data[6] = dx * 5; y_data[6] = y_st;

                x_data[7] = dx * 6; y_data[7] = y_st;
                y_st -= H;
                x_data[8] = dx * 6; y_data[8] = y_st;

                x_data[9] = dx * 7; y_data[9] = y_st;
                y_st += H;
                x_data[10] = dx * 7; y_data[10] = y_st;

                x_data[11] = dx * 8; y_data[11] = y_st;
                y_st -= H;
                x_data[12] = dx * 8; y_data[12] = y_st;

                x_data[13] = dx * 9; y_data[13] = y_st;
                y_st += H;
                x_data[14] = dx * 9; y_data[14] = y_st;

                x_data[15] = dx * 10; y_data[15] = y_st;
                y_st -= H;
                x_data[16] = dx * 10; y_data[16] = y_st;

                x_data[17] = dx * 18; y_data[17] = y_st;
                x_data[18] = dx * 18; y_data[18] = y_st;
                x_data[19] = dx * 19; y_data[19] = y_st;
                x_data[20] = dx * 20; y_data[20] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);
                point2 = new Point(x_data[2], h_st - y_data[2]);
                point3 = new Point(x_data[3], h_st - y_data[3]);
                point4 = new Point(x_data[4], h_st - y_data[4]);
                point5 = new Point(x_data[5], h_st - y_data[5]);
                point6 = new Point(x_data[6], h_st - y_data[6]);
                point7 = new Point(x_data[7], h_st - y_data[7]);
                point8 = new Point(x_data[8], h_st - y_data[8]);
                point9 = new Point(x_data[9], h_st - y_data[9]);
                point10 = new Point(x_data[10], h_st - y_data[10]);
                point11 = new Point(x_data[11], h_st - y_data[11]);
                point12 = new Point(x_data[12], h_st - y_data[12]);
                point13 = new Point(x_data[13], h_st - y_data[13]);
                point14 = new Point(x_data[14], h_st - y_data[14]);
                point15 = new Point(x_data[15], h_st - y_data[15]);
                point16 = new Point(x_data[16], h_st - y_data[16]);
                point17 = new Point(x_data[17], h_st - y_data[17]);
                point18 = new Point(x_data[18], h_st - y_data[18]);
                point19 = new Point(x_data[19], h_st - y_data[19]);
                point20 = new Point(x_data[20], h_st - y_data[20]);

                Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19, point20 };

                // Draw lines between original points to screen.
                g.DrawLines(greenPen, curvePoints);   //畫直線




                y_st = h + offset;

                x_data[0] = dx * 0; y_data[0] = y_st;
                x_data[1] = dx * 20; y_data[1] = y_st;

                // Create points that define curve.
                point0 = new Point(x_data[0], h_st - y_data[0]);
                point1 = new Point(x_data[1], h_st - y_data[1]);

                Point[] curvePoints3 = { point0, point1 };

                // Draw lines between original points to screen.
                g.DrawLines(blackPen, curvePoints3);   //畫直線



            }


            ArrowPen = new Pen(Color.Red, 6);   //重新設定pp的線條樣式
            ArrowPen.EndCap = LineCap.ArrowAnchor;

            if ((draw_case == 1) || (draw_case == 2))
            {
                x_st = dx * 10;
                y_st = h_st - (h + H + h + title_size3 + h + offset);

                x_sp = dx * 10;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
            }
            else if (draw_case == 3)
            {

            }
            else if (draw_case == 4)
            {
                x_st = dx * 8 + 3;
                y_st = h_st - (h + H + h + title_size3 + h + offset);
                x_sp = dx * 8 + 3;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                g.DrawString("Initialize OK", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st, y_st - H / 2));

                x_st = dx * 18 + 3;
                y_st = h_st - (h + H + h + title_size3 + h + offset);
                x_sp = dx * 18 + 3;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

            }
            else if (draw_case == 5)
            {

            }
            else if (draw_case == 6)
            {
                x_st = dx * 5;
                y_st = h_st - (h + H + h + title_size3 + h + offset);

                x_sp = dx * 5;
                y_sp = h_st - (h + H + h + title_size3 + h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

            }

            ArrowPen = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            ArrowPen.EndCap = LineCap.ArrowAnchor;

            if (draw_case == 1)
            {
                x_st = dx * 10;
                y_st = h_st - (h + offset);

                x_sp = dx * 10;
                y_sp = h_st - (h + offset + (H - offset * 2));
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 11;
                x_sp = dx * 11;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 12;
                x_sp = dx * 12;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 13;
                x_sp = dx * 13;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                x_st = dx * 14;
                x_sp = dx * 14;
                g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
            }
            else if (draw_case == 2)
            {

                y_st = h_st - (h + offset);
                y_sp = h_st - (h + offset + (H - offset * 2));

                for (int i = 1; i < 13; i++)
                {
                    x_st = dx * i * 3 / 2 + 5;
                    x_sp = dx * i * 3 / 2 + 5;
                    if (i == 12)
                    {
                        ArrowPen = new Pen(Color.Red, 10);   //重新設定pp的線條樣式
                        ArrowPen.EndCap = LineCap.ArrowAnchor;
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                    else
                    {
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                }
            }
            else if (draw_case == 3)
            {
                y_st = h_st - (h + offset);
                y_sp = h_st - (h + offset + (H - offset * 2));

                int x_st2 = 0;
                int y_st2 = h_st - (h + 60);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + 60);

                for (int i = 1; i < 4; i++)
                {
                    x_st = dx * i * 13 / 2 - 70;
                    x_sp = dx * i * 13 / 2 - 70;
                    richTextBox1.Text += "x = " + x_st.ToString() + "\n";
                    if (i == 3)
                    {
                        ArrowPen = new Pen(Color.Red, 10);   //重新設定pp的線條樣式
                        ArrowPen.EndCap = LineCap.ArrowAnchor;
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);

                        //int height = h + title_size1 + title_size2 + h + H + h + title_size3 + h + H + h;
                        Pen PenStyle2 = new Pen(Color.Black, 2);
                        PenStyle2.DashStyle = DashStyle.Dash;
                        g.DrawLine(PenStyle2, x_st, h + title_size1 + 30, x_sp, height);
                    }
                    else
                    {
                        g.DrawLine(ArrowPen, x_st, y_st, x_sp, y_sp);
                    }
                    if (i == 1)
                        x_st2 = x_st;
                    if (i == 2)
                        x_sp2 = x_st;
                }

                ArrowPen = new Pen(Color.Red, 5);   //重新設定pp的線條樣式
                ArrowPen.StartCap = LineCap.ArrowAnchor;
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                richTextBox1.Text += "x_st2 = " + x_st2.ToString() + "x_sp2 = " + x_sp2.ToString() + "\n";

                g.DrawString("1 sec", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 40, y_st2 + 5));
                g.DrawString("Conflict!", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(315, y_st2 - 55));

            }
            else if (draw_case == 4)
            {
                int x_st2 = 0;
                int y_st2 = h_st - (h + offset);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + offset + (H - offset * 2));

                x_st2 = dx * 8 + 6;
                x_sp2 = dx * 8 + 6;
                ArrowPen = new Pen(Color.Red, 8);   //重新設定pp的線條樣式
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";

                g.DrawString("Detect OK Signal", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2, y_st2 - H / 2));

                x_st2 = dx * 18 + 6;
                x_sp2 = dx * 18 + 6;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";
            }
            else if (draw_case == 5)
            {



            }
            else if (draw_case == 6)
            {
                int x_st2 = 0;
                int y_st2 = h_st - (h + offset);
                int x_sp2 = 0;
                int y_sp2 = h_st - (h + offset + (H - offset * 2));

                x_st2 = dx * 5;
                x_sp2 = dx * 5;
                ArrowPen = new Pen(Color.Red, 8);   //重新設定pp的線條樣式
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2, x_sp2, y_sp2);
                //richTextBox1.Text += "(" + x_st2.ToString() + ", " + y_st2.ToString() + ") - (" + x_sp2.ToString() + ", " + y_sp2.ToString() + ")\n";

                g.DrawString("Detect OK Signal", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 10, y_st2 - H / 2 - 30));



                ArrowPen = new Pen(Color.Black, 5);   //重新設定pp的線條樣式
                ArrowPen.StartCap = LineCap.ArrowAnchor;
                ArrowPen.EndCap = LineCap.ArrowAnchor;
                g.DrawLine(ArrowPen, x_st2, y_st2 - H / 2 + 20, x_st2 + 300, y_st2 - H / 2 + 20);
                richTextBox1.Text += "x_st2 = " + x_st2.ToString() + "x_sp2 = " + x_sp2.ToString() + "\n";

                g.DrawString("0.2 sec", new Font("Times New Roman", 17), new SolidBrush(Color.Red), new PointF(x_st2 + 120, y_st2 - H / 2 + 25));



            }

            int offset2 = 15;
            SolidBrush sb;
            Font f;
            f = new Font("Times New Roman", 17);
            sb = new SolidBrush(Color.Purple);
            if ((draw_case == 1) || (draw_case == 2))
            {
                g.DrawString("IE Insert Bouncing", f, sb, new PointF(0, h + offset2));
                //g.DrawString("Push Button Bouncing", f, sb, new PointF(0, h + offset2));
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                g.DrawString("IE initialization fails", f, sb, new PointF(0, h + offset2));
            }
            else if (draw_case == 5)
            {
                g.DrawString("Send Command to IE Error", f, sb, new PointF(0, h + offset2));
            }
            else if (draw_case == 6)
            {
                g.DrawString("Pedal Bouncing", f, sb, new PointF(0, h + offset2));
            }

            if ((draw_case == 1) || (draw_case == 2))
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("IE Insert", f, sb, new PointF(0, h + title_size1 + offset2));
                //g.DrawString("User Push Button", f, sb, new PointF(0, h + title_size1 + offset2));
                if (draw_case == 1)
                {
                    sb = new SolidBrush(Color.Green);
                    f = new Font("Times New Roman", 11);
                    g.DrawString("Hardware Response", f, sb, new PointF(310, h + title_size1 + title_size2 + h + 10));
                }
            }
            else if ((draw_case == 3) || (draw_case == 4))
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("IE Plug-in & initialize", f, sb, new PointF(0, h + title_size1 + offset2));
            }
            else if (draw_case == 5)
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("Send Data without Check-Sum", f, sb, new PointF(0, h + title_size1 + offset2));
            }
            else if (draw_case == 6)
            {
                sb = new SolidBrush(Color.Red);
                g.DrawString("Real Pedal Bouncing", f, sb, new PointF(0, h + title_size1 + offset2));
            }


            f = new Font("Times New Roman", 17);
            sb = new SolidBrush(Color.Blue);
            if (draw_case == 1)
                g.DrawString("Software Response", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 2)
                g.DrawString("Software Detect Stable IE Signal", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 3)
                g.DrawString("Software Detect IE", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 4)
                g.DrawString("Software Detect IE OK Signal", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 5)
                g.DrawString("Send Data with Check-Sum", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));
            else if (draw_case == 6)
                g.DrawString("Software Catthes First One", f, sb, new PointF(0, h + title_size1 + title_size2 + h + H + h + offset2));

            pictureBox1.Image = bitmap1;



        }


        private void button24_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

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

        private void button25_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_item_location2();
            pictureBox1.Location = new Point(50, 50);
            pictureBox1.Size = new Size(887, 636);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            Graphics g;

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            gamma = 2.2;
            //畫出真正的Gamma 2.2曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            gammaPen = new Pen(Color.Green, 2);
            gamma = 2.3;
            //畫出真正的Gamma 2.3曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            gammaPen = new Pen(Color.Blue, 2);
            gamma = 2.4;
            //畫出真正的Gamma 2.4曲線
            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                curvePoints[i].X = data_in[i] * 3;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線




            int YST0 = 0x00;
            int YST1 = 0x14;
            int YST2 = 0x22;
            int YST3 = 0x37;
            int YST4 = 0x4B;
            int YST5 = 0x5E;
            int YST6 = 0x6B;
            int YST7 = 0x76;
            int YST8 = 0x82;
            int YST9 = 0x8C;
            int YST10 = 0x9F;
            int YST11 = 0xAB;
            int YST12 = 0xB5;
            int YST13 = 0xCF;
            int YST14 = 0xDE;
            int YST15 = 0xED;

            int YSLP15 = 0x1B;

            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;

                if (data_in[i] <= 4)
                    data_out[i] = YST0 + (YST1 - YST0) * (data_in[i] - 0) / 4;
                else if (data_in[i] <= 8)
                    data_out[i] = YST1 + (YST2 - YST1) * (data_in[i] - 4) / 4;
                else if (data_in[i] <= 16)
                    data_out[i] = YST2 + (YST3 - YST2) * (data_in[i] - 8) / 8;
                else if (data_in[i] <= 32)
                    data_out[i] = YST4 + (YST4 - YST3) * (data_in[i] - 16) / 16;
                else if (data_in[i] <= 40)
                    data_out[i] = YST5 + (YST5 - YST4) * (data_in[i] - 32) / 8;
                else if (data_in[i] <= 48)
                    data_out[i] = YST6 + (YST6 - YST5) * (data_in[i] - 40) / 8;
                else if (data_in[i] <= 56)
                    data_out[i] = YST7 + (YST7 - YST6) * (data_in[i] - 48) / 8;
                else if (data_in[i] <= 64)
                    data_out[i] = YST8 + (YST8 - YST7) * (data_in[i] - 56) / 8;
                else if (data_in[i] <= 72)
                    data_out[i] = YST9 + (YST9 - YST8) * (data_in[i] - 64) / 8;
                else if (data_in[i] <= 80)
                    data_out[i] = YST10 + (YST10 - YST9) * (data_in[i] - 72) / 8;
                else if (data_in[i] <= 96)
                    data_out[i] = YST11 + (YST11 - YST10) * (data_in[i] - 80) / 16;
                else if (data_in[i] <= 112)
                    data_out[i] = YST12 + (YST12 - YST11) * (data_in[i] - 96) / 16;
                else if (data_in[i] <= 144)
                    data_out[i] = YST13 + (YST13 - YST12) * (data_in[i] - 112) / 32;
                else if (data_in[i] <= 176)
                    data_out[i] = YST14 + (YST14 - YST13) * (data_in[i] - 144) / 32;
                else if (data_in[i] <= 208)
                    data_out[i] = YST15 + (YST15 - YST14) * (data_in[i] - 176) / 32;
                else
                {
                    if (cb_manual.Checked == false)
                    {
                        data_out[i] = YST15 + YSLP15 * (data_in[i] - 208) / 64;


                    }
                    else
                    {

                        data_out[i] = YST15 + YSLP15 * (data_in[i] - 208) / 64;
                    }
                }
            }

            //int YSLP15 = 0x1B;
            //Yst15 + Yslp15 × (data - 208) / 64


            richTextBox1.Text += "In:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_in[i].ToString() + " ";
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Out:\n";
            for (i = 0; i < 256; i++)
                richTextBox1.Text += data_out[i].ToString() + " ";
            richTextBox1.Text += "\n";

            pictureBox1.Size = new Size(256 * 3, 256 * 2);   //改變圖框大小

            Pen redPen = new Pen(Color.Red, 3);

            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = data_in[i] * 3;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;


                //curvePoints[i].X = i;
                //curvePoints[i].Y = H - (int)y1_data[i] - 100;
                //curvePoints[i].Y = H - (offset_y + (int)y1_data[i] + (draw_max - draw_min) / 2000) * 2;
                //curvePoints[i].Y = 100;

            }

            // Draw lines between original points to screen.
            g.DrawLines(redPen, curvePoints);   //畫直線

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1));

            pictureBox1.Image = bitmap1;
        }

        bool isDrawing = false;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;

            pictureBox1_MouseMove(sender, e);
        }

        bool isDoingMagnifying = false;
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            int region = 30;
            if (isMagnifying == true)
            {
                //pictureBox1擷取一小部分貼到pictureBox2上, 達到放大功能
                if (isDoingMagnifying == false)
                {
                    isDoingMagnifying = true;

                    if (((e.X - region * 2) < 0) || ((e.X + region * 2) > pictureBox1.Width))
                    {
                        isDoingMagnifying = false;
                        return;
                    }

                    if (((e.Y - region * 2) < 0) || ((e.Y + region * 2) > pictureBox1.Height))
                    {
                        isDoingMagnifying = false;
                        return;
                    }

                    RectangleF rect = new RectangleF(e.X, e.Y, 50, 50);

                    try
                    {
                        // 擷取部份影像，顯示於pictureBox2，區域為(起點x座標, 起點y座標, 寬度, 高度)
                        // 將處理之後的圖片貼出來
                        pictureBox2.Image = bitmap1.Clone(rect, PixelFormat.Format32bppArgb);
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息p : " + ex.Message + "\t";
                        //richTextBox1.Text += "e.X = " + e.X.ToString() + ", e.Y = " + e.Y.ToString() + "\n";
                        //richTextBox1.Text += "t1 = " + (e.X - region).ToString() + ", t2 = " + (e.X + region).ToString() + "\n";
                        //richTextBox1.Text += "t3 = " + (e.Y - region).ToString() + ", t4 = " + (e.Y + region).ToString() + "\n";
                        //richTextBox1.Text += "W = " + pictureBox1.Width.ToString() + ", H = " + pictureBox1.Height.ToString() + "\n";
                    }
                    GC.Collect();       //回收資源
                    isDoingMagnifying = false;
                }
                return;
            }

            if (isDrawing == false)
                return;

            if (cb_snake.Checked == false)
                return;

            this.Text = e.X.ToString() + ", " + e.Y.ToString();
            int w = pictureBox1.Width;
            int h = pictureBox1.Height;
            int i;
            int j;
            int r;
            //g.Clear(Color.White);
            for (j = 0; j < h; j++)
            {
                if ((j > (e.Y - region)) && (j < (e.Y + region)))
                {
                    for (i = 0; i < w; i++)
                    {
                        if ((i > (e.X - region)) && (i < (e.X + region)))
                        {
                            r = (int)Math.Sqrt((e.X - i) * (e.X - i) + (e.Y - j) * (e.Y - j));
                            if (r < region)
                                bitmap1.SetPixel(i, j, Color.FromArgb(255 - r * (256 / region), 0xff, 0x0, 0x0));
                        }



                    }


                }

            }

            pictureBox1.Image = bitmap1;

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }

        private void cb_snake_CheckedChanged(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            //指定畫布大小
            pictureBox1.Width = 600;
            pictureBox1.Height = 600;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            p = new Pen(Color.Red, 3);     // 設定畫筆為紅色、粗細為 3 點。

            if (cb_snake.Checked == true)
            {
                g.Clear(Color.Lime);
            }
            else
            {
                g.Clear(Color.Pink);
            }
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            int width = pictureBox1.Width;
            int height = pictureBox1.Height;

            //把PictureBox上的東西匯出至檔案
            Bitmap bm = new Bitmap(width, height);
            pictureBox1.DrawToBitmap(bm, new Rectangle(0, 0, width, height));   //匯出全部, 可以在此選擇匯出區域

            string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
            string filename1 = filename + ".jpg";
            string filename2 = filename + ".bmp";
            string filename3 = filename + ".png";

            try
            {
                bm.Save(@filename1, ImageFormat.Jpeg);
                bm.Save(@filename2, ImageFormat.Bmp);
                bm.Save(@filename3, ImageFormat.Png);

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

        bool isMagnifying = false;
        private void cb_magnifying_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_magnifying.Checked == true)
                isMagnifying = true;
            else
                isMagnifying = false;
        }

    }
}
