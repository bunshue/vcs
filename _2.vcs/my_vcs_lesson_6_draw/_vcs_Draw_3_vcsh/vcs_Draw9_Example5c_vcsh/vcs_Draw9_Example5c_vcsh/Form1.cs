using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

namespace vcs_Draw9_Example5c_vcsh
{
    public partial class Form1 : Form
    {
        int W = 450;
        int H = 450;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            x_st = 10;
            y_st = 35;
            dx = W + 30;
            dy = H + 80;
            pictureBox0.Size = new Size(W, H - 50);
            pictureBox1.Size = new Size(W, H - 50);
            pictureBox0.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 120);
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        //------------------------------------------------------------  # 60個

        //#region queue_breadth_first_tree
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
        private void DrawTree(Graphics gr, Pen pen, int max_depth, float x, float y, float max_length, float initial_theta, float length_scale, float dtheta)
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
                if (branch.Depth == 1)
                {
                    pen.Color = Color.Red;
                }
                else
                {
                    int g = 255 * (max_depth - branch.Depth) / max_depth;
                    int r = 139 * (branch.Depth - 3) / max_depth;
                    if (r < 0)
                    {
                        r = 0;
                    }
                    int b = 0;
                    pen.Color = Color.FromArgb(r, g, b);
                }

                // Set the pen's thickness depending on the depth.
                int thickness = 10 * branch.Depth / max_depth;
                if (thickness < 0)
                {
                    thickness = 0;
                }
                pen.Width = thickness;

                // See where this branch should end.
                float x1 = (float)(branch.X + branch.Length * Math.Cos(branch.Theta));
                float y1 = (float)(branch.Y + branch.Length * Math.Sin(branch.Theta));

                // Draw the branch.
                gr.DrawLine(pen, branch.X, branch.Y, x1, y1);

                // If branch.depth > 1, add child branches to the queue.
                if (branch.Depth > 1)
                {
                    branches.Enqueue(new BranchInfo(x1, y1, branch.Theta + dtheta, branch.Length * length_scale, branch.Depth - 1));
                    branches.Enqueue(new BranchInfo(x1, y1, branch.Theta - dtheta, branch.Length * length_scale, branch.Depth - 1));
                }
            }
        }

        // Draw the tree.
        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox0.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            try
            {
                float root_x = pictureBox0.ClientSize.Width / 2;
                float root_y = pictureBox0.ClientSize.Height - 4;
                float length_scale = float.Parse(txtLengthScale.Text);
                float dtheta = (float)(Math.PI / 180.0 * (double)nudDtheta.Value);
                using (Pen the_pen = new Pen(Color.Black))
                {
                    DrawTree(e.Graphics, the_pen, (int)nudDepth.Value, root_x, root_y, (int)nudLength.Value, (float)(-Math.PI / 2), length_scale, dtheta);
                }
            }
            catch
            {
            }
        }

        // Recursively draw a binary tree branch.
        private void DrawBranch(Graphics gr, Pen pen, int depth, int max_depth, float x, float y,
            float length, float theta, float length_scale, float dtheta)
        {
            // See where this branch should end.
            float x1 = (float)(x + length * Math.Cos(theta));
            float y1 = (float)(y + length * Math.Sin(theta));

            // Set the pen's color depending on the depth.
            if (depth == 1)
            {
                pen.Color = Color.Red;
            }
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
            if (thickness < 0)
            {
                thickness = 0;
            }
            pen.Width = thickness;

            // Draw the branch.
            gr.DrawLine(pen, x, y, x1, y1);

            // If depth > 1, draw the attached branches.
            if (depth > 1)
            {
                DrawBranch(gr, pen, depth - 1, max_depth, x1, y1, length * length_scale, theta + dtheta, length_scale, dtheta);
                DrawBranch(gr, pen, depth - 1, max_depth, x1, y1, length * length_scale, theta - dtheta, length_scale, dtheta);
            }
        }

        // Draw the tree.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox1.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            try
            {
                float root_x = pictureBox1.ClientSize.Width / 2;
                float root_y = pictureBox1.ClientSize.Height - 4;
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

        private void pictureBox0_Resize(object sender, EventArgs e)
        {
            // Redraw.
            pictureBox0.Refresh();
        }

        private void pictureBox1_Resize(object sender, EventArgs e)
        {
            // Redraw.
            pictureBox1.Refresh();
        }

        private void parameter_ValueChanged(object sender, EventArgs e)
        {
            // Redraw.
            pictureBox0.Refresh();
            pictureBox1.Refresh();
        }

        private void nud_KeyUp(object sender, KeyEventArgs e)
        {
            // Redraw.
            pictureBox0.Refresh();
            pictureBox1.Refresh();
        }
        //#endregion queue_breadth_first_tree
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

