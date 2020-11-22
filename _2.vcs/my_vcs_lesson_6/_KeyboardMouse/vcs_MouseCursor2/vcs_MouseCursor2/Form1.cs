using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for MatrixOrder

namespace vcs_MouseCursor2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Cursors.
        private Cursor[] Cursors;
        private const int NumCursors = 18;

        private void Form1_Load(object sender, EventArgs e)
        {
            // Geometry.
            const int cursor_wid = 32;
            const int cursor_hgt = 32;
            float cx = cursor_wid / 2f;
            float cy = cursor_hgt / 2f;
            float rx = cx * 0.9f;
            float ry = cx * 0.4f;
            RectangleF rect = new RectangleF(-rx, -ry, 2 * rx, 2 * ry);
            float radius = cx * 0.15f;

            // Make the transformations we will use.
            Matrix transform1 = new Matrix();
            transform1.Rotate(60f, MatrixOrder.Append);
            transform1.Translate(cx, cy, MatrixOrder.Append);
            Matrix transform2 = new Matrix();
            transform2.Rotate(-60f, MatrixOrder.Append);
            transform2.Translate(cx, cy, MatrixOrder.Append);
            Matrix transform3 = new Matrix();
            transform3.Translate(cx, cy, MatrixOrder.Append);

            // Make an orbital image.
            Bitmap orbital_bm = new Bitmap(cursor_wid, cursor_hgt);
            using (Graphics gr = Graphics.FromImage(orbital_bm))
            {
                // Use a transparent background.
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.Clear(Color.Transparent);

                // Draw the orbitals.
                gr.Transform = transform1;
                gr.DrawEllipse(Pens.Red, rect);

                gr.Transform = transform2;
                gr.DrawEllipse(Pens.Red, rect);

                gr.Transform = transform3;
                gr.DrawEllipse(Pens.Red, rect);

                // Draw the nucleus.
                gr.FillEllipse(Brushes.Black,
                    -radius, -radius, 2 * radius, 2 * radius);
            }

            // Make the cursors.
            Cursors = new Cursor[NumCursors];
            double theta1 = 0;
            double dtheta1 = 2 * Math.PI / NumCursors;
            double theta2 = 0;
            double dtheta2 = 2 * Math.PI / NumCursors * 2;
            double theta3 = 0;
            double dtheta3 = 2 * Math.PI / NumCursors * 3;
            for (int i = 0; i < NumCursors; i++)
            {
                Bitmap cursor_bm = new Bitmap(cursor_wid, cursor_hgt);
                using (Graphics gr = Graphics.FromImage(cursor_bm))
                {
                    // Copy the background orbitals.
                    gr.SmoothingMode = SmoothingMode.AntiAlias;
                    gr.DrawImage(orbital_bm, 0, 0);

                    // Draw the electrons.
                    gr.Transform = transform1;
                    double x1 = rx * Math.Cos(theta1);
                    double y1 = ry * Math.Sin(theta1);
                    gr.FillEllipse(Brushes.Red,
                        (int)(x1 - radius), (int)(y1 - radius),
                        2 * radius, 2 * radius);
                    theta1 += dtheta1;

                    gr.Transform = transform2;
                    double x2 = rx * Math.Cos(theta2);
                    double y2 = ry * Math.Sin(theta2);
                    gr.FillEllipse(Brushes.Green,
                        (int)(x2 - radius), (int)(y2 - radius),
                        2 * radius, 2 * radius);
                    theta2 += dtheta2;

                    gr.Transform = transform3;
                    double x3 = rx * Math.Cos(theta3);
                    double y3 = ry * Math.Sin(theta3);
                    gr.FillEllipse(Brushes.Blue,
                        (int)(x3 - radius), (int)(y3 - radius),
                        2 * radius, 2 * radius);
                    theta3 += dtheta3;
                }

                // Turn the bitmap into a cursor.
                Cursors[i] = new Cursor(cursor_bm.GetHicon());

                // Increment theta.
                theta1 += dtheta1;
            }
        }

        // Display the next cursor.
        private int CursorNumber = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            CursorNumber = (CursorNumber + 1) % NumCursors;
            this.Cursor = Cursors[CursorNumber];
        }


    }
}
