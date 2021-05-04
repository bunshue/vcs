using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for Matrix

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Matrix myMatrix1 = new Matrix();  // 第一種方式
            Matrix myMatrix2 = new Matrix(1, 2, 4, 5, 7, 8); // 第二種方式

            float m11 = myMatrix2.Elements[0];
            float m12 = myMatrix2.Elements[1];
            float m21 = myMatrix2.Elements[2];
            float m22 = myMatrix2.Elements[3];
            float dx = myMatrix2.Elements[4];
            float dy = myMatrix2.Elements[5];

            float dx2 = myMatrix2.OffsetX;
            float dy2 = myMatrix2.OffsetY;


            Rectangle rect = new Rectangle(0, 0, 100, 100);
            Point[] pt = new Point[3] { new Point(0, 0), new Point(100, 0), new Point(0, 100) };
            Matrix myMatrix3 = new Matrix(rect, pt); // 第三種方式

            RectangleF rect2 = new Rectangle(0, 0, 100, 100);
            PointF[] pt2 = new PointF[3] { new PointF(0, 0), new PointF(100, 0), new PointF(0, 100) };
            Matrix myMatrix4 = new Matrix(rect2, pt2); // 第四種方式

            e.Graphics.Transform = myMatrix1;

        }
    }
}
