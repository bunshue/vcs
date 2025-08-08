using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
    
namespace howto_breadth_first_tree
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
            public float X, Y, Theta;
            public BranchInfo(float x, float y, float theta)
            {
                X = x;
                Y = y;
                Theta = theta;
            }
        }

        // Draw a binary tree.
        private void DrawBranch(Graphics gr, Pen pen, int depth, int max_depth, float x, float y,
            float length, float theta, float length_scale, float dtheta)
        {
            // Add the first branch to a stack.
            Stack<BranchInfo> branches = new Stack<BranchInfo>();
            branches.Push(new BranchInfo(x, y, theta));

            // Process the branches until we reach the desired depth.
            while (depth > 0)
            {
                // Make a stack for new branches.
                Stack<BranchInfo> new_branches = new Stack<BranchInfo>();

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

                // Process all of the branches in the branches stack.
                while (branches.Count > 0)
                {
                    // Get the next branch.
                    BranchInfo branch = branches.Pop();

                    // See where this branch should end.
                    float x1 = (float)(branch.X + length * Math.Cos(branch.Theta));
                    float y1 = (float)(branch.Y + length * Math.Sin(branch.Theta));

                    // Draw the branch.
                    gr.DrawLine(pen, branch.X, branch.Y, x1, y1);

                    // If depth > 1, add the attached
                    // branches to the new_branches stack.
                    if (depth > 1)
                    {
                        new_branches.Push(new BranchInfo(x1, y1, branch.Theta + dtheta));
                        new_branches.Push(new BranchInfo(x1, y1, branch.Theta - dtheta));
                    }
                }

                // Decrement depth so we know how deep
                // into the tree we still need to go.
                depth--;

                // Set the length for the next level of branches.
                length = length * length_scale;

                // Prepare to process the next level of branches.
                branches = new_branches;
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
