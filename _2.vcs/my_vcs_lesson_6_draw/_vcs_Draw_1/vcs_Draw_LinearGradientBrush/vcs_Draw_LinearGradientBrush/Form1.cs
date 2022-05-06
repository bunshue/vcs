using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

//兩種漸層色使用範例

namespace vcs_Draw_LinearGradientBrush
{
    public partial class Form1 : Form
    {
        Color color_st = Color.White;
        Color color_sp = Color.Green;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            color_st = pictureBox_gradient_color_st.BackColor;
            color_sp = pictureBox_gradient_color_sp.BackColor;
            draw_gradient_color();
        }


        private void button1_Click(object sender, EventArgs e)
        {
            UseHorizontalLinearGradients1();
        }

        void UseHorizontalLinearGradients1()
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            Rectangle r = new Rectangle(10, 10, 100, 100);

            LinearGradientBrush theBrush = null;
            int yOffSet = 10;

            Array obj = Enum.GetValues(typeof(LinearGradientMode));

            for (int x = 0; x < obj.Length; x++)
            {
                LinearGradientMode temp = (LinearGradientMode)obj.GetValue(x);
                theBrush = new LinearGradientBrush(r, Color.Red, Color.Blue, temp);

                g.DrawString(temp.ToString(), new Font("Times New Roman", 10), new SolidBrush(Color.Black), 0, yOffSet);

                g.FillRectangle(theBrush, 120, yOffSet, 200, 50);
                yOffSet += 80;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            UseHorizontalLinearGradients2();
        }

