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

namespace vcs_Color
{
    public partial class Form1 : Form
    {
        Graphics g;
        Graphics g2;
        Pen p;

        //RGB-波長轉換用
        double[,] rgb_data = new double[,] {
            {380,0.1741,0.0050,0.8209,0.00145,0.0000,0.0065 },
            {385,0.1740,0.0050,0.8210,0.0022,0.0001,0.0105 },
            {390,0.1738,0.0049,0.8213,0.0042,0.0001,0.0201 },
            {395,0.1736,0.0049,0.8215,0.0076,0.0002,0.0362 },
            {400,0.1733,0.0048,0.8219,0.0143,0.0004,0.0679 },
            {405,0.1730,0.0048,0.8222,0.0232,0.0006,0.1102 },
            {410,0.1726,0.0048,0.8226,0.0435,0.0012,0.2074 },
            {415,0.1721,0.0048,0.8231,0.0776,0.0022,0.3713 },
            {420,0.1714,0.0051,0.8235,0.1344,0.0040,0.6456 },
            {425,0.1703,0.0058,0.8239,0.2148,0.0073,1.0391 },
            {430,0.1689,0.0069,0.8242,0.2839,0.0116,1.3856 },
            {435,0.1669,0.0086,0.8245,0.3285,0.0168,1.6230 },
            {440,0.1644,0.0109,0.8247,0.3483,0.0230,1.7471 },
            {445,0.1611,0.0138,0.8251,0.3481,0.0298,1.7826 },
            {450,0.1566,0.0177,0.8257,0.3362,0.0380,1.7721 },
            {455,0.1510,0.0227,0.8263,0.3187,0.0480,1.7441 },
            {460,0.1440,0.0297,0.8263,0.2908,0.0600,1.6692 },
            {465,0.1355,0.0399,0.8246,0.2511,0.0739,1.5281 },
            {470,0.1241,0.0578,0.8181,0.1954,0.0910,1.2876 },
            {475,0.1096,0.0868,0.8036,0.1421,0.1126,1.0419 },
            {480,0.0913,0.1327,0.7760,0.0956,0.1390,0.8130 },
            {485,0.0687,0.2007,0.7306,0.0580,0.1693,0.6162 },
            {490,0.0454,0.2950,0.6596,0.0320,0.2080,0.4652 },
            {495,0.0235,0.4127,0.5638,0.0147,0.2586,0.3533 },
            {500,0.0082,0.5384,0.4534,0.0049,0.3230,0.2720 },
            {505,0.0039,0.6548,0.3413,0.0024,0.4073,0.2123 },
            {510,0.0139,0.7502,0.2359,0.0093,0.5030,0.1582 },
            {515,0.0389,0.8120,0.1491,0.0291,0.6082,0.1117 },
            {520,0.0743,0.8338,0.0919,0.0633,0.7100,0.0782 },
            {525,0.1142,0.8262,0.0596,0.1096,0.7932,0.0573 },
            {530,0.1547,0.8059,0.0394,0.1655,0.8620,0.0422 },
            {535,0.1929,0.7816,0.0255,0.2257,0.9149,0.0298 },
            {540,0.2296,0.7543,0.0161,0.2904,0.9540,0.0203 },
            {545,0.2658,0.7243,0.0099,0.3597,0.9803,0.0134 },
            {550,0.3016,0.6923,0.0061,0.4334,0.9950,0.0087 },
            {555,0.3373,0.6589,0.0038,0.5121,1.0000,0.0057 },
            {560,0.3731,0.6245,0.0024,0.5945,0.9950,0.0039 },
            {565,0.4087,0.5896,0.0017,0.6784,0.9786,0.0027 },
            {570,0.4441,0.5547,0.0012,0.7621,0.9520,0.0021 },
            {575,0.4788,0.5202,0.0010,0.8425,0.9154,0.0010 },
            {580,0.5125,0.4866,0.0009,0.9163,0.8700,0.0017 },
            {585,0.5448,0.4544,0.0008,0.9786,0.8163,0.0014 },
            {590,0.5752,0.4242,0.0006,1.0263,0.7570,0.0011 },
            {595,0.6029,0.3965,0.0006,1.0567,0.6949,0.0010 },
            {600,0.6270,0.3725,0.0005,1.0522,0.6130,0.0008 },
            {605,0.6482,0.3514,0.0004,1.0456,0.5668,0.0006 },
            {610,0.6658,0.3340,0.0002,1.0026,0.5030,0.0003 },
            {615,0.6801,0.3197,0.0002,0.9384,0.4412,0.0002 },
            {620,0.6915,0.3083,0.0002,0.8544,0.3810,0.0002 },
            {625,0.7006,0.2993,0.0001,0.7514,0.3210,0.0001 },
            {630,0.7079,0.2920,0.0001,0.6424,0.2650,0.0000 },
            {635,0.7140,0.2859,0.0001,0.5419,0.2170,0.0000 },
            {640,0.7219,0.2809,0.0001,0.4479,0.1750,0.0000 },
            {645,0.7230,0.2770,0.0000,0.3608,0.1382,0.0000 },
            {650,0.7260,0.2740,0.0000,0.2835,0.1070,0.0000 },
            {655,0.7283,0.2717,0.0000,0.2187,0.0816,0.0000 },
            {660,0.7300,0.2700,0.0000,0.1649,0.0610,0.0000 },
            {665,0.7311,0.2689,0.0000,0.1212,0.0446,0.0000 },
            {670,0.7320,0.2680,0.0000,0.0874,0.0320,0.0000 },
            {675,0.7327,0.2673,0.0000,0.0636,0.0232,0.0000 },
            {680,0.7334,0.2666,0.0000,0.0468,0.0170,0.0000 },
            {685,0.7340,0.2660,0.0000,0.0329,0.0119,0.0000 },
            {690,0.7344,0.2656,0.0000,0.0227,0.0082,0.0000 },
            {695,0.7346,0.2654,0.0000,0.0158,0.0057,0.0000 },
            {700,0.7347,0.2653,0.0000,0.0114,0.0041,0.0000 },
            {705,0.7347,0.2653,0.0000,0.0081,0.0029,0.0000 },
            {710,0.7347,0.2653,0.0000,0.0058,0.0021,0.0000 },
            {715,0.7347,0.2653,0.0000,0.0041,0.0015,0.0000 },
            {720,0.7347,0.2653,0.0000,0.0029,0.0010,0.0000 },
            {725,0.7347,0.2653,0.0000,0.0020,0.0007,0.0000 },
            {730,0.7347,0.2653,0.0000,0.0014,0.0005,0.0000 },
            {735,0.7347,0.2653,0.0000,0.0010,0.0004,0.0000 },
            {740,0.7347,0.2653,0.0000,0.0007,0.0002,0.0000 },
            {745,0.7347,0.2653,0.0000,0.0005,0.0002,0.0000 },
            {750,0.7347,0.2653,0.0000,0.0003,0.0001,0.0000 },
            {755,0.7347,0.2653,0.0000,0.0002,0.0001,0.0000 },
            {760,0.7347,0.2653,0.0000,0.0002,0.0001,0.0000 },
            {765,0.7347,0.2653,0.0000,0.0001,0.0000,0.0000 },
            {770,0.7347,0.2653,0.0000,0.0001,0.0000,0.0000 },
            {775,0.7347,0.2653,0.0000,0.0001,0.0000,0.0000 },
            {780,0.7347,0.2653,0.0000,0.0000,0.0000,0.0000 }
            };

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

