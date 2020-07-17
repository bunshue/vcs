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

            show_item_location();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);
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

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Graphics graphic = this.CreateGraphics();
            Font f = new Font("標楷體", 18, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Black);
            graphic.DrawString("生日快樂!", f, sb, 10, 10);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            DrawVerticalString();
        }

        int dd = 0;
        public void DrawVerticalString()
        {
            Graphics g = this.CreateGraphics();
            string str = "imsLink每次影像重抓 像是會慢一陣子";
            Font f = new Font("Arial", 16);
            SolidBrush sb = new SolidBrush(Color.Black);
            StringFormat drawFormat = new StringFormat();

            dd++;
            float x = 150.0F + dd;
            float y = 50.0F + dd;


            //richTextBox1.Text += "111\t" + drawFormat.FormatFlags.ToString() + "\n";
            //drawFormat.FormatFlags = StringFormatFlags.
            g.DrawString(str, f, sb, x, y, drawFormat);

            //richTextBox1.Text += "222\t" + drawFormat.FormatFlags.ToString() + "\n";
            //drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;
            g.DrawString(str, f, sb, x, y + 100, drawFormat);

            drawFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            //richTextBox1.Text += "333\t" + drawFormat.FormatFlags.ToString() + "\n";
            g.DrawString(str, f, sb, x, y, drawFormat);

            f.Dispose();
            sb.Dispose();
            g.Dispose();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            // Construct a new Rectangle.
            Rectangle r = new Rectangle(new Point(50, 50), new Size(300, 300));
            Font f = new Font("標楷體", 12, FontStyle.Bold);
            SolidBrush sb = new SolidBrush(Color.Black);

            StringFormat fmt = new StringFormat(StringFormatFlags.NoClip);

            // Draw the bounding rectangle
            g.DrawRectangle(Pens.Black, r);

            fmt.LineAlignment = StringAlignment.Near;    //向上對齊
            fmt.Alignment = StringAlignment.Near;      //水平靠左
            g.DrawString("對齊上左方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Near;    //向上對齊
            fmt.Alignment = StringAlignment.Center;      //水平置中
            g.DrawString("對齊上中方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Near;    //向上對齊
            fmt.Alignment = StringAlignment.Far;      //水平靠右
            g.DrawString("對齊上右方", f, sb, (RectangleF)r, fmt);


            fmt.LineAlignment = StringAlignment.Center;    //向中對齊
            fmt.Alignment = StringAlignment.Near;      //水平靠左
            g.DrawString("對齊中左方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Center;    //向中對齊
            fmt.Alignment = StringAlignment.Center;      //水平置中
            g.DrawString("對齊中中方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Center;  //向中對齊
            fmt.Alignment = StringAlignment.Far;         //水平靠右
            g.DrawString("對齊中右方", f, sb, (RectangleF)r, fmt);


            fmt.LineAlignment = StringAlignment.Far;    //向下對齊
            fmt.Alignment = StringAlignment.Near;      //水平靠左
            g.DrawString("對齊下左方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Far;    //向下對齊
            fmt.Alignment = StringAlignment.Center;      //水平置中
            g.DrawString("對齊下中方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Far;  //向下對齊
            fmt.Alignment = StringAlignment.Far;         //水平靠右
            g.DrawString("對齊下右方", f, sb, (RectangleF)r, fmt);

            fmt.LineAlignment = StringAlignment.Center;  //向中對齊
            fmt.Alignment = StringAlignment.Far;         //水平靠右
            fmt.FormatFlags = StringFormatFlags.DirectionVertical;  //直書
            g.DrawString("向中對齊+水平靠右+直書", f, Brushes.Red, (RectangleF)r, fmt);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //使用StringFormat與適當DrawString方法來指定置中對齊的文字。
            Graphics g = this.CreateGraphics();
            string text1 = "Use StringFormat and Rectangle objects to center text in a rectangle.";
            using (Font font1 = new Font("Arial", 22, FontStyle.Bold, GraphicsUnit.Point))
            {
                Rectangle rect1 = new Rectangle(10, 10, 130, 140);

                // Create a StringFormat object with the each line of text, and the block
                // of text centered on the page.
                StringFormat stringFormat = new StringFormat();
                stringFormat.Alignment = StringAlignment.Center;
                stringFormat.LineAlignment = StringAlignment.Center;

                // Draw the text and the surrounding rectangle.
                g.DrawString(text1, font1, Brushes.Blue, rect1, stringFormat);
                g.DrawRectangle(Pens.Black, rect1);
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //使用TextFormatFlags列舉型別換行，以及以垂直和水平置中與適當的文字DrawText方法。
            Graphics g = this.CreateGraphics();
            string text2 = "Use TextFormatFlags and Rectangle objects to center text in a rectangle.";

            using (Font font2 = new Font("Arial", 12, FontStyle.Bold, GraphicsUnit.Point))
            {
                Rectangle rect2 = new Rectangle(150, 10, 130, 140);

                // Create a TextFormatFlags with word wrapping, horizontal center and
                // vertical center specified.
                TextFormatFlags flags = TextFormatFlags.HorizontalCenter |
                    TextFormatFlags.VerticalCenter | TextFormatFlags.WordBreak;

                // Draw the text and the surrounding rectangle.
                TextRenderer.DrawText(g, text2, font2, rect2, Color.Blue, flags);
                g.DrawRectangle(Pens.Black, rect2);
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {

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

        private void button18_Click(object sender, EventArgs e)
        {
            //p = new Pen(Color.Red, 5);
            int width, height;
            width = pictureBox1.ClientSize.Width;
            height = pictureBox1.ClientSize.Height;
            g.Clear(Color.LightGreen);
            g.DrawRectangle(p, 0, 0, width - 1, height - 1);

        }

        private void button19_Click(object sender, EventArgs e)
        {
            //g.Clear(Color.LightGreen);
            p.Width = 10;
            for (int i = 0; i <= pictureBox1.Width; i = i + 36)
            {
                g.DrawLine(p, i, 0, i, pictureBox1.Height);
                p.Width += 2;
            }

        }








    }
}
