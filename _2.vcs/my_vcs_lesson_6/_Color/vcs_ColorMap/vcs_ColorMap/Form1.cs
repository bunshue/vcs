using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;    //for PropertyInfo
using System.Runtime.InteropServices;   //for dll

namespace vcs_ColorMap
{
    public partial class Form1 : Form
    {
        Graphics g;
        Graphics g2;
        Pen p;

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

        public static RGB YUVToRGB(YUV yuv)
        {
            double r = yuv.Y + 1.4075 * (yuv.V - 128);
            double g = yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128));
            double b = yuv.Y + 1.7790 * (yuv.U - 128);
            if (r > 255)
                r = 255;
            if (g > 255)
                g = 255;
            if (b > 255)
                b = 255;
            if (r < 0)
                r = 0;
            if (g < 0)
                g = 0;
            if (b < 0)
                b = 0;

            return new RGB((byte)r, (byte)g, (byte)b);
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();


            //設定 comboBox1
            comboBox1.DrawItem += new DrawItemEventHandler(comboBox1_DrawItem);

            /*
            列舉系統的所有Color並以ComboBox顯示
            首先利用Reflection的方式取得系統中的所有Color，將利Color的名子加到cmbColor中。
            接著在cmbColor中自行繪制顯示的內容，在這邊需要將cmbColor中的屬性'DrawMode'設為'OwnerDrawFixed'，並新的DrawItem事件
            */

