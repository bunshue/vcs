using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for SmoothingMode
using System.Diagnostics;           //for Debug

namespace vcs_DrawEllipse2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // A rectangle that define the ellipse.
        private bool GotEllipse = false;
        private Rectangle Ellipse;

        // Used while drawing ellipses.
        private bool DrawingEllipse = false;
        private int StartX, StartY, EndX, EndY;

        // Ellipse equations.
        private float Dx, Dy, Rx, Ry;
        private float A, B, C, D, E, F;

        private void Form1_Load(object sender, EventArgs e)
        {
            this.DoubleBuffered = true;
        }

        // Let the user click and drag to select ellipses.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            DrawingEllipse = true;
            GotEllipse = false;

            StartX = e.X;
            StartY = e.Y;
            EndX = e.X;
            EndY = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (!DrawingEllipse) return;

            EndX = e.X;
            EndY = e.Y;

            // Redraw.
            this.Refresh();
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we are not drawing.
            if (!DrawingEllipse) return;

            EndX = e.X;
            EndY = e.Y;

            // Make sure the ellipse has non-zero width and height.
            lstParameters.Items.Clear();
            if ((StartX != EndX) && (StartY != EndY))
            {
                Ellipse = new Rectangle(
                    Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                    Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
                GotEllipse = true;

                // Find and display the ellipse's formula.
                GetEllipseFormula(Ellipse, out Dx, out Dy, out Rx, out Ry,
                    out A, out B, out C, out D, out E, out F);

                lblXNumerator.Text = "x - " + Dx.ToString();
                lblXDenominator.Text = Rx.ToString();
                lblYNumerator.Text = "y - " + Dy.ToString();
                lblYDenominator.Text = Ry.ToString();

                lstParameters.Items.Add("A = " + A.ToString());
                lstParameters.Items.Add("B = " + B.ToString());
                lstParameters.Items.Add("C = " + C.ToString());
                lstParameters.Items.Add("D = " + D.ToString());
                lstParameters.Items.Add("E = " + E.ToString());
                lstParameters.Items.Add("F = " + F.ToString());
            }
            else
            {
                lblXNumerator.Text = "";
                lblXDenominator.Text = "";
                lblYNumerator.Text = "";
                lblYDenominator.Text = "";
            }

            // We are no longer drawing a new ellipse.
            DrawingEllipse = false;

            // Redraw.
            this.Refresh();
        }

        // Get the equation for this ellipse.
        private void GetEllipseFormula(RectangleF rect,
            out float Dx, out float Dy, out float Rx, out float Ry,
            out float A, out float B, out float C, out float D,
            out float E, out float F)
        {
            Dx = rect.X + rect.Width / 2f;
            Dy = rect.Y + rect.Height / 2f;
            Rx = rect.Width / 2f;
            Ry = rect.Height / 2f;

            A = 1f / Rx / Rx;
            B = 1f / Ry / Ry;
            C = 0;
            D = -2f * Dx / Rx / Rx;
            E = -2f * Dy / Ry / Ry;
            F = Dx * Dx / Rx / Rx + Dy * Dy / Ry / Ry - 1;

            // Verify the parameters.
            Console.WriteLine();
            float xmid = rect.Left + rect.Width / 2f;
            float ymid = rect.Top + rect.Height / 2f;
            VerifyEquation(A, B, C, D, E, F, rect.Left, ymid);
            VerifyEquation(A, B, C, D, E, F, rect.Right, ymid);
            VerifyEquation(A, B, C, D, E, F, xmid, rect.Top);
            VerifyEquation(A, B, C, D, E, F, xmid, rect.Bottom);
        }

        // Verify that the equation gives a value
        // close to 0 for the given point (x, y).
        private void VerifyEquation(float A, float B, float C, float D, float E, float F, float x, float y)
        {
            float total = A * x * x + B * y * y + C * x * y + D * x + E * y + F;
            Console.WriteLine("VerifyEquation (" + x + ", " + y + ") = " + total);
            Debug.Assert(Math.Abs(total) < 0.001f);
        }

        // Draw the ellipses.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the first ellipse.
            if (GotEllipse)
            {
                // Fill the ellipse.
                e.Graphics.FillEllipse(Brushes.LightBlue, Ellipse);

                // Plot the ellipse's equation.
                List<PointF> points = new List<PointF>();
                for (float x = Dx - Rx; x <= Dx + Rx; x++)
                {
                    float radicand = (x - Dx) / Rx;
                    radicand = 1 - radicand * radicand;
                    if (radicand >= 0f)
                    {
                        points.Add(new PointF(
                            x, (float)(Dy + Ry * Math.Sqrt(radicand))));
                    }
                }
                for (float x = Dx + Rx; x >= Dx - Rx; x--)
                {
                    float radicand = (x - Dx) / Rx;
                    radicand = 1 - radicand * radicand;
                    if (radicand > 0f)
                    {
                        points.Add(new PointF(
                            x, (float)(Dy - Ry * Math.Sqrt(radicand))));
                    }
                }
                e.Graphics.DrawPolygon(Pens.Blue, points.ToArray());
            }

            // Draw the new ellipse if we are drawing one.
            if (DrawingEllipse)
            {
                e.Graphics.DrawEllipse(Pens.Red,
                    Math.Min(StartX, EndX), Math.Min(StartY, EndY),
                    Math.Abs(StartX - EndX), Math.Abs(StartY - EndY));
            }

            // Draw lines between the parts of the fractions.
            e.Graphics.DrawLine(Pens.Black,
                lblXDenominator.Left, lblXDenominator.Top - 1,
                lblXDenominator.Right, lblXDenominator.Top - 1);
            e.Graphics.DrawLine(Pens.Black,
                lblYDenominator.Left, lblYDenominator.Top - 1,
                lblYDenominator.Right, lblYDenominator.Top - 1);
        }
    }
}

