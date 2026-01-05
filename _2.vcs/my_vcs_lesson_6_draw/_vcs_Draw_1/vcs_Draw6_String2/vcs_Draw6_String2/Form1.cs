using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;
using System.Drawing.Drawing2D;

/*
C#利用GDI+繪制旋轉文字等效果
C#中利用GDI+繪制旋轉文本的文字，網上有很多資料，基本都使用矩陣旋轉的方式實現。
但基本都只提及按點旋轉，若要實現在矩形范圍內旋轉文本，資料較少。
經過琢磨，可以將矩形內旋轉轉化為按點旋轉，不過需要經過不少的計算過程。
利用下面的類可以實現該功能。
*/

namespace vcs_Draw6_String2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Location = new Point(10, 10);
            pictureBox1.Size = new Size(988, 470);
            pictureBox1.Location = new Point(10, 30);
            label2.Location = new Point(10, 510);
            pictureBox2.Size = new Size(988, 100);
            pictureBox2.Location = new Point(10, 540);

            pictureBox2.Resize += new EventHandler(pictureBox2_Resize);
            pictureBox2.Paint += new PaintEventHandler(pictureBox2_Paint);

            this.Size = new Size(1167, 693);
            this.Text = "vcs_Draw6_String2";
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Font _font = new Font("Arial", 12);
            Brush _brush = new SolidBrush(Color.Black);
            Pen _pen = new Pen(Color.Black, 1f);
            string _text = "繪製旋轉文字效果";

            // 繪制圍繞點旋轉的文本  
            StringFormat format = new StringFormat();
            format.Alignment = StringAlignment.Center;
            format.LineAlignment = StringAlignment.Center;

            DrawString(e.Graphics, _text, _font, _brush, new PointF(100, 80), format, 45f);
            DrawString(e.Graphics, _text, _font, _brush, new PointF(200, 80), format, -45f);
            DrawString(e.Graphics, _text, _font, _brush, new PointF(300, 80), format, 90f);
            DrawString(e.Graphics, _text, _font, _brush, new PointF(400, 80), format, -60f);

            // 繪制矩形內旋轉的文本  
            // First line  
            RectangleF rc = RectangleF.FromLTRB(50, 150, 200, 230);
            RectangleF rect = rc;
            format.Alignment = StringAlignment.Near;

            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 30);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Near;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, -30);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Center;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, -90);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Far;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 70);

            // Second line  
            rect = rc;
            rect.Location += new SizeF(0, 100);
            format.Alignment = StringAlignment.Center;

            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 40);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Near;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 30);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Center;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, -70);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Far;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 60);

            // Third line  
            rect = rc;
            rect.Location += new SizeF(0, 200);
            format.Alignment = StringAlignment.Far;

            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, -30);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Near;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, -30);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Center;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 90);

            rect.Location += new SizeF(180, 0);
            format.LineAlignment = StringAlignment.Far;
            e.Graphics.DrawRectangle(_pen, rect.Left, rect.Top, rect.Width, rect.Height);
            DrawString(e.Graphics, _text, _font, _brush, rect, format, 45);



        }

        /// <summary>  
        /// 繪制根據矩形旋轉文本  
        /// </summary>  
        /// <param name="s">文本</param>  
        /// <param name="font">字體</param>  
        /// <param name="brush">填充</param>  
        /// <param name="layoutRectangle">局部矩形</param>  
        /// <param name="format">布局方式</param>  
        /// <param name="angle">角度</param>  
        public void DrawString(Graphics g, string s, Font font, Brush brush, RectangleF layoutRectangle, StringFormat format, float angle)
        {
            // 求取字符串大小  
            SizeF size = g.MeasureString(s, font);

            // 根據旋轉角度，求取旋轉後字符串大小  
            SizeF sizeRotate = ConvertSize(size, angle);

            // 根據旋轉後尺寸、布局矩形、布局方式計算文本旋轉點  
            PointF rotatePt = GetRotatePoint(sizeRotate, layoutRectangle, format);

            // 重設布局方式都為Center  
            StringFormat newFormat = new StringFormat(format);
            newFormat.Alignment = StringAlignment.Center;
            newFormat.LineAlignment = StringAlignment.Center;

            // 繪制旋轉後文本  
            DrawString(g, s, font, brush, rotatePt, newFormat, angle);
        }

        /// <summary>  
        /// 繪制根據點旋轉文本，一般旋轉點給定位文本包圍盒中心點  
        /// </summary>  
        /// <param name="s">文本</param>  
        /// <param name="font">字體</param>  
        /// <param name="brush">填充</param>  
        /// <param name="point">旋轉點</param>  
        /// <param name="format">布局方式</param>  
        /// <param name="angle">角度</param>  
        public void DrawString(Graphics g, string s, Font font, Brush brush, PointF point, StringFormat format, float angle)
        {
            // Save the matrix  
            Matrix mtxSave = g.Transform;

            Matrix mtxRotate = g.Transform;
            mtxRotate.RotateAt(angle, point);
            g.Transform = mtxRotate;

            g.DrawString(s, font, brush, point, format);

            // Reset the matrix  
            g.Transform = mtxSave;
        }

        private SizeF ConvertSize(SizeF size, float angle)
        {
            Matrix matrix = new Matrix();
            matrix.Rotate(angle);

            // 旋轉矩形四個頂點  
            PointF[] pts = new PointF[4];
            pts[0].X = -size.Width / 2f;
            pts[0].Y = -size.Height / 2f;
            pts[1].X = -size.Width / 2f;
            pts[1].Y = size.Height / 2f;
            pts[2].X = size.Width / 2f;
            pts[2].Y = size.Height / 2f;
            pts[3].X = size.Width / 2f;
            pts[3].Y = -size.Height / 2f;
            matrix.TransformPoints(pts);

            // 求取四個頂點的包圍盒  
            float left = float.MaxValue;
            float right = float.MinValue;
            float top = float.MaxValue;
            float bottom = float.MinValue;

            foreach (PointF pt in pts)
            {
                // 求取並集  
                if (pt.X < left)
                    left = pt.X;
                if (pt.X > right)
                    right = pt.X;
                if (pt.Y < top)
                    top = pt.Y;
                if (pt.Y > bottom)
                    bottom = pt.Y;
            }

            SizeF result = new SizeF(right - left, bottom - top);
            return result;
        }

        private PointF GetRotatePoint(SizeF size, RectangleF layoutRectangle, StringFormat format)
        {
            PointF pt = new PointF();

            switch (format.Alignment)
            {
                case StringAlignment.Near:
                    pt.X = layoutRectangle.Left + size.Width / 2f;
                    break;
                case StringAlignment.Center:
                    pt.X = (layoutRectangle.Left + layoutRectangle.Right) / 2f;
                    break;
                case StringAlignment.Far:
                    pt.X = layoutRectangle.Right - size.Width / 2f;
                    break;
                default:
                    break;
            }

            switch (format.LineAlignment)
            {
                case StringAlignment.Near:
                    pt.Y = layoutRectangle.Top + size.Height / 2f;
                    break;
                case StringAlignment.Center:
                    pt.Y = (layoutRectangle.Top + layoutRectangle.Bottom) / 2f;
                    break;
                case StringAlignment.Far:
                    pt.Y = layoutRectangle.Bottom - size.Height / 2f;
                    break;
                default:
                    break;
            }

            return pt;
        }

        //文字對齊效果 ST

        // Text justification.
        public enum TextJustification
        {
            Left,
            Right,
            Center,
            Full
        }

        // Arrangement parameters.
        private Padding TextMargin = new Padding(5);
        private const float ParagraphIndent = 40f;
        private const float LineSpacing = 1f;
        private const float ExtraParagraphSpacing = 0.5f;

        // The text to display.
        private const string MessageText = "拉 動 表 單 看 文 字 對 齊 效 果"; //以空白為分界

        // Draw justified text on the PictureBox.
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox2.BackColor);
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            // Draw within a rectangle excluding the margins.
            RectangleF rect = new RectangleF(
                TextMargin.Left, TextMargin.Top,
                pictureBox2.ClientSize.Width - TextMargin.Left - TextMargin.Right,
                pictureBox2.ClientSize.Height - TextMargin.Top - TextMargin.Bottom);

            // Draw the text.
            using (Font f = new Font("Times New Roman", 10))
            {
                DrawJustifiedLine(e.Graphics, rect, f, Brushes.Blue, MessageText);
            }

            // Show the text drawing area.
            e.Graphics.DrawRectangle(Pens.Silver, Rectangle.Round(rect));
        }

        // Draw justified text on the Graphics object
        // in the indicated Rectangle.
        private void DrawJustifiedLine(Graphics gr, RectangleF rect, Font font, Brush brush, string text)
        {
            // Break the text into words.
            string[] words = text.Split(' ');

            // Add a space to each word and get their lengths.
            float[] word_width = new float[words.Length];
            float total_width = 0;
            for (int i = 0; i < words.Length; i++)
            {
                // See how wide this word is.
                SizeF size = gr.MeasureString(words[i], font);
                word_width[i] = size.Width;
                total_width += word_width[i];
            }

            // Get the additional spacing between words.
            float extra_space = rect.Width - total_width;
            int num_spaces = words.Length - 1;
            if (words.Length > 1)
            {
                extra_space /= num_spaces;
            }

            // Draw the words.
            float x = rect.Left;
            float y = rect.Top;
            for (int i = 0; i < words.Length; i++)
            {
                // Draw the word.
                gr.DrawString(words[i], font, brush, x, y);

                // Move right to draw the next word.
                x += word_width[i] + extra_space;
            }
        }

        private void pictureBox2_Resize(object sender, EventArgs e)
        {
            pictureBox2.Refresh();
        }
        //文字對齊效果 SP
    }
}
