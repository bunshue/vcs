#define FIG1
//#define FIG34

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

using System.Drawing.Imaging;   //for ImageFormat

using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw9_Example7_vcsh
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        //for sierpinski1 ST
        // Corner information.
        List<PointF> Corners;

        // The most recent point.
        PointF LastPoint;
        //for sierpinski1 SP

        // Sierpinski 2 & 3
        // The root of the Pentagon object hierarchy.
        private Pentagon Root5 = null;
        // The root of the Octagon object hierarchy.
        private Octagon Root8 = null;

        int W = 230;
        int H = 230;

        int fractal_num_points = 5000;

        float rotating_angle = 0;

        private int NumPoints_ngon_stars = 3;


        //畫 pickover_popcorn ST
        // The bitmap.
        private Bitmap bitmap_pickover1;    //單色
        private Bitmap bitmap_pickover2;    //彩色

        // Parameters;
        private float HH = 0.05f;
        private int IterationsPerPixel = 20;
        private int dx = 5;

        // Red, green, or blue?
        private const int RgbRed = 0;
        private const int RgbGreen = 1;
        private const int RgbBlue = 2;
        private int RgbType = RgbRed;
        //畫 pickover_popcorn SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //for sierpinski1 ST
            DefineCorners();
            //for sierpinski1 SP

            redraw_all();

            lblStatus.Text = "";

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
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

            //button
            x_st = 1800;
            y_st = 40;
            dx = 110;
            dy = 38;

            label1.Location = new Point(x_st + dx * 0 + 55, y_st + dy * 0 + 20);
            numericUpDown1.Location = new Point(x_st + dx * 0 + 55, y_st + dy * 0 + 50);
            numericUpDown1.Value = 0;

            bt_save.Location = new Point(x_st + dx * 0 + 55, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            richTextBox1.Size = new Size(richTextBox1.Size.Width - 70, this.Height - richTextBox1.Size.Height - 20);

            pictureBox_sierpinski1.Size = new Size(W, H);
            pictureBox_sierpinski2.Size = new Size(W, H);
            pictureBox_sierpinski3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox_skyline.Size = new Size(W, H * 4 / 5);
            pictureBox_ngon_stars.Size = new Size(W, H);
            pictureBox_dragon.Size = new Size(W, H);
            pictureBox_dragon4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox13.BackColor = Color.LightSalmon;
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox_snowflake.Size = new Size(W, H);
            pictureBox_snowflake2.Size = new Size(W, H);
            pictureBox_fractal1.Size = new Size(W, H);
            pictureBox_fractal2.Size = new Size(W, H);
            pictureBox_pickover_popcorn1.Size = new Size(W, H);
            pictureBox_pickover_popcorn2.Size = new Size(W, H);
            pictureBox22.Size = new Size(W, H);

            pictureBox_sierpinski1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_sierpinski2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_sierpinski3.BorderStyle = BorderStyle.Fixed3D;
            pictureBox4.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_skyline.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_ngon_stars.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_dragon.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_dragon4.BorderStyle = BorderStyle.Fixed3D;
            pictureBox5.BorderStyle = BorderStyle.Fixed3D;
            pictureBox12.BorderStyle = BorderStyle.Fixed3D;
            pictureBox13.BorderStyle = BorderStyle.Fixed3D;
            pictureBox13.BackColor = Color.LightSalmon;
            pictureBox14.BorderStyle = BorderStyle.Fixed3D;
            pictureBox15.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_snowflake.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_snowflake2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_fractal1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_fractal2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_pickover_popcorn1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox_pickover_popcorn2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox22.BorderStyle = BorderStyle.Fixed3D;

            x_st = 10;
            y_st = 10;
            dx = W + 70;
            dy = H + 45;

            pictureBox_sierpinski1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_sierpinski2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox_sierpinski3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_snowflake.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_snowflake2.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            pictureBox_skyline.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox_ngon_stars.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox_dragon.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox_dragon4.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            pictureBox12.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            richTextBox_ransom_note.Size = new Size(W, H + 40);
            richTextBox_ransom_note_result.Size = new Size(W, H + 40);
            pictureBox_ransom_note.Size = new Size(W, H + 40);

            pictureBox13.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            groupBox1.Location = new Point(x_st + dx * 2+40, y_st + dy * 3 - 45);
            richTextBox_ransom_note.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox_ransom_note.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            richTextBox_ransom_note_result.Location = new Point(x_st + dx * 5, y_st + dy * 2);

            pictureBox_fractal1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            pictureBox_fractal2.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            groupBox2.Location = new Point(x_st + dx * 2 - 30, y_st + dy * 3);

            picSamples.Location = new Point(x_st + dx * 2 - 30, y_st + dy * 3 + 102);

            pictureBox22.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            pictureBox_pickover_popcorn1.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            pictureBox_pickover_popcorn2.Location = new Point(x_st + dx * 5, y_st + dy * 3);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

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

        // Define the corners.
        private void DefineCorners()
        {
            int W = this.pictureBox_sierpinski1.ClientSize.Width;
            int H = this.pictureBox_sierpinski1.ClientSize.Height;

            // Initialize the corners.
            Corners = new List<PointF>();
            Corners.Add(new PointF(W / 2, 10));
            Corners.Add(new PointF(10, H - 10));
            Corners.Add(new PointF(W - 10, H - 10));

            // Start at the first point.
            LastPoint = Corners[0];
        }

        // Make the Pentagon objects and redraw.
        private void MakePentagons()
        {
            // Build the Root.
            int depth = (int)numericUpDown1.Value;
            PointF center = new PointF(
                pictureBox5.ClientSize.Width / 2,
                pictureBox5.ClientSize.Height / 2);
            float radius = (float)Math.Min(center.X, center.Y);
            Root5 = MakePentagon(depth, center, radius);

            // Redraw.
            pictureBox5.Refresh();
        }

        // Scale factor for moving to smaller pentagons.
        private float size_scale5 = (float)(1.0 / (2.0 * (1 + Math.Cos(Math.PI / 180 * 72))));

        // Recursively generate a Pentagon and its descendants.
        private Pentagon MakePentagon(int depth, PointF center, float radius)
        {
            // Make the Pentagon.
            Pentagon parent = new Pentagon(GetPentagonPoints(center, radius));

            // If we are not done recursing, make children.
            if (depth > 0)
            {
                // Find the smaller pentagons' centers.
                float d = radius - radius * size_scale5;
                PointF[] centers = GetPentagonPoints(center, d);

                // Recursively draw the smaller pentagons.
                foreach (PointF point in centers)
                {
                    parent.Children.Add(MakePentagon(
                        depth - 1, point, radius * size_scale5));
                }
            }

            return parent;
        }

        // Find the pentagon's corners.
        private PointF[] GetPentagonPoints(PointF center, float radius)
        {
            PointF[] points = new PointF[5];
            double theta = -Math.PI / 2.0;
            double dtheta = 2.0 * Math.PI / 5.0;
            for (int i = 0; i < 5; i++)
            {
                points[i] = new PointF(
                    center.X + (float)(radius * Math.Cos(theta)),
                    center.Y + (float)(radius * Math.Sin(theta)));
                theta += dtheta;
            }
            return points;
        }

                // Make the Octagon objects and redraw.
        private void MakeOctagons()
        {
            // Build the Root.
            int depth = (int)numericUpDown1.Value;

            PointF center = new PointF(
                pictureBox12.ClientSize.Width / 2,
                pictureBox12.ClientSize.Height / 2);
            float radius = (float)Math.Min(center.X, center.Y);
            radius -= 5;
            Root8 = MakeOctagon(depth, center, radius);

            // Redraw.
            pictureBox12.Refresh();
        }

        // Scale factor for moving to smaller octagons.
        private float size_scale8 = (float)(1.0 / (2.0 * (1 + Math.Cos(Math.PI / 180 * 45))));

        // Recursively generate a Octagon and its descendants.
        private Octagon MakeOctagon(int depth, PointF center, float radius)
        {
            // Make the Octagon.
            Octagon parent = new Octagon(GetOctagonPoints(center, radius));

            // If we are not done recursing, make children.
            if (depth > 0)
            {
                // Find the smaller octagons' centers.
                float d = radius - radius * size_scale8;
                PointF[] centers = GetOctagonPoints(center, d);

                // Recursively draw the smaller octagons.
                foreach (PointF point in centers)
                {
                    parent.Children.Add(MakeOctagon(
                        depth - 1, point, radius * size_scale8));
                }
            }

            return parent;
        }

        // Find the octagon's corners.
        private PointF[] GetOctagonPoints(PointF center, float radius)
        {
            PointF[] points = new PointF[8];
            double theta = -Math.PI / 2.0;
            double dtheta = 2.0 * Math.PI / 8.0;
            for (int i = 0; i < 8; i++)
            {
                points[i] = new PointF(
                    center.X + (float)(radius * Math.Cos(theta)),
                    center.Y + (float)(radius * Math.Sin(theta)));
                theta += dtheta;
            }
            return points;
        }

        // Coordinates of the points in the initiator.
        private List<PointF> Initiator;

        // Angles and distances for the generator.
        private float ScaleFactor;
        private List<float> GeneratorDTheta;

        /*
        // Coordinates of the points in the initiator.
        private List<PointF> Initiator;

        // Angles and distances for the generator.
        private float ScaleFactor;
        private List<float> GeneratorDTheta;
        */

        void Draw_SnowFlake1()
        {
            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // Define an initiator and generator.
            Initiator = new List<PointF>();
            float sqrt_3 = (float)Math.Sqrt(3.0);
            float side1 = (pictureBox_snowflake.ClientSize.Height - 10f) / 2f;
            float side2 = (pictureBox_snowflake.ClientSize.Width - 10f) / 2f / sqrt_3 * 2f;
            float side = Math.Min(side1, side2);
            float height = side * sqrt_3 / 2f;
            float y1 = (pictureBox_snowflake.ClientSize.Height - 2 * side) / 2;
            float y2 = y1 + side / 2;
            float y3 = y2 + side;
            float y4 = y1 + 2 * side;
            float x1 = (pictureBox_snowflake.ClientSize.Width - 2 * height) / 2;
            float x2 = x1 + height;
            float x3 = x2 + height;
            Initiator.Add(new PointF(x1, y2));
            Initiator.Add(new PointF(x2, y1));
            Initiator.Add(new PointF(x3, y2));
            Initiator.Add(new PointF(x3, y3));
            Initiator.Add(new PointF(x2, y4));
            Initiator.Add(new PointF(x1, y3));
            Initiator.Add(new PointF(x1, y2));

            //// Initiator for drawing a single generator.
            //Initiator = new List<PointF>();
            //Initiator.Add(new PointF(5, pictureBox_snowflake.ClientSize.Height / 3));
            //Initiator.Add(new PointF(
            //    pictureBox_snowflake.ClientSize.Width - 5,
            //    pictureBox_snowflake.ClientSize.Height / 3));

            ScaleFactor = (float)(1.0 / 3.0);

            GeneratorDTheta = new List<float>();
            float pi_over_3 = (float)(Math.PI / 3f);
            GeneratorDTheta.Add(0);
            GeneratorDTheta.Add(pi_over_3);
            GeneratorDTheta.Add(pi_over_3);
            GeneratorDTheta.Add(-2 * pi_over_3);
            GeneratorDTheta.Add(-pi_over_3);
            GeneratorDTheta.Add(-pi_over_3);
            GeneratorDTheta.Add(2 * pi_over_3);

            // Get the parameters.
            int depth = (int)numericUpDown1.Value;
            Bitmap bm = new Bitmap(
                pictureBox_snowflake.ClientSize.Width,
                pictureBox_snowflake.ClientSize.Height);
            pictureBox_snowflake.Image = bm;

            // Draw the snowflake.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                DrawSnowflake(gr, depth);
            }

            this.Cursor = Cursors.Default;

        }

        // Draw the complete snowflake.
        private void DrawSnowflake(Graphics gr, int depth)
        {
            gr.Clear(pictureBox_snowflake.BackColor);

            // Draw the snowflake.
            for (int i = 1; i < Initiator.Count; i++)
            {
                PointF p1 = Initiator[i - 1];
                PointF p2 = Initiator[i];

                float dx = p2.X - p1.X;
                float dy = p2.Y - p1.Y;
                float length = (float)Math.Sqrt(dx * dx + dy * dy);
                float theta = (float)Math.Atan2(dy, dx);
                DrawSnowflakeEdge(gr, depth, ref p1, theta, length);
            }
        }

        // Recursively draw a snowflake edge starting at
        // (x1, y1) in direction theta and distance dist.
        // Leave the coordinates of the endpoint in
        // (x1, y1).
        private void DrawSnowflakeEdge(Graphics gr, int depth, ref PointF p1, float theta, float dist)
        {
            if (depth == 0)
            {
                PointF p2 = new PointF(
                    (float)(p1.X + dist * Math.Cos(theta)),
                    (float)(p1.Y + dist * Math.Sin(theta)));
                gr.DrawLine(Pens.Blue, p1, p2);
                p1 = p2;
                return;
            }

            // Recursively draw the edge.
            dist *= ScaleFactor;
            for (int i = 0; i < GeneratorDTheta.Count; i++)
            {
                theta += GeneratorDTheta[i];
                DrawSnowflakeEdge(gr, depth - 1, ref p1, theta, dist);
            }
        }

        void Draw_SnowFlake2()
        {
            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // Define an initiator and generator.
            Initiator = new List<PointF>();
            float height = 0.75f * (Math.Min(
                pictureBox_snowflake2.ClientSize.Width,
                pictureBox_snowflake2.ClientSize.Height) - 20);
            float width = (float)(height / Math.Sqrt(3.0) * 2);
            float y3 = pictureBox_snowflake2.ClientSize.Height - 10;
            float y1 = y3 - height;
            float x3 = pictureBox_snowflake2.ClientSize.Height / 2;
            float x1 = x3 - width / 2;
            float x2 = x1 + width;
            Initiator.Add(new PointF(x1, y1));
            Initiator.Add(new PointF(x2, y1));
            Initiator.Add(new PointF(x3, y3));
            Initiator.Add(new PointF(x1, y1));

            ScaleFactor = 1 / 3f;                   // Make subsegments 1/3 size.

            GeneratorDTheta = new List<float>();
            float pi_over_3 = (float)(Math.PI / 3f);
            GeneratorDTheta.Add(0);                 // Draw in the original direction.
            GeneratorDTheta.Add(-pi_over_3);        // Turn -60 degrees.
            GeneratorDTheta.Add(2 * pi_over_3);     // Turn 120 degrees.
            GeneratorDTheta.Add(-pi_over_3);        // Turn -60 degrees.

            // Get the parameters.
            int depth = (int)numericUpDown1.Value;

            Bitmap bm = new Bitmap(pictureBox_snowflake2.ClientSize.Width, pictureBox_snowflake2.ClientSize.Height);
            pictureBox_snowflake2.Image = bm;

            // Draw the snowflake.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                DrawSnowflake2(gr, depth);
            }

            this.Cursor = Cursors.Default;


        }

        // Draw the complete snowflake.
        private void DrawSnowflake2(Graphics gr, int depth)
        {
            gr.Clear(pictureBox_snowflake2.BackColor);

            // Draw the snowflake.
            for (int i = 1; i < Initiator.Count; i++)
            {
                PointF p1 = Initiator[i - 1];
                PointF p2 = Initiator[i];

                float dx = p2.X - p1.X;
                float dy = p2.Y - p1.Y;
                float length = (float)Math.Sqrt(dx * dx + dy * dy);
                float theta = (float)Math.Atan2(dy, dx);
                DrawSnowflakeEdge2(gr, depth, ref p1, theta, length);
            }
        }

        // Recursively draw a snowflake edge starting at
        // (x1, y1) in direction theta and distance dist.
        // Leave the coordinates of the endpoint in
        // (x1, y1).
        private void DrawSnowflakeEdge2(Graphics gr, int depth, ref PointF p1, float theta, float dist)
        {
            if (depth == 0)
            {
                PointF p2 = new PointF(
                    (float)(p1.X + dist * Math.Cos(theta)),
                    (float)(p1.Y + dist * Math.Sin(theta)));
                gr.DrawLine(Pens.Blue, p1, p2);
                p1 = p2;
                return;
            }

            // Recursively draw the edge.
            dist *= ScaleFactor;
            for (int i = 0; i < GeneratorDTheta.Count; i++)
            {
                theta += GeneratorDTheta[i];
                DrawSnowflakeEdge2(gr, depth - 1, ref p1, theta, dist);
            }
        }

        void Draw_SnowFlake3()
        {
            // Define an initiator and generator.
            Initiator = new List<PointF>();
            float height = Math.Min(
                pictureBox4.ClientSize.Width,
                pictureBox4.ClientSize.Height) - 100;
            float x1 = (pictureBox4.ClientSize.Width - height) / 2;
            float x2 = x1 + height;
            float y1 = (pictureBox4.ClientSize.Height - height) / 2;
            float y2 = y1 + height;
            Initiator.Add(new PointF(x1, y1));
            Initiator.Add(new PointF(x2, y1));
            Initiator.Add(new PointF(x2, y2));
            Initiator.Add(new PointF(x1, y2));
            Initiator.Add(new PointF(x1, y1));

            ScaleFactor = (float)(1.0 / Math.Sqrt(5.0));

            GeneratorDTheta = new List<float>();
            GeneratorDTheta.Add((float)-Math.Atan(1.0 / 2.0));
            float pi_over_2 = (float)(Math.PI / 2);
            GeneratorDTheta.Add(pi_over_2);
            GeneratorDTheta.Add(-pi_over_2);

            // Get the parameters.
            int depth = (int)numericUpDown1.Value;

            Bitmap bm = new Bitmap(pictureBox4.ClientSize.Width, pictureBox4.ClientSize.Height);
            pictureBox4.Image = bm;

            // Draw the snowflake.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                DrawSnowflake3(gr, depth);
            }
        }

        // Draw the complete snowflake.
        private void DrawSnowflake3(Graphics gr, int depth)
        {
            gr.Clear(pictureBox4.BackColor);

            // Draw the snowflake.
            for (int i = 1; i < Initiator.Count; i++)
            {
                PointF p1 = Initiator[i - 1];
                PointF p2 = Initiator[i];

                float dx = p2.X - p1.X;
                float dy = p2.Y - p1.Y;
                float length = (float)Math.Sqrt(dx * dx + dy * dy);
                float theta = (float)Math.Atan2(dy, dx);
                DrawSnowflakeEdge3(gr, depth, ref p1, theta, length);
            }
        }

        // Recursively draw a snowflake edge starting at
        // (x1, y1) in direction theta and distance dist.
        // Leave the coordinates of the endpoint in
        // (x1, y1).
        private void DrawSnowflakeEdge3(Graphics gr, int depth, ref PointF p1, float theta, float dist)
        {
            if (depth == 0)
            {
                PointF p2 = new PointF(
                    (float)(p1.X + dist * Math.Cos(theta)),
                    (float)(p1.Y + dist * Math.Sin(theta)));
                gr.DrawLine(Pens.Blue, p1, p2);
                p1 = p2;
                return;
            }

            // Recursively draw the edge.
            dist *= ScaleFactor;
            for (int i = 0; i < GeneratorDTheta.Count; i++)
            {
                theta += GeneratorDTheta[i];
                DrawSnowflakeEdge3(gr, depth - 1, ref p1, theta, dist);
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            richTextBox1.Clear();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        // Font names we may use.
        private string[] FontNames =
        {
            "Times New Roman",
            "Courier New",
            "Comic Sans MS",
            "Arial",
            "News Gothic MT",
            "AvantGarde Md BT",
            //"Benguiat Bk BT",
            "Bookman Old Style",
            "Bremen Bd BT",
            "Century Gothic",
            "Dauphin",
            "Curlz MT",
            "GoudyHandtooled BT",
        };

        // Colors we may use.
        private Brush[] FontBrushes =
        {
            Brushes.Red,
            Brushes.Green,
            Brushes.Blue,
            Brushes.Orange,
            Brushes.Brown,
            Brushes.Magenta,
            Brushes.Purple,
            Brushes.BurlyWood,
            Brushes.HotPink,
        };

        // Colors we may use.
        private Color[] FontColors =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Orange,
            Color.Brown,
            Color.Magenta,
            Color.Purple,
            Color.BurlyWood,
            Color.HotPink,
        };

        // The random number generator we will use.
        private Random Rand = new Random();

        private void richTextBox_ransom_note_TextChanged(object sender, EventArgs e)
        {
            DrawRansomNoteText();
            DrawRansomNoteText2();
        }

        // Draw the text in the PictureBox.
        private void DrawRansomNoteText()
        {
            if (pictureBox_ransom_note.Image != null) pictureBox_ransom_note.Image.Dispose();
            Bitmap bm = new Bitmap(pictureBox_ransom_note.Width, pictureBox_ransom_note.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.TextRenderingHint = TextRenderingHint.AntiAlias;
                gr.PageUnit = GraphicsUnit.Pixel;

                float x = 0;
                float y = 0;
                float max_y = 0;
                foreach (char ch in richTextBox_ransom_note.Text)
                {
                    DrawCharacter(gr, bm.Width - 10, ref x, ref y, ref max_y, ch);
                }
            }

            // Display the result.
            pictureBox_ransom_note.Image = bm;
        }

        // Draw a character in a random font.
        private void DrawCharacter(Graphics gr, int right_margin, ref float x, ref float y, ref float max_y, char ch)
        {
            const float min_size = 25;
            const float max_size = 35;

            // Pick the random font characteristics.
            string font_name = FontNames[Rand.Next(0, FontNames.Length)];
            float font_size = (float)(min_size + Rand.NextDouble() * (max_size - min_size));
            FontStyle font_style = FontStyle.Regular;
            if (Rand.Next(0, 2) == 1) font_style |= FontStyle.Bold;
            if (Rand.Next(0, 2) == 1) font_style |= FontStyle.Italic;
            //if (Rand.Next(0,2) == 1) font_style |= FontStyle.Strikeout;
            //if (Rand.Next(0,2) == 1) font_style |= FontStyle.Underline;
            Brush brush = FontBrushes[Rand.Next(0, FontBrushes.Length)];

            // Draw the character.
            using (Font font = new Font(font_name, font_size, font_style))
            {
                // Measure the character.
                string text = "M" + ch + "M";
                SizeF size = gr.MeasureString(text, font);
                SizeF x_size = gr.MeasureString("MM", font);
                size.Width = size.Width - x_size.Width + 5;

                // See if we have room.
                if (x + size.Width * 0.75f > right_margin)
                {
                    // Start a new line.
                    x = 0;
                    y = max_y;
                }

                // Draw the character.
                gr.DrawString(ch.ToString(), font, brush, x, y);

                // Set the position for the next character.
                x += size.Width * 0.75f;
                if (max_y < y + size.Height) max_y = y + size.Height;
            }
        }


        // Draw the text in the RichTextBox.
        private void DrawRansomNoteText2()
        {
            richTextBox_ransom_note_result.Text = "";
            richTextBox_ransom_note_result.Text = "";
            foreach (char ch in richTextBox_ransom_note.Text)
            {
                DrawCharacter(ch);
            }
        }

        // Draw a character in a random font.
        private void DrawCharacter(char ch)
        {
            const float min_size = 25;
            const float max_size = 35;

            // Pick the random font characteristics.
            string font_name = FontNames[Rand.Next(0, FontNames.Length)];
            float font_size = (float)(min_size + Rand.NextDouble() * (max_size - min_size));
            FontStyle font_style = FontStyle.Regular;
            if (Rand.Next(0, 2) == 1) font_style |= FontStyle.Bold;
            if (Rand.Next(0, 2) == 1) font_style |= FontStyle.Italic;
            //if (Rand.Next(0,2) == 1) font_style |= FontStyle.Strikeout;
            //if (Rand.Next(0,2) == 1) font_style |= FontStyle.Underline;

            richTextBox_ransom_note_result.SelectionFont = new Font(font_name, font_size, font_style);
            richTextBox_ransom_note_result.SelectionColor = FontColors[Rand.Next(0, FontColors.Length)];
            richTextBox_ransom_note_result.AppendText(ch.ToString());
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox5.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            if (Root5 == null) return;

            Root5.Draw(e.Graphics);
        }

        private void pictureBox12_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox12.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            if (Root8 == null) return;

            Root8.Draw(e.Graphics);
        }

        // http://en.wikipedia.org/wiki/Dragon_curve
        // http://en.wikipedia.org/wiki/Heighway_dragon
        // http://ecademy.agnesscott.edu/~lriddle/ifs/heighway/heighway.htm

        // The direction the curve should turn next.
        private enum Direction
        {
            Left,
            Right
        }

        // Draw the dragon.
        private void pictureBox_dragon_Paint(object sender, PaintEventArgs e)
        {
            MakeDragonImage(e);
        }

        void MakeDragonImage(PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox_dragon.BackColor);

            // Find the first control points.
            const int margin = 5;
            float dx = Math.Min((pictureBox_dragon.ClientSize.Width - 2 * margin) / 1.5f, (pictureBox_dragon.ClientSize.Height - 2 * margin));

            // Center it.
            float x0 = (pictureBox_dragon.ClientSize.Width - dx * 1.5f) / 2f + dx / 3f;
            float y0 = (pictureBox_dragon.ClientSize.Height - dx) / 2f + dx / 3f;

            // Recursively draw the lines.
            int depth = (int)numericUpDown1.Value;
            DrawDragonLine(e.Graphics, depth, Direction.Right, x0, y0, dx, 0);

            // Draw a box around it and some other lines to show size.
            e.Graphics.DrawRectangle(Pens.Green, x0 - dx / 3, y0 - dx / 3, 1.5f * dx, dx);
            e.Graphics.DrawLine(Pens.Blue, x0, y0, x0 + dx, y0 + 0);
            e.Graphics.FillEllipse(Brushes.Blue, x0 - 2, y0 - 2, 5, 5);
        }

        // Recursively draw the dragon curve between the two points.
        private void DrawDragonLine(Graphics gr, int level, Direction turn_towards, float x1, float y1, float dx, float dy)
        {
            if (level <= 0)
            {
                gr.DrawLine(Pens.Red, x1, y1, x1 + dx, y1 + dy);

#if DRAW_POINTS
                gr.DrawEllipse(Pens.Blue, x1 - 2, y1 - 2, 4, 4);
                gr.DrawEllipse(Pens.Blue, x1 + dx - 2, y1 + dy - 2, 4, 4);
#endif
            }
            else
            {
#if DRAW_LEVEL_MINUS_1
                if (level == 1)
                {
                    gr.DrawLine(Pens.Silver, x1, y1, x1 + dx, y1 + dy);
                }
#endif
                float nx = (float)(dx / 2);
                float ny = (float)(dy / 2);
                float dx2 = -ny + nx;
                float dy2 = nx + ny;
                if (turn_towards == Direction.Right)
                {
                    // Turn to the right.
                    DrawDragonLine(gr, level - 1, Direction.Right, x1, y1, dx2, dy2);
                    float x2 = x1 + dx2;
                    float y2 = y1 + dy2;
                    DrawDragonLine(gr, level - 1, Direction.Left, x2, y2, dy2, -dx2);
                }
                else
                {
                    // Turn to the left.
                    DrawDragonLine(gr, level - 1, Direction.Right, x1, y1, dy2, -dx2);
                    float x2 = x1 + dy2;
                    float y2 = y1 - dx2;
                    DrawDragonLine(gr, level - 1, Direction.Left, x2, y2, dx2, dy2);
                }
            }
        }

        private void pictureBox_dragon4_Paint(object sender, PaintEventArgs e)
        {
            //MakeDragon4Image(e);
        }

        // Select the clicked color as the one to draw last.
        private Color DrawLastColor = Color.Black;

        // Draw the dragon.
        void MakeDragon4Image()
        {
            Bitmap bm = new Bitmap(pictureBox_dragon4.ClientSize.Width, pictureBox_dragon4.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(pictureBox_dragon4.BackColor);

                // Find the first control point.
                const int margin = 5;
                float dx = Math.Min(
                    (pictureBox_dragon4.ClientSize.Width - 2 * margin) / (14 / 6f),
                    (pictureBox_dragon4.ClientSize.Height - 2 * margin) / (14 / 6f));

                // Center it.
                float x0 = pictureBox_dragon4.ClientSize.Width / 2;
                float y0 = pictureBox_dragon4.ClientSize.Height / 2;

                // Recursively draw the lines.
                //int level = (int)nudLevel.Value;
                int level = (int)numericUpDown1.Value;
                if (DrawLastColor != Color.Red)
                    DrawDragonLine(gr, Pens.Red, level, Direction.Right, x0, y0, dx, 0);
                if (DrawLastColor != Color.Green)
                    DrawDragonLine(gr, Pens.Green, level, Direction.Right, x0, y0, 0, dx);
                if (DrawLastColor != Color.Blue)
                    DrawDragonLine(gr, Pens.Blue, level, Direction.Right, x0, y0, -dx, 0);
                if (DrawLastColor != Color.Black)
                    DrawDragonLine(gr, Pens.Black, level, Direction.Right, x0, y0, 0, -dx);

                // Redraw the one we should draw last.
                if (DrawLastColor == Color.Red)
                    DrawDragonLine(gr, Pens.Red, level, Direction.Right, x0, y0, dx, 0);
                else if (DrawLastColor == Color.Green)
                    DrawDragonLine(gr, Pens.Green, level, Direction.Right, x0, y0, 0, dx);
                else if (DrawLastColor == Color.Blue)
                    DrawDragonLine(gr, Pens.Blue, level, Direction.Right, x0, y0, -dx, 0);
                else if (DrawLastColor == Color.Black)
                    DrawDragonLine(gr, Pens.Black, level, Direction.Right, x0, y0, 0, -dx);
            }

            // Display the result.
            pictureBox_dragon4.Image = bm;

        }

        // Recursively draw the dragon curve between the two points.
        private void DrawDragonLine(Graphics gr, Pen pen, int level, Direction turn_towards, float x1, float y1, float dx, float dy)
        {
            if (level <= 0)
            {
                gr.DrawLine(pen, x1, y1, x1 + dx, y1 + dy);

#if DRAW_POINTS
                gr.DrawEllipse(Pens.Blue, x1 - 2, y1 - 2, 4, 4);
                gr.DrawEllipse(Pens.Blue, x1 + dx - 2, y1 + dy - 2, 4, 4);
#endif
            }
            else
            {
#if DRAW_LEVEL_MINUS_1
                if (level == 1)
                {
                    gr.DrawLine(Pens.Silver, x1, y1, x1 + dx, y1 + dy);
                }
#endif
                float nx = (float)(dx / 2);
                float ny = (float)(dy / 2);
                float dx2 = -ny + nx;
                float dy2 = nx + ny;
                if (turn_towards == Direction.Right)
                {
                    // Turn to the right.
                    DrawDragonLine(gr, pen, level - 1, Direction.Right, x1, y1, dx2, dy2);
                    float x2 = x1 + dx2;
                    float y2 = y1 + dy2;
                    DrawDragonLine(gr, pen, level - 1, Direction.Left, x2, y2, dy2, -dx2);
                }
                else
                {
                    // Turn to the left.
                    DrawDragonLine(gr, pen, level - 1, Direction.Right, x1, y1, dy2, -dx2);
                    float x2 = x1 + dy2;
                    float y2 = y1 - dx2;
                    DrawDragonLine(gr, pen, level - 1, Direction.Left, x2, y2, dx2, dy2);
                }
            }
        }

        private void timer_change_Tick(object sender, EventArgs e)
        {
            numericUpDown1.Value++;
            if (numericUpDown1.Value == 5)
                numericUpDown1.Value = 0;

            fractal_num_points += 1000;
            if (fractal_num_points > 12000)
                fractal_num_points = 5000;

            NumPoints_ngon_stars++;
            if (NumPoints_ngon_stars > 12)
                NumPoints_ngon_stars = 3;

            // for pickover popcorn ST
            HH += 0.01f;
            if (HH > 0.1)
                HH = 0.01f;

            IterationsPerPixel += 10;
            if (IterationsPerPixel > 80)
                IterationsPerPixel = 10;

            dx++;
            if (dx > 30)
                dx = 5;
            // for pickover popcorn SP

            redraw_all();
        }

        void redraw_all()
        {
            MakePentagons();    //Sierpinski 1
            MakeOctagons();     //Sierpinski 2

            DrawRansomNoteText();
            DrawRansomNoteText2();

            pictureBox_dragon.Refresh();    //Heighway Dragon 1
            MakeDragon4Image();             //Heighway Dragon 2

            Draw_SnowFlake1();
            Draw_SnowFlake2();
            Draw_SnowFlake3();

            draw_connection_balls();        //pictureBox13
            draw_random_circles();          //pictureBox14
            draw_Apollonian_Gasket();       //pictureBox15

            DrawGasket1();  //sierpinski_carpet
            DrawGasket2();  //sierpinski_triangle

            draw_fractal1();
            draw_fractal2();

            pictureBox_ngon_stars.Refresh();
            pictureBox22.Refresh();

            draw_pickover_popcorn1();    //for pickover popcorn 單色
            draw_pickover_popcorn2();    //for pickover popcorn 彩色


        }

        private void pictureBox_fractal1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void pictureBox_fractal2_Paint(object sender, PaintEventArgs e)
        {

        }

        // Draw the stars.
        private void pictureBox_ngon_stars_Paint(object sender, PaintEventArgs e)
        {
            if (NumPoints_ngon_stars < 3)
            {
                return;
            }
            e.Graphics.Clear(pictureBox_ngon_stars.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Get the radii.
            int r1, r2, r3;
            r3 = Math.Min(pictureBox_ngon_stars.ClientSize.Width, pictureBox_ngon_stars.ClientSize.Height) / 2;
            r1 = r3 / 2;
            r2 = r3 / 4;
            r3 = r1 + r2;

            // Position variables.
            int cx = pictureBox_ngon_stars.ClientSize.Width / 2;
            int cy = pictureBox_ngon_stars.ClientSize.Height / 2;

            // Position the original points.
            PointF[] pts1 = new PointF[NumPoints_ngon_stars];
            PointF[] pts2 = new PointF[NumPoints_ngon_stars];
            double theta = -Math.PI / 2;
            double dtheta = 2 * Math.PI / NumPoints_ngon_stars;
            for (int i = 0; i < NumPoints_ngon_stars; i++)
            {
                pts1[i].X = (float)(r1 * Math.Cos(theta));
                pts1[i].Y = (float)(r1 * Math.Sin(theta));
                pts2[i].X = (float)(r2 * Math.Cos(theta));
                pts2[i].Y = (float)(r2 * Math.Sin(theta));
                theta += dtheta;
            }

            // Draw stars.
            int max = NumPoints_ngon_stars - 1;
            for (int skip = 1; skip <= max; skip++)
            {
                // See if they are relatively prime.
                if (GCD(skip, NumPoints_ngon_stars) == 1)
                {
                    // Draw the big version of the star.
                    DrawStar(e.Graphics, cx, cy, pts1, skip);

                    // Draw the smaller version.
                    theta = -Math.PI / 2 + skip * 2 * Math.PI / NumPoints_ngon_stars;
                    int x = (int)(cx + r3 * Math.Cos(theta));
                    int y = (int)(cy + r3 * Math.Sin(theta));

                    DrawStar(e.Graphics, x, y, pts2, skip);
                }
            }
        }

        // Return the greatest common divisor (GCD) of a and b.
        private long GCD(long a, long b)
        {
            long remainder;

            // Pull out remainders.
            for (; ; )
            {
                remainder = a % b;
                if (remainder == 0) break;
                a = b;
                b = remainder;
            }

            return b;
        }

        // Draw a star centered at (x, y) using this skip value.
        private void DrawStar(Graphics gr, int x, int y, PointF[] orig_pts, int skip)
        {
            // Make a PointF array with the points in the proper order.
            PointF[] pts = new PointF[NumPoints_ngon_stars];
            for (int i = 0; i < NumPoints_ngon_stars; i++)
            {
                pts[i] = orig_pts[(i * skip) % NumPoints_ngon_stars];
            }

            // Draw the star.
            gr.TranslateTransform(x, y);
            gr.DrawPolygon(Pens.Blue, pts);
            gr.ResetTransform();
        }




        #region sierpinski

        // Draw the carpet.
        private void DrawGasket1()
        {
            int Level = (int)numericUpDown1.Value;

            Bitmap bm = new Bitmap(
                pictureBox_sierpinski3.ClientSize.Width,
                pictureBox_sierpinski3.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the top-level carpet.
                const float margin = 10;
                RectangleF rect = new RectangleF(
                    margin, margin,
                    pictureBox_sierpinski3.ClientSize.Width - 2 * margin,
                    pictureBox_sierpinski3.ClientSize.Height - 2 * margin);
                DrawRectangle(gr, Level, rect);
            }

            // Display the result.
            pictureBox_sierpinski3.Image = bm;

            // Save the bitmap into a file.
            bm.Save("Carpet " + Level + ".bmp");
        }

        // Draw a carpet in the rectangle.
        private void DrawRectangle(Graphics gr, int level, RectangleF rect)
        {
            // See if we should stop.
            if (level == 0)
            {
                // Fill the rectangle.
                gr.FillRectangle(Brushes.Blue, rect);
            }
            else
            {
                // Divide the rectangle into 9 pieces.
                float wid = rect.Width / 3f;
                float x0 = rect.Left;
                float x1 = x0 + wid;
                float x2 = x0 + wid * 2f;

                float hgt = rect.Height / 3f;
                float y0 = rect.Top;
                float y1 = y0 + hgt;
                float y2 = y0 + hgt * 2f;

                // Recursively draw smaller carpets.
                DrawRectangle(gr, level - 1, new RectangleF(x0, y0, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x1, y0, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x2, y0, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x0, y1, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x2, y1, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x0, y2, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x1, y2, wid, hgt));
                DrawRectangle(gr, level - 1, new RectangleF(x2, y2, wid, hgt));
            }
        }

        // Draw the triangle.
        private void DrawGasket2()
        {
            int Level = (int)numericUpDown1.Value;

            Bitmap bm = new Bitmap(
                pictureBox_sierpinski2.ClientSize.Width,
                pictureBox_sierpinski2.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the top-level triangle.
                const float margin = 10;
                PointF top_point = new PointF(
                    pictureBox_sierpinski2.ClientSize.Width / 2f,
                    margin);
                PointF left_point = new PointF(
                    margin,
                    pictureBox_sierpinski2.ClientSize.Height - margin);
                PointF right_point = new PointF(
                    pictureBox_sierpinski2.ClientRectangle.Right - margin,
                    pictureBox_sierpinski2.ClientRectangle.Bottom - margin);
                DrawTriangle(gr, Level, top_point, left_point, right_point);
            }

            // Display the result.
            pictureBox_sierpinski2.Image = bm;

            // Save the bitmap into a file.
            bm.Save("Triangle " + Level + ".bmp");
        }

        // Draw a triangle between the points.
        private void DrawTriangle(Graphics gr, int level,
            PointF top_point, PointF left_point, PointF right_point)
        {
            // See if we should stop.
            if (level == 0)
            {
                // Fill the triangle.
                PointF[] points =
                {
                    top_point, right_point, left_point
                };
                gr.FillPolygon(Brushes.Red, points);
            }
            else
            {
                // Find the edge midpoints.
                PointF left_mid = new PointF(
                    (top_point.X + left_point.X) / 2f,
                    (top_point.Y + left_point.Y) / 2f);
                PointF right_mid = new PointF(
                    (top_point.X + right_point.X) / 2f,
                    (top_point.Y + right_point.Y) / 2f);
                PointF bottom_mid = new PointF(
                    (left_point.X + right_point.X) / 2f,
                    (left_point.Y + right_point.Y) / 2f);

                // Recursively draw smaller triangles.
                DrawTriangle(gr, level - 1, top_point, left_mid, right_mid);
                DrawTriangle(gr, level - 1, left_mid, left_point, bottom_mid);
                DrawTriangle(gr, level - 1, right_mid, bottom_mid, right_point);
            }
        }
        #endregion

        //連接球 ST
        void draw_connection_balls()
        {
            Graphics g;
            Pen p;
            SolidBrush sb;
            Bitmap bitmap1;

            bitmap1 = new Bitmap(pictureBox13.Width, pictureBox13.Height);
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);
            sb = new SolidBrush(Color.Navy);

            int i;
            var random = new Random();

            /*
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.
            var chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            var chars2 = "0123456789";
            var stringChars1 = new char[10];
            var stringChars2 = new char[11];
            for (int i = 0; i < stringChars1.Length; i++)
            {
                if (i < 2)
                {
                    stringChars1[i] = chars1[random.Next(chars1.Length)];
                }
                else
                {
                    stringChars1[i] = chars2[random.Next(chars2.Length)];
                }
            }
            var finalString1 = new String(stringChars1);
            richTextBox1.Text += "相機序號1：" + finalString1 + "\n";

            for (int i = 0; i < stringChars2.Length; i++)
            {
                stringChars2[i] = chars2[random.Next(chars2.Length)];
            }
            var finalString2 = new String(stringChars2);
            richTextBox1.Text += "相機序號2：" + finalString2 + "\n";
            */

            int N = 10;
            int[] x = new int[N];
            int[] y = new int[N];

            int[,] position = new int[N, 2];	//建立一個二維陣列

            int w = pictureBox13.Width;
            int h = pictureBox13.Height;

            int cx = 100;
            int cy = 100;
            int r = 15;

            for (i = 0; i < N; i++)
            {
                position[i, 0] = random.Next(w - 2 * r) + r;  //x1, x2, x3.....
                position[i, 1] = random.Next(h - 2 * r) + r;  //y1, y2, y3.....
            }
            richTextBox1.Text += "每個點的位置\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += position[i, 0].ToString() + "\t" + position[i, 1].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < N; i++)
            {
                x[i] = i;
                y[i] = random.Next(N);
                /*
                do
                {
                    y[i] = random.Next(N);
                }
                while (x[i] == y[i]);
                */
            }
            richTextBox1.Text += "\n";


            richTextBox1.Text += "x array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += x[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "y array\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += y[i].ToString() + "\n";
            }
            richTextBox1.Text += "\n";


            Point pointa;
            Point pointb;
            for (i = 0; i < N; i++)
            {
                pointa = new Point(position[x[i], 0], position[x[i], 1]);
                pointb = new Point(position[y[i], 0], position[y[i], 1]);
                g.DrawLine(p, pointa, pointb);     // Draw line to screen.
            }

            for (i = 0; i < N; i++)
            {
                cx = position[i, 0];
                cy = position[i, 1];

                //richTextBox1.Text += position[i, 0].ToString() + "\t" + position[i, 1].ToString() + "\n";
                //richTextBox1.Text += "(" + (cx - r).ToString() + ", " + (cy - r).ToString() + ") - (" + (cx + r).ToString() + ", " + (cy + r).ToString() + ")\n";
                //g.FillEllipse(sb, cx - r, cy - r, r * 2, r * 2);
                FillCircle(g, sb, cx, cy, r);

                //g.DrawEllipse(new Pen(Color.Red, 3), cx - r, cy - r, r * 2, r * 2);
                DrawCircle(g, p, cx, cy, r);
            }
            pictureBox13.Image = bitmap1;
        }

        void DrawCircle(Graphics g, Pen p, int cx, int cy, int r)
        {
            g.DrawEllipse(p, cx - r, cy - r, r * 2, r * 2);
        }

        void FillCircle(Graphics g, SolidBrush sb, int cx, int cy, int r)
        {
            g.FillEllipse(sb, cx - r, cy - r, r * 2, r * 2);
        }

        //連接球 SP

        //任意圈圈圖 ST
        void draw_random_circles()
        {
            Bitmap bm = new Bitmap(pictureBox14.ClientSize.Width, pictureBox14.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.Silver);

                Random rnd = new Random();
                int max_r = Math.Min(pictureBox14.ClientRectangle.Width, pictureBox14.ClientRectangle.Height) / 3;
                int min_r = max_r / 4;
                for (int i = 0; i < 15; i++)
                {
                    int r = rnd.Next(min_r, max_r);
                    int x = rnd.Next(min_r, pictureBox14.ClientRectangle.Width - min_r);
                    int y = rnd.Next(min_r, pictureBox14.ClientRectangle.Height - min_r);
                    gr.DrawEllipse(Pens.Black, x - r, y - r, 2 * r, 2 * r);
                }
            }
            pictureBox14.Image = bm;
        }
        //任意圈圈圖 SP

        // Apollonian Gasket ST
        void draw_Apollonian_Gasket()
        {
            int width = Math.Min(pictureBox15.ClientSize.Width, pictureBox15.ClientSize.Height);
            pictureBox15.Image = FindApollonianPacking(width);
        }

        // Find the Apollonian packing.
        private Bitmap FindApollonianPacking(int width)
        {
            Bitmap bm = new Bitmap(width, width);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                if (rb1.Checked == true)
                    gr.Clear(Color.LightGreen);
                else
                    gr.Clear(Color.Black);

                // Create the three central tangent circles.
                float radius = width * 0.225f;
                float x = width / 2;
                float gasket_height = 2 * (float)(radius + 2 * radius / Math.Sqrt(3));
                float y = (width - gasket_height) / 2 + radius;
                Circle circle0 = new Circle(x, y, radius);

                // Draw a box around the gasket. (For debugging.)
                //gr.DrawRectangle(Pens.Orange,
                //    x - gasket_height / 2,
                //    y - radius,
                //    gasket_height,
                //    gasket_height);

                x -= radius;
                y += (float)(radius * Math.Sqrt(3));
                Circle circle1 = new Circle(x, y, radius);
                x += 2 * radius;
                Circle circle2 = new Circle(x, y, radius);

                if (rb1.Checked == true)
                {
                    // Draw the three central circles.
                    circle0.Draw(gr, Pens.Blue);
                    circle1.Draw(gr, Pens.Blue);
                    circle2.Draw(gr, Pens.Blue);
                }

                // Find the circle that contains them all.
                Circle big_circle = FindApollonianCircle(circle0, circle1, circle2, -1, -1, -1);
                if (rb1.Checked == true)
                {
                    big_circle.Draw(gr, Pens.Blue);
                }
                else
                {
                    // Draw the big circle.
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        big_circle.Draw(gr, the_brush);
                    }

                    // Draw the three central circles.
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        circle0.Draw(gr, the_brush);
                    }
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        circle1.Draw(gr, the_brush);
                    }
                    using (Brush the_brush = new SolidBrush(RandomColor()))
                    {
                        circle2.Draw(gr, the_brush);
                    }
                }

                // Set level to smaller values such as 3 to see partially drawn gaskets.
                int level = 10000;

                // Find the central circle.
                FindCircleOutsideAll(level, gr, circle0, circle1, circle2);

                // Find circles tangent to the big circle.
                FindCircleOutsideTwo(level, gr, circle0, circle1, big_circle);
                FindCircleOutsideTwo(level, gr, circle1, circle2, big_circle);
                FindCircleOutsideTwo(level, gr, circle2, circle0, big_circle);
            }
            return bm;
        }

        // Draw a circle tangent to these three circles and that is outside all three.
        private void FindCircleOutsideAll(int level, Graphics gr, Circle circle0, Circle circle1, Circle circle2)
        {
            Circle new_circle = FindApollonianCircle(circle0, circle1, circle2, 1, 1, 1);
            if (new_circle == null) return;
            if (new_circle.Radius < 0.1) return;

            if (rb1.Checked == true)
            {
                new_circle.Draw(gr, Pens.Blue);
            }
            else
            {
                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    new_circle.Draw(gr, the_brush);
                }
            }

            if (--level > 0)
            {
                FindCircleOutsideAll(level, gr, circle0, circle1, new_circle);
                FindCircleOutsideAll(level, gr, circle0, circle2, new_circle);
                FindCircleOutsideAll(level, gr, circle1, circle2, new_circle);
            }
        }

        // Draw a circle tangent to these three circles and that is outside two of them.
        private void FindCircleOutsideTwo(int level, Graphics gr, Circle circle0, Circle circle1, Circle circle_contains)
        {
            Circle new_circle = FindApollonianCircle(circle0, circle1, circle_contains, 1, 1, -1);
            if (new_circle == null) return;
            if (new_circle.Radius < 0.1) return;

            if (rb1.Checked == true)
            {
                new_circle.Draw(gr, Pens.Blue);
            }
            else
            {
                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    new_circle.Draw(gr, the_brush);
                }
            }

            if (--level > 0)
            {
                FindCircleOutsideTwo(level, gr, new_circle, circle0, circle_contains);
                FindCircleOutsideTwo(level, gr, new_circle, circle1, circle_contains);
                FindCircleOutsideAll(level, gr, circle0, circle1, new_circle);
            }
        }

        // Find the circles that touch each of the three input circles.
        private Circle[] FindApollonianCircles(Circle[] given_circles)
        {
            // Make a list for results.
            List<Circle> solution_circles = new List<Circle>();

            // Loop over all of the signs.
            foreach (int s0 in new int[] { -1, 1 })
            {
                foreach (int s1 in new int[] { -1, 1 })
                {
                    foreach (int s2 in new int[] { -1, 1 })
                    {
                        Circle new_circle = FindApollonianCircle(
                            given_circles[0], given_circles[1], given_circles[2],
                            s0, s1, s2);
                        if (new_circle != null) solution_circles.Add(new_circle);
                    }
                }
            }

            // Return the results.
            return solution_circles.ToArray();
        }

        // Find a solution to Apollonius' problem.
        // For discussion and method, see:
        //    http://mathworld.wolfram.com/ApolloniusProblem.html
        //    http://en.wikipedia.org/wiki/Problem_of_Apollonius#Algebraic_solutions
        // For most of a Java code implementation, see:
        //    http://www.diku.dk/hjemmesider/ansatte/rfonseca/implementations/apollonius.html
        private Circle FindApollonianCircle(Circle c1, Circle c2, Circle c3, int s1, int s2, int s3)
        {
            // Make sure c2 doesn't have the same X or Y coordinate as the others.
            const float tiny = 0.0001f;
            if ((Math.Abs(c2.Center.X - c1.Center.X) < tiny) ||
                (Math.Abs(c2.Center.Y - c1.Center.Y) < tiny))
            {
                Circle temp_circle = c2;
                c2 = c3;
                c3 = temp_circle;
                int temp_s = s2;
                s2 = s3;
                s3 = temp_s;
            }
            if ((Math.Abs(c2.Center.X - c3.Center.X) < tiny) ||
                (Math.Abs(c2.Center.Y - c3.Center.Y) < tiny))
            {
                Circle temp_circle = c2;
                c2 = c1;
                c1 = temp_circle;
                int temp_s = s2;
                s2 = s1;
                s1 = temp_s;
            }

            /*
            Debug.Assert(
                (c2.Center.X != c1.Center.X) && (c2.Center.Y != c1.Center.Y) &&
                (c2.Center.X != c3.Center.X) && (c2.Center.Y != c3.Center.Y),
                "Cannot find points without matching coordinates.");
            */
            float x1 = c1.Center.X;
            float y1 = c1.Center.Y;
            float r1 = c1.Radius;
            float x2 = c2.Center.X;
            float y2 = c2.Center.Y;
            float r2 = c2.Radius;
            float x3 = c3.Center.X;
            float y3 = c3.Center.Y;
            float r3 = c3.Radius;

            float v11 = 2 * x2 - 2 * x1;
            float v12 = 2 * y2 - 2 * y1;
            float v13 = x1 * x1 - x2 * x2 + y1 * y1 - y2 * y2 - r1 * r1 + r2 * r2;
            float v14 = 2 * s2 * r2 - 2 * s1 * r1;

            float v21 = 2 * x3 - 2 * x2;
            float v22 = 2 * y3 - 2 * y2;
            float v23 = x2 * x2 - x3 * x3 + y2 * y2 - y3 * y3 - r2 * r2 + r3 * r3;
            float v24 = 2 * s3 * r3 - 2 * s2 * r2;

            float w12 = v12 / v11;
            float w13 = v13 / v11;
            float w14 = v14 / v11;

            float w22 = v22 / v21 - w12;
            float w23 = v23 / v21 - w13;
            float w24 = v24 / v21 - w14;

            float P = -w23 / w22;
            float Q = w24 / w22;
            float M = -w12 * P - w13;
            float N = w14 - w12 * Q;

            float a = N * N + Q * Q - 1;
            float b = 2 * M * N - 2 * N * x1 + 2 * P * Q - 2 * Q * y1 + 2 * s1 * r1;
            float c = x1 * x1 + M * M - 2 * M * x1 + P * P + y1 * y1 - 2 * P * y1 - r1 * r1;

            // Find roots of a quadratic equation
            double[] solutions = QuadraticSolutions(a, b, c);
            if (solutions.Length < 1) return null;
            float rs = (float)solutions[0];
            float xs = M + N * rs;
            float ys = P + Q * rs;

            /*
            Debug.Assert(!float.IsNaN(rs) && !float.IsNaN(xs) && !float.IsNaN(ys),
                "Error finding Apollonian circle.");
            */

            if (rb1.Checked == false)
            {
                if (float.IsInfinity(xs) || float.IsInfinity(ys) || float.IsInfinity(rs)) return null;
            }
            if ((Math.Abs(xs) < tiny) || (Math.Abs(ys) < tiny) || (Math.Abs(rs) < tiny)) return null;
            return new Circle(xs, ys, rs);
        }

        // Return solutions to a quadratic equation.
        private double[] QuadraticSolutions(double a, double b, double c)
        {
            const double tiny = 0.000001;
            double discriminant = b * b - 4 * a * c;

            // See if there are no real solutions.
            if (discriminant < 0)
            {
                return new double[] { };
            }

            // See if there is one solution.
            if (discriminant < tiny)
            {
                return new double[] { -b / (2 * a) };
            }

            // There are two solutions.
            return new double[]
            {
                (-b + Math.Sqrt(discriminant)) / (2 * a),
                (-b - Math.Sqrt(discriminant)) / (2 * a),
            };
        }


        // Return a random color.
        private Random rand = new Random();
        private Color[] Colors15 =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
            Color.Yellow,
            Color.LightGreen,
            Color.LightBlue,
            Color.Cyan,
        };

        private Color RandomColor()
        {
            return Colors15[rand.Next(0, Colors15.Length)];
        }

        // Apollonian Gasket SP


        // 畫箭頭 ST

        // Draw an arrow normally and rotated around a point.
        private void pictureBox22_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the basic arrow.
            DrawArrow(Pens.Blue, e.Graphics);

            // Draw the point of rotation.
            Point center = new Point(50, 70);
            e.Graphics.FillEllipse(Brushes.Red, center.X - 3, center.Y - 3, 6, 6);

            // Rotate 30 degrees around the point.
            e.Graphics.Transform = RotateAroundPoint(rotating_angle, center);
            rotating_angle += 5;

            // Draw the arrow rotated.
            DrawArrow(Pens.Green, e.Graphics);
        }

        // Draw an arrow.
        private void DrawArrow(Pen pen, Graphics gr)
        {
            Point[] pts = 
            {
                new Point( 50,  50),
                new Point(150,  50),
                new Point(150,  20),
                new Point(200,  70),
                new Point(150, 120),
                new Point(150,  90),
                new Point( 50,  90)
            };
            gr.DrawPolygon(pen, pts);
        }

        // Return a rotation matrix to rotate around a point.
        private Matrix RotateAroundPoint(float angle, Point center)
        {
            // Translate the point to the origin.
            Matrix result = new Matrix();
            result.RotateAt(angle, center);
            return result;
        }

        // 畫箭頭 SP


        // 畫 Fractal 1 ST

        // Draw the fractal.
        void draw_fractal1()
        {
            // Generate the points.
            int num_points = fractal_num_points;
            Point[] points = new Point[num_points];
            Point current_point = new Point(0, 0);
            int prime = 7;
            for (long i = 0; i < num_points; i++)
            {
                // Find the next prime.
                while (!IsPrime(prime)) prime += 2;

                // Use this prime.
                switch (prime % 5)
                {
                    case 1:
                        current_point.Y--;
                        break;
                    case 2:
                        current_point.X++;
                        break;
                    case 3:
                        current_point.Y++;
                        break;
                    case 4:
                        current_point.X--;
                        break;
                }
                points[i] = current_point;

                // Move to the next possible prime.
                prime += 2;
            }

            // Draw the points.
            int width = pictureBox_fractal1.Width;
            Bitmap bm = new Bitmap(width, width);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.Black);

                // Get the largest and smallest coordinates.
                var x_query =
                    from Point point in points
                    select point.X;
                int[] xs = x_query.ToArray();
                int xmin = xs.Min();
                int xmax = xs.Max();
                int wid = xmax - xmin;

                var y_query =
                    from Point point in points
                    select point.Y;
                int[] ys = y_query.ToArray();
                int ymin = ys.Min();
                int ymax = ys.Max();
                int hgt = ymax - ymin;

                float scale = width / Math.Max(wid, hgt);

                // Scale and translate.
                gr.TranslateTransform(-xmin, -ymin);
                gr.ScaleTransform(scale, scale, MatrixOrder.Append);

                using (Pen thin_pen = new Pen(Color.Red, 0))
                {
                    // Draw the lines.
                    gr.DrawLines(thin_pen, points);

                    // Draw the axes.
                    thin_pen.Color = Color.Blue;
                    gr.DrawLine(thin_pen, xmin, 0, xmax, 0);
                    gr.DrawLine(thin_pen, 0, ymin, 0, ymax);
                }
            }

            pictureBox_fractal1.Image = bm;
        }

        // Return true if the value is prime.
        // For speed, asssume value > 2 and value is odd.
        private bool IsPrime(long value)
        {
            long stop_at = (long)Math.Sqrt(value);
            for (long factor = 3; factor <= stop_at; factor += 2)
            {
                if (value % factor == 0) return false;
            }
            return true;
        }


        // 畫 Fractal 1 SP


        // 畫 Fractal 2 ST

        // Draw the fractal.
        void draw_fractal2()
        {
            // Generate the points.
            int num_points = fractal_num_points;
            Point[] points = new Point[num_points];
            Dictionary<Point, int> hits = new Dictionary<Point, int>();
            Point current_point = new Point(0, 0);
            int prime = 7;
            for (long i = 0; i < num_points; i++)
            {
                // Find the next prime.
                while (!IsPrime(prime)) prime += 2;

                // Use this prime.
                switch (prime % 5)
                {
                    case 1:
                        current_point.Y--;
                        break;
                    case 2:
                        current_point.X++;
                        break;
                    case 3:
                        current_point.Y++;
                        break;
                    case 4:
                        current_point.X--;
                        break;
                }
                points[i] = current_point;
                int count = 0;
                if (hits.ContainsKey(current_point))
                    count = hits[current_point];
                hits[current_point] = count + 1;

                // Move to the next possible prime.
                prime += 2;
            }

            // Draw the points.
            int width = pictureBox_fractal2.Width;
            Bitmap bm = new Bitmap(width, width);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.Black);

                // Get the largest and smallest coordinates.
                var x_query =
                    from Point point in points
                    select point.X;
                int[] xs = x_query.ToArray();
                int xmin = xs.Min();
                int xmax = xs.Max();
                int wid = xmax - xmin;

                var y_query =
                    from Point point in points
                    select point.Y;
                int[] ys = y_query.ToArray();
                int ymin = ys.Min();
                int ymax = ys.Max();
                int hgt = ymax - ymin;

                float scale = width / Math.Max(wid, hgt);

                // Get the largest hit count.
                int max_hit = hits.Values.ToArray().Max();

                // Scale and translate.
                gr.TranslateTransform(-xmin, -ymin);
                gr.ScaleTransform(scale, scale, MatrixOrder.Append);

                using (Pen thin_pen = new Pen(Color.Black, 0))
                {
                    // Draw the lines.
                    for (int i = 1; i < num_points; i++)
                    {
                        // Set the pen color.
                        thin_pen.Color = MapRainbowColor(hits[points[i]], 1, max_hit);
                        gr.DrawLine(thin_pen, points[i - 1], points[i]);
                    }

                    // Draw the axes.
                    thin_pen.Color = Color.Blue;
                    gr.DrawLine(thin_pen, xmin, 0, xmax, 0);
                    gr.DrawLine(thin_pen, 0, ymin, 0, ymax);
                }
            }
            pictureBox_fractal2.Image = bm;
        }

        // Map a value to a rainbow color.
        private Color MapRainbowColor(float value, float red_value, float blue_value)
        {
            // Convert into a value between 0 and 1023.
            int int_value = (int)(1023 * (value - red_value) / (blue_value - red_value));

            // Map different color bands.
            if (int_value < 256)
            {
                // Red to yellow. (255, 0, 0) to (255, 255, 0).
                return Color.FromArgb(255, int_value, 0);
            }
            else if (int_value < 512)
            {
                // Yellow to green. (255, 255, 0) to (0, 255, 0).
                int_value -= 256;
                return Color.FromArgb(255 - int_value, 255, 0);
            }
            else if (int_value < 768)
            {
                // Green to aqua. (0, 255, 0) to (0, 255, 255).
                int_value -= 512;
                return Color.FromArgb(0, 255, int_value);
            }
            else
            {
                // Aqua to blue. (0, 255, 255) to (0, 0, 255).
                int_value -= 768;
                return Color.FromArgb(0, 255 - int_value, 255);
            }
        }

        // 畫 Fractal 2 SP

        //for sierpinski1 ST
        int aa = 0;
        // Add 1000 points to the gasket.
        private void timer_sierpinski1_Tick(object sender, EventArgs e)
        {
            aa++;
            if (aa > 20)
            {
                // Clear.
                using (Graphics gr = this.pictureBox_sierpinski1.CreateGraphics())
                {
                    gr.Clear(this.BackColor);
                }
                aa = 0;
            }

            // Draw points.
            Random rand = new Random();
            using (Graphics gr = this.pictureBox_sierpinski1.CreateGraphics())
            {
                // Draw the corners.
                foreach (PointF pt in Corners)
                {
                    gr.FillEllipse(Brushes.White, pt.X - 2, pt.Y - 2, 4, 4);
                    gr.DrawEllipse(Pens.Blue, pt.X - 2, pt.Y - 2, 4, 4);
                }

                // Draw 1000 points.
                for (int i = 1; i <= 400; i++)
                {
                    int j = rand.Next(0, 3);
                    LastPoint = new PointF((LastPoint.X + Corners[j].X) / 2, (LastPoint.Y + Corners[j].Y) / 2);
                    gr.DrawLine(Pens.Red, LastPoint.X, LastPoint.Y, LastPoint.X + 1, LastPoint.Y + 1);
                }
            }
        }
        //for sierpinski1 SP




        int NumBuildings = 5;
        private Rectangle[] Buildings = null;
        private Point[] Skyline = null;

        void drawBuildings()
        {
            // Create random buildings.
            const int margin = 10;
            int wid = pictureBox_skyline.ClientSize.Width;
            int hgt = pictureBox_skyline.ClientSize.Height;
            int xmin = margin;
            int xmax = wid - margin;
            int basey = hgt - margin;
            int min_hgt = margin;
            int max_hgt = hgt - 2 * margin;
            int min_wid = margin;
            int max_wid = (wid - 2 * margin) / 4;

            int num_buildings = NumBuildings;
            Buildings = new Rectangle[num_buildings];
            Random rand = new Random();
            for (int i = 0; i < num_buildings; i++)
            {
                const int block_size = 10;
                int width = rand.Next(min_wid, max_wid + 1);
                width = block_size * (int)(width / block_size);
                if (width < block_size) width = block_size;

                int height = rand.Next(min_hgt, max_hgt + 1);
                height = block_size * (int)(height / block_size);
                if (height < block_size) height = block_size;

                int x = rand.Next(xmin, xmax - width + 1);
                int y = basey - height;

                Buildings[i] = new Rectangle(x, y, width, height);
            }

            // Find the skyline.
            Skyline = FindSkyline(Buildings).ToArray();

            // Redraw.
            pictureBox_skyline.Refresh();
        }

        // Draw the buildings and skyline.
        private void pictureBox_skyline_Paint(object sender, PaintEventArgs e)
        {
            if (Buildings == null) return;
            e.Graphics.Clear(pictureBox_skyline.BackColor);

            // Draw the skyline.
            using (Pen pen = new Pen(Color.Black, 5))
            {
                e.Graphics.DrawLines(pen, Skyline);
            }

            // Draw the buildings.
            using (Brush brush = new SolidBrush(Color.FromArgb(128, Color.LightBlue)))
            {
                foreach (Rectangle building in Buildings)
                {
                    e.Graphics.FillRectangle(brush, building);
                    e.Graphics.DrawRectangle(Pens.Blue, building);
                }
            }
        }

        // Return a skyline point list for the rectangles.
        private List<Point> FindSkyline(Rectangle[] buildings)
        {
            // Create building start and end events.
            int num_buildings = buildings.Length;
            List<BuildingEvent> building_events = new List<BuildingEvent>();
            for (int i = 0; i < num_buildings; i++)
            {
                building_events.Add(new BuildingEvent(
                    buildings[i].X,
                    BuildingEvent.EventTypes.Start, i));
                building_events.Add(new BuildingEvent(
                    buildings[i].Right,
                    BuildingEvent.EventTypes.End, i));
            }

            // Sort the events.
            building_events.Sort();

            // Make a list for the currently active buildings.
            List<Rectangle> active_buildings = new List<Rectangle>();

            // Initially ymin is the building baseline.
            int ground = buildings[0].Bottom;
            int ymin = ground;

            // Make the result list.
            List<Point> results = new List<Point>();
            results.Add(new Point(0, ymin));

            // Process the events.
            int num_events = 2 * num_buildings;
            foreach (BuildingEvent building_event in building_events)
            {
                // Get the building index;
                int building_index = building_event.BuildingIndex;

                // Get the event's X coordinate.
                int event_x = building_event.X;

                // See if it's a start or stop.
                if (building_event.EventType == BuildingEvent.EventTypes.Start)
                {
                    // It's a start.
                    // See if this building is taller
                    // than the currently active one.
                    if (buildings[building_index].Top < ymin)
                    {
                        results.Add(new Point(event_x, ymin));
                        ymin = buildings[building_index].Y;
                        results.Add(new Point(event_x, ymin));
                    }

                    // Add the building to the active list.
                    active_buildings.Add(buildings[building_index]);
                }
                else
                {
                    // It's a stop.
                    // Remove the building from the active list.
                    active_buildings.Remove(buildings[building_index]);

                    // See if this building was the tallest.
                    if (buildings[building_index].Top <= ymin)
                    {
                        // This building was tallest.
                        // Mark this point.
                        results.Add(new Point(event_x, ymin));

                        // Find the new tallest active building.
                        if (active_buildings.Count == 0) ymin = ground;
                        else
                        {
                            ymin = active_buildings[0].Top;
                            for (int j = 1; j < active_buildings.Count; j++)
                            {
                                if (ymin > active_buildings[j].Top)
                                    ymin = active_buildings[j].Top;
                            }
                        }

                        // Mark this point.
                        results.Add(new Point(event_x, ymin));
                    }
                }
            }

            // Add a final point off to the right.
            results.Add(new Point(10000, ground));

            return results;
        }

        private void timer_skyline_Tick(object sender, EventArgs e)
        {
            NumBuildings++;
            if (NumBuildings > 15)
                NumBuildings = 5;
            drawBuildings();

        }

        //畫 pickover_popcorn ST
        // Plot a bunch of points.
        void draw_pickover_popcorn1()
        {
            this.Text = "h = " + HH.ToString() + " \tInterations = " + IterationsPerPixel.ToString() + " \tdx = " + dx.ToString();

            // Make a new bitmap.
            bitmap_pickover1 = new Bitmap(pictureBox_pickover_popcorn1.ClientSize.Width, pictureBox_pickover_popcorn1.ClientSize.Height);
            pictureBox_pickover_popcorn1.Image = bitmap_pickover1;

            // Plot a series for each point.
            for (int x = 0; x < bitmap_pickover1.Width; x += dx)
            {
                for (int y = 0; y < bitmap_pickover1.Height; y += dx)
                {
                    PlotPoints1(bitmap_pickover1, HH, x, y, IterationsPerPixel);
                }
                pictureBox_pickover_popcorn1.Refresh();
            }
            pictureBox_pickover_popcorn1.Refresh();
        }

        // Plot points for the clicked pixel.
        private void pictureBox_pickover_popcorn1_MouseClick(object sender, MouseEventArgs e)
        {
            // Plot the point's series.
            PlotPoints1(bitmap_pickover1, HH, e.X, e.Y, IterationsPerPixel);
            pictureBox_pickover_popcorn1.Refresh();
        }

        // Plot points for a pixel using the equations:
        //      x(n + 1) = x(n) - h * Sin(y(n) + Tan(3 * y(n)))
        //      y(n + 1) = y(n) - h * Sin(x(n) + Tan(3 * x(n)))
        private void PlotPoints1(Bitmap bm, float h, int pix_x, int pix_y, int iterations)
        {
            // Convert the first point to world coordinates.
            float wx, wy;
            DeviceToWorld(pix_x, pix_y, out wx, out wy);

            // Plot points.
            bm.SetPixel(pix_x, pix_y, Color.Blue);
            for (int i = 0; i < iterations; i++)
            {
                float new_x = (float)(wx - h * Math.Sin(wy + Math.Tan(3 * wy)));
                float new_y = (float)(wy - h * Math.Sin(wx + Math.Tan(3 * wx)));
                wx = new_x;
                wy = new_y;

                WorldToDevice(wx, wy, out pix_x, out pix_y);
                if (pix_x >= 0 && pix_x < bm.Width &&
                    pix_y >= 0 && pix_y < bm.Height)
                {
                    bm.SetPixel(pix_x, pix_y, Color.Red);
                }
            }
        }

        // Convert between world and device coordinates.
        private const float Wxmin = -4.0f;
        private const float Wxmax = 4.0f;
        private const float Wymin = -3.0f;
        private const float Wymax = 3.0f;
        private const float Wwid = (Wxmax - Wxmin);
        private const float Whgt = (Wymax - Wymin);
        private const float Dxmin = 0f;
        private const float Dxmax = 600f;
        private const float Dymin = 0f;
        private const float Dymax = 500f;
        private const float Dwid = (Dxmax - Dxmin);
        private const float Dhgt = (Dymax - Dymin);
        private void WorldToDevice(float wx, float wy, out int dx, out int dy)
        {
            dx = (int)(Dxmin + Dwid * (wx - Wxmin) / Wwid);
            dy = (int)(Dymin + Dhgt * (wy - Wymin) / Whgt);
        }
        private void DeviceToWorld(int dx, int dy, out float wx, out float wy)
        {
            wx = Wxmin + Wwid * (dx - Dxmin) / Dwid;
            wy = Wymin + Whgt * (dy - Dymin) / Dhgt;
        }


        //彩色

        //畫 pickover_popcorn ST
        // Plot a bunch of points.

        // Plot a bunch of points.
        void draw_pickover_popcorn2()
        {
            // Make a new bitmap.
            bitmap_pickover2 = new Bitmap(pictureBox_pickover_popcorn2.ClientSize.Width, pictureBox_pickover_popcorn2.ClientSize.Height);
            pictureBox_pickover_popcorn2.Image = bitmap_pickover2;

            // Plot a series for each point.
            RgbType = RgbRed;
            for (int x = 0; x < bitmap_pickover2.Width; x += dx)
            {
                for (int y = 0; y < bitmap_pickover2.Height; y += dx)
                {
                    PlotPoints2(bitmap_pickover2, HH, x, y, IterationsPerPixel, RgbType);
                    RgbType = ++RgbType % 3;
                }
                pictureBox_pickover_popcorn2.Refresh();
            }
            pictureBox_pickover_popcorn2.Refresh();
        }

        // Plot points for the clicked pixel.
        private void pictureBox_pickover_popcorn2_MouseClick(object sender, MouseEventArgs e)
        {
            // Plot the point's series.
            PlotPoints2(bitmap_pickover2, HH, e.X, e.Y, IterationsPerPixel, RgbType);
            RgbType = ++RgbType % 3;
            pictureBox_pickover_popcorn2.Refresh();
        }

        // Plot points for a pixel using the equations:
        //      x(n + 1) = x(n) - h * Sin(y(n) + Tan(3 * y(n)))
        //      y(n + 1) = y(n) - h * Sin(x(n) + Tan(3 * x(n)))
        private void PlotPoints2(Bitmap bm, float h, int pix_x, int pix_y, int iterations, int rgb_type)
        {
            // Convert the first point to world coordinates.
            float wx, wy;
            DeviceToWorld(pix_x, pix_y, out wx, out wy);

            // Plot points.
            bm.SetPixel(pix_x, pix_y, Color.Blue);
            for (int i = 0; i < iterations; i++)
            {
                float new_x = (float)(wx - h * Math.Sin(wy + Math.Tan(3 * wy)));
                float new_y = (float)(wy - h * Math.Sin(wx + Math.Tan(3 * wx)));
                wx = new_x;
                wy = new_y;

                WorldToDevice(wx, wy, out pix_x, out pix_y);
                if (pix_x >= 0 && pix_x < bm.Width &&
                    pix_y >= 0 && pix_y < bm.Height)
                {
                    Color color = bm.GetPixel(pix_x, pix_y);
                    int new_r = color.R;
                    int new_g = color.G;
                    int new_b = color.B;
                    switch (RgbType)
                    {
                        case RgbRed:
                            new_r = new_r + (255 - new_r) / 2;
                            break;
                        case RgbGreen:
                            new_g = new_g + (255 - new_g) / 2;
                            break;
                        case RgbBlue:
                            new_b = new_b + (255 - new_b) / 2;
                            break;
                    }

                    color = Color.FromArgb(255, new_r, new_g, new_b);
                    bm.SetPixel(pix_x, pix_y, color);
                }
            }
        }
        //畫 pickover_popcorn SP


        private void timer_battery1_Tick(object sender, EventArgs e)
        {
            ShowPowerStatus();
        }

        float percent = 0;
        private void ShowPowerStatus()
        {
            percent += 0.13f;
            if (percent > 1)
                percent -= 1;
            richTextBox1.Text += percent.ToString() + " ";

            lblStatus.Text = percent.ToString("P0");
            //string percent_text = percent.ToString("P0");

            // Draw battery images.
            picVBattery1.Image = DrawBattery(
                percent,
                picVBattery1.ClientSize.Width,
                picVBattery1.ClientSize.Height,
                Color.Transparent, Color.Gray,
                Color.LightGreen, Color.White,
                true);
            picVBattery2.Image = DrawBattery(
                percent,
                picVBattery1.ClientSize.Width,
                picVBattery1.ClientSize.Height,
                Color.Transparent, Color.Gray,
                Color.LightGreen, Color.White,
                false);
            picHBattery1.Image = DrawBattery(
                percent,
                picHBattery1.ClientSize.Width,
                picHBattery1.ClientSize.Height,
                Color.Transparent, Color.Gray,
                Color.LightGreen, Color.White,
                true);
            picHBattery2.Image = DrawBattery(
                percent,
                picHBattery1.ClientSize.Width,
                picHBattery1.ClientSize.Height,
                Color.Transparent, Color.Gray,
                Color.LightGreen, Color.White,
                false);
        }

        private Bitmap DrawBattery(
            float percent, int wid, int hgt,
            Color bg_color, Color outline_color,
            Color charged_color, Color uncharged_color,
            bool striped)
        {
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // If the battery has a horizontal orientation,
                // rotate so we can draw it vertically.
                if (wid > hgt)
                {
                    gr.RotateTransform(90, MatrixOrder.Append);
                    gr.TranslateTransform(wid, 0, MatrixOrder.Append);
                    int temp = wid;
                    wid = hgt;
                    hgt = temp;
                }

                // Draw the battery.
                DrawVerticalBattery(gr, percent, wid, hgt, bg_color,
                    outline_color, charged_color, uncharged_color,
                    striped);
            }
            return bm;
        }

        // Draw a vertically oriented battery with
        // the indicated percentage filled in.
        private void DrawVerticalBattery(Graphics gr,
            float percent, int wid, int hgt,
            Color bg_color, Color outline_color,
            Color charged_color, Color uncharged_color,
            bool striped)
        {
            gr.Clear(bg_color);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a rectangle for the main body.
            float thickness = hgt / 20f;
            RectangleF body_rect = new RectangleF(
                thickness * 0.5f, thickness * 1.5f,
                wid - thickness, hgt - thickness * 2f);

            using (Pen pen = new Pen(outline_color, thickness))
            {
                // Fill the body with the uncharged color.
                using (Brush brush = new SolidBrush(uncharged_color))
                {
                    gr.FillRectangle(brush, body_rect);
                }

                // Fill the charged area.
                float charged_hgt = body_rect.Height * percent;
                RectangleF charged_rect = new RectangleF(
                    body_rect.Left, body_rect.Bottom - charged_hgt,
                    body_rect.Width, charged_hgt);
                using (Brush brush = new SolidBrush(charged_color))
                {
                    gr.FillRectangle(brush, charged_rect);
                }

                // Optionally stripe multiples of 25%
                if (striped)
                    for (int i = 1; i <= 3; i++)
                    {
                        float y = body_rect.Bottom - i * 0.25f * body_rect.Height;
                        gr.DrawLine(pen, body_rect.Left, y, body_rect.Right, y);
                    }

                // Draw the main body.
                gr.DrawPath(pen, MakeRoundedRect(
                    body_rect, thickness, thickness,
                    true, true, true, true));

                // Draw the positive terminal.
                RectangleF terminal_rect = new RectangleF(
                    wid / 2f - thickness, 0,
                    2 * thickness, thickness);
                gr.DrawPath(pen, MakeRoundedRect(
                    terminal_rect, thickness / 2f, thickness / 2f,
                    true, true, false, false));
            }
        }

        // Draw a rectangle in the indicated Rectangle
        // rounding the indicated corners.
        private GraphicsPath MakeRoundedRect(
            RectangleF rect, float xradius, float yradius,
            bool round_ul, bool round_ur, bool round_lr, bool round_ll)
        {
            // Make a GraphicsPath to draw the rectangle.
            PointF point1, point2;
            GraphicsPath path = new GraphicsPath();

            // Upper left corner.
            if (round_ul)
            {
                RectangleF corner = new RectangleF(
                    rect.X, rect.Y,
                    2 * xradius, 2 * yradius);
                path.AddArc(corner, 180, 90);
                point1 = new PointF(rect.X + xradius, rect.Y);
            }
            else point1 = new PointF(rect.X, rect.Y);

            // Top side.
            if (round_ur)
                point2 = new PointF(rect.Right - xradius, rect.Y);
            else
                point2 = new PointF(rect.Right, rect.Y);
            path.AddLine(point1, point2);

            // Upper right corner.
            if (round_ur)
            {
                RectangleF corner = new RectangleF(
                    rect.Right - 2 * xradius, rect.Y,
                    2 * xradius, 2 * yradius);
                path.AddArc(corner, 270, 90);
                point1 = new PointF(rect.Right, rect.Y + yradius);
            }
            else point1 = new PointF(rect.Right, rect.Y);

            // Right side.
            if (round_lr)
                point2 = new PointF(rect.Right, rect.Bottom - yradius);
            else
                point2 = new PointF(rect.Right, rect.Bottom);
            path.AddLine(point1, point2);

            // Lower right corner.
            if (round_lr)
            {
                RectangleF corner = new RectangleF(
                    rect.Right - 2 * xradius,
                    rect.Bottom - 2 * yradius,
                    2 * xradius, 2 * yradius);
                path.AddArc(corner, 0, 90);
                point1 = new PointF(rect.Right - xradius, rect.Bottom);
            }
            else point1 = new PointF(rect.Right, rect.Bottom);

            // Bottom side.
            if (round_ll)
                point2 = new PointF(rect.X + xradius, rect.Bottom);
            else
                point2 = new PointF(rect.X, rect.Bottom);
            path.AddLine(point1, point2);

            // Lower left corner.
            if (round_ll)
            {
                RectangleF corner = new RectangleF(
                    rect.X, rect.Bottom - 2 * yradius,
                    2 * xradius, 2 * yradius);
                path.AddArc(corner, 90, 90);
                point1 = new PointF(rect.X, rect.Bottom - yradius);
            }
            else point1 = new PointF(rect.X, rect.Bottom);

            // Left side.
            if (round_ul)
                point2 = new PointF(rect.X, rect.Y + yradius);
            else
                point2 = new PointF(rect.X, rect.Y);
            path.AddLine(point1, point2);

            // Join with the start point.
            path.CloseFigure();

            return path;
        }

        private void picSamples_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(picSamples.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            const float xradius = 20;
            const float yradius = 20;

            // Top rectangle.
            const float margin = 10;
            float hgt = (picSamples.ClientSize.Height - 3 * margin) / 2f;
            RectangleF rect = new RectangleF(
                margin, margin,
                picSamples.ClientSize.Width - 2 * margin,
                hgt);
            using (Pen pen = new Pen(Color.Green, 5))
            {
                GraphicsPath path = MakeRoundedRect(
                    rect, xradius, yradius, true, true, true, true);
                e.Graphics.FillPath(Brushes.LightGreen, path);
                e.Graphics.DrawPath(pen, path);
            }

            // Bottom left rectangle.
            float wid = (picSamples.ClientSize.Width - 3 * margin) / 2f;
            rect = new RectangleF(
                margin, hgt + 2 * margin, wid, hgt);
            using (Pen pen = new Pen(Color.Green, 5))
            {
                GraphicsPath path = MakeRoundedRect(
                    rect, xradius, yradius, false, true, false, true);
                e.Graphics.FillPath(Brushes.LightGreen, path);
                e.Graphics.DrawPath(pen, path);
            }

            // Bottom right rectangle.
            rect = new RectangleF(
                wid + 2 * margin, hgt + 2 * margin, wid, hgt);
            using (Pen pen = new Pen(Color.Green, 5))
            {
                GraphicsPath path = MakeRoundedRect(
                    rect, xradius, yradius, true, false, true, false);
                e.Graphics.FillPath(Brushes.LightGreen, path);
                e.Graphics.DrawPath(pen, path);
            }

            e.Graphics.DrawString("畫矩形圓邊", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(55, 22));

        }



    }
}
