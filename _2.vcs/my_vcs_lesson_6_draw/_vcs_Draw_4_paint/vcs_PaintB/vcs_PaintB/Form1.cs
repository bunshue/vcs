using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;//for SmoothingMode, DashStyle

namespace vcs_PaintB
{
    public partial class Form1 : Form
    {
        // The ellipses to draw.
        private List<Rectangle> Ellipses = new List<Rectangle>();

        // The points for the new ellipse we are drawing.
        private Point StartPoint, EndPoint;
        private bool DrawingNew = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
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

            this.Size = new Size(1200, 820);

            pictureBox1.Size = new Size(800, 680);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            int w = this.ClientSize.Width - richTextBox1.Location.X - 10;   //border : 10
            int h = this.ClientSize.Height - richTextBox1.Location.Y - 10;   //border : 10
            richTextBox1.Size = new Size(w, h);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Text = "vcs_Network5";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_new_Click(object sender, EventArgs e)
        {
            Ellipses = new List<Rectangle>();
            this.Refresh();
        }

        // Draw the current ellipses.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the existing ellipses.
            foreach (Rectangle rect in Ellipses)
            {
                e.Graphics.DrawEllipse(Pens.Black, rect);
            }

            // If we are creating a new ellipse, draw it.
            if (DrawingNew)
            {
                using (Pen dashed_pen = new Pen(Color.Green, 0))
                {
                    dashed_pen.DashStyle = DashStyle.Custom;
                    dashed_pen.DashPattern = new float[] { 5, 5 };
                    Rectangle rect = new Rectangle(
                        Math.Min(StartPoint.X, EndPoint.X),
                        Math.Min(StartPoint.Y, EndPoint.Y),
                        Math.Abs(StartPoint.X - EndPoint.X),
                        Math.Abs(StartPoint.Y - EndPoint.Y));
                    e.Graphics.DrawEllipse(dashed_pen, rect);
                }
            }
            this.Text = Ellipses.Count.ToString();
        }

        // Start selecting an ellipse.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            DrawingNew = true;
            StartPoint = e.Location;
            EndPoint = e.Location;
        }

        // Continue drawing the new ellipse.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!DrawingNew) return;
            EndPoint = e.Location;
            pictureBox1.Refresh();
        }

        // Finish drawing the new ellipse.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!DrawingNew) return;
            DrawingNew = false;

            // If the start and end points are different,
            // save the new ellipse.
            if (StartPoint.X != EndPoint.X &&
                StartPoint.Y != EndPoint.Y)
            {
                Rectangle rect = new Rectangle(
                    Math.Min(StartPoint.X, EndPoint.X),
                    Math.Min(StartPoint.Y, EndPoint.Y),
                    Math.Abs(StartPoint.X - EndPoint.X),
                    Math.Abs(StartPoint.Y - EndPoint.Y));
                Ellipses.Add(rect);
            }

            pictureBox1.Refresh();
        }
    }
}
