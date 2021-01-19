using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_queue_breadth_first_tree
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Hold branch information.
        private class BranchInfo
        {
            public float X, Y, Theta, Length;
            public int Depth;
            public BranchInfo(float x, float y, float theta, float length, int depth)
            {
                X = x;
                Y = y;
                Theta = theta;
                Length = length;
                Depth = depth;
            }
        }

        // Draw a binary tree.
        private void DrawTree(Graphics gr, Pen pen,
            int max_depth, float x, float y, float max_length,
            float initial_theta, float length_scale, float dtheta)
        {
            // Add the trunk to a queue.
            Queue<BranchInfo> branches = new Queue<BranchInfo>();
            branches.Enqueue(new BranchInfo(x, y, initial_theta, max_length, max_depth));

            // Process branches until the queue is empty.
            while (branches.Count > 0)
            {
                // Draw the next branch.
                BranchInfo branch = branches.Dequeue();

                // Set the pen's color depending on the depth.
                if (branch.Depth == 1) pen.Color = Color.Red;
                else
                {
                    int g = 255 * (max_depth - branch.Depth) / max_depth;
                    int r = 139 * (branch.Depth - 3) / max_depth;
                    if (r < 0) r = 0;
                    int b = 0;
                    pen.Color = Color.FromArgb(r, g, b);
                }

                // Set the pen's thickness depending on the depth.
                int thickness = 10 * branch.Depth / max_depth;
                if (thickness < 0) thickness = 0;
                pen.Width = thickness;

                // See where this branch should end.
                float x1 = (float)(branch.X + branch.Length * Math.Cos(branch.Theta));
                float y1 = (float)(branch.Y + branch.Length * Math.Sin(branch.Theta));

                // Draw the branch.
                gr.DrawLine(pen, branch.X, branch.Y, x1, y1);

                // If branch.depth > 1, add child branches to the queue.
                if (branch.Depth > 1)
                {
                    branches.Enqueue(new BranchInfo(x1, y1,
                        branch.Theta + dtheta, branch.Length * length_scale, branch.Depth - 1));
                    branches.Enqueue(new BranchInfo(x1, y1,
                        branch.Theta - dtheta, branch.Length * length_scale, branch.Depth - 1));
                }
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
                    DrawTree(e.Graphics, the_pen,
                        (int)nudDepth.Value, root_x, root_y,
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
