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

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 820;
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
            bt_exit.Location = new Point(x_st + dx * 4, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 9 + 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width + 240, this.Height - richTextBox1.Location.Y - 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //pictureBox1.Location = new Point(10, 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
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

        private Color[] Colors = new Color[]
        {
            Color.AliceBlue,
            Color.AntiqueWhite,
            Color.Aqua,
            Color.Aquamarine,
            Color.Azure,
            Color.Beige,
            Color.Bisque,

            Color.Black,
            Color.BlanchedAlmond,
            Color.Blue,
            Color.BlueViolet,
            Color.Brown,
            Color.BurlyWood,
            Color.CadetBlue,

            Color.Chartreuse,
            Color.Chocolate,
            Color.Coral,
            Color.CornflowerBlue,
            Color.Cornsilk,
            Color.Crimson,
            Color.Cyan,

            Color.DarkBlue,
            Color.DarkCyan,
            Color.DarkGoldenrod,
            Color.DarkGray,
            Color.DarkGreen,
            Color.DarkKhaki,
            Color.DarkMagenta,


            Color.DarkOliveGreen,
            Color.DarkOrange,
            Color.DarkOrchid,
            Color.DarkRed,
            Color.DarkSalmon,
            Color.DarkSeaGreen,
            Color.DarkSlateBlue,

            Color.DarkSlateGray,
            Color.DarkTurquoise,
            Color.DarkViolet,
            Color.DeepPink,
            Color.DeepSkyBlue,
            Color.DimGray,
            Color.DodgerBlue,

            Color.Firebrick,
            Color.FloralWhite,
            Color.ForestGreen,
            Color.Fuchsia,
            Color.Gainsboro,
            Color.GhostWhite,
            Color.Gold,

            Color.Goldenrod,
            Color.Gray,
            Color.Green,
            Color.GreenYellow,
            Color.Honeydew,
            Color.HotPink,
            Color.IndianRed,

            Color.Indigo,
            Color.Ivory,
            Color.Khaki,
            Color.Lavender,
            Color.LavenderBlush,
            Color.LawnGreen,
            Color.LemonChiffon,

            Color.LightBlue,
            Color.LightCoral,
            Color.LightCyan,
            Color.LightGoldenrodYellow,
            Color.LightGreen,
            Color.LightGray,
            Color.LightPink,

            Color.LightSalmon,
            Color.LightSeaGreen,
            Color.LightSkyBlue,
            Color.LightSlateGray,
            Color.LightSteelBlue,
            Color.LightYellow,
            Color.Lime,

            Color.LimeGreen,
            Color.Linen,
            Color.Magenta,
            Color.Maroon,
            Color.MediumAquamarine,
            Color.MediumBlue,
            Color.MediumOrchid,

            Color.MediumPurple,
            Color.MediumSeaGreen,
            Color.MediumSlateBlue,
            Color.MediumSpringGreen,
            Color.MediumTurquoise,
            Color.MediumVioletRed,
            Color.MidnightBlue,

            Color.MintCream,
            Color.MistyRose,
            Color.Moccasin,
            Color.NavajoWhite,
            Color.Navy,
            Color.OldLace,
            Color.Olive,

            Color.OliveDrab,
            Color.Orange,
            Color.OrangeRed,
            Color.Orchid,
            Color.PaleGoldenrod,
            Color.PaleGreen,
            Color.PaleTurquoise,

            Color.PaleVioletRed,
            Color.PapayaWhip,
            Color.PeachPuff,
            Color.Peru,
            Color.Pink,
            Color.Plum,
            Color.PowderBlue,

            Color.Purple,
            Color.Red,
            Color.RosyBrown,
            Color.RoyalBlue,
            Color.SaddleBrown,
            Color.Salmon,
            Color.SandyBrown,

            Color.SeaGreen,
            Color.SeaShell,
            Color.Sienna,
            Color.Silver,
            Color.SkyBlue,
            Color.SlateBlue,
            Color.SlateGray,

            Color.Snow,
            Color.SpringGreen,
            Color.SteelBlue,
            Color.Tan,
            Color.Teal,
            Color.Thistle,
            Color.Tomato,

            Color.Turquoise,
            Color.Violet,
            Color.Wheat,
            Color.White,
            Color.WhiteSmoke,
            Color.Yellow,
            Color.YellowGreen,
        };

        private void button11_Click(object sender, EventArgs e)
        {
            int i = 0;
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

            int len;
            len = Colors.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int x_st = 0;
            int y_st = 0;
            for (i = 0; i < len; i++)
            {
                sb = new SolidBrush(Colors[i % len]);
                g.FillRectangle(sb, x_st + w * (i / 20), y_st + h * (i % 20), w, h);
                richTextBox1.Text += Colors[i % len].Name + "\n";

                Font f;
                f = new Font("標楷體", 12);
                sb = new SolidBrush(Color.FromArgb(255 - Colors[i % len].R, 255 - Colors[i % len].G, 255 - Colors[i % len].B));
                g.DrawString(Colors[i % len].Name.ToString(), f, sb, new PointF(x_st + w * (i / 20), y_st + h * (i % 20) + 12));

            }
            pictureBox1.Image = bitmap1;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            int width = 780;
            int height = 600;

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

        private void button13_Click(object sender, EventArgs e)
        {
            int width = 780;
            int height = 600;

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

            pictureBox1.Image = bitmap1;

        }

        private void button14_Click(object sender, EventArgs e)
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
            Image newImage = Image.FromFile(@"C:\______test_files\cat\cat2.png");
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
            p = new Pen(Color.Red, 10);     // 設定畫筆為藍色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);

            GraphicsPath myPath1 = DrawRoundRect(100, 100, 200, 100, 30);
            g.FillPath(sb, myPath1);

            GraphicsPath myPath2 = DrawRoundRect(100, 250, 400, 300, 50);
            g.DrawPath(p, myPath2);
        }

        //繪製圓角矩形
        private GraphicsPath DrawRoundRect(float x, float y, float width, float height, float cornerRadius)
        {
            GraphicsPath roundedRect = new GraphicsPath();
            Rectangle rect = new Rectangle((int)x, (int)y, (int)width, (int)height);
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();
            return roundedRect;
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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


    }
}
