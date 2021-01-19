using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_kaleidoscope
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The polylines we are drawing.
        List<List<Point>> Polylines = new List<List<Point>>();
        List<Point> NewPolyline = null;

        // Exit.
        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Clear old polylines.
        private void mnuFileNew_Click(object sender, EventArgs e)
        {
            Polylines = new List<List<Point>>();
            picCanvas.Refresh();
        }

        // Start drawing.
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            NewPolyline = new List<Point>();
            Polylines.Add(NewPolyline);
            NewPolyline.Add(e.Location);
        }

        // Continue drawing.
        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;
            NewPolyline.Add(e.Location);
            picCanvas.Refresh();
        }

        // Stop drawing.
        private void picCanvas_MouseUp(object sender, MouseEventArgs e)
        {
            if (NewPolyline == null) return;
            NewPolyline = null;
            picCanvas.Refresh();
        }

        // Draw the polylines.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a list of transformations, starting with the identity.
            List<Matrix> matrices = new List<Matrix>();
            matrices.Add(new Matrix());

            // Make transformation matrices for the selected style.
            int wid = picCanvas.ClientSize.Width;
            int hgt = picCanvas.ClientSize.Height;
            Rectangle src_rect = new Rectangle(0, 0, wid, hgt);
            if (mnuStyleReflectX.Checked || mnuStyleReflectXY.Checked)
            {
                // Reflect across X axis.
                Point[] pts = { new Point(wid, 0), new Point(0, 0), new Point(wid, hgt) };
                Matrix mat = new Matrix(src_rect, pts);
                matrices.Add(mat);
            }
            if (mnuStyleReflectY.Checked || mnuStyleReflectXY.Checked)
            {
                // Reflect across Y axis.
                Point[] pts = { new Point(0, hgt), new Point(wid, hgt), new Point(0, 0) };
                Matrix mat = new Matrix(src_rect, pts);
                matrices.Add(mat);
            }
            if (mnuStyleReflectXY.Checked)
            {
                // Reflect across X and Y axes.
                Point[] pts = { new Point(wid, hgt), new Point(0, hgt), new Point(wid, 0) };
                Matrix mat = new Matrix(src_rect, pts);
                matrices.Add(mat);
            }
            if (mnuStyleRotate2.Checked)
            {
                // Rotate 180 degrees.
                Matrix mat = new Matrix();
                mat.RotateAt(180, new PointF(wid / 2, hgt / 2));
                matrices.Add(mat);
            }
            if (mnuStyleRotate4.Checked)
            {
                // Rotate 90 degrees three times.
                for (int i = 1; i <= 3; i++)
                {
                    Matrix mat = new Matrix();
                    mat.RotateAt(i * 90, new PointF(wid / 2, hgt / 2));
                    matrices.Add(mat);
                }
            }
            if (mnuStyleRotate8.Checked)
            {
                // Rotate 45 degrees seven times.
                for (int i = 1; i <= 7; i++)
                {
                    Matrix mat = new Matrix();
                    mat.RotateAt(i * 45, new PointF(wid / 2, hgt / 2));
                    matrices.Add(mat);
                }
            }

            // Loop through all of the transformations.
            foreach (Matrix mat in matrices)
            {
                e.Graphics.Transform = mat;
                foreach (List<Point> pline in Polylines)
                {
                    e.Graphics.DrawLines(Pens.Blue, pline.ToArray());
                }
            }
        }

        // Uncheck all other menu items.
        private void mnuStyle_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem clicked = sender as ToolStripMenuItem;

            clicked.Checked = true;
            foreach (ToolStripMenuItem item in mnuStyle.DropDownItems)
            {
                if (item != clicked) item.Checked = false;
            }
        }
    }
}
