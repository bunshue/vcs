using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw6_Rectangle2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Previously selected rectangles.
        private List<Rectangle> Rectangles = new List<Rectangle>();

        // The rectangle we are selecting.
        private Rectangle NewRectangle;

        // Variables used to select a new rectangle.
        private int StartX, StartY, EndX, EndY;
        private bool SelectingRectangle = false;

        // Start selecting a rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Save the current point.
            StartX = e.X;
            StartY = e.Y;
            EndX = e.X;
            EndY = e.Y;

            // Make a new selection rectangle.
            NewRectangle = new Rectangle(
                Math.Min(StartX, EndX),
                Math.Min(StartY, EndY),
                Math.Abs(StartX - EndX),
                Math.Abs(StartY - EndY));

            // Start marching.
            SelectingRectangle = true;
            timer1.Enabled = true;
        }

        // Continue selecting a rectangle.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!SelectingRectangle) return;

            // Save the current point.
            EndX = e.X;
            EndY = e.Y;

            // Make a new selection rectangle.
            NewRectangle = new Rectangle(
                Math.Min(StartX, EndX),
                Math.Min(StartY, EndY),
                Math.Abs(StartX - EndX),
                Math.Abs(StartY - EndY));

            // Redraw.
            Refresh();
        }

        // Finish selecting a rectangle.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!SelectingRectangle) return;
            SelectingRectangle = false;
            timer1.Enabled = false;
            if ((StartX == EndX) || (StartY == EndY)) return;

            // Save the newly selected rectangle.
            Rectangles.Add(new Rectangle(
                Math.Min(StartX, EndX),
                Math.Min(StartY, EndY),
                Math.Abs(StartX - EndX),
                Math.Abs(StartY - EndY)));

            // Redraw.
            Refresh();
        }

        // Parameters for drawing the dashed rectangle.
        private float Offset = 0;
        private float OffsetDelta = 2;
        private float[] DashPattern = { 5, 5 };

        // Draw the rectangles.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Offset += OffsetDelta;

            // Draw previously selected rectangles.
            for (int i = 0; i < Rectangles.Count; i++)
            {
                e.Graphics.FillRectangle(
                    RectangleBrushes[i % RectangleBrushes.Length],
                    Rectangles[i]);
                e.Graphics.DrawRectangle(Pens.Black, Rectangles[i]);
            }

            // Draw the new rectangle.
            if (SelectingRectangle)
            {
                e.Graphics.DrawRectangle(NewRectangle, Color.Yellow,
                    Color.Red, 2f, Offset, DashPattern);
            }
        }

        // Redraw.
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        // The rectangles' colors.
        private Brush[] RectangleBrushes =
        {
            Brushes.Red,
            Brushes.Green,
            Brushes.Blue,
            Brushes.Lime,
            Brushes.Orange,
            Brushes.Fuchsia,
            Brushes.Yellow,
            Brushes.LightGreen,
            Brushes.LightBlue,
            Brushes.Cyan,
        };

    }
}
