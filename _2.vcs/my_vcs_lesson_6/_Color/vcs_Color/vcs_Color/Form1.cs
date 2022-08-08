using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;    //for PropertyInfo

namespace vcs_Color
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;

        int[,] rgb_array = new int[64, 3] {
{   0,   0, 143},
{   0,   0, 159},
{   0,   0, 175},
{   0,   0, 191},
{   0,   0, 207},
{   0,   0, 223},
{   0,   0, 239},
{   0,   0, 255},
{   0,  16, 255},
{   0,  32, 255},
{   0,  48, 255},
{   0,  64, 255},
{   0,  80, 255},
{   0,  96, 255},
{   0, 112, 255},
{   0, 128, 255},
{   0, 143, 255},
{   0, 159, 255},
{   0, 175, 255},
{   0, 191, 255},
{   0, 207, 255},
{   0, 223, 255},
{   0, 239, 255},
{   0, 255, 255},
{  16, 255, 239},
{  32, 255, 223},
{  48, 255, 207},
{  64, 255, 191},
{  80, 255, 175},
{  96, 255, 159},
{ 112, 255, 143},
{ 128, 255, 128},
{ 143, 255, 112},
{ 159, 255,  96},
{ 175, 255,  80},
{ 191, 255,  64},
{ 207, 255,  48},
{ 223, 255,  32},
{ 239, 255,  16},
{ 255, 255,   0},
{ 255, 239,   0},
{ 255, 223,   0},
{ 255, 207,   0},
{ 255, 191,   0},
{ 255, 175,   0},
{ 255, 159,   0},
{ 255, 143,   0},
{ 255, 128,   0},
{ 255, 112,   0},
{ 255,  96,   0},
{ 255,  80,   0},
{ 255,  64,   0},
{ 255,  48,   0},
{ 255,  32,   0},
{ 255,  16,   0},
{ 255,   0,   0},
{ 239,   0,   0},
{ 223,   0,   0},
{ 207,   0,   0},
{ 191,   0,   0},
{ 175,   0,   0},
{ 159,   0,   0},
{ 143,   0,   0},
{ 128,   0,   0}
};


        int[,] rgb_array2 = new int[12, 3] {
{0     ,0     ,0},
{255   ,255   ,255},
{255     ,0     ,0},
{0   ,255     ,0},
{0     ,0   ,255},
{255   ,255     ,0},
{255     ,0   ,255},
{0   ,255   ,255},
{128   ,128   ,128},
{128     ,0     ,0},
{255   ,158   ,102},
{125   ,255   ,212}
};

        string[] rgb_array2_name = new string[] {
"black（黑）","white（白）","red（紅）","green（綠）",
"blue（藍）","yellow（黃）","magenta（錳紫）","cyan（青藍）",
"gray（灰）","dark red（暗紅）","copper（銅色）","aquamarine（碧綠）"};


        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 6);
        }

        void show_item_location()
        {
            /*
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            //設定執行後的表單大小
            this.Size = new Size(1920, 1040);
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);
            */

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 180 + 10;
            dy = 55 + 10;

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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(900, 700);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.BackColor = Color.Pink;

            richTextBox1.Size = new Size(300, 700);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1700, 800);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //已知的顏色列舉

            pictureBox1.Size = new Size(900, 600);

            Graphics g = pictureBox1.CreateGraphics();

            // 將 KnownColor 列舉的內容項目複雜到 allColors 陣列
            Array colorsArray = Enum.GetValues(typeof(KnownColor));
            KnownColor[] allColors = new KnownColor[colorsArray.Length];
            Array.Copy(colorsArray, allColors, colorsArray.Length);

            richTextBox1.Text += "共有 " + allColors.Length.ToString() + " 種顏色\n";
            // Loop through printing out the values' names in the colors 
            // they represent.
            float y = -20;
            float x = 0;

            for (int i = 0; i < allColors.Length; i++)
            {
                // 一排 25 個
                if (i > 0 && i % 25 == 0)
                {
                    x += 120.0f;
                    y = 0.0f;
                }
                else
                {
                    // 在該排中 往下列出
                    y += 22.0F;
                }

                // 產生該顏色的塗刷
                SolidBrush sb = new SolidBrush(Color.FromName(allColors[i].ToString()));
                Font f = new Font("Times New Roman", 12);
                g.DrawString(allColors[i].ToString(), f, sb, x, y);

                // 釋放該塗刷
                sb.Dispose();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //DrawColorMap
            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            g.Clear(Color.White);
            Brush b;
            int i;
            int N = rgb_array.Length / 3;
            int hh = 9;
            int border = 20;

            for (i = 0; i < N; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, rgb_array[i, 0], rgb_array[i, 1], rgb_array[i, 2]));
                //rgb_array
                //g.FillRectangle(b, w / 10, i * hh + h/10, w / 10 * 8, hh);
                g.FillRectangle(b, border, i * hh + border, w - border * 2, hh);
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //DrawColorMap
            int W = 600;
            int H = 700;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);

            g.Clear(Color.White);
            Brush b;
            int i;
            int N = rgb_array2.Length / 3;
            int hh = 50;
            int border = 40;

            string str = "R   G   B   Y";

            i = 0;
            g.DrawString(str, new Font("標楷體", 18), new SolidBrush(Color.Blue), new PointF(border + 160, i * hh + border - 30));

            for (i = 0; i < N; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, rgb_array2[i, 0], rgb_array2[i, 1], rgb_array2[i, 2]));
                g.FillRectangle(b, border, i * hh + border, W / 4, hh);

                RGB pp = new RGB((byte)rgb_array2[i, 0], (byte)rgb_array2[i, 1], (byte)rgb_array2[i, 2]);
                YUV yyy = new YUV();
                yyy = RGBToYUV(pp);

                str = rgb_array2[i, 0].ToString("D3") + " " + rgb_array2[i, 1].ToString("D3") + " " + rgb_array2[i, 2].ToString("D3") + " " + ((int)yyy.Y).ToString("D3");
                g.DrawString(str, new Font("標楷體", 18), new SolidBrush(Color.Blue), new PointF(border + 150, i * hh + border));

                byte rrr = (byte)rgb_array2[i, 0];
                byte ggg = (byte)rgb_array2[i, 1];
                byte bbb = (byte)rgb_array2[i, 2];

                int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                b = new SolidBrush(zz);
                g.FillRectangle(b, border + 350, i * hh + border, W / 4, hh);
            }
            pictureBox1.Image = bitmap1;


        }

        private void button3_Click(object sender, EventArgs e)
        {
            g.Clear(Color.White);

            //Draw System Color
            //// List the system colors.
            int y = 10;

            // Enumerate the SystemColors class's static Color properties.
            Type type = typeof(SystemColors);
            foreach (PropertyInfo field_info in type.GetProperties())
            {
                DrawColorSample(g, ref y,
                    (Color)field_info.GetValue(null, null),
                    field_info.Name);
            }

            richTextBox1.Text += "共有 " + type.GetProperties().Length.ToString() + " 種顏色\n";

        }

        // Display a color sample.
        private void DrawColorSample(Graphics gr, ref int y, Color clr, string clr_name)
        {
            using (SolidBrush br = new SolidBrush(clr))
            {
                gr.FillRectangle(br, 10, y, 90, 10);
            }
            gr.DrawRectangle(Pens.Black, 10, y, 90, 10);
            gr.DrawString(clr_name, this.Font, Brushes.Black, 110, y);
            y += 20;
        }

        private void button4_Click(object sender, EventArgs e)
        {

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

        private void button10_Click(object sender, EventArgs e)
        {
            //顏色名稱1
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;

            Bitmap bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            int i;
            int j;
            int w = 120;
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
            SolidBrush sb = new SolidBrush(c);
            g.FillRectangle(sb, w * i, h * j, w - 1, h - 1);

            //sb = new SolidBrush(Color.Black);
            sb = new SolidBrush(Color.FromArgb(255 - c.R, 255 - c.G, 255 - c.B));

            f = new Font("標楷體", 12);
            g.DrawString(c.Name, f, sb, new PointF(w * i, h * j + h / 3));
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //顏色名稱2
            int i = 0;
            int j = 0;
            int w = 100;
            int h = 35;

            int width = w * 7;
            int height = h * 20;

            pictureBox1.Size = new Size(width, height);
            //pictureBox1.Location = new Point(0, 0);

            Bitmap bitmap1 = new Bitmap(width, height);

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

        private void button12_Click(object sender, EventArgs e)
        {
            //顏色名稱3
            int i = 0;
            //int j = 0;
            int w = 100;
            int h = 35;

            int width = w * 7;
            int height = h * 20;

            pictureBox1.Size = new Size(width, height);
            //pictureBox1.Location = new Point(0, 0);

            Bitmap bitmap1 = new Bitmap(width, height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            int len;
            len = Colors.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int x_st = 0;
            int y_st = 0;
            for (i = 0; i < len; i++)
            {
                SolidBrush sb = new SolidBrush(Colors[i % len]);
                g.FillRectangle(sb, x_st + w * (i / 20), y_st + h * (i % 20), w, h);
                richTextBox1.Text += Colors[i % len].Name + "\n";

                Font f = new Font("標楷體", 12);
                sb = new SolidBrush(Color.FromArgb(255 - Colors[i % len].R, 255 - Colors[i % len].G, 255 - Colors[i % len].B));
                g.DrawString(Colors[i % len].Name.ToString(), f, sb, new PointF(x_st + w * (i / 20), y_st + h * (i % 20) + 12));

            }
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

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }


    }
}

