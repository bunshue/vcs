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

namespace test_LinearGradientBrush
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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            UseHorizontalLinearGradients1(e);

        }

        public void UseHorizontalLinearGradients1(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            Rectangle r = new Rectangle(10, 10, 100, 100);

            LinearGradientBrush theBrush = null;
            int yOffSet = 10;

            Array obj = Enum.GetValues(typeof(LinearGradientMode));

            for (int x = 0; x < obj.Length; x++)
            {
                LinearGradientMode temp = (LinearGradientMode)obj.GetValue(x);
                theBrush = new LinearGradientBrush(r, Color.Red,
                  Color.Blue, temp);

                g.DrawString(temp.ToString(), new Font("Times New Roman", 10),
                  new SolidBrush(Color.Black), 0, yOffSet);

                g.FillRectangle(theBrush, 120, yOffSet, 200, 50);
                yOffSet += 80;
            }
        }

        public void UseHorizontalLinearGradients2(PaintEventArgs e)
        {
            LinearGradientBrush linGrBrush = new LinearGradientBrush(
               new Point(0, 10),
               new Point(200, 10),
               Color.FromArgb(255, 255, 0, 0),   // Opaque red
               Color.FromArgb(255, 0, 0, 255));  // Opaque blue

            Pen pen = new Pen(linGrBrush);

            e.Graphics.DrawLine(pen, 0, 10, 200, 10);
            e.Graphics.FillEllipse(linGrBrush, 0, 30, 200, 100);
            e.Graphics.FillRectangle(linGrBrush, 0, 155, 500, 30);
        }
    }
}
