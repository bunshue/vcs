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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 800;
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

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

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
            pen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(pen, 50, 400, 50, 100);  //畫出X軸及y軸
            g.DrawLine(pen, 50, 400, 350, 400);

            pen = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            //pp.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot; //DashStyle設定線條 點
            //pp.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor; //設定為圓頭

            pen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

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
            g.FillRectangle(bb, 70, 70, 200, 100);
            //畫出一個填滿的方框

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
                    data_out[i] = YST15 + YSLP15 * (data_in[i] - 208) / 64;
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

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

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

        private void button25_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }


    }
}
