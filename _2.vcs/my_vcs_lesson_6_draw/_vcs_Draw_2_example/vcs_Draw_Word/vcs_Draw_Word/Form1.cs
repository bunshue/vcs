using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for Matrix
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
            pt_st = new Point(100, 100);

        }

        private void button1_Click(object sender, EventArgs e)
        {
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
            matrix.Translate(130, 88);
            //對繪圖平面實施坐標變換、、
            g.Transform = matrix;
            SolidBrush grayBrush = new SolidBrush(Color.Gray);
            SolidBrush colorBrush = new SolidBrush(Color.BlueViolet);
            string text = "博客園";
            //繪制陰影
            g.DrawString(text, newFont, grayBrush, new PointF(0, 30));
            g.ResetTransform();
            //繪制前景
            g.DrawString(text, newFont, colorBrush, new PointF(0, 30));
        }

        //浮雕效果
        private void button2_Click(object sender, EventArgs e)
        {
            //浮雕文字
            Brush backBrush = Brushes.Black;
            Brush foreBrush = Brushes.White;
            Font font = new Font("宋體", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客園";
            SizeF size = g.MeasureString(text, font);
            Single posX = (this.Width - Convert.ToInt16(size.Width)) / 2;
            Single posY = (this.Height - Convert.ToInt16(size.Height)) / 2;
            g.DrawString(text, font, backBrush, posX + 1, posY + 1);
            g.DrawString(text, font, foreBrush, posX, posY);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //印版效果

            //印版文字
            int i = 0;
            Brush backBrush = Brushes.Black;
            Brush foreBrush = Brushes.Violet;
            Font font = new Font("Times New Roman", System.Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            string text = "博客園";
            SizeF size = g.MeasureString(text, font);
            Single posX = (this.Width - Convert.ToInt16(size.Width)) / 2;
            Single posY = (this.Height - Convert.ToInt16(size.Height)) / 3;
            while (i < Convert.ToInt16(20))
            {
                g.DrawString(text, font, backBrush, posX - i, posY + i);
                i = i + 1;
            }
            g.DrawString(text, font, foreBrush, posX, posY);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //倒影文字
            Brush backBrush = Brushes.Gray;
            Brush foreBrush = Brushes.Black;
            Font font = new Font("幼圓", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客園";
            SizeF size = g.MeasureString(text, font);
            int posX = (this.Width - Convert.ToInt16(size.Width)) / 2;
            int posY = (this.Height - Convert.ToInt16(size.Height)) / 2;
            g.TranslateTransform(posX, posY);
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

        private void button5_Click(object sender, EventArgs e)
        {
            //陰影文字
            string text = "博客園";
            Brush shadowBrush = Brushes.Gray;
            Brush foreBrush = Brushes.Black;
            Font font = new Font("幼圓", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            SizeF size = g.MeasureString(text, font);
            Single posX = (this.Width - Convert.ToInt16(size.Width)) / 4;
            Single posY = (this.Height - Convert.ToInt16(size.Height)) / 3;
            g.DrawString(text, font, shadowBrush, posX + Convert.ToInt16(20), posY + Convert.ToInt16(20));
            g.DrawString(text, font, foreBrush, posX, posY);


            //有點問題

        }

        private void button6_Click(object sender, EventArgs e)
        {
            /*
            //紋理效果
            //使用圖像填充文字線條
            TextureBrush brush = new TextureBrush(Image.FromFile(Application.StartupPath + "\\myPicture.jpg"));
            Graphics g = e.Graphics;
            g.DrawString("博客園", new Font("隸書", 60), brush, new PointF(0, 0));
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //傾斜效果
            Brush foreBrush = Brushes.Blue;
            Font font = new Font("幼圆", Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            string text = "博客园";
            SizeF size = g.MeasureString(text, font);
            Single posX = (this.Width - Convert.ToInt16(size.Width)) / 2;
            Single posY = (this.Height - Convert.ToInt16(size.Height)) / 2;
            g.TranslateTransform(posX, posY);
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

        private void button8_Click(object sender, EventArgs e)
        {
            //漸層色文字
            String text = " 博客园";
            Brush ShadowBrush = Brushes.Gray;
            Brush ForeBrush = Brushes.Black;
            Font font = new Font("幼圆", System.Convert.ToInt16(40), FontStyle.Regular);
            Graphics g = this.pictureBox1.CreateGraphics();
            //g.Clear(Color.White);
            PointF point = new PointF(0, 0);
            SizeF size = g.MeasureString(text, font);
            RectangleF rectangle = new RectangleF(point, size);
            Brush brush = new LinearGradientBrush(rectangle, Color.Red, Color.Green, LinearGradientMode.Horizontal);
            int width = (this.Width - Convert.ToInt16(size.Width)) / 2;
            int height = (this.Height - Convert.ToInt16(size.Height)) / 2;
            g.DrawString(text, font, brush, width, height);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //旋轉效果
            //旋轉顯示文字
            Graphics g = this.pictureBox1.CreateGraphics();
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            for (int i = 0; i <= 360; i += 10)
            {
                //平移Graphics對象到窗體中心
                g.TranslateTransform(this.Width / 2, this.Height / 2);
                //設置Graphics對象的輸出角度
                g.RotateTransform(i);
                //設置文字填充顏色
                Brush brush = Brushes.DarkViolet;
                //旋轉顯示文字
                g.DrawString(".bo ke yuan ", new Font("Lucida Console", 11f), brush, 0, 0);
                //恢復全局變換矩陣
                g.ResetTransform();
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }
    }
}

