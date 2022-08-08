using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;    //for PropertyInfo

namespace vcs_ColorMap
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
                                                g = pictureBox1.CreateGraphics();
                                                p = new Pen(Color.Red, 6);


            show_item_location();
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
            dx = 120 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 7, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 7, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 7, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 7, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 7, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 7, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 7, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 7, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 7, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 8, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 8, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 8, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 8, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 8, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 8, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 8, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 8, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 8, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 8, y_st + dy * 9);

            pictureBox1.Size = new Size(600, 700);
            pictureBox1.BackColor = Color.Pink;

            comboBox1.Location = new Point(x_st + dx * 9, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 9, y_st + dy * 1);

            this.Size = new Size(1500, 800);
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

        /*
        列舉系統的所有Color並以ComboBox顯示
        首先利用Reflection的方式取得系統中的所有Color，將利Color的名子加到cmbColor中。
        接著在cmbColor中自行繪制顯示的內容，在這邊需要將cmbColor中的屬性'DrawMode'設為'OwnerDrawFixed'，並新的DrawItem事件
        */
        private void button3_Click(object sender, EventArgs e)
        {
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
            //獲取系統預定義顏色
            Array colors = System.Enum.GetValues(typeof(KnownColor));
            foreach (object colorName in colors)
            {
                richTextBox1.Text += "get color : " + colorName.ToString() + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
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

        private void button10_Click(object sender, EventArgs e)
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

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

    }
}

