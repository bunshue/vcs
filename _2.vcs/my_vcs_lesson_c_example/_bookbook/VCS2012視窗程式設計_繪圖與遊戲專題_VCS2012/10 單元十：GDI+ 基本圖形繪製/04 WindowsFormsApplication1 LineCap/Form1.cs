using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for LineCap

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
            Pen pen1 = new Pen(Color.Black, 10);  // 黑色畫筆 粗細為 10

            int X = 20;
            int Y = 30;

            pen1.StartCap = LineCap.Flat; // 扁平線條端點。開端
            pen1.EndCap = LineCap.Flat; // 扁平線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.Flat", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.Square; // 方形線條端點。開端
            pen1.EndCap = LineCap.Square; // 方形線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.Square", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.Round; // 圓形線條端點。開端
            pen1.EndCap = LineCap.Round; // 圓形線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.Round", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.Triangle; // 三角形線條端點。開端
            pen1.EndCap = LineCap.Triangle; // 三角形線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.Triangle", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.SquareAnchor; // 方形錨點線條端點。開端
            pen1.EndCap = LineCap.SquareAnchor; // 方形錨點線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.SquareAnchor", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.RoundAnchor; // 圓形錨點線條端點。開端
            pen1.EndCap = LineCap.RoundAnchor; // 圓形錨點線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.RoundAnchor", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.DiamondAnchor; // 鑽石形線條端點。開端
            pen1.EndCap = LineCap.DiamondAnchor; // 鑽石形線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.DiamondAnchor", this.Font, Brushes.Black, X + 220, Y - 10);

            Y = Y + 30;
            pen1.StartCap = LineCap.ArrowAnchor; // 箭頭形狀線條端點。開端
            pen1.EndCap = LineCap.ArrowAnchor; // 箭頭形狀線條端點。末端
            e.Graphics.DrawLine(pen1, X, Y, X + 200, Y);
            e.Graphics.DrawString("LineCap.ArrowAnchor", this.Font, Brushes.Black, X + 220, Y - 10);
        }
    }
}
