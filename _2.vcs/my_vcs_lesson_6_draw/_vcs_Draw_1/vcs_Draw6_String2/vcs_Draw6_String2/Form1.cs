using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

/*
C#利用GDI+繪制旋轉文字等效果，

C#中利用GDI+繪制旋轉文本的文字，網上有很多資料，基本都使用矩陣旋轉的方式實現。但基本都只提及按點旋轉，若要實現在矩形范圍內旋轉文本，資料較少。經過琢磨，可以將矩形內旋轉轉化為按點旋轉，不過需要經過不少的計算過程。利用下面的類可以實現該功能。
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

        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
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

    }
}
