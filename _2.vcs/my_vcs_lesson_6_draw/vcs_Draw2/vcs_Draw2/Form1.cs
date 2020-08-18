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
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 3);

            if (radioButton1.Checked == true)
            {
                g = pictureBox1.CreateGraphics();
                p = new Pen(Color.Red, 10);     //default pen
                pictureBox1.Location = new Point(50, 50);

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
            int width = 1920 / 2;
            int height = 1080 / 2;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            int i;
            int j;
            int w = 150;
            int h = 100;
            Color c = new Color();

            i = 0; j = 0; c = Color.Red;
            drawBox(i, j, w, h, c);

            i = 1; j = 0; c = Color.Green;
            drawBox(i, j, w, h, c);

            i = 2; j = 0; c = Color.Blue;
            drawBox(i, j, w, h, c);

            i = 0; j = 1; c = Color.Cyan;
            drawBox(i, j, w, h, c);

            i = 1; j = 1; c = Color.Magenta;
            drawBox(i, j, w, h, c);

            i = 2; j = 1; c = Color.Yellow;
            drawBox(i, j, w, h, c);

            i = 3; j = 1; c = Color.Black;
            drawBox(i, j, w, h, c);

            i = 4; j = 1; c = Color.White;
            drawBox(i, j, w, h, c);

            i = 0; j = 2; c = Color.Orange;
            drawBox(i, j, w, h, c);

            i = 1; j = 2; c = Color.OrangeRed;
            drawBox(i, j, w, h, c);

            i = 2; j = 2; c = Color.Olive;
            drawBox(i, j, w, h, c);

            i = 3; j = 2; c = Color.Navy;
            drawBox(i, j, w, h, c);

            i = 4; j = 2; c = Color.Orchid;
            drawBox(i, j, w, h, c);

            i = 0; j = 3; c = Color.Wheat;
            drawBox(i, j, w, h, c);

            i = 1; j = 3; c = Color.Peru;
            drawBox(i, j, w, h, c);

            i = 2; j = 3; c = Color.Pink;
            drawBox(i, j, w, h, c);

            i = 3; j = 3; c = Color.HotPink;
            drawBox(i, j, w, h, c);

            i = 4; j = 3; c = Color.Honeydew;
            drawBox(i, j, w, h, c);

            pictureBox1.Image = bitmap1;

        }

        void drawBox(int i, int j, int w, int h, Color c)
        {
            Font f;
            sb = new SolidBrush(c);
            g.FillRectangle(sb, w * i, h * j, w - 1, h - 1);

            //sb = new SolidBrush(Color.Black);
            sb = new SolidBrush(Color.FromArgb(255 - c.R, 255 - c.G, 255 - c.B));

            f = new Font("標楷體", 12);
            g.DrawString(c.Name, f, sb, new PointF(w * i, h * j + h / 3));
        }



        private void button10_Click(object sender, EventArgs e)
        {
            int i = 0;
            int j = 0;
            int w = 114;
            int h = 40;

            panel1.Visible = false;
            this.Size = new Size(this.Size.Width, this.Size.Height + 150);
            int width = w * 7;
            int height = h * 20;

            pictureBox1.Size = new Size(width, height);
            pictureBox1.Location = new Point(0, 0);

            bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            Color c = new Color();

            i = 0; c = Color.AliceBlue; drawBox(i, j, w, h, c);
            i++; c = Color.AntiqueWhite; drawBox(i, j, w, h, c);
            i++; c = Color.Aqua; drawBox(i, j, w, h, c);
            i++; c = Color.Aquamarine; drawBox(i, j, w, h, c);
            i++; c = Color.Azure; drawBox(i, j, w, h, c);
            i++; c = Color.Beige; drawBox(i, j, w, h, c);
            i++; c = Color.Bisque; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Black; drawBox(i, j, w, h, c);
            i++; c = Color.BlanchedAlmond; drawBox(i, j, w, h, c);
            i++; c = Color.Blue; drawBox(i, j, w, h, c);
            i++; c = Color.BlueViolet; drawBox(i, j, w, h, c);
            i++; c = Color.Brown; drawBox(i, j, w, h, c);
            i++; c = Color.BurlyWood; drawBox(i, j, w, h, c);
            i++; c = Color.CadetBlue; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Chartreuse; drawBox(i, j, w, h, c);
            i++; c = Color.Chocolate; drawBox(i, j, w, h, c);
            i++; c = Color.Coral; drawBox(i, j, w, h, c);
            i++; c = Color.CornflowerBlue; drawBox(i, j, w, h, c);
            i++; c = Color.Cornsilk; drawBox(i, j, w, h, c);
            i++; c = Color.Crimson; drawBox(i, j, w, h, c);
            i++; c = Color.Cyan; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.DarkBlue; drawBox(i, j, w, h, c);
            i++; c = Color.DarkCyan; drawBox(i, j, w, h, c);
            i++; c = Color.DarkGoldenrod; drawBox(i, j, w, h, c);
            i++; c = Color.DarkGray; drawBox(i, j, w, h, c);
            i++; c = Color.DarkGreen; drawBox(i, j, w, h, c); drawBox(i, j, w, h, c);
            i++; c = Color.DarkKhaki; drawBox(i, j, w, h, c);
            i++; c = Color.DarkMagenta; drawBox(i, j, w, h, c);


            j++;
            i = 0; c = Color.DarkOliveGreen; drawBox(i, j, w, h, c);
            i++; c = Color.DarkOrange; drawBox(i, j, w, h, c);
            i++; c = Color.DarkOrchid; drawBox(i, j, w, h, c);
            i++; c = Color.DarkRed; drawBox(i, j, w, h, c);
            i++; c = Color.DarkSalmon; drawBox(i, j, w, h, c);
            i++; c = Color.DarkSeaGreen; drawBox(i, j, w, h, c);
            i++; c = Color.DarkSlateBlue; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.DarkSlateGray; drawBox(i, j, w, h, c);
            i++; c = Color.DarkTurquoise; drawBox(i, j, w, h, c);
            i++; c = Color.DarkViolet; drawBox(i, j, w, h, c);
            i++; c = Color.DeepPink; drawBox(i, j, w, h, c);
            i++; c = Color.DeepSkyBlue; drawBox(i, j, w, h, c);
            i++; c = Color.DimGray; drawBox(i, j, w, h, c);
            i++; c = Color.DodgerBlue; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Firebrick; drawBox(i, j, w, h, c);
            i++; c = Color.FloralWhite; drawBox(i, j, w, h, c);
            i++; c = Color.ForestGreen; drawBox(i, j, w, h, c);
            i++; c = Color.Fuchsia; drawBox(i, j, w, h, c);
            i++; c = Color.Gainsboro; drawBox(i, j, w, h, c);
            i++; c = Color.GhostWhite; drawBox(i, j, w, h, c);
            i++; c = Color.Gold; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Goldenrod; drawBox(i, j, w, h, c);
            i++; c = Color.Gray; drawBox(i, j, w, h, c);
            i++; c = Color.Green; drawBox(i, j, w, h, c);
            i++; c = Color.GreenYellow; drawBox(i, j, w, h, c);
            i++; c = Color.Honeydew; drawBox(i, j, w, h, c);
            i++; c = Color.HotPink; drawBox(i, j, w, h, c);
            i++; c = Color.IndianRed; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Indigo; drawBox(i, j, w, h, c);
            i++; c = Color.Ivory; drawBox(i, j, w, h, c);
            i++; c = Color.Khaki; drawBox(i, j, w, h, c);
            i++; c = Color.Lavender; drawBox(i, j, w, h, c);
            i++; c = Color.LavenderBlush; drawBox(i, j, w, h, c);
            i++; c = Color.LawnGreen; drawBox(i, j, w, h, c);
            i++; c = Color.LemonChiffon; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.LightBlue; drawBox(i, j, w, h, c);
            i++; c = Color.LightCoral; drawBox(i, j, w, h, c);
            i++; c = Color.LightCyan; drawBox(i, j, w, h, c);
            i++; c = Color.LightGoldenrodYellow; drawBox(i, j, w, h, c);
            i++; c = Color.LightGreen; drawBox(i, j, w, h, c);
            i++; c = Color.LightGray; drawBox(i, j, w, h, c);
            i++; c = Color.LightPink; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.LightSalmon; drawBox(i, j, w, h, c);
            i++; c = Color.LightSeaGreen; drawBox(i, j, w, h, c);
            i++; c = Color.LightSkyBlue; drawBox(i, j, w, h, c);
            i++; c = Color.LightSlateGray; drawBox(i, j, w, h, c);
            i++; c = Color.LightSteelBlue; drawBox(i, j, w, h, c);
            i++; c = Color.LightYellow; drawBox(i, j, w, h, c);
            i++; c = Color.Lime; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.LimeGreen; drawBox(i, j, w, h, c);
            i++; c = Color.Linen; drawBox(i, j, w, h, c);
            i++; c = Color.Magenta; drawBox(i, j, w, h, c);
            i++; c = Color.Maroon; drawBox(i, j, w, h, c);
            i++; c = Color.MediumAquamarine; drawBox(i, j, w, h, c);
            i++; c = Color.MediumBlue; drawBox(i, j, w, h, c);
            i++; c = Color.MediumOrchid; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.MediumPurple; drawBox(i, j, w, h, c);
            i++; c = Color.MediumSeaGreen; drawBox(i, j, w, h, c);
            i++; c = Color.MediumSlateBlue; drawBox(i, j, w, h, c);
            i++; c = Color.MediumSpringGreen; drawBox(i, j, w, h, c);
            i++; c = Color.MediumTurquoise; drawBox(i, j, w, h, c);
            i++; c = Color.MediumVioletRed; drawBox(i, j, w, h, c);
            i++; c = Color.MidnightBlue; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.MintCream; drawBox(i, j, w, h, c);
            i++; c = Color.MistyRose; drawBox(i, j, w, h, c);
            i++; c = Color.Moccasin; drawBox(i, j, w, h, c);
            i++; c = Color.NavajoWhite; drawBox(i, j, w, h, c);
            i++; c = Color.Navy; drawBox(i, j, w, h, c);
            i++; c = Color.OldLace; drawBox(i, j, w, h, c);
            i++; c = Color.Olive; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.OliveDrab; drawBox(i, j, w, h, c);
            i++; c = Color.Orange; drawBox(i, j, w, h, c);
            i++; c = Color.OrangeRed; drawBox(i, j, w, h, c);
            i++; c = Color.Orchid; drawBox(i, j, w, h, c);
            i++; c = Color.PaleGoldenrod; drawBox(i, j, w, h, c);
            i++; c = Color.PaleGreen; drawBox(i, j, w, h, c);
            i++; c = Color.PaleTurquoise; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.PaleVioletRed; drawBox(i, j, w, h, c);
            i++; c = Color.PapayaWhip; drawBox(i, j, w, h, c);
            i++; c = Color.PeachPuff; drawBox(i, j, w, h, c);
            i++; c = Color.Peru; drawBox(i, j, w, h, c);
            i++; c = Color.Pink; drawBox(i, j, w, h, c);
            i++; c = Color.Plum; drawBox(i, j, w, h, c);
            i++; c = Color.PowderBlue; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Purple; drawBox(i, j, w, h, c);
            i++; c = Color.Red; drawBox(i, j, w, h, c);
            i++; c = Color.RosyBrown; drawBox(i, j, w, h, c);
            i++; c = Color.RoyalBlue; drawBox(i, j, w, h, c);
            i++; c = Color.SaddleBrown; drawBox(i, j, w, h, c);
            i++; c = Color.Salmon; drawBox(i, j, w, h, c);
            i++; c = Color.SandyBrown; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.SeaGreen; drawBox(i, j, w, h, c);
            i++; c = Color.SeaShell; drawBox(i, j, w, h, c);
            i++; c = Color.Sienna; drawBox(i, j, w, h, c);
            i++; c = Color.Silver; drawBox(i, j, w, h, c);
            i++; c = Color.SkyBlue; drawBox(i, j, w, h, c);
            i++; c = Color.SlateBlue; drawBox(i, j, w, h, c);
            i++; c = Color.SlateGray; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Snow; drawBox(i, j, w, h, c);
            i++; c = Color.SpringGreen; drawBox(i, j, w, h, c);
            i++; c = Color.SteelBlue; drawBox(i, j, w, h, c);
            i++; c = Color.Tan; drawBox(i, j, w, h, c);
            i++; c = Color.Teal; drawBox(i, j, w, h, c);
            i++; c = Color.Thistle; drawBox(i, j, w, h, c);
            i++; c = Color.Tomato; drawBox(i, j, w, h, c);

            j++;
            i = 0; c = Color.Turquoise; drawBox(i, j, w, h, c);
            i++; c = Color.Violet; drawBox(i, j, w, h, c);
            i++; c = Color.Wheat; drawBox(i, j, w, h, c);
            i++; c = Color.White; drawBox(i, j, w, h, c);
            i++; c = Color.WhiteSmoke; drawBox(i, j, w, h, c);
            i++; c = Color.Yellow; drawBox(i, j, w, h, c);
            i++; c = Color.YellowGreen; drawBox(i, j, w, h, c);




            
            







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