            g = pictureBox1.CreateGraphics();
            g2 = pictureBox2.CreateGraphics();
            p = new Pen(Color.Red, 6);

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

            pictureBox1.Size = new Size(850, 700);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox1.BackColor = Color.Pink;

            pictureBox2.Size = new Size(370, 90);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            pictureBox2.BackColor = Color.Pink;

            comboBox1.Location = new Point(x_st + dx * 7 + 100, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 650);
            richTextBox1.Location = new Point(x_st + dx * 7 + 100, y_st + dy * 1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1770, 800);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        private void button4_Click(object sender, EventArgs e)
        {
            //獲取系統預定義顏色
            Array colors = System.Enum.GetValues(typeof(KnownColor));
            foreach (object colorName in colors)
            {
                richTextBox1.Text += "get color : " + colorName.ToString() + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
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

        private void button6_Click(object sender, EventArgs e)
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

        private void button7_Click(object sender, EventArgs e)
        {
            //建立調色盤
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


        private void button8_Click(object sender, EventArgs e)
        {
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

        //波長轉RGB ST

        private Color getColorFromWaveLength(int Wavelength)
        {
            double Gamma = 1.00;
            int IntensityMax = 255;
            double Blue;
            double Green;
            double Red;
            double Factor;

            if (Wavelength >= 350 && Wavelength <= 439)
            {
                Red = -(Wavelength - 440d) / (440d - 350d);
                Green = 0.0;
                Blue = 1.0;
            }
            else if (Wavelength >= 440 && Wavelength <= 489)
            {
                Red = 0.0;
                Green = (Wavelength - 440d) / (490d - 440d);
                Blue = 1.0;
            }
            else if (Wavelength >= 490 && Wavelength <= 509)
            {
                Red = 0.0;
                Green = 1.0;
                Blue = -(Wavelength - 510d) / (510d - 490d);

            }
            else if (Wavelength >= 510 && Wavelength <= 579)
            {
                Red = (Wavelength - 510d) / (580d - 510d);
                Green = 1.0;
                Blue = 0.0;
            }
            else if (Wavelength >= 580 && Wavelength <= 644)
            {
                Red = 1.0;
                Green = -(Wavelength - 645d) / (645d - 580d);
                Blue = 0.0;
            }
            else if (Wavelength >= 645 && Wavelength <= 780)
            {
                Red = 1.0;
                Green = 0.0;
                Blue = 0.0;
            }
            else
            {
                Red = 0.0;
                Green = 0.0;
                Blue = 0.0;
            }
            if (Wavelength >= 350 && Wavelength <= 419)
            {
                Factor = 0.3 + 0.7 * (Wavelength - 350d) / (420d - 350d);
            }
            else if (Wavelength >= 420 && Wavelength <= 700)
            {
                Factor = 1.0;
            }
            else if (Wavelength >= 701 && Wavelength <= 780)
            {
                Factor = 0.3 + 0.7 * (780d - Wavelength) / (780d - 700d);
            }
            else
            {
                Factor = 0.0;
            }

            int R = this.factorAdjust(Red, Factor, IntensityMax, Gamma);
            int G = this.factorAdjust(Green, Factor, IntensityMax, Gamma);
            int B = this.factorAdjust(Blue, Factor, IntensityMax, Gamma);

            return Color.FromArgb(R, G, B);
        }

        private int factorAdjust(double Color,
         double Factor,
         int IntensityMax,
         double Gamma)
        {
            if (Color == 0.0)
            {
                return 0;
            }
            else
            {
                return (int)Math.Round(IntensityMax * Math.Pow(Color * Factor, Gamma));
            }
        }


        void getColorFromWaveLength2(double l) // RGB <0,1> <- lambda l <400,700> [nm]
        {
            double t;
            double r = 0.0;
            double g = 0.0;
            double b = 0.0;
            if ((l >= 400.0) && (l < 410.0)) { t = (l - 400.0) / (410.0 - 400.0); r = +(0.33 * t) - (0.20 * t * t); }
            else if ((l >= 410.0) && (l < 475.0)) { t = (l - 410.0) / (475.0 - 410.0); r = 0.14 - (0.13 * t * t); }
            else if ((l >= 545.0) && (l < 595.0)) { t = (l - 545.0) / (595.0 - 545.0); r = +(1.98 * t) - (t * t); }
            else if ((l >= 595.0) && (l < 650.0)) { t = (l - 595.0) / (650.0 - 595.0); r = 0.98 + (0.06 * t) - (0.40 * t * t); }
            else if ((l >= 650.0) && (l < 700.0)) { t = (l - 650.0) / (700.0 - 650.0); r = 0.65 - (0.84 * t) + (0.20 * t * t); }
            if ((l >= 415.0) && (l < 475.0)) { t = (l - 415.0) / (475.0 - 415.0); g = +(0.80 * t * t); }
            else if ((l >= 475.0) && (l < 590.0)) { t = (l - 475.0) / (590.0 - 475.0); g = 0.8 + (0.76 * t) - (0.80 * t * t); }
            else if ((l >= 585.0) && (l < 639.0)) { t = (l - 585.0) / (639.0 - 585.0); g = 0.84 - (0.84 * t); }
            if ((l >= 400.0) && (l < 475.0)) { t = (l - 400.0) / (475.0 - 400.0); b = +(2.20 * t) - (1.50 * t * t); }
            else if ((l >= 475.0) && (l < 560.0)) { t = (l - 475.0) / (560.0 - 475.0); b = 0.7 - (t) + (0.30 * t * t); }

            richTextBox1.Text += "l = " + l.ToString() + "\n";
            richTextBox1.Text += "r = " + r.ToString() + "\n";
            richTextBox1.Text += "g = " + g.ToString() + "\n";
            richTextBox1.Text += "b = " + b.ToString() + "\n";

            richTextBox1.Text += "r = " + Math.Floor(r * 255).ToString() + "\n";
            richTextBox1.Text += "g = " + Math.Floor(g * 255).ToString() + "\n";
            richTextBox1.Text += "b = " + Math.Floor(b * 255).ToString() + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //波長轉RGB RGB轉波長

            //波長轉RGB

            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 2);

            int lambda = 350;
            for (lambda = 350; lambda <= 780; lambda++)
            {
                Color c = getColorFromWaveLength(lambda);
                p = new Pen(c, 2);
                g.DrawLine(p, (lambda - 350) * 2, 0, (lambda - 350) * 2, 200);


                if (lambda == 500)
                {
                    richTextBox1.Text += "l = " + lambda.ToString() + "\n";
                    richTextBox1.Text += "r = " + c.R.ToString() + "\n";
                    richTextBox1.Text += "g = " + c.G.ToString() + "\n";
                    richTextBox1.Text += "b = " + c.B.ToString() + "\n";
                }

            }
            pictureBox1.Image = bmp;

            //RGB轉波長

            Color pt;
            int xx = 0;
            for (xx = 0; xx < 800; xx += 50)
            {
                pt = bmp.GetPixel(xx, 100);

                p = new Pen(pt, 40);
                g.DrawLine(p, xx * 1, 300, xx * 1, 400);

                p = new Pen(pt, 6);
                g.DrawLine(p, xx * 1, 200 - 40 / 2, xx * 1, 300);

                //再由RGB轉波長

                int wavelength = RGBToWavelength(pt);
                richTextBox1.Text += wavelength.ToString() + " ";

                Font f = new Font("標楷體", 12);
                g.DrawString(wavelength.ToString(), f, Brushes.Black, new PointF(xx * 1, 400));
            }

            richTextBox1.Text += "\n";

            /*
            double l = 500;

            getColorFromWaveLength2(l);
            */


        }
        //波長轉RGB SP

        int RGBToWavelength(Color color)
        {
            int wavelength = 0;
            int ROW = rgb_data.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = rgb_data.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = rgb_data.Length;//獲取整個二維陣列的長度，即所有元 的個數
            /*
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";
            */

            double r = color.R;
            double g = color.G;
            double b = color.B;

            double x = 0;
            double y = 0;
            double z = 0;

            x = (0.490 * r + 0.310 * g + 0.200 * b) / (0.667 * r + 1.132 * g + 1.200 * b);
            y = (0.117 * r + 0.812 * g + 0.010 * b) / (0.667 * r + 1.132 * g + 1.200 * b);
            z = (0.000 * r + 0.010 * g + 0.990 * b) / (0.667 * r + 1.132 * g + 1.200 * b);
            /*
            richTextBox1.Text += "x = " + x.ToString() + "\n";
            richTextBox1.Text += "y = " + y.ToString() + "\n";
            richTextBox1.Text += "z = " + z.ToString() + "\n";
            */
            double abs_min = double.MaxValue;
            double abs = 0;
            int index = 0;
            int i;
            for (i = 0; i < ROW; i++)
            {
                abs = Math.Abs(rgb_data[i, 1] - x) + Math.Abs(rgb_data[i, 2] - y) + Math.Abs(rgb_data[i, 3] - z);
                if (abs < abs_min)
                {
                    abs_min = abs;
                    index = i;
                }
            }

            wavelength = (int)rgb_data[index, 0];
            //richTextBox1.Text += "index = " + index.ToString() + "\twavelength = " + rgb_data[index, 0].ToString() + "\n";

            return wavelength;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            double l = 500;

            getColorFromWaveLength2(l);

        }

        private void button18_Click(object sender, EventArgs e)
        {
            //GetHueExample

            int w = pictureBox1.ClientSize.Width;
            int h = pictureBox1.ClientSize.Height;

            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 2);

            pictureBox1.Image = bmp;


            Color color = Color.FromArgb(255, 255, 0, 0);


            GetHueExample(g, color, 0);

            color = Color.FromArgb(255, 200, 0, 100);
            GetHueExample(g, color, 450);

        }

        public void GetHueExample(Graphics g, Color color, int dx)
        {
            // Color structures. One is a variable used for temporary storage. The other
            // is a constant used for comparisons.
            Color someColor = Color.FromArgb(0);
            //Color redShade = Color.FromArgb(255, 200, 0, 100);
            Color redShade = color;

            // Array to store KnownColor values that match the hue of the redShade color.
            KnownColor[] colorMatches = new KnownColor[15];

            // Number of matches found.
            int count = 0;

            // Iterate through the KnownColor enums until 15 matches are found.
            for (KnownColor enumValue = 0; enumValue <= KnownColor.YellowGreen && count < 15; enumValue++)
            {
                someColor = Color.FromKnownColor(enumValue);
                if (someColor.GetHue() == redShade.GetHue())
                {
                    colorMatches[count] = enumValue;
                    richTextBox1.Text += "取得顏色 : " + Color.FromKnownColor(colorMatches[count]).ToString() + ", hue = " + redShade.GetHue().ToString() + "\n";

                    count++;
                }
            }

            // Display the redShade color and its argb value.
            SolidBrush myBrush1 = new SolidBrush(redShade);
            Font myFont = new Font("Arial", 12);
            int x = 20 + dx;
            int y = 20;
            someColor = redShade;
            g.FillRectangle(myBrush1, x, y, 100, 30);
            g.DrawString(someColor.ToString(), myFont, Brushes.Black, x + 120, y);

            // Iterate through the matches that were found and display each color that
            // corresponds with the enum value in the array. also display the name of
            // the KnownColor.
            for (int i = 0; i < count; i++)
            {
                y += 40;
                someColor = Color.FromKnownColor(colorMatches[i]);
                myBrush1.Color = someColor;
                g.FillRectangle(myBrush1, x, y, 100, 30);
                g.DrawString(someColor.ToString(), myFont, Brushes.Black, x + 120, y);
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {

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

        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);
        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }

        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }

        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }

        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }

        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }

        int cnt = 0;
        Brush b = new SolidBrush(Color.White);
        Color cl_old;

        private void timer1_Tick(object sender, EventArgs e)
        {
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);
            if (cl_old != cl)
            {
                cnt = 0;
                g2.Clear(BackColor);

                g2.DrawString(cl.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5, 0));
                g2.DrawString(cl.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Green), new PointF(5 + 75, 0));
                g2.DrawString(cl.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 150, 0));

                cl_old = cl;

                int rr = cl.R;
                int gg = cl.G;
                int bb = cl.B;

                RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
                YUV yy = new YUV();
                yy = RGBToYUV(pp);

                g2.DrawString(((int)yy.Y).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Yellow), new PointF(5, 35));
                g2.DrawString(((int)yy.U).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 75, 35));
                g2.DrawString(((int)yy.V).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5 + 150, 35));
            }
            else
            {
                cnt++;
                if ((cnt > 25) && (cnt % 5) == 0)
                {
                    //this.Size = new Size(240, 55);
                    g2.Clear(BackColor);
                    g2.DrawString(DateTime.Now.ToString("HH:mm:ss"), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(20, 5));
                }
            }
        }
    }
}
