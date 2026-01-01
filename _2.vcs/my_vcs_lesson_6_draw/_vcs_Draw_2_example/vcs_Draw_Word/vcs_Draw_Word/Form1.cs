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
        string draw_text = "群曜醫電";

        Point pt_st;    //文字的起始點(左上方)

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pt_st = new Point(100, 100);

            int W = this.Width;
            int H = this.Height;
            //this.Width / 2, this.Height / 2);
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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

            pictureBox1.Size = new Size(800, 720);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 720);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 800);
            this.Text = "vcs_Draw_Word";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            do_word_effect1();
            do_word_effect2();
            do_word_effect3();
            do_word_effect4();
            do_word_effect5();
            do_word_effect6();
            do_word_effect7();
            do_word_effect8();
            do_word_effect9();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            do_word_effect1();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            do_word_effect2();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            do_word_effect3();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            do_word_effect4();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            do_word_effect5();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            do_word_effect6();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            do_word_effect7();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            do_word_effect8();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            do_word_effect9();
        }

        void do_word_effect1()
        {
            int x_st = 0;
            int y_st = 30;
            //投影文字
            Graphics g = this.pictureBox1.CreateGraphics();
            //設置文本輸出質量
            g.TextRenderingHint = TextRenderingHint.ClearTypeGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            Font newFont = new Font("Times New Roman", 48);
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
            string text = "博客園1";
            //繪制陰影
            g.DrawString(text, newFont, grayBrush, new PointF(x_st, y_st));
            g.ResetTransform();
            //繪制前景
            g.DrawString(text, newFont, colorBrush, new PointF(x_st, y_st));
        }

        void do_word_effect2()
        {
            int x_st = 20;
            int y_st = 100;
            //浮雕效果
            Brush backBrush = Brushes.Black;
            Brush foreBrush = Brushes.White;
            Font font = new Font("宋體", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客園2";
            SizeF size = g.MeasureString(text, font);
            g.DrawString(text, font, backBrush, x_st + 1, y_st + 1);
            g.DrawString(text, font, foreBrush, x_st, y_st);
        }

        void do_word_effect3()
        {
            int x_st = 20;
            int y_st = 200;

            //印版效果

            //印版文字
            int i = 0;
            Brush backBrush = Brushes.Black;
            Brush foreBrush = Brushes.Violet;
            Font font = new Font("Times New Roman", System.Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客園3";
            SizeF size = g.MeasureString(text, font);
            while (i < Convert.ToInt16(20))
            {
                g.DrawString(text, font, backBrush, x_st - i, y_st + i);
                i = i + 1;
            }
            g.DrawString(text, font, foreBrush, x_st, y_st);
        }

        void do_word_effect4()
        {
            int x_st = 20;
            int y_st = 350;

            //倒影文字
            Brush backBrush = Brushes.Gray;
            Brush foreBrush = Brushes.Black;
            Font font = new Font("幼圓", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客園4";
            SizeF size = g.MeasureString(text, font);

            g.TranslateTransform(x_st, y_st);

            int ascent = font.FontFamily.GetCellAscent(font.Style);
            int spacing = font.FontFamily.GetLineSpacing(font.Style);
            int lineHeight = System.Convert.ToInt16(font.GetHeight(g));
            int height = lineHeight * ascent / spacing;
            GraphicsState state = g.Save();
            g.ScaleTransform(1, -1.0F);
            g.DrawString(text, font, backBrush, 0, -height);
            g.Restore(state);
            g.DrawString(text, font, foreBrush, 0, -height);
        }

        void do_word_effect5()
        {
            int x_st = 20;
            int y_st = 450;

            //陰影文字
            string text = "博客園5";
            Brush shadowBrush = Brushes.Gray;
            Brush foreBrush = Brushes.Black;
            Font font = new Font("幼圓", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            SizeF size = g.MeasureString(text, font);

            g.DrawString(text, font, shadowBrush, x_st + Convert.ToInt16(20), y_st + Convert.ToInt16(20));
            g.DrawString(text, font, foreBrush, x_st, y_st);

            //有點問題
        }

        void do_word_effect6()
        {
            int x_st = 0;
            int y_st = 30;

            //紋理效果
            /*
            //紋理效果
            //使用圖像填充文字線條
            TextureBrush brush = new TextureBrush(Image.FromFile(Application.StartupPath + "\\myPicture.jpg"));
            Graphics g = e.Graphics;
            g.DrawString("博客園", new Font("隸書", 60), brush, new PointF(0, 0));
            */
        }

        void do_word_effect7()
        {
            int x_st = 400;
            int y_st = 20;

            //傾斜效果
            Brush foreBrush = Brushes.Blue;
            Font font = new Font("幼圆", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客园7";
            SizeF size = g.MeasureString(text, font);

            g.TranslateTransform(x_st, y_st);

            Matrix transform = g.Transform;

            //右倾斜文字
            //float shearX = -0.230F;

            //左倾斜文字
            float shearX = 0.550F;
            float shearY = 0.10F;
            transform.Shear(shearX, shearY);
            g.Transform = transform;
            g.DrawString(text, font, foreBrush, 0, 0);
        }

        void do_word_effect8()
        {
            int x_st = 400;
            int y_st = 200;

            //漸層色文字
            String text = "天階夜色涼如水8";
            Brush ShadowBrush = Brushes.Gray;
            Brush ForeBrush = Brushes.Black;
            Font font = new Font("幼圆", System.Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            //g.Clear(Color.White);
            PointF point = new PointF(0, 0);
            SizeF size = g.MeasureString(text, font);
            RectangleF rectangle = new RectangleF(point, size);
            Brush brush = new LinearGradientBrush(rectangle, Color.Red, Color.Green, LinearGradientMode.Horizontal);
            g.DrawString(text, font, brush, x_st, y_st);
        }

        void do_word_effect9()
        {
            int x_st = 400;
            int y_st = 400;

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