            //用Reflection的方式取得系統中的所有Color，將利Color的名子加到comboBox中。
            Type type = typeof(Color);
            PropertyInfo[] propInfo = type.GetProperties(BindingFlags.Static | BindingFlags.Public);
            var names = from color in propInfo
                        where color.Name != "Transparent"
                        select color.Name;
            comboBox1.Items.Clear();
            foreach (var item in names)
            {
                comboBox1.Items.Add(item);
            }
            comboBox1.SelectedIndex = 0;
            richTextBox1.Text += "共有 " + comboBox1.Items.Count.ToString() + " 種顏色\n";
        }

        private void comboBox1_DrawItem(object sender, DrawItemEventArgs e)
        {
            Graphics g = e.Graphics;
            Rectangle rect = e.Bounds;
            if (e.Index >= 0)
            {
                string colorName = ((ComboBox)sender).Items[e.Index].ToString();
                Font font = new Font("Arial", 9, FontStyle.Regular);
                Color color = Color.FromName(colorName);
                Brush brush = new SolidBrush(color);
                g.FillRectangle(brush, rect.X + 5, rect.Y, 50, rect.Height);
                g.DrawString(colorName, font, Brushes.Black, rect.X + 15, rect.Top);
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 80;
            dx = 140;
            dy = 70;

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

            y_st = 10;
            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(1400, 900);

            richTextBox1.Size = new Size(200, 900);
            richTextBox1.Location = new Point(x_st + dx * 8 + 580, y_st + dy * 0);
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

        private Color[] AllColors1 = new Color[]
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

        private void button0_Click(object sender, EventArgs e)
        {
            //顏色名稱0
            //生成Color類所有static預定義成員的顏色表
            richTextBox1.Text += "生成Color類所有static預定義成員的顏色表\n";
            //生成Color類所有static預定義成員的顏色表


            //生成Color類所有static預定義成員的顏色表

            const long CELLS_PER_LINE = 10;

            const float MARGIN = 12;
            const float CELL_WIDTH = 160;
            const float CELL_HEIGHT = 64;
            const float COLOR_LEFT_MARGIN = 8;
            const float COLOR_TOP_MARGIN = 8;
            const float COLOR_CELL_WIDTH = 48;
            const float COLOR_CELL_HEIGHT = 32;
            const float TEXT_TOP_MARGIN = COLOR_TOP_MARGIN + COLOR_CELL_HEIGHT + 2;

            List<Color> vColors = new List<Color>();
            Type t = typeof(Color);
            PropertyInfo[] vProps = t.GetProperties();
            foreach (PropertyInfo propInfo in vProps)
            {
                if (MemberTypes.Property == propInfo.MemberType && typeof(Color) == propInfo.PropertyType)
                {
                    Color tmpColor = (Color)propInfo.GetValue(null, null);
                    vColors.Add(tmpColor);
                }
            }

            Bitmap bitmap1 = new Bitmap((int)(CELLS_PER_LINE * CELL_WIDTH + MARGIN * 2), (int)((vColors.Count / CELLS_PER_LINE + 1) * CELL_HEIGHT + MARGIN * 2));
            using (Graphics grp = Graphics.FromImage(bitmap1))
            {
                grp.Clear(Color.Black);

                for (int i = 0; i < vColors.Count; i++)
                {
                    float nLeftBase = MARGIN + i % CELLS_PER_LINE * CELL_WIDTH;
                    float nTopBase = MARGIN + i / CELLS_PER_LINE * CELL_HEIGHT;

                    grp.DrawRectangle(new Pen(Color.White), nLeftBase, nTopBase, CELL_WIDTH, CELL_HEIGHT);

                    grp.FillRectangle(new SolidBrush(vColors[i]), nLeftBase + COLOR_LEFT_MARGIN, nTopBase + COLOR_TOP_MARGIN, COLOR_CELL_WIDTH, COLOR_CELL_HEIGHT);

                    grp.DrawString(vColors[i].Name, new Font("宋體", 9, FontStyle.Regular), new SolidBrush(Color.White), nLeftBase + COLOR_LEFT_MARGIN, nTopBase + TEXT_TOP_MARGIN);
                }
            }

            pictureBox1.Image = bitmap1;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //bitmap1.Save("AllColor.bmp");
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

        private void button1_Click(object sender, EventArgs e)
        {
            //顏色名稱1
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            int i = 0;
            int w = 130;
            int h = 60;
            int len = AllColors1.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            for (i = 0; i < len; i++)
            {
                Color c = AllColors1[i];
                drawBox(i % 10, i / 10, w, h, c);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //顏色名稱2
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            int i = 0;
            int w = 130;
            int h = 60;
            int len = AllColors1.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            int x_st = 0;
            int y_st = 0;
            for (i = 0; i < len; i++)
            {
                SolidBrush sb = new SolidBrush(AllColors1[i % len]);
                g.FillRectangle(sb, x_st + w * (i % 10), y_st + h * (i / 10), w, h);
                richTextBox1.Text += AllColors1[i % len].Name + "\n";

                Font f = new Font("標楷體", 12);
                sb = new SolidBrush(Color.FromArgb(255 - AllColors1[i % len].R, 255 - AllColors1[i % len].G, 255 - AllColors1[i % len].B));
                g.DrawString(AllColors1[i % len].Name.ToString(), f, sb, new PointF(x_st + w * (i % 10), y_st + h * (i / 10) + 12));
            }
            pictureBox1.Image = bitmap1;
        }

        string[,] AllColors3 = new string[,]
        {
            {"黑Black","0,0,0"},
            {"暗灰Dimgray","64,64,64"},
            {"灰色Gray","128,128,128"},
            {"暗灰Dark Gray","169,169,169"},
            {"銀色Silver","192,192,192"},
            {"淺灰色Light Gray","211,211,211"},
            {"庚斯博羅灰Gainsboro","220,220,220"},
            {"白色White","255,255,255"},
            {"紅色Red","255,0,0"},
            {"腥紅色Scarlet","255, 36, 0"},
            {"朱紅色Vermilion","255, 77, 0"},
            {"陽橙Sun Orange","255, 115, 0"},
            {"橙色Orange","255, 165, 0"},
            {"琥珀色Amber","255, 191, 0"},
            {"金色Gold","255, 215, 0"},
            {"黃色Yellow","255, 255, 0"},
            {"檸檬綠Lime","204, 255, 0"},
            {"蘋果綠Apple Green","140, 230, 0"},
            {"黃綠色Bright Green","102, 255, 0"},
            {"綠色green","0, 255, 0"},
            {"青色cyan","0, 255, 255"},
            {"深天藍Deep Sky Blue","0, 191, 255"},
            {"蔚藍色azure","0, 127, 255"},
            {"極濃海藍Ultramarine","0, 51, 255"},
            {"藍色blue","0, 0, 255"},
            {"木槿紫Mauve","102, 64, 255"},
            {"紫丁香色Lilac","179, 153, 255"},
            {"紫(紫羅蘭)Violet","139, 0, 255"},
            {"錦葵紫 Mallow","217, 77, 255"},
            {"優品紫紅Opera Mauve","230, 128, 255"},
            {"紫色 Purple","128, 0, 128"},
            {"粉紅Pink","255, 192,203"},
            {"玫瑰褐Rosy Brown","18,143,143"},
            {"亮珊瑚色Light Coral","240,128,128"},
            {"印度紅 Indian Red","205,92,92"},
            {"暖粉紅Hot Pink","255, 155,180"},
            {"淺玫瑰紅Rose Pink","255, 102,204"},
            {"妃紅","237,87,54"},
            {"品紅?pinkish red","240,0,86"},
            {"洋紅Megenta","255, 0, 255"},
            {"玫瑰紅Rose Red","255, 13,16"},
            {"櫻桃Cerise","222,49,99"},
            {"紅寶石色Ruby","204,0,128"},
            {"胭脂紅Carmine","230,0,92"},
            {"緋紅Crimson","220,20,60"},
            {"褐色Brown","165,42,42"},
            {"磚紅色Fire Brick","178, 34, 34"},
            {"樞機紅Cardinal Red","153,0,54"},
            {"勃艮第酒紅Burgundy","71,0,36"},
            {"暗紅Dark Red","139,0,0"},
            {"米色Beige","245,245,210"},
            {"小麥色Wheat","245,222,179"},
            {"薑黃","255,199,115"},
            {"蜜橙Honey Orange","255, 179,102"},
            {"杏黃Apricot","230,153,102"},
            {"橘黃","255,137,54"},
            {"珊瑚紅 Coral","255, 127,80"},
            {"熱帶橙Tropical Orange","255, 128,51"},
            {"蕃茄紅 Tomato","255, 99, 71"},
            {"柿子橙Persimmon","255, 77, 64"},
            {"巧克力色Chocolate","210,105,30"},
            {"古銅色Bronze","184,115,51"},
            {"駝色Camel","161,107,71"},
            {"卡其色Khaki","153,107,31"},
            {"橄欖色Olive","128, 128, 0"},
            {"椰褐Coconut Brown","71,31,0"},
            {"鵝黃?light yellow","255,241,67"},
            {"鴨黃","250,255,114"},
            {"香檳黃Champagne Yellow","255,255,153"},
            {"櫻草色primrose yellow","234,255,86"},
            {"芥末黃Mustard","204, 204, 77"},
            {"亮檸檬綠Light Lime","204, 255, 0"},
            {"黃綠 Yellow Green","154, 205, 50"},
            {"嫩綠pomona green verdancy","189,221,34"},
            {"草綠 Grass Green","153, 230, 77"},
            {"碧綠(寶綠) Emerald","80,200,120"},
            {"碧綠azure green","42,221,156"},
            {"檸檬綠Lime Green","50, 205, 50"},
            {"孔雀石綠Malachite","34,195,46"},
            {"薄荷綠Mint","22,152,43"},
            {"春綠色Spring Green","0, 255, 128"},
            {"孔雀綠Peacock Green","0,161,92"},
            {"暗綠Dark Green","0,100,1"},
            {"水色Aqua","175, 223, 228"},
            {"淺藍色baby blue","137,207,240"},
            {"藍綠色Aquamarin","127, 255, 212"},
            {"水藍 Aqua Blue","102, 255, 230"},
            {"土耳其藍Turquoise Blue","51, 230, 204"},
            {"綠松色Turquoise","48, 213, 200"},
            {"鴨綠色Teal","0, 128, 128"},
            {"水","100, 149, 237"},
            {"矢車菊藍Cornflower Blue","100, 149, 237"},
            {"蔚藍Cerulean blue","42, 82, 190"},
            {"水手藍Marine Blue","0, 71,125"},
            {"普魯士藍Prussian blue","0, 49, 83"},
            {"粉末藍Powder Blue","0, 51, 153"},
            {"藍寶石色Sapphire","8, 37, 103"},
            {"午夜藍Midnight Blue","25, 25, 112"},
            {"藏青(海軍藍)Navy","0,0,128"},
            {"淡紫丁香色Pail Lilac","230, 207, 230"},
            {"鐵線蓮紫 Clematis","204, 163, 204"},
            {"亮紫Light Violet","238, 130, 238"},
            {"淡紫丁香色Pail Lilac","230, 207, 230"},
            {"紫水晶色Amethyst","102, 51, 204"},
            {"暗蘭紫 Dark Orchid","153, 50, 204"},
            {"暗紫 Dark Violet","148, 0, 211"},
            {"三色堇紫 Pansy","116, 0, 161"},
            {"靛色Indigo","75,0,128"},
            {"金色","234,205,118"},
            {"假金","168,138,77"},
            {"烏金","167,142,68"},
            {"赤金","242,190,69"},
            {"銀白","233,231,239"},
            {"銀色","211,212,213"},
            {"假銀","150,149,148"},
            {"老銀","186,202,198"},
            {"銅綠","84,150,136"},
            {"不銹鋼","128,128,128"},
            {"不銹鋼","169,169,169"},
            {"深牛皮紙","199,126,123"},
            {"淺牛皮紙","226,203,173"},
            {"亞洲人膚色","219,161,118"},
            {"非洲人膚色","182,147,118"},
            {"藍天","104,165,218"},
            {"藍天偏暖","116,132,193"},
            {"藍天偏冷","98,176,227"},
        };

        private void button3_Click(object sender, EventArgs e)
        {
            //顏色名稱3
            //AllColors3
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //顏色名稱4
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            // 將 KnownColor 列舉的內容項目複雜到 allColors 陣列
            Array colorsArray = Enum.GetValues(typeof(KnownColor));
            KnownColor[] AllColors4 = new KnownColor[colorsArray.Length];
            Array.Copy(colorsArray, AllColors4, colorsArray.Length);

            int i = 0;
            int w = 130;
            int h = 50;
            int len = AllColors4.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            int x_st = 0;
            int y_st = 0;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + Color.FromName(AllColors4[i].ToString()) + "\n";
                Color clr = Color.FromName(AllColors4[i].ToString());//取出顏色
                SolidBrush sb = new SolidBrush(clr);
                g.FillRectangle(sb, x_st + w * (i % 10), y_st + h * (i / 10), w, h);

                Font f = new Font("標楷體", 12);
                Color clr2 = Color.FromArgb(255 - clr.R, 255 - clr.G, 255 - clr.B);
                sb = new SolidBrush(clr2);
                g.DrawString(clr.Name.ToString(), f, sb, new PointF(x_st + w * (i % 10), y_st + h * (i / 10) + 12));
                sb.Dispose();// 釋放該塗刷
            }
            pictureBox1.Image = bitmap1;
        }

        int[,] AllColors5 = new int[64, 3]
        {
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

        private void button5_Click(object sender, EventArgs e)
        {
            //顏色名稱5
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            Brush b;
            int i;
            int hh = 9;
            int border = 20;

            int len = AllColors5.GetUpperBound(0) + 1;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            for (i = 0; i < len; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, AllColors5[i, 0], AllColors5[i, 1], AllColors5[i, 2]));
                //g.FillRectangle(b, w / 10, i * hh + h/10, w / 10 * 8, hh);
                g.FillRectangle(b, border, i * hh + border, width - border * 2, hh);
            }
            pictureBox1.Image = bitmap1;
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

        string[,] AllColors6 = new string[,]
        {
            {"LightPink,淺粉紅", "FFB6C1", "255,182,193"},
            {"Pink,粉紅", "FFC0CB", "255,192,203"},
            {"Crimson,深紅(猩紅)", "DC143C", "220,20,60"},
            {"LavenderBlush,淡紫紅", "FFF0F5", "255,240,245"},
            {"PaleVioletRed,弱紫羅蘭紅", "DB7093", "219,112,147"},
            {"HotPink,熱情的粉紅", "FF69B4", "255,105,180"},
            {"DeepPink,深粉紅", "FF1493", "255,20,147"},
            {"MediumVioletRed,中紫羅蘭紅", "C71585", "199,21,133"},
            {"Orchid,暗紫色(蘭花紫)", "DA70D6", "218,112,214"},
            {"Thistle,薊色", "D8BFD8", "216,191,216"},
            {"Plum,洋李色(李子紫)", "DDA0DD", "221,160,221"},
            {"Violet,紫羅蘭", "EE82EE", "238,130,238"},
            {"Magenta,洋紅(玫瑰紅)", "FF00FF", "255,0,255"},
            {"Fuchsia,紫紅(燈籠海棠)", "FF00FF", "255,0,255"},
            {"DarkMagenta,深洋紅", "8B008B", "139,0,139"},
            {"Purple,紫色", "800080", "128,0,128"},
            {"MediumOrchid,中蘭花紫", "BA55D3", "186,85,211"},
            {"DarkViolet,暗紫羅蘭", "9400D3", "148,0,211"},
            {"DarkOrchid,暗蘭花紫", "9932CC", "153,50,204"},
            {"Indigo,靛青/紫蘭色", "4B0082", "75,0,130"},
            {"BlueViolet,藍紫羅蘭", "8A2BE2", "138,43,226"},
            {"MediumPurple,中紫色", "9370DB", "147,112,219"},
            {"MediumSlateBlue,中暗藍色(中板巖藍)", "7B68EE", "123,104,238"},
            {"SlateBlue,石藍色(板巖藍)", "6A5ACD", "106,90,205"},
            {"DarkSlateBlue,暗灰藍色(暗板巖藍)", "483D8B", "72,61,139"},
            {"Lavender,淡紫色(熏衣草淡紫)", "E6E6FA", "230,230,250"},
            {"GhostWhite,幽靈白", "F8F8FF", "248,248,255"},
            {"Blue,純藍", "0000FF", "0,0,255"},
            {"MediumBlue,中藍色", "0000CD", "0,0,205"},
            {"MidnightBlue,午夜藍", "191970", "25,25,112"},
            {"DarkBlue,暗藍色", "00008B", "0,0,139"},
            {"Navy,海軍藍", "000080", "0,0,128"},
            {"RoyalBlue,皇家藍/寶藍", "4169E1", "65,105,225"},
            {"CornflowerBlue,矢車菊藍", "6495ED", "100,149,237"},
            {"LightSteelBlue,亮鋼藍", "B0C4DE", "176,196,222"},
            {"LightSlateGray,亮藍灰(亮石板灰)", "778899", "119,136,153"},
            {"SlateGray,灰石色(石板灰)", "708090", "112,128,144"},
            {"DodgerBlue,閃蘭色(道奇藍)", "1E90FF", "30,144,255"},
            {"AliceBlue,愛麗絲藍", "F0F8FF", "240,248,255"},
            {"SteelBlue,鋼藍/鐵青", "4682B4", "70,130,180"},
            {"LightSkyBlue,亮天藍色", "87CEFA", "135,206,250"},
            {"SkyBlue,天藍色", "87CEEB", "135,206,235"},
            {"DeepSkyBlue,深天藍", "00BFFF", "0,191,255"},
            {"LightBlue,亮藍", "ADD8E6", "173,216,230"},
            {"PowderBlue,粉藍色(火藥青)", "B0E0E6", "176,224,230"},
            {"CadetBlue,軍蘭色(軍服藍)", "5F9EA0", "95,158,160"},
            {"Azure,蔚藍色", "F0FFFF", "240,255,255"},
            {"LightCyan,淡青色", "E0FFFF", "224,255,255"},
            {"PaleTurquoise,弱綠寶石", "AFEEEE", "175,238,238"},
            {"Cyan,青色", "00FFFF", "0,255,255"},
            {"Aqua,淺綠色(水色)", "00FFFF", "0,255,255"},
            {"DarkTurquoise,暗綠寶石", "00CED1", "0,206,209"},
            {"DarkSlateGray,暗瓦灰色(暗石板灰)", "2F4F4F", "47,79,79"},
            {"DarkCyan,暗青色", "008B8B", "0,139,139"},
            {"Teal,水鴨色", "008080", "0,128,128"},
            {"MediumTurquoise,中綠寶石", "48D1CC", "72,209,204"},
            {"LightSeaGreen,淺海洋綠", "20B2AA", "32,178,170"},
            {"Turquoise,綠寶石", "40E0D0", "64,224,208"},
            {"Aquamarine,寶石碧綠", "7FFFD4", "127,255,212"},
            {"MediumAquamarine,中寶石碧綠", "66CDAA", "102,205,170"},
            {"MediumSpringGreen,中春綠色", "00FA9A", "0,250,154"},
            {"MintCream,薄荷奶油", "F5FFFA", "245,255,250"},
            {"SpringGreen,春綠色", "00FF7F", "0,255,127"},
            {"MediumSeaGreen,中海洋綠", "3CB371", "60,179,113"},
            {"SeaGreen,海洋綠", "2E8B57", "46,139,87"},
            {"Honeydew,蜜色(蜜瓜色)", "F0FFF0", "240,255,240"},
            {"LightGreen,淡綠色", "90EE90", "144,238,144"},
            {"PaleGreen,弱綠色", "98FB98", "152,251,152"},
            {"DarkSeaGreen,暗海洋綠", "8FBC8F", "143,188,143"},
            {"LimeGreen,閃光深綠", "32CD32", "50,205,50"},
            {"Lime,閃光綠", "00FF00", "0,255,0"},
            {"ForestGreen,森林綠", "228B22", "34,139,34"},
            {"Green,純綠", "008000", "0,128,0"},
            {"DarkGreen,暗綠色", "006400", "0,100,0"},
            {"Chartreuse,黃綠色(查特酒綠)", "7FFF00", "127,255,0"},
            {"LawnGreen,草綠色(草坪綠_", "7CFC00", "124,252,0"},
            {"GreenYellow,綠黃色", "ADFF2F", "173,255,47"},
            {"DarkOliveGreen,暗橄欖綠", "556B2F", "85,107,47"},
            {"YellowGreen,黃綠色", "9ACD32", "154,205,50"},
            {"OliveDrab,橄欖褐色", "6B8E23", "107,142,35"},
            {"Beige,米色/灰棕色", "F5F5DC", "245,245,220"},
            {"LightGoldenrodYellow,亮菊黃", "FAFAD2", "250,250,210"},
            {"Ivory,象牙色", "FFFFF0", "255,255,240"},
            {"LightYellow,淺黃色", "FFFFE0", "255,255,224"},
            {"Yellow,純黃", "FFFF00", "255,255,0"},
            {"Olive,橄欖", "808000", "128,128,0"},
            {"DarkKhaki,暗黃褐色(深卡嘰布)", "BDB76B", "189,183,107"},
            {"LemonChiffon,檸檬綢", "FFFACD", "255,250,205"},
            {"PaleGoldenrod,灰菊黃(蒼麒麟色)", "EEE8AA", "238,232,170"},
            {"Khaki,黃褐色(卡嘰布)", "F0E68C", "240,230,140"},
            {"Gold,金色", "FFD700", "255,215,0"},
            {"Cornsilk,玉米絲色", "FFF8DC", "255,248,220"},
            {"Goldenrod,金菊黃", "DAA520", "218,165,32"},
            {"DarkGoldenrod,暗金菊黃", "B8860B", "184,134,11"},
            {"FloralWhite,花的白色", "FFFAF0", "255,250,240"},
            {"OldLace,老花色(舊蕾絲)", "FDF5E6", "253,245,230"},
            {"Wheat,淺黃色(小麥色)", "F5DEB3", "245,222,179"},
            {"Moccasin,鹿皮色(鹿皮靴)", "FFE4B5", "255,228,181"},
            {"Orange,橙色", "FFA500", "255,165,0"},
            {"PapayaWhip,番木色(番木瓜)", "FFEFD5", "255,239,213"},
            {"BlanchedAlmond,白杏色", "FFEBCD", "255,235,205"},
            {"NavajoWhite,納瓦白(土著白)", "FFDEAD", "255,222,173"},
            {"AntiqueWhite,古董白", "FAEBD7", "250,235,215"},
            {"Tan,茶色", "D2B48C", "210,180,140"},
            {"BurlyWood,硬木色", "DEB887", "222,184,135"},
            {"Bisque,陶坯黃", "FFE4C4", "255,228,196"},
            {"DarkOrange,深橙色", "FF8C00", "255,140,0"},
            {"Linen,亞麻布", "FAF0E6", "250,240,230"},
            {"Peru,秘魯色", "CD853F", "205,133,63"},
            {"PeachPuff,桃肉色", "FFDAB9", "255,218,185"},
            {"SandyBrown,沙棕色", "F4A460", "244,164,96"},
            {"Chocolate,巧克力色", "D2691E", "210,105,30"},
            {"SaddleBrown,重褐色(馬鞍棕色)", "8B4513", "139,69,19"},
            {"Seashell,海貝殼", "FFF5EE", "255,245,238"},
            {"Sienna,黃土赭色", "A0522D", "160,82,45"},
            {"LightSalmon,淺鮭魚肉色", "FFA07A", "255,160,122"},
            {"Coral,珊瑚", "FF7F50", "255,127,80"},
            {"OrangeRed,橙紅色", "FF4500", "255,69,0"},
            {"DarkSalmon,深鮮肉/鮭魚色", "E9967A", "233,150,122"},
            {"Tomato,番茄紅", "FF6347", "255,99,71"},
            {"MistyRose,淺玫瑰色(薄霧玫瑰)", "FFE4E1", "255,228,225"},
            {"Salmon,鮮肉/鮭魚色", "FA8072", "250,128,114"},
            {"Snow,雪白色", "FFFAFA", "255,250,250"},
            {"LightCoral,淡珊瑚色", "F08080", "240,128,128"},
            {"RosyBrown,玫瑰棕色", "BC8F8F", "188,143,143"},
            {"IndianRed,印度紅", "CD5C5C", "205,92,92"},
            {"Red,純紅", "FF0000", "255,0,0"},
            {"Brown,棕色", "A52A2A", "165,42,42"},
            {"FireBrick,火磚色(耐火磚)", "B22222", "178,34,34"},
            {"DarkRed,深紅色", "8B0000", "139,0,0"},
            {"Maroon,栗色", "800000", "128,0,0"},
            {"White,純白", "FFFFFF", "255,255,255"},
            {"WhiteSmoke,白煙", "F5F5F5", "245,245,245"},
            {"Gainsboro,淡灰色(庚斯博羅灰)", "DCDCDC", "220,220,220"},
            {"LightGrey,淺灰色", "D3D3D3", "211,211,211"},
            {"Silver,銀灰色", "C0C0C0", "192,192,192"},
            {"DarkGray,深灰色", "A9A9A9", "169,169,169"},
            {"Gray,灰色", "808080", "128,128,128"},
            {"DimGray,暗淡的灰色", "696969", "105,105,105"},
            {"Black,純黑", "000000", "0,0,0"},
        };

        private void button6_Click(object sender, EventArgs e)
        {
            //顏色名稱6
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            int i = 0;
            int w = 130;
            int h = 60;
            int len = AllColors6.GetUpperBound(0) + 1;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            int x_st = 0;
            int y_st = 0;
            for (i = 0; i < len/10; i++)
            {
                string color_name = AllColors6[i, 0];
                string color_hex = AllColors6[i, 1];
                string color_rgb = AllColors6[i, 2];

                richTextBox1.Text += color_name + "\t" + color_hex + "\t" + color_rgb + "\n";
                //split

                /*
                SolidBrush sb = new SolidBrush(AllColors1[i % len]);
                g.FillRectangle(sb, x_st + w * (i % 10), y_st + h * (i / 10), w, h);
                richTextBox1.Text += AllColors1[i % len].Name + "\n";

                Font f = new Font("標楷體", 12);
                sb = new SolidBrush(Color.FromArgb(255 - AllColors1[i % len].R, 255 - AllColors1[i % len].G, 255 - AllColors1[i % len].B));
                g.DrawString(AllColors1[i % len].Name.ToString(), f, sb, new PointF(x_st + w * (i % 10), y_st + h * (i / 10) + 12));
                */
            }
            pictureBox1.Image = bitmap1;
        }

        string[,] AllColors7 = new string[,]
        {
            {"三色堇紫","#7400a1"},
            {"中岩藍","#7b68ee"},
            {"中春綠色","#00fa9a"},
            {"中海綠","#3cb371"},
            {"中碧藍色","#66cdaa"},
            {"中紫紅","#9370db"},
            {"中綠松石色","#48d1cc"},
            {"中藍","#0000cd"},
            {"中蘭紫","#ba55d3"},
            {"中青紫紅","#c71585"},
            {"亞麻色","#faf0e6"},
            {"亮卡其色","#f0e68c"},
            {"亮天藍","#87cefa"},
            {"亮岩灰","#778899"},
            {"亮檸檬绿／檸檬绿色","#ccff00"},
            {"亮海綠","#20b2aa"},
            {"亮灰色","#d3d3d3"},
            {"亮珊瑚色","#f08080"},
            {"亮粉紅","#ffb6c1"},
            {"亮紫","#ee82ee"},
            {"亮綠","#90ee90"},
            {"亮藍","#add8e6"},
            {"亮金菊黃","#fafad2"},
            {"亮鋼藍","#b0c4de"},
            {"亮青／淺藍／淺藍色","#e0ffff"},
            {"亮鮭紅","#ffa07a"},
            {"亮黃","#ffffe0"},
            {"優品紫紅","#e680ff"},
            {"勃艮第酒紅","#470024"},
            {"午夜藍","#003366"},
            {"午夜藍","#191970"},
            {"卡其色","#996b1f"},
            {"印度紅","#cd5c5c"},
            {"古董白","#faebd7"},
            {"古銅色","#b87333"},
            {"含羞草黃","#e6d933"},
            {"咖啡色","#4d3900"},
            {"品紅","#f400a1"},
            {"品藍／皇室藍","#4169e1"},
            {"國際奇連藍","#002fa7"},
            {"天藍","#87ceeb"},
            {"天青石藍","#0d33ff"},
            {"奶油色","#fffdd0"},
            {"嫩綠","#99ff4d"},
            {"嬰兒粉藍","#b0e0e6"},
            {"孔雀石綠","#22c32e"},
            {"孔雀綠","#00a15c"},
            {"孔雀藍","#00808c"},
            {"小麥色","#f5deb3"},
            {"尖晶石紅","#ff73b3"},
            {"山茶紅","#e63995"},
            {"岩灰","#708090"},
            {"岩藍","#6a5acd"},
            {"巧克力色","#d2691e"},
            {"常春藤綠","#36bf36"},
            {"幽靈白","#f8f8ff"},
            {"庚斯博羅灰","#dcdcdc"},
            {"愛麗絲藍","#f0f8ff"},
            {"日曬色","#d2b48c"},
            {"明綠／黃綠色","#66ff00"},
            {"昏灰","#696969"},
            {"春綠／春綠色","#00ff80"},
            {"普鲁士藍","#003153"},
            {"暖粉紅","#ff69b4"},
            {"暗卡其色","#bdb76b"},
            {"暗嬰兒粉藍／粉末藍","#003399"},
            {"暗岩灰","#2f4f4f"},
            {"暗岩藍","#483d8b"},
            {"暗橄欖綠","#556b2f"},
            {"暗橙","#ff8c00"},
            {"暗洋紅","#8b008b"},
            {"暗海綠","#8fbc8f"},
            {"暗灰","#a9a9a9"},
            {"暗灰色","#404040"},
            {"暗礦藍","#24367d"},
            {"暗紅","#8b0000"},
            {"暗紫","#9400d3"},
            {"暗綠","#006400"},
            {"暗綠松石色","#00ced1"},
            {"暗藍","#00008b"},
            {"暗蘭紫","#9932cc"},
            {"暗金菊色","#b8860b"},
            {"暗青","#008b8b"},
            {"暗鮭紅","#e9967a"},
            {"月黃","#ffff4d"},
            {"木槿紫","#6640ff"},
            {"朱紅／朱紅色","#ff4d00"},
            {"杏仁白","#ffebcd"},
            {"杏黃","#e69966"},
            {"查特酒綠","#7fff00"},
            {"柿子橙","#ff4d40"},
            {"栗色","#800000"},
            {"桃色","#ffe5b4"},
            {"梅紅色","#dda0dd"},
            {"森林綠","#228b22"},
            {"椰褐","#4d1f00"},
            {"極濃海藍","#0033ff"},
            {"樞機紅","#990036"},
            {"橄欖色","#808000"},
            {"橄欖軍服綠","#6b8e23"},
            {"橘色","#f28500"},
            {"橙紅","#ff4500"},
            {"橙色","#ffa500"},
            {"橙黃色","#ffcc00"},
            {"檸檬綠","#32cd32"},
            {"檸檬綢色","#fffacd"},
            {"櫻桃紅／櫻桃色","#de3163"},
            {"殼黃紅","#ffb3bf"},
            {"水手藍","#00477d"},
            {"水色","#afdfe4"},
            {"水藍","#66ffe6"},
            {"沙棕","#e6c3c3"},
            {"沙褐","#f4a460"},
            {"洋玫瑰紅","#ff0da6"},
            {"洋紅／洋紅色","#ff00ff"},
            {"海綠","#2e8b57"},
            {"海貝色","#fff5ee"},
            {"淡紫丁香色","#e6cfe6"},
            {"深天藍","#00bfff"},
            {"深粉紅","#ff1493"},
            {"淺灰紫紅","#8674a1"},
            {"淺玫瑰紅","#ff66cc"},
            {"淺珊瑚紅","#ff80bf"},
            {"淺珍珠紅","#ffb3e6"},
            {"淺粉紅","#ffd9e6"},
            {"淺鮭紅","#ff8099"},
            {"湛藍／蔚藍色","#007fff"},
            {"濃藍","#006374"},
            {"火鶴紅","#e68ab8"},
            {"灰丁寧藍／白牛仔布色","#5e86c1"},
            {"灰土色","#ccb38c"},
            {"灰紫紅","#db7093"},
            {"灰綠","#98fb98"},
            {"灰綠松石色","#afeeee"},
            {"灰色","#808080"},
            {"灰藍","#7ab8cc"},
            {"灰金菊色","#eee8aa"},
            {"烏賊墨色／深褐色","#704214"},
            {"熱帶橙","#ff8033"},
            {"燃橙／燃橙色","#cc5500"},
            {"玉米絲色","#fff8dc"},
            {"玫瑰紅","#ff007f"},
            {"玫瑰褐","#bc8f8f"},
            {"珊瑚紅","#ff7f50"},
            {"琥珀色","#ffbf00"},
            {"白煙色","#f5f5f5"},
            {"白色","#ffffff"},
            {"矢車菊藍","#6495ed"},
            {"硬木色","#deb887"},
            {"碧綠／寶石綠","#50c878"},
            {"碧藍色／藍綠色","#7fffd4"},
            {"礦紫","#b8a1cf"},
            {"礦藍","#004d99"},
            {"秘魯色","#cd853f"},
            {"米黃色／米色","#f5f5dc"},
            {"粉撲桃色","#ffdab9"},
            {"粉紅／粉紅色","#ffc0cb"},
            {"紅寶石色","#cc0080"},
            {"紅色","#ff0000"},
            {"紫丁香色","#b399ff"},
            {"紫水晶色","#6633cc"},
            {"紫羅蘭色","#8b00ff"},
            {"紫色","#800080"},
            {"紫藤色","#5c50e6"},
            {"綠松石綠","#4de680"},
            {"綠松石色／綠松色","#30d5c8"},
            {"綠松石藍","#33e6cc"},
            {"綠色","#008000"},
            {"綠黃","#adff2f"},
            {"緋紅","#dc143c"},
            {"纈草紫","#5000b8"},
            {"耐火磚紅","#b22222"},
            {"胭脂紅","#e6005c"},
            {"腥紅／猩紅色","#ff2400"},
            {"舊蕾絲色","#fdf5e6"},
            {"芥末黃","#cccc4d"},
            {"花卉白","#fffaf0"},
            {"苔蘚綠","#697723"},
            {"茉莉黃","#e6c35c"},
            {"茜紅／深茜紅","#e32636"},
            {"草坪綠","#7cfc00"},
            {"草綠","#99e64d"},
            {"萬壽菊黃","#ff9900"},
            {"葉綠","#73b839"},
            {"蒼色","#a6ffcc"},
            {"蔚藍／天青藍","#2a52be"},
            {"蕃木瓜色","#ffefd5"},
            {"蕃茄紅","#ff6347"},
            {"薄荷奶油色","#f5fffa"},
            {"薄荷綠","#16982b"},
            {"薊紫","#d8bfd8"},
            {"薩克斯藍","#4798b3"},
            {"薰衣草紫紅","#fff0f5"},
            {"薰衣草紫／薰衣草色","#e6e6fa"},
            {"藍寶石色／青玉色","#082567"},
            {"藍紫","#8a2be2"},
            {"藍色","#0000ff"},
            {"藏青／海軍藍／海軍藍","#000080"},
            {"蘋果綠","#8ce600"},
            {"蘭紫／蘭花色","#da70d6"},
            {"蜜橙","#ffb366"},
            {"蜜瓜綠","#f0fff0"},
            {"褐色","#a52a2a"},
            {"象牙色","#fffff0"},
            {"赭色","#cc7722"},
            {"赭黃","#a0522d"},
            {"軍服藍","#5f9ea0"},
            {"道奇藍","#1e90ff"},
            {"那瓦霍白","#ffdead"},
            {"金色","#ffd700"},
            {"金菊色","#daa520"},
            {"鈷綠","#66ff59"},
            {"鈷藍／鈷藍色","#0047ab"},
            {"鉻綠","#127436"},
            {"鉻黃","#e6b800"},
            {"銀色","#c0c0c0"},
            {"鋼青色","#4682b4"},
            {"錦葵紫","#d94dff"},
            {"鐵灰色","#625b57"},
            {"鐵線蓮紫","#cca3cc"},
            {"長春花色","#ccccff"},
            {"陳玫紅","#b85798"},
            {"陶坯黃","#ffe4c4"},
            {"陽橙","#ff7300"},
            {"雪色","#fffafa"},
            {"霧玫瑰色","#ffe4e1"},
            {"青瓷綠","#73e68c"},
            {"青色","#00ffff"},
            {"青藍","#0dbf8c"},
            {"靛色","#4b0080"},
            {"鞍褐","#8b4513"},
            {"韋奇伍德瓷藍","#5686bf"},
            {"香檳黃","#ffff99"},
            {"駝色","#a16b47"},
            {"鮭紅","#fa8072"},
            {"鮭肉色","#ff8c69"},
            {"鮮紅","#e60000"},
            {"鮮绿色／綠色","#00ff00"},
            {"鮮黃／黃色／黃色","#ffff00"},
            {"鳧綠／鴨綠色","#008080"},
            {"鹿皮鞋色","#ffe4b5"},
            {"黃綠","#9acd32"},
            {"黑色","#000000"},
            {"鼠尾草藍","#4d80e6"},
        };

        private void button7_Click(object sender, EventArgs e)
        {
            //顏色名稱7
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            int i;
            int ww = 130;
            int hh = 35;

            int len = AllColors7.GetUpperBound(0) + 1;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            for (i = 0; i < len; i++)
            {
                Brush b = new SolidBrush(System.Drawing.ColorTranslator.FromHtml(AllColors7[i, 1]));
                g.FillRectangle(b, (i % 10) * ww, (i / 10) * hh, ww, hh);
            }
            pictureBox1.Image = bitmap1;
        }

        int[,] AllColors8 = new int[12, 3] {
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

        //沒用到
        string[] AllColors8Name = new string[]
        {
            "black（黑）","white（白）","red（紅）","green（綠）",
            "blue（藍）","yellow（黃）","magenta（錳紫）","cyan（青藍）",
            "gray（灰）","dark red（暗紅）","copper（銅色）","aquamarine（碧綠）"
        };

        private void button8_Click(object sender, EventArgs e)
        {
            //顏色名稱8
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            g.Clear(Color.White);
            Brush b;
            int i;
            int N = AllColors8.Length / 3;
            int hh = 50;
            int border = 40;
            string str = "R   G   B   Y";

            int len = AllColors8.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            i = 0;
            g.DrawString(str, new Font("標楷體", 18), new SolidBrush(Color.Blue), new PointF(border + 160, i * hh + border - 30));

            for (i = 0; i < N; i++)
            {
                b = new SolidBrush(Color.FromArgb(255, AllColors8[i, 0], AllColors8[i, 1], AllColors8[i, 2]));
                g.FillRectangle(b, border, i * hh + border, width / 4, hh);

                RGB pp = new RGB((byte)AllColors8[i, 0], (byte)AllColors8[i, 1], (byte)AllColors8[i, 2]);
                YUV yyy = new YUV();
                yyy = RGBToYUV(pp);

                str = AllColors8[i, 0].ToString("D3") + " " + AllColors8[i, 1].ToString("D3") + " " + AllColors8[i, 2].ToString("D3") + " " + ((int)yyy.Y).ToString("D3");
                g.DrawString(str, new Font("標楷體", 18), new SolidBrush(Color.Blue), new PointF(border + 150, i * hh + border));

                byte rrr = (byte)AllColors8[i, 0];
                byte ggg = (byte)AllColors8[i, 1];
                byte bbb = (byte)AllColors8[i, 2];

                int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                b = new SolidBrush(zz);
                g.FillRectangle(b, border + 350, i * hh + border, width / 4, hh);
            }
            pictureBox1.Image = bitmap1;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //顏色名稱9
            //獲取系統預定義顏色
            //獲取系統預定義顏色
            Array colors = System.Enum.GetValues(typeof(KnownColor));
            foreach (object colorName in colors)
            {
                richTextBox1.Text += "get color : " + colorName.ToString() + "\n";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //顏色名稱10 System Color
            int width = pictureBox1.Size.Width;
            int height = pictureBox1.Size.Height;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            int y = 10;

            // Enumerate the SystemColors class's static Color properties.
            Type type = typeof(SystemColors);

            int len = type.GetProperties().Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 種顏色\n";

            foreach (PropertyInfo field_info in type.GetProperties())
            {
                DrawColorSample(g, ref y,
                    (Color)field_info.GetValue(null, null),
                    field_info.Name);
            }

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
            //建立調色盤
            MakeColorPalette(this, 10, 10);
        }

        // Make a color palette on the given parent.
        private void MakeColorPalette(Control parent, int x, int y)
        {
            Color[] colors = 
            {
                Color.White,
                Color.FromArgb(255, 255, 192, 192),
                Color.FromArgb(255, 255, 224, 192),
                Color.FromArgb(255, 255, 255, 192),
                Color.FromArgb(255, 192, 255, 192),
                Color.FromArgb(255, 192, 255, 255),
                Color.FromArgb(255, 192, 192, 255),
                Color.FromArgb(255, 255, 192, 255),
                Color.FromArgb(255, 224, 224, 224),
                Color.FromArgb(255, 255, 128, 128),
                Color.FromArgb(255, 255, 192, 128),
                Color.FromArgb(255, 255, 255, 128),
                Color.FromArgb(255, 128, 255, 128),
                Color.FromArgb(255, 128, 255, 255),
                Color.FromArgb(255, 128, 128, 255),
                Color.FromArgb(255, 255, 128, 255),
                Color.Silver,
                Color.Red,
                Color.FromArgb(255, 255, 128, 0),
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Fuchsia,
                Color.Gray,
                Color.FromArgb(255, 192, 0, 0),
                Color.FromArgb(255, 192, 64, 0),
                Color.FromArgb(255, 192, 192, 0),
                Color.FromArgb(255, 0, 192, 0),
                Color.FromArgb(255, 0, 192, 192),
                Color.FromArgb(255, 0, 0, 192),
                Color.FromArgb(255, 192, 0, 192),
                Color.FromArgb(255, 64, 64, 64),
                Color.Maroon,
                Color.FromArgb(255, 128, 64, 0),
                Color.Olive,
                Color.Green,
                Color.Teal,
                Color.Navy,
                Color.Purple,
                Color.Black,
                Color.FromArgb(255, 64, 0, 0),
                Color.FromArgb(255, 128, 64, 64),
                Color.FromArgb(255, 64, 64, 0),
                Color.FromArgb(255, 0, 64, 0),
                Color.FromArgb(255, 0, 64, 64),
                Color.FromArgb(255, 0, 0, 64),
                Color.FromArgb(255, 64, 0, 64),
            };
            const int num_rows = 6;
            const int num_columns = 8;
            const int pbx_width = 60;
            const int pbx_height = 60;
            const int spacing = 4;

            int row_y = y;
            for (int row = 0; row < num_rows; row++)
            {
                int column_x = x;
                for (int column = 0; column < num_columns; column++)
                {
                    PictureBox pbx = new PictureBox();
                    pbx.Click += Color_Click;
                    pbx.BackColor = colors[row * num_columns + column];
                    pbx.Size = new Size(pbx_width, pbx_height);
                    pbx.Location = new Point(column_x, row_y);
                    pbx.BorderStyle = BorderStyle.Fixed3D;
                    this.pictureBox1.Controls.Add(pbx);
                    column_x += pbx_width + spacing;
                }
                row_y += pbx_height + spacing;
            }
        }

        private void Color_Click(object sender, EventArgs e)
        {
            PictureBox pic = sender as PictureBox;
            this.pictureBox1.BackColor = pic.BackColor;
        }
        private void button15_Click(object sender, EventArgs e)
        {
            //小小兵的顏色
            //Minion Yellow Color
            //HEX #FFD55E / RGB (255, 213, 94)
            //顏色的名稱
            //https://www.color-name.com/

            this.pictureBox1.BackColor = Color.FromArgb(255, 213, 94);

            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_anime\minion-yellow.png";
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //從顏色的名稱 取得顏色的分量
            Color slateBlue = Color.FromName("SlateBlue");
            byte g = slateBlue.G;
            byte b = slateBlue.B;
            byte r = slateBlue.R;
            byte a = slateBlue.A;
            string text = String.Format("Slate Blue has these ARGB values: Alpha:{0}, " +
                "red:{1}, green: {2}, blue {3}", new object[] { a, r, g, b });

            richTextBox1.Text += text + "\n";
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

/*
            //顏色名稱2
            int i = 0;
            int j = 0;
            int w = 120;
            int h = 35;

            int width = w * 7;
            int height = h * 20;
            Bitmap bitmap1 = new Bitmap(width, height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.Pink);

            Color c = new Color();


            pictureBox1.Image = bitmap1;

*/