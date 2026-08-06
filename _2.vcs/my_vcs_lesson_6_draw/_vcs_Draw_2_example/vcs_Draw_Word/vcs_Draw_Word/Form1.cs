using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for Matrix, SmoothingMode
using System.Drawing.Text;  //for TextRenderingHint

namespace vcs_Draw_Word
{
    public partial class Form1 : Form
    {
        string draw_text = "牡丹亭";
        int font_size = 40;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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

            pictureBox1.Size = new Size(830, 830);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 720);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 900);
            this.Text = "vcs_Draw_Word";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            /*
            Bitmap bitmap1 = new Bitmap(830, 830);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);
            pictureBox1.Image = bitmap1;
            */

            draw_grid();

            int x_st = 20;
            int y_st = 20;
            int dx = 250;
            int dy = 140;

            richTextBox1.Text += "1投影文字\n";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 0;
            do_word_effect1(x_st, y_st);

            richTextBox1.Text += "2浮雕效果\n";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 1;
            do_word_effect2(x_st, y_st);

            richTextBox1.Text += "3印版效果\n";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 2;
            do_word_effect3(x_st, y_st);

            richTextBox1.Text += "4倒影文字\n";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 3 + 50;
            do_word_effect4(x_st, y_st);

            richTextBox1.Text += "5陰影文字\n";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 4;
            do_word_effect5(x_st, y_st);

            richTextBox1.Text += "6字體做陰影效果\n";

            x_st = 20 + dx * 1;
            y_st = 20 + dy * 0;
            do_word_effect6(x_st, y_st);

            richTextBox1.Text += "7傾斜效果\n";
            x_st = 20 + dx * 1;
            y_st = 20 + dy * 1;
            do_word_effect7(x_st, y_st);

            richTextBox1.Text += "8漸層色文字\n";
            x_st = 20 + dx * 1;
            y_st = 20 + dy * 2;
            do_word_effect8(x_st, y_st);

            richTextBox1.Text += "9旋轉效果\n";
            x_st = 20 + dx * 1 + 200;
            y_st = 20 + dy * 4;
            do_word_effect9(x_st, y_st);
        }

        //------------------------------------------------------------  # 60個

        int xx = 100;
        int yy = 100;
        int dy = 100;
        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawRectangle(Pens.Red, xx, yy, 300, 50);
            yy += dy;
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        void draw_grid()
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            /*
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            for (int i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Red, i, 0, i, H);  // 垂直線
            }
            for (int j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Red, 0, j, W, j);  // 水平線
            }
            */

            int x_st = 20;
            int y_st = 20;
            int dx = 250;
            int dy = 140;
            for (int i = x_st; i <= 820; i += dx)
            {
                g.DrawLine(Pens.Red, i, y_st, i, 820);  // 垂直線
            }
            for (int j = y_st; j <= 820; j += dy)
            {
                g.DrawLine(Pens.Red, x_st, j, 820, j);  // 水平線
            }


            Font f = new Font("標楷體", 20);

            int dd = dy - 32;

            string draw_text = "1投影文字";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 0 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));


            draw_text = "2浮雕效果";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 1 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "3印版效果";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 2 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "4倒影文字";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 3 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "5陰影文字";
            x_st = 20 + dx * 0;
            y_st = 20 + dy * 4 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "6字體做陰影效果";

            x_st = 20 + dx * 1;
            y_st = 20 + dy * 0 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "7傾斜效果";
            x_st = 20 + dx * 1;
            y_st = 20 + dy * 1 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "8漸層色文字";
            x_st = 20 + dx * 1;
            y_st = 20 + dy * 2 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

            draw_text = "9旋轉效果";
            x_st = 20 + dx * 1;
            y_st = 20 + dy * 4 + dd;
            g.DrawString(draw_text, f, new SolidBrush(Color.Black), new PointF(x_st, y_st));

        }

        void do_word_effect1(int x_st, int y_st)
        {
            //投影文字
            Graphics g = this.pictureBox1.CreateGraphics();
            //設置文本輸出質量
            g.TextRenderingHint = TextRenderingHint.ClearTypeGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            Font f = new Font("標楷體", font_size);
            Matrix matrix = new Matrix();
            //投射
            matrix.Shear(-1.5f, 0.0f);
            //縮放
            matrix.Scale(1, 0.5f);
            //平移
            matrix.Translate(x_st + 130, y_st + 58);
            //對繪圖平面實施坐標變換、、
            g.Transform = matrix;
            SolidBrush grayBrush = new SolidBrush(Color.Gray);
            SolidBrush colorBrush = new SolidBrush(Color.BlueViolet);
            string draw_text = "博客園1";
            //繪制陰影
            g.DrawString(draw_text, f, grayBrush, new PointF(x_st, y_st));
            g.ResetTransform();
            //繪制前景
            g.DrawString(draw_text, f, colorBrush, new PointF(x_st, y_st));
        }

        void do_word_effect2(int x_st, int y_st)
        {
            //浮雕效果
            Brush backBrush = Brushes.Black;
            Brush foreBrush = Brushes.White;
            Font f = new Font("標楷體", font_size, FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string draw_text = "博客園2";
            g.DrawString(draw_text, f, backBrush, x_st + 1, y_st + 1);
            g.DrawString(draw_text, f, foreBrush, x_st, y_st);
        }

        void do_word_effect3(int x_st, int y_st)
        {
            //印版效果
            //印版文字
            int i = 0;
            Brush backBrush = Brushes.Black;
            Brush foreBrush = Brushes.Violet;
            Font f = new Font("標楷體", font_size, FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string draw_text = "博客園3";
            while (i < 20)
            {
                g.DrawString(draw_text, f, backBrush, x_st - i, y_st + i);
                i = i + 1;
            }
            g.DrawString(draw_text, f, foreBrush, x_st, y_st);
        }

        void do_word_effect4(int x_st, int y_st)
        {
            //倒影文字

            Brush backBrush = Brushes.Gray;
            Brush foreBrush = Brushes.Black;
            Font f = new Font("標楷體", font_size, FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string draw_text = "博客園4";

            g.TranslateTransform(x_st, y_st);

            int ascent = f.FontFamily.GetCellAscent(f.Style);
            int spacing = f.FontFamily.GetLineSpacing(f.Style);
            int lineHeight = System.Convert.ToInt16(f.GetHeight(g));
            int height = lineHeight * ascent / spacing;
            GraphicsState state = g.Save();
            g.ScaleTransform(1, -1.0F);
            g.DrawString(draw_text, f, backBrush, 0, -height);
            g.Restore(state);
            g.DrawString(draw_text, f, foreBrush, 0, -height);
        }

        void do_word_effect5(int x_st, int y_st)
        {
            //陰影文字
            string draw_text = "博客園5";
            Brush shadowBrush = Brushes.Gray;
            Brush foreBrush = Brushes.Black;
            Font f = new Font("標楷體", font_size, FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();

            g.DrawString(draw_text, f, shadowBrush, x_st + 20, y_st + 20);
            g.DrawString(draw_text, f, foreBrush, x_st, y_st);

            //有點問題
        }

        void do_word_effect6(int x_st, int y_st)
        {
            //字體做陰影效果 同樣字往右下寫一遍 顏色不同

            string draw_text = "牡丹亭";

            Graphics g = this.pictureBox1.CreateGraphics();
            int font_size_default = 80;
            Font f = new Font("標楷體", font_size_default);
            g.DrawString(draw_text, f, new SolidBrush(Color.Pink), new PointF(x_st, y_st));
            g.DrawString(draw_text, f, new SolidBrush(Color.Red), new PointF(x_st + 5, y_st + 5));
        }

        void do_word_effect7(int x_st, int y_st)
        {
            //傾斜效果
            Brush foreBrush = Brushes.Blue;
            Font f = new Font("標楷體", font_size, FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string draw_text = "博客園7";

            g.TranslateTransform(x_st, y_st);

            Matrix transform = g.Transform;

            //右倾斜文字
            //float shearX = -0.230F;

            //左倾斜文字
            float shearX = 0.550F;
            float shearY = 0.10F;
            transform.Shear(shearX, shearY);
            g.Transform = transform;
            g.DrawString(draw_text, f, foreBrush, 0, 0);
        }

        void do_word_effect8(int x_st, int y_st)
        {
            //漸層色文字
            String draw_text = "天階夜色涼如水8";
            Brush ShadowBrush = Brushes.Gray;
            Brush ForeBrush = Brushes.Black;
            Font f = new Font("標楷體", font_size, FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            PointF point = new PointF(0, 0);
            SizeF size = g.MeasureString(draw_text, f);
            RectangleF rectangle = new RectangleF(point, size);
            Brush brush = new LinearGradientBrush(rectangle, Color.Red, Color.Green, LinearGradientMode.Horizontal);
            g.DrawString(draw_text, f, brush, x_st, y_st);
        }

        void do_word_effect9(int x_st, int y_st)
        {
            //旋轉效果顯示文字
            Graphics g = this.pictureBox1.CreateGraphics();
            g.SmoothingMode = SmoothingMode.AntiAlias;
            for (int i = 0; i <= 360; i += 10)
            {
                //平移Graphics對象到窗體中心
                g.TranslateTransform(x_st, y_st);
                //設置Graphics對象的輸出角度
                g.RotateTransform(i);
                //設置文字填充顏色
                Brush brush = Brushes.DarkViolet;
                //旋轉顯示文字
                g.DrawString("Happy New Year", new Font("Lucida Console", 11f), brush, 0, 0);
                //恢復全局變換矩陣
                g.ResetTransform();
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