        public void UseHorizontalLinearGradients2()
        {
            Graphics g = this.pictureBox1.CreateGraphics();

            LinearGradientBrush linGrBrush = new LinearGradientBrush(
               new Point(0, 10),
               new Point(200, 10),
               Color.FromArgb(255, 255, 0, 0),   // Opaque red
               Color.FromArgb(255, 0, 0, 255));  // Opaque blue

            Pen pen = new Pen(linGrBrush);

            g.DrawLine(pen, 0, 10, 200, 10);
            g.FillEllipse(linGrBrush, 0, 30, 200, 100);
            g.FillRectangle(linGrBrush, 0, 155, 500, 30);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //漸層色

            Graphics g = this.pictureBox1.CreateGraphics();

            LinearGradientBrush lgb = new LinearGradientBrush(new Point(0, 0), new Point(0, 400), Color.Red, Color.Green);
            g.FillRectangle(lgb, 0, 0, 400, 400);

            //另法
            LinearGradientBrush brush = new LinearGradientBrush(this.ClientRectangle, Color.White, Color.Red, LinearGradientMode.Horizontal);
            brush.SetSigmaBellShape(0.5f);
            //Graphics g = this.CreateGraphics();
            g.FillRectangle(brush, 50, 150, 300, 100);
            Font f = new Font("Times New Roman", 60);
            g.DrawString("文字漸層色", f, brush, 1, 1);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //漸層色 3種

            Bitmap bitmap1 = new Bitmap(600, 600);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //漸層色1
            // Define a brush with two points and their colors.
            using (LinearGradientBrush br = new LinearGradientBrush(new Point(10, 10), new Point(140, 50), Color.Red, Color.White))
            {
                g.FillRectangle(br, 10, 10, 125, 50);
                g.DrawRectangle(Pens.Black, 10, 10, 125, 50);
            }

            // Define a brush with a Rectangle, colors, and gradient mode.
            Rectangle rect = new Rectangle(145, 10, 125, 50);
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Blue, Color.White, LinearGradientMode.ForwardDiagonal))
            {
                g.FillRectangle(br, rect);
                g.DrawRectangle(Pens.Black, rect);
            }

            // Define a gradient with more than 2 colors.
            rect = new Rectangle(10, 70, 260, 50);
            using (LinearGradientBrush br = new LinearGradientBrush(rect, Color.Blue, Color.White, 0f))
            {
                // Create a ColorBlend object. Note that you
                // must initialize it before you save it in the
                // brush's InterpolationColors property.
                ColorBlend colorBlend = new ColorBlend();
                colorBlend.Colors = new Color[] 
                {
                    Color.Red,
                    Color.Orange,
                    Color.Yellow,
                    Color.Lime,
                    Color.Blue,
                    Color.Indigo,
                    Color.Violet,
                };
                colorBlend.Positions = new float[]
                {
                    0f, 1/6f, 2/6f, 3/6f, 4/6f, 5/6f, 1f
                };
                br.InterpolationColors = colorBlend;

                g.FillRectangle(br, rect);
                g.DrawRectangle(Pens.Black, rect);
            }

            //漸層色2
            //用漸變色填充
            //LinearGradientBrush：使用沿漸變混合的兩種顏色進行繪制
            rect = new Rectangle(0, 0, 500, 100);//定義矩形,參數為起點橫縱坐標以及其長和寬
            rect.Location = new Point(50, 300);
            LinearGradientBrush b = new LinearGradientBrush(rect, Color.Red, Color.Black, LinearGradientMode.Horizontal);
            g.FillRectangle(b, rect);

            //漸層色3
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 30 + i, 500, 30 + i);
            }

            pictureBox1.Image = bitmap1;

        }

        private void pictureBox_gradient_color_st_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color_st = colorDialog1.Color;
                pictureBox_gradient_color_st.BackColor = color_st;
                draw_gradient_color();
            }
        }

        private void pictureBox_gradient_color_sp_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color_sp = colorDialog1.Color;
                pictureBox_gradient_color_sp.BackColor = color_sp;
                draw_gradient_color();
            }
        }

        void draw_gradient_color()
        {
            int W = pictureBox_gradient_color.ClientSize.Width;
            int H = pictureBox_gradient_color.ClientSize.Height;

            Bitmap bitmap1 = new Bitmap(W, H);

            int i;
            int j;

            byte r_st = color_st.R;
            byte g_st = color_st.G;
            byte b_st = color_st.B;

            byte r_sp = color_sp.R;
            byte g_sp = color_sp.G;
            byte b_sp = color_sp.B;

            int r_diff = r_sp - r_st;
            int g_diff = g_sp - g_st;
            int b_diff = b_sp - b_st;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    bitmap1.SetPixel(i, j, Color.FromArgb(255, r_st + i * r_diff / W, g_st + i * g_diff / W, b_st + i * b_diff / W));
                }
            }
            pictureBox_gradient_color.Image = bitmap1;
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            GradientColor(e);
        }

        //抽取成一個方法實現漸變色,在Paint中引用
        private void GradientColor(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Color FColor = Color.Red;
            Color TColor = Color.Green;

            Brush b = new LinearGradientBrush(this.panel1.ClientRectangle, FColor, TColor, LinearGradientMode.Horizontal);

            g.FillRectangle(b, this.panel1.ClientRectangle);

            /*
             * Horizontal = 0　　　　　　摘要:指定從左到右的漸變。
             * 
             * Vertical = 1　　　　　　　摘要: 指定從上到下的漸變。
             * 
             * ForwardDiagonal = 2　　  摘要:指定從左上到右下的漸變。
             * 
             * BackwardDiagonal = 3　　 摘要:指定從右上到左下的漸變。
             */
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //漸層色1
            //LinearGradientBrush線形漸層塗刷

            Graphics g = pictureBox1.CreateGraphics();

            LinearGradientBrush lbrush = new LinearGradientBrush(
       new Point(0, 0),  // 開始的位置
       new Point(400, 200),// 結束的位置
       Color.White, // 第一種顏色
       Color.Blue); // 第二種顏色

            g.FillRectangle(lbrush, 0, 0, 400, 200);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //漸層色2
            //PathGradientBrush 路徑漸層塗刷

            Graphics g = pictureBox1.CreateGraphics();

            Point[] pt = new Point[3];  // 路徑
            pt[0] = new Point(0, 0);
            pt[1] = new Point(200, 200);
            pt[2] = new Point(400, 0);
            PathGradientBrush lbrush = new PathGradientBrush(pt);  // 中央顏色 
            lbrush.CenterColor = Color.Blue;
            Color[] colorArray = new Color[] { Color.Red, Color.Green, Color.Yellow };
            lbrush.SurroundColors = colorArray; // 路徑中點的顏色
            g.FillRectangle(lbrush, 0, 0, 400, 200);
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

    }
}

