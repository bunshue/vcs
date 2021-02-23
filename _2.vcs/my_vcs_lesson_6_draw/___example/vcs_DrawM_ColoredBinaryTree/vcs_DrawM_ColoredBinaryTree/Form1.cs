using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_DrawM_ColoredBinaryTree
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Recursively draw a binary tree branch.
        private void DrawBranch(Graphics gr, Pen pen, int depth, int max_depth, float x, float y,
            float length, float theta, float length_scale, float dtheta)
        {
            // See where this branch should end.
            float x1 = (float)(x + length * Math.Cos(theta));
            float y1 = (float)(y + length * Math.Sin(theta));

            // Set the pen's color depending on the depth.
            if (depth == 1) pen.Color = Color.Red;
            else
            {
                int g = 255 * (max_depth - depth) / max_depth;
                int r = 139 * (depth - 3) / max_depth;
                if (r < 0) r = 0;
                int b = 0;
                pen.Color = Color.FromArgb(r, g, b);
            }

            // Set the pen's thickness depending on the depth.
            int thickness = 10 * depth / max_depth;
            if (thickness < 0) thickness = 0;
            pen.Width = thickness;

            // Draw the branch.
            gr.DrawLine(pen, x, y, x1, y1);

            // If depth > 1, draw the attached branches.
            if (depth > 1)
            {
                DrawBranch(gr, pen, depth - 1, max_depth, x1, y1,
                    length * length_scale, theta + dtheta, length_scale,
                    dtheta);
                DrawBranch(gr, pen, depth - 1, max_depth, x1, y1,
                    length * length_scale, theta - dtheta, length_scale,
                    dtheta);
            }
        }

        // Draw the tree.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(picCanvas.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            try
            {
                float root_x = picCanvas.ClientSize.Width / 2;
                float root_y = picCanvas.ClientSize.Height - 4;
                float length_scale = float.Parse(txtLengthScale.Text);
                float dtheta = (float)(Math.PI / 180.0 * (double)nudDtheta.Value);
                using (Pen the_pen = new Pen(Color.Black))
                {
                    DrawBranch(e.Graphics, the_pen,
                        (int)nudDepth.Value, (int)nudDepth.Value, root_x, root_y,
                        (int)nudLength.Value, (float)(-Math.PI / 2), length_scale,
                        dtheta);
                }
            }
            catch
            {
            }
        }

        // Redraw.
        private void parameter_ValueChanged(object sender, EventArgs e)
        {
            picCanvas.Refresh();
        }

        // Redraw.
        private void picCanvas_Resize(object sender, EventArgs e)
        {
            picCanvas.Refresh();
        }

        // Redraw.
        private void nud_KeyUp(object sender, KeyEventArgs e)
        {
            picCanvas.Refresh();
        }
    }
}
