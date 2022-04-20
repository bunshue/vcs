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
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

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
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H - 50);
            pictureBox5.Size = new Size(W, H - 50);
            pictureBox6.Size = new Size(W, H - 100);
            pictureBox7.Size = new Size(W, H - 100);
            pictureBox0.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox3.BorderStyle = BorderStyle.Fixed3D;
            pictureBox4.BorderStyle = BorderStyle.Fixed3D;
            pictureBox5.BorderStyle = BorderStyle.Fixed3D;
            pictureBox6.BorderStyle = BorderStyle.Fixed3D;
            pictureBox7.BorderStyle = BorderStyle.Fixed3D;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 1 - 120);
            //groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1 - 80);
            //groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 80);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 1 - 80);

            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 2 - 120);
            //groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 2 - 120);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 2 - 160);

            //ClientSize = new Size(bt_exit.Right + 10, richTextBox1.Bottom + 80);    //自動表單邊界

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }


        #region queue_breadth_first_tree
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
        #endregion queue_breadth_first_tree


    }
}

