using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawEllipse
{
    public partial class Form1 : Form
    {
        private const float small = 0.1f;

        // Rectangles that define the ellipses.
        private bool GotEllipse1 = false;
        private bool GotEllipse2 = false;
        private Rectangle Ellipse1;
        private Rectangle Ellipse2;

        // The points of intersection.
        private List<PointF> Roots = new List<PointF>();
        private List<float> RootSign1 = new List<float>();
        private List<float> RootSign2 = new List<float>();
        private List<PointF> PointsOfIntersection = new List<PointF>();

        // Used while drawing ellipses.
        private int DrawingEllipseNum = 0;
        private int StartX;
        private int StartY;
        private int EndX;
        private int EndY;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;
            /*
            // Some sample ellipses to start off.
            Ellipse1 = new Rectangle(234, 223, 255, 150);
            Ellipse2 = new Rectangle(152, 233, 210, 155);

            //// Test 1.
            //Ellipse1 = new Rectangle(75, 25, 50, 50);
            //Ellipse2 = new Rectangle(50, 50, 50, 50);
            //// Test 2.
            //Ellipse1 = new Rectangle(25, 25, 50, 50);
            //Ellipse2 = new Rectangle(50, 50, 50, 50);
            //// Test 3.
            //Ellipse1 = new Rectangle(75, 75, 50, 50);
            //Ellipse2 = new Rectangle(50, 50, 50, 50);
            //// Test 4.
            //Ellipse1 = new Rectangle(25, 75, 50, 50);
            //Ellipse2 = new Rectangle(50, 50, 50, 50);
            //// Test 5.
            //Ellipse1 = new Rectangle(25, 50, 75, 50);
            //Ellipse2 = new Rectangle(50, 25, 50, 100);

            GotEllipse1 = true;
            GotEllipse2 = true;
            */
            richTextBox1.Text += "左鍵畫一圓, 右鍵畫一圓\n";
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int W = 160;
            int H = 60;

            richTextBox1.Size = new Size(305, 420);
            //richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 7);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1068, 492);
            this.Text = "vcs_DrawEllipse";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        // Draw the ellipses.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the first ellipse.
            if (GotEllipse1)
            {
                //richTextBox1.Text += "111\n";
                using (Brush brush = new SolidBrush(Color.FromArgb(128, Color.Blue)))
                {
                    e.Graphics.FillEllipse(brush, Ellipse1);
                }
                e.Graphics.DrawEllipse(Pens.Blue, Ellipse1);
            }

            // Draw the second ellipse.
            if (GotEllipse2)
            {
                //richTextBox1.Text += "222\n";
                using (Brush brush = new SolidBrush(Color.FromArgb(128, Color.Red)))
                {
                    e.Graphics.FillEllipse(brush, Ellipse2);
                }
                e.Graphics.DrawEllipse(Pens.Red, Ellipse2);
            }

            // Draw the new ellipse if we are drawing one.
            if (DrawingEllipseNum == 1)
            {
                //richTextBox1.Text += "aaa\n";
                e.Graphics.DrawEllipse(Pens.Blue,
                    Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                    Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
            }
            else if (DrawingEllipseNum == 2)
            {
                //richTextBox1.Text += "bbb\n";
                e.Graphics.DrawEllipse(Pens.Red,
                    Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                    Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
            }

            // Draw the points of intersection.
            const int radius = 4;
            foreach (PointF pt in PointsOfIntersection)
            {
                RectangleF rect = new RectangleF(pt.X - radius, pt.Y - radius, 2 * radius, 2 * radius);
                e.Graphics.DrawEllipse(Pens.Green, rect);
            }
        }

        // Let the user click and drag to select ellipses.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Remove previous points of intersection.
            Roots = new List<PointF>();
            RootSign1 = new List<float>();
            RootSign2 = new List<float>();
            PointsOfIntersection = new List<PointF>();

            // If we are already drawing, stop.
            if (DrawingEllipseNum > 0)
            {
                DrawingEllipseNum = 0;
                pictureBox1.Refresh();
                return;
            }

            // See which mouse button is pressed.
            if (e.Button == MouseButtons.Left)
            {
                DrawingEllipseNum = 1;
                GotEllipse1 = false;
            }
            else if (e.Button == MouseButtons.Right)
            {
                DrawingEllipseNum = 2;
                GotEllipse2 = false;
            }

            StartX = e.X;
            StartY = e.Y;
            EndX = e.X;
            EndY = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (DrawingEllipseNum == 0)
            {
                return;
            }

            EndX = e.X;
            EndY = e.Y;

            // Redraw.
            pictureBox1.Refresh();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (DrawingEllipseNum == 0)
            {
                return;
            }

            EndX = e.X;
            EndY = e.Y;

            // Make sure the ellipse has non-zero width and height.
            if ((StartX != EndX) && (StartY != EndY))
            {
                // See which ellipse we are drawing.
                if (DrawingEllipseNum == 1)
                {
                    Ellipse1 = new Rectangle(
                        Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                        Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                    GotEllipse1 = true;
                }
                else if (DrawingEllipseNum == 2)
                {
                    Ellipse2 = new Rectangle(
                        Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                        Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                    GotEllipse2 = true;
                }
            }

            // We are no longer drawing a new ellipse.
            DrawingEllipseNum = 0;

            // Redraw.
            pictureBox1.Refresh();
        }
    }
}
