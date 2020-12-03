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


        // Sierpinski
        // The root of the Pentagon object hierarchy.
        private Pentagon Root5 = null;
        // The root of the Octagon object hierarchy.
        private Octagon Root8 = null;

        int W = 200;
        int H = 200;

        private const int Period = 21;
        private Color[] Colors;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.Red);             //useless??
            pictureBox1.BackColor = Color.Pink;
            show_item_location();
            DrawRansomNoteText();
            DrawRansomNoteText2();

            MakePentagons();
            MakeOctagons();

            button1_Click(sender, e);

            richTextBox1.Text += "picturebox1 W = " + pictureBox1.Size.Width.ToString() + ", H = " + pictureBox1.Size.Height.ToString() + "\n";
            richTextBox1.Text += "picturebox1 client W = " + pictureBox1.ClientSize.Width.ToString() + ", H = " + pictureBox1.ClientSize.Height.ToString() + "\n";

            // Initialize the colors.
            Colors = new Color[] {
                Color.Pink,
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Violet,
                Color.Pink,
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Violet,
                Color.Pink,
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Violet
            };
            MakeDragon4Image();
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
            x_st = 1150 + 220;
            y_st = 40;
            dx = 110;
            dy = 38;

            label1.Location = new Point(x_st + dx * 0 - 20, y_st + dy * 0 - 30);
            numericUpDown1.Location = new Point(x_st + dx * 0 + 40, y_st + dy * 0 - 30);

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            bt_save.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_exit.Location = new Point(x_st + dx * 0, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            pictureBox1.Size = new Size(W * 2, H * 2);
            pictureBox_hex.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox_Chrysanthemum.Size = new Size(W, H);
            pictureBox_dragon.Size = new Size(W, H);
            pictureBox_dragon4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox_Chrysanthemum2.Size = new Size(W, H);
            pictureBox_polar.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox_snowflake.Size = new Size(W, H);
            pictureBox_snowflake2.Size = new Size(W, H);

            x_st = 10;
            y_st = 10;
            dx = W + 30;
            dy = H + 20;
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_hex.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_snowflake.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_snowflake2.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            pictureBox_dragon.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox_dragon4.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            richTextBox_ransom_note.Size = new Size(W, H + 40);
            richTextBox_ransom_note_result.Size = new Size(W, H + 40);
            pictureBox_ransom_note.Size = new Size(W, H + 40);

            pictureBox_Chrysanthemum.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox_Chrysanthemum2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox_polar.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            richTextBox_ransom_note.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox_ransom_note.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            richTextBox_ransom_note_result.Location = new Point(x_st + dx * 5, y_st + dy * 2);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(button0.Right + 10, richTextBox1.Bottom + 100);    //自動表單邊界
        }

        private void button0_Click(object sender, EventArgs e)
        {
            MakePentagons();
            MakeOctagons();
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
                pictureBox8.ClientSize.Width / 2,
                pictureBox8.ClientSize.Height / 2);
            float radius = (float)Math.Min(center.X, center.Y);
            radius -= 5;
            Root8 = MakeOctagon(depth, center, radius);

            // Redraw.
            pictureBox8.Refresh();
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
        private void button1_Click(object sender, EventArgs e)
        {
            Draw_SnowFlake1();
            Draw_SnowFlake2();
            Draw_SnowFlake3();
        }

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




        private void button2_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(W * 2, H * 2);

            // Brushes used to fill pie slices.
            Brush[] SliceBrushes =
            {
                Brushes.Red,
                Brushes.LightGreen,
                Brushes.Blue,
                Brushes.LightBlue,
                Brushes.Green,
                Brushes.Lime,
                Brushes.Orange,
                Brushes.Fuchsia,
                Brushes.Yellow,
                Brushes.Cyan,
            };
            // Pens used to outline pie slices.
            Pen[] SlicePens = { Pens.Black };

            // The data values to chart.
            float[] Values = new float[10];

            // Make some random data.
            Random rand = new Random();
            for (int i = 0; i < Values.Length; i++)
            {
                // Pick a random value between 5 and 40.
                Values[i] = (float)(5 + 35 * rand.NextDouble());
            }

            //ResizeRedraw = true;

            // Draw the pie chart.

            Graphics g = pictureBox1.CreateGraphics();

            g.Clear(BackColor);
            if ((pictureBox1.Size.Width < 20) || (pictureBox1.Size.Height < 20)) return;

            g.SmoothingMode = SmoothingMode.AntiAlias;
            Rectangle rect = new Rectangle(10, 10, pictureBox1.Size.Width - 20, pictureBox1.Size.Height - 20);

            richTextBox1.Text += "W = " + pictureBox1.Size.Width.ToString() + ", H = " + pictureBox1.Size.Height.ToString() + "\n";
            DrawLabeledPieChart(g, rect, -90, SliceBrushes, SlicePens, Values, "0.0", Font, Brushes.Black);

            //pictureBox1.Image = 


        }

        // Draw a pie chart.
        private static void DrawLabeledPieChart(Graphics gr, Rectangle rect, float initial_angle, Brush[] brushes, Pen[] pens, float[] values, string label_format, Font label_font, Brush label_brush)
        {
            // Get the total of all angles.
            float total = values.Sum();

            gr.DrawRectangle(new Pen(Color.Red, 3), rect);

            // Draw the slices.
            float start_angle = initial_angle;
            for (int i = 0; i < values.Length; i++)
            {
                float sweep_angle = values[i] * 360f / total;

                // Fill and outline the pie slice.
                gr.FillPie(brushes[i % brushes.Length], rect, start_angle, sweep_angle);
                gr.DrawPie(pens[i % pens.Length], rect, start_angle, sweep_angle);

                start_angle += sweep_angle;
            }

            // Label the slices.
            // We label the slices after drawing them all so one
            // slice doesn't cover the label on another very thin slice.
            using (StringFormat string_format = new StringFormat())
            {
                // Center text.
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;

                // Find the center of the rectangle.
                float cx = (rect.Left + rect.Right) / 2f;
                float cy = (rect.Top + rect.Bottom) / 2f;

                // Place the label about 2/3 of the way out to the edge.
                float radius = (rect.Width + rect.Height) / 2f * 0.33f;

                start_angle = initial_angle;
                for (int i = 0; i < values.Length; i++)
                {
                    float sweep_angle = values[i] * 360f / total;

                    // Label the slice.
                    double label_angle = Math.PI * (start_angle + sweep_angle / 2f) / 180f;
                    float x = cx + (float)(radius * Math.Cos(label_angle));
                    float y = cy + (float)(radius * Math.Sin(label_angle));
                    gr.DrawString(values[i].ToString(label_format),
                        label_font, label_brush, x, y, string_format);

                    start_angle += sweep_angle;
                }
            }
        }



        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(W * 2, H * 5 / 4);

            // Brushes used to fill pie slices.
            Brush[] SliceBrushes =
            {
                Brushes.Red,
                Brushes.LightGreen,
                Brushes.Blue,
                Brushes.LightBlue,
                Brushes.Green,
                Brushes.Lime,
                Brushes.Orange,
                Brushes.Fuchsia,
                Brushes.Yellow,
                Brushes.Cyan,
            };

            // Pens used to outline pie slices.
            Pen[] SlicePens = { Pens.Black };

            // Top 10 languages on September 13, 2012 according to:
            //      http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html
            // The data values to chart.
            float[] Values = 
            {
                19.295f,
                16.267f,
                9.770f,
                9.147f,
                6.596f,
                5.614f,
                5.528f,
                3.861f,
                2.267f,
                1.724f,
            };

            // The values' annotations.
            string[] Annotations = new string[]
            {
                "C",
                "Java",
                "Objective-C",
                "C++",
                "C#",
                "PHP",
                "(Visual) Basic",
                "Python",
                "Perl",
                "Ruby",
            };

            // Draw the pie chart.

            Graphics g = pictureBox1.CreateGraphics();

            const int top_margin = 30;
            const int left_margin = 15;
            g.Clear(BackColor);
            if ((pictureBox1.Size.Width < 2 * top_margin) || (pictureBox1.Size.Height < 2 * top_margin))
                return;

            g.SmoothingMode = SmoothingMode.AntiAlias;

            int circle_width = pictureBox1.Size.Height - 2 * top_margin;
            int annotation_width = (pictureBox1.Size.Width - circle_width) / 2 - 2 * left_margin;
            int annotation_height = pictureBox1.Size.Height - 2 * left_margin;
            Rectangle left_rect = new Rectangle(
                left_margin, left_margin, annotation_width, annotation_height);
            Rectangle ellipse_rect = new Rectangle(
                left_rect.Right + left_margin, top_margin, circle_width, circle_width);
            Rectangle right_rect = new Rectangle(
                ellipse_rect.Right + left_margin, left_rect.Top,
                left_rect.Width, left_rect.Height);
            using (Font annotation_font = new Font("Times New Roman", 12))
            {
                DrawAnnotatedPieChart(g,
                    ellipse_rect, left_rect, right_rect, 1.1f, 0,
                    SliceBrushes, SlicePens,
                    Values, Annotations, "0.0", Font, Brushes.Black,
                    annotation_font, Pens.Blue, Brushes.Green,
                    Brushes.LightBlue, null);
            }







        }

        // Draw a pie chart.
        private static void DrawAnnotatedPieChart(Graphics gr, Rectangle ellipse_rect, Rectangle left_rect, Rectangle right_rect, float annotation_radius_scale, float initial_angle, Brush[] brushes, Pen[] pens, float[] values, string[] annotations, string label_format, Font label_font, Brush label_brush, Font annotation_font, Pen annotation_pen, Brush annotation_brush, Brush rectangle_brush, Pen rectangle_pen)
        {
            // Get the total of all angles.
            float total = values.Sum();

            // Draw the slices.
            float start_angle = initial_angle;
            for (int i = 0; i < values.Length; i++)
            {
                float sweep_angle = values[i] * 360f / total;

                // Fill and outline the pie slice.
                gr.FillPie(brushes[i % brushes.Length], ellipse_rect, start_angle, sweep_angle);
                gr.DrawPie(pens[i % pens.Length], ellipse_rect, start_angle, sweep_angle);

                start_angle += sweep_angle;
            }

            // Draw the rectangles if desired.
            if (rectangle_brush != null)
            {
                gr.FillRectangle(rectangle_brush, left_rect);
                gr.FillRectangle(rectangle_brush, right_rect);
            }
            if (rectangle_pen != null)
            {
                gr.DrawRectangle(rectangle_pen, left_rect);
                gr.DrawRectangle(rectangle_pen, right_rect);
            }

            // Label and annotate the slices.
            // We label the slices after drawing them all so one
            // slice doesn't cover the label on another very thin slice.
            using (StringFormat string_format = new StringFormat())
            {
                // Find the center of the rectangle.
                float cx = (ellipse_rect.Left + ellipse_rect.Right) / 2;
                float cy = (ellipse_rect.Top + ellipse_rect.Bottom) / 2;

                // Place the label about 2/3 of the way out to the edge.
                float radius = (ellipse_rect.Width + ellipse_rect.Height) / 2f * 0.33f;

                // Distances for annotation lines.
                float annotation_rx1 = ellipse_rect.Width / 2;
                float annotation_ry1 = ellipse_rect.Height / 2;
                float annotation_rx2 = annotation_rx1 * annotation_radius_scale;
                float annotation_ry2 = annotation_ry1 * annotation_radius_scale;

                start_angle = start_angle = initial_angle;
                for (int i = 0; i < values.Length; i++)
                {
                    float sweep_angle = values[i] * 360f / total;

                    // Label the slice.
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    double label_angle = Math.PI * (start_angle + sweep_angle / 2) / 180;
                    float x = cx + (float)(radius * Math.Cos(label_angle));
                    float y = cy + (float)(radius * Math.Sin(label_angle));
                    gr.DrawString(values[i].ToString(label_format),
                        label_font, label_brush, x, y, string_format);

                    // Draw a radial line to connect to the annotation.
                    float x1 = cx + (float)(annotation_rx1 * Math.Cos(label_angle));
                    float y1 = cy + (float)(annotation_rx1 * Math.Sin(label_angle));
                    float x2 = cx + (float)(annotation_rx2 * Math.Cos(label_angle));
                    float y2 = cy + (float)(annotation_rx2 * Math.Sin(label_angle));
                    gr.DrawLine(annotation_pen, x1, y1, x2, y2);

                    // Draw a horizontal line to the annotation.
                    if (x2 < x1)
                    {
                        // Draw to the left.
                        gr.DrawLine(annotation_pen, x2, y2, left_rect.Right, y2);

                        // Draw the annotation right justified.
                        string_format.Alignment = StringAlignment.Far;
                        gr.DrawString(annotations[i], annotation_font, annotation_brush,
                            left_rect.Right, y2, string_format);
                    }
                    else
                    {
                        // Draw to the right.
                        gr.DrawLine(annotation_pen, x2, y2, right_rect.Left, y2);

                        // Draw the annotation left justified.
                        string_format.Alignment = StringAlignment.Near;
                        gr.DrawString(annotations[i], annotation_font, annotation_brush,
                            right_rect.Left, y2, string_format);
                    }

                    start_angle += sweep_angle;
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(W * 2, H * 2);

            // Brushes used to fill pie slices.
            Brush[] SliceBrushes =
            {
                Brushes.Red,
                Brushes.LightGreen,
                Brushes.Blue,
                Brushes.LightBlue,
                Brushes.Green,
                Brushes.Lime,
                Brushes.Orange,
                Brushes.Fuchsia,
                Brushes.Yellow,
                Brushes.Cyan,
            };

            // Pens used to outline pie slices.
            Pen[] SlicePens = { Pens.Black };

            // The data values to chart.
            float[] Values = new float[10];

            // Make some random data.
            Random rand = new Random();
            for (int i = 0; i < Values.Length; i++)
            {
                Values[i] = rand.Next(10, 40);
            }

            // Draw the pie chart.
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(BackColor);
            if ((pictureBox1.Size.Width < 20) || (pictureBox1.Size.Height < 20))
                return;

            g.SmoothingMode = SmoothingMode.AntiAlias;
            Rectangle rect = new Rectangle(10, 10, pictureBox1.Size.Width - 20, pictureBox1.Size.Height - 20);
            DrawPieChart(g, rect, SliceBrushes, SlicePens, Values);
        }

        // Draw a pie chart.
        private static void DrawPieChart(Graphics gr, Rectangle rect, Brush[] brushes, Pen[] pens, float[] values)
        {
            // Get the total of all angles.
            float total = values.Sum();

            // Draw the slices.
            float start_angle = 0;
            for (int i = 0; i < values.Length; i++)
            {
                float sweep_angle = values[i] * 360f / total;
                gr.FillPie(brushes[i % brushes.Length], rect, start_angle, sweep_angle);
                gr.DrawPie(pens[i % pens.Length], rect, start_angle, sweep_angle);
                start_angle += sweep_angle;
            }
        }


        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(W * 2, H * 2);

            // Draw pie slices.

            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(BackColor);

            g.SmoothingMode = SmoothingMode.AntiAlias;

            const int margin = 10;
            const int width = 100;
            Pen outline_pen = Pens.Red;
            Brush fill_brush = Brushes.LightGreen;

            using (Pen ellipse_pen = new Pen(Color.Blue))
            {
                ellipse_pen.DashPattern = new float[] { 5, 5 };

                // Northeast wedge.
                Rectangle rect = new Rectangle(margin + 30, 10, width, width);
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 300, 30);
                g.DrawPie(outline_pen, rect, 300, 30);

                // Everything else.
                rect.X += width + margin;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 300, -330);
                g.DrawPie(outline_pen, rect, 300, -330);

                // East wedge.
                rect.Y += width + margin;
                rect.X = margin + 30;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 315, 90);
                g.DrawPie(outline_pen, rect, 315, 90);

                // Everything else.
                rect.X += width + margin;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 315, -270);
                g.DrawPie(outline_pen, rect, 315, -270);

                // Northwest quadrant.
                rect.Y += width + margin;
                rect.X = margin + 30;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 180, 90);
                g.DrawPie(outline_pen, rect, 180, 90);

                // Everything else.
                rect.X += width + margin;
                g.DrawEllipse(ellipse_pen, rect);
                g.FillPie(fill_brush, rect, 180, -270);
                g.DrawPie(outline_pen, rect, 180, -270);
            }







        }

        void Draw_SnowFlake3()
        {
            // Define an initiator and generator.
            Initiator = new List<PointF>();
            float height = Math.Min(
                pictureBox2.ClientSize.Width,
                pictureBox2.ClientSize.Height) - 100;
            float x1 = (pictureBox2.ClientSize.Width - height) / 2;
            float x2 = x1 + height;
            float y1 = (pictureBox2.ClientSize.Height - height) / 2;
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

            Bitmap bm = new Bitmap(pictureBox2.ClientSize.Width, pictureBox2.ClientSize.Height);
            pictureBox2.Image = bm;

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
            gr.Clear(pictureBox2.BackColor);

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

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox1.Image = null;
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        private void pictureBox8_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox8.BackColor);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            if (Root8 == null) return;

            Root8.Draw(e.Graphics);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }


        // http://en.wikipedia.org/wiki/Dragon_curve
        // http://en.wikipedia.org/wiki/Heighway_dragon
        // http://ecademy.agnesscott.edu/~lriddle/ifs/heighway/heighway.htm

        private void button6_Click(object sender, EventArgs e)
        {
            pictureBox_dragon.Refresh();

            MakeDragon4Image();
        }

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

        private void button7_Click(object sender, EventArgs e)
        {
            // Draw some text along a line segment.
            Graphics g = pictureBox1.CreateGraphics();
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            // Draw some text along some line segments.
            DrawOnSegment(g, new PointF(20, 20), new PointF(330, 150), "This is some text above a line segment.", true);
            DrawOnSegment(g, new PointF(20, 20), new PointF(330, 150), "This is some text below a line segment.", false);

            DrawOnSegment(g, new PointF(330, 200), new PointF(20, 120), "This is some text above a line segment.", true);
            DrawOnSegment(g, new PointF(330, 200), new PointF(20, 120), "This is some text below a line segment.", false);
        }

        // Draw some text.
        private void DrawOnSegment(Graphics gr, PointF start_point, PointF end_point, string txt, bool text_above_segment)
        {
            int start_ch = 0;

            gr.DrawLine(Pens.Green, start_point, end_point);
            DrawTextOnSegment(gr, Brushes.Blue, this.Font, txt,
                ref start_ch, ref start_point, end_point, text_above_segment);
        }

        // Draw some text along a line segment.
        // Leave char_num pointing to the next character to be drawn.
        // Leave start_point holding the last point used.
        private void DrawTextOnSegment(Graphics gr, Brush brush, Font font, string txt, ref int first_ch, ref PointF start_point, PointF end_point, bool text_above_segment)
        {
            float dx = end_point.X - start_point.X;
            float dy = end_point.Y - start_point.Y;
            float dist = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= dist;
            dy /= dist;

            // See how many characters will fit.
            int last_ch = first_ch;
            while (last_ch < txt.Length)
            {
                string test_string = txt.Substring(first_ch, last_ch - first_ch + 1);
                if (gr.MeasureString(test_string, font).Width > dist)
                {
                    // This is one too many characters.
                    last_ch--;
                    break;
                }
                last_ch++;
            }
            if (last_ch < first_ch) return;
            if (last_ch >= txt.Length) last_ch = txt.Length - 1;
            string chars_that_fit = txt.Substring(first_ch, last_ch - first_ch + 1);

            // Rotate and translate to position the characters.
            GraphicsState state = gr.Save();
            if (text_above_segment)
            {
                gr.TranslateTransform(0, -gr.MeasureString(chars_that_fit, font).Height, MatrixOrder.Append);
            }
            float angle = (float)(180 * Math.Atan2(dy, dx) / Math.PI);
            gr.RotateTransform(angle, MatrixOrder.Append);
            gr.TranslateTransform(start_point.X, start_point.Y, MatrixOrder.Append);

            // Draw the characters that fit.
            gr.DrawString(chars_that_fit, font, brush, 0, 0);

            // Restore the saved state.
            gr.Restore(state);

            // Update first_ch and start_point.
            first_ch = last_ch + 1;
            float text_width = gr.MeasureString(chars_that_fit, font).Width;
            start_point = new PointF(start_point.X + dx * text_width, start_point.Y + dy * text_width);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();

            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            // Draw some text along some paths.
            GraphicsPath path = new GraphicsPath();
            path.AddArc(new RectangleF(40, 40, 320, 220), 180, 180);
            g.DrawPath(Pens.Green, path);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, false);

            path = new GraphicsPath();
            path.AddArc(new RectangleF(40, 50, 320, 220), 0, 180);
            g.DrawPath(Pens.Red, path);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, false);
        }

        // Draw some text along a GraphicsPath.
        private void DrawTextOnPath(Graphics gr, Brush brush, Font font, string txt, GraphicsPath path, bool text_above_path)
        {
            // Make a copy so we don't mess up the original.
            path = (GraphicsPath)path.Clone();

            // Flatten the path into segments.
            path.Flatten();

            // Draw characters.
            int start_ch = 0;
            PointF start_point = path.PathPoints[0];
            for (int i = 1; i < path.PointCount; i++)
            {
                PointF end_point = path.PathPoints[i];
                DrawTextOnSegment2(gr, brush, font, txt, ref start_ch,
                    ref start_point, end_point, text_above_path);
                if (start_ch >= txt.Length) break;
            }
        }

        // Draw some text along a line segment.
        // Leave char_num pointing to the next character to be drawn.
        // Leave start_point holding the coordinates of the last point used.
        private void DrawTextOnSegment2(Graphics gr, Brush brush, Font font, string txt, ref int first_ch, ref PointF start_point, PointF end_point, bool text_above_segment)
        {
            float dx = end_point.X - start_point.X;
            float dy = end_point.Y - start_point.Y;
            float dist = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= dist;
            dy /= dist;

            // See how many characters will fit.
            int last_ch = first_ch;
            while (last_ch < txt.Length)
            {
                string test_string = txt.Substring(first_ch, last_ch - first_ch + 1);
                if (gr.MeasureString(test_string, font).Width > dist)
                {
                    // This is one too many characters.
                    last_ch--;
                    break;
                }
                last_ch++;
            }
            if (last_ch < first_ch) return;
            if (last_ch >= txt.Length) last_ch = txt.Length - 1;
            string chars_that_fit = txt.Substring(first_ch, last_ch - first_ch + 1);

            // Rotate and translate to position the characters.
            GraphicsState state = gr.Save();
            if (text_above_segment)
            {
                gr.TranslateTransform(0,
                    -gr.MeasureString(chars_that_fit, font).Height,
                    MatrixOrder.Append);
            }
            float angle = (float)(180 * Math.Atan2(dy, dx) / Math.PI);
            gr.RotateTransform(angle, MatrixOrder.Append);
            gr.TranslateTransform(start_point.X, start_point.Y, MatrixOrder.Append);

            // Draw the characters that fit.
            gr.DrawString(chars_that_fit, font, brush, 0, 0);

            // Restore the saved state.
            gr.Restore(state);

            // Update first_ch and start_point.
            first_ch = last_ch + 1;
            float text_width = gr.MeasureString(chars_that_fit, font).Width;
            start_point = new PointF(
                start_point.X + dx * text_width,
                start_point.Y + dy * text_width);
        }


        private void pictureBox_Chrysanthemum_Paint(object sender, PaintEventArgs e)
        {
            pictureBox_Chrysanthemum.BackColor = Color.Black;
            // Draw the curve.

            // Scale and translate.
            const float ymax = -11;
            const float ymin = 11;
            const float hgt = ymin - ymax;
            const float wid = hgt;
            float scale = Math.Min(
                pictureBox_Chrysanthemum.Size.Width / wid,
                pictureBox_Chrysanthemum.Size.Height / hgt);
            e.Graphics.ScaleTransform(scale, scale);
            e.Graphics.TranslateTransform(
                pictureBox_Chrysanthemum.Size.Width / 2,
                pictureBox_Chrysanthemum.Size.Height / 2,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the curve.
            const long num_lines = 5000;

            // Generate the points.
            double t = 0;
            double r = 5 * (1 + Math.Sin(11 * t / 5))
                - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
            PointF pt1 = new PointF((float)(r * Math.Sin(t)), (float)(-r * Math.Cos(t)));

            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                for (int i = 0; i <= num_lines; i++)
                {
                    t = i * Period * Math.PI / num_lines;
                    r = 5 * (1 + Math.Sin(11 * t / 5))
                        - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                        * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
                    PointF pt0 = pt1;
                    pt1 = new PointF((float)(r * Math.Sin(t)), (float)(r * Math.Cos(t)));
                    the_pen.Color = GetColor(t);
                    e.Graphics.DrawLine(the_pen, pt0, pt1);
                }
            }



        }

        // Return a color from the Colors array.
        private Color GetColor(double t)
        {
            int index = (int)(t / Math.PI);
            return Colors[index % Colors.Length];
        }

        private void pictureBox_Chrysanthemum2_Paint(object sender, PaintEventArgs e)
        {
            pictureBox_Chrysanthemum2.BackColor = Color.Black;
            // Draw the curve.

            // Scale and translate.
            const float ymax = -11;
            const float ymin = 11;
            const float hgt = ymin - ymax;
            const float wid = hgt;
            float scale = Math.Min(
                pictureBox_Chrysanthemum2.Size.Width / wid,
                pictureBox_Chrysanthemum2.Size.Height / hgt);
            e.Graphics.ScaleTransform(scale, scale);
            e.Graphics.TranslateTransform(
                pictureBox_Chrysanthemum2.Size.Width / 2,
                pictureBox_Chrysanthemum2.Size.Height / 2,
                System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the curve.
            const long num_lines = 5000;

            // Generate the points.
            double t = 0;
            double r = 5 * (1 + Math.Sin(11 * t / 5))
                - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
            PointF pt1 = new PointF((float)(r * Math.Sin(t)), (float)(-r * Math.Cos(t)));

            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                using (SolidBrush the_brush = new SolidBrush(Color.Blue))
                {
                    for (int i = 0; i <= num_lines; i++)
                    {
                        t = i * Period * Math.PI / num_lines;
                        r = 5 * (1 + Math.Sin(11 * t / 5))
                            - 4 * Math.Pow(Math.Sin(17 * t / 3), 4)
                            * Math.Pow(Math.Sin(2 * Math.Cos(3 * t) - 28 * t), 8);
                        PointF pt0 = pt1;
                        pt1 = new PointF((float)(r * Math.Sin(t)), (float)(r * Math.Cos(t)));
                        Color the_color = GetColor(t);

                        // Fill the triangle from this edge to the origin.
                        the_brush.Color = Color.FromArgb(64,
                            the_color.R, the_color.G, the_color.B);
                        PointF[] pts = { pt0, pt1, new PointF(0, 0) };
                        e.Graphics.FillPolygon(the_brush, pts);

                        // Draw the curve's outer edge.
                        the_pen.Color = the_color;
                        e.Graphics.DrawLine(the_pen, pt0, pt1);
                    }
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

        // The height of a hexagon.
        private const float HexHeight = 50;

        // Selected hexagons.
        private List<PointF> Hexagons = new List<PointF>();

#if FIG34
        // The selected search rectangle.
        // Used to draw Figures 3 and 4.
        private List<RectangleF> TestRects = new List<RectangleF>();
#endif

        // Redraw the grid.
        private void pictureBox_hex_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the selected hexagons.
            foreach (PointF point in Hexagons)
            {
                e.Graphics.FillPolygon(Brushes.LightBlue,
                    HexToPoints(HexHeight, point.X, point.Y));
            }

            // Draw the grid.
            DrawHexGrid(e.Graphics, Pens.Black,
                0, pictureBox_hex.ClientSize.Width,
                0, pictureBox_hex.ClientSize.Height,
                HexHeight);

#if FIG34
            // Draw the selected rectangles for Figures 3 and 4.
            using (Pen pen = new Pen(Color.Red, 3))
            {
                pen.DashStyle = DashStyle.Dash;
                foreach (RectangleF rect in TestRects)
                {
                    e.Graphics.DrawRectangle(pen, Rectangle.Round(rect));
                }
            }
#endif
        }

        // Draw a hexagonal grid for the indicated area.
        // (You might be able to draw the hexagons without
        // drawing any duplicate edges, but this is a lot easier.)
        private void DrawHexGrid(Graphics gr, Pen pen,
            float xmin, float xmax, float ymin, float ymax,
            float height)
        {
            // Loop until a hexagon won't fit.
            for (int row = 0; ; row++)
            {
                // Get the points for the row's first hexagon.
                PointF[] points = HexToPoints(height, row, 0);

                // If it doesn't fit, we're done.
                if (points[4].Y > ymax) break;

                // Draw the row.
                for (int col = 0; ; col++)
                {
                    // Get the points for the row's next hexagon.
                    points = HexToPoints(height, row, col);

                    // If it doesn't fit horizontally,
                    // we're done with this row.
                    if (points[3].X > xmax) break;

                    // If it fits vertically, draw it.
                    if (points[4].Y <= ymax)
                    {
                        gr.DrawPolygon(pen, points);

#if FIG1
                        // Label the hexagon (for Figure 1).
                        using (StringFormat sf = new StringFormat())
                        {
                            sf.Alignment = StringAlignment.Center;
                            sf.LineAlignment = StringAlignment.Center;
                            float x = (points[0].X + points[3].X) / 2;
                            float y = (points[1].Y + points[4].Y) / 2;
                            string label = "(" + row.ToString() + ", " +
                                col.ToString() + ")";
                            gr.DrawString(label, this.Font,
                                Brushes.Black, x, y, sf);
                        }
#endif
                    }
                }
            }
        }

        private void pictureBox_hex_Resize(object sender, EventArgs e)
        {
            pictureBox_hex.Refresh();
        }

        // Display the row and column under the mouse.
        private void pictureBox_hex_MouseMove(object sender, MouseEventArgs e)
        {
            int row, col;
            PointToHex(e.X, e.Y, HexHeight, out row, out col);
            this.Text = "(" + row + ", " + col + ")";
        }

        // Add the clicked hexagon to the Hexagons list.
        private void pictureBox_hex_MouseClick(object sender, MouseEventArgs e)
        {
            int row, col;
            PointToHex(e.X, e.Y, HexHeight, out row, out col);
            Hexagons.Add(new PointF(row, col));

#if FIG34
            // Used to draw Figures 3 and 4.
            PointF[] points = HexToPoints(HexHeight, row, col);
            TestRects.Add(new RectangleF(
                points[0].X, points[1].Y,
                0.75f * (points[3].X - points[0].X),
                points[4].Y - points[1].Y));
#endif

            pictureBox_hex.Refresh();
        }

        // Return the width of a hexagon.
        private float HexWidth(float height)
        {
            return (float)(4 * (height / 2 / Math.Sqrt(3)));
        }

        // Return the row and column of the hexagon at this point.
        private void PointToHex(float x, float y, float height,
            out int row, out int col)
        {
            // Find the test rectangle containing the point.
            float width = HexWidth(height);
            col = (int)(x / (width * 0.75f));

            if (col % 2 == 0)
                row = (int)(y / height);
            else
                row = (int)((y - height / 2) / height);

            // Find the test area.
            float testx = col * width * 0.75f;
            float testy = row * height;
            if (col % 2 == 1) testy += height / 2;

            // See if the point is above or
            // below the test hexagon on the left.
            bool is_above = false, is_below = false;
            float dx = x - testx;
            if (dx < width / 4)
            {
                float dy = y - (testy + height / 2);
                if (dx < 0.001)
                {
                    // The point is on the left edge of the test rectangle.
                    if (dy < 0) is_above = true;
                    if (dy > 0) is_below = true;
                }
                else if (dy < 0)
                {
                    // See if the point is above the test hexagon.
                    if (-dy / dx > Math.Sqrt(3)) is_above = true;
                }
                else
                {
                    // See if the point is below the test hexagon.
                    if (dy / dx > Math.Sqrt(3)) is_below = true;
                }
            }

            // Adjust the row and column if necessary.
            if (is_above)
            {
                if (col % 2 == 0) row--;
                col--;
            }
            else if (is_below)
            {
                if (col % 2 == 1) row++;
                col--;
            }
        }

        // Return the points that define the indicated hexagon.
        private PointF[] HexToPoints(float height, float row, float col)
        {
            // Start with the leftmost corner of the upper left hexagon.
            float width = HexWidth(height);
            float y = height / 2;
            float x = 0;

            // Move down the required number of rows.
            y += row * height;

            // If the column is odd, move down half a hex more.
            if (col % 2 == 1) y += height / 2;

            // Move over for the column number.
            x += col * (width * 0.75f);

            // Generate the points.
            return new PointF[]
                {
                    new PointF(x, y),
                    new PointF(x + width * 0.25f, y - height / 2),
                    new PointF(x + width * 0.75f, y - height / 2),
                    new PointF(x + width, y),
                    new PointF(x + width * 0.75f, y + height / 2),
                    new PointF(x + width * 0.25f, y + height / 2),
                };
        }

        // Draw the graph.
        private void pictureBox_polar_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(Color.White);

            // Set up a transformation to map the region
            // -2.1 <= X <= 2.1, -2.1 <= Y <= 2.1 onto the  Bitmap.
            RectangleF rect = new RectangleF(-2.1f, -2.1f, 4.2f, 4.2f);
            PointF[] pts =
                    {
                        new PointF(0, H),
                        new PointF(W, H),
                        new PointF(0, 0),
                    };
            //e.Graphics
            e.Graphics.Transform = new Matrix(rect, pts);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            using (Pen thin_pen = new Pen(Color.Blue, 0))
            {
                // Draw the X and Y axes.
                thin_pen.Color = Color.Blue;
                e.Graphics.DrawLine(thin_pen, -2.1f, 0, 2.1f, 0);
                const float big_tick = 0.1f;
                const float small_tick = 0.05f;
                for (float x = (int)-2.1f; x <= 2.1f; x += 1)
                    e.Graphics.DrawLine(thin_pen, x, -small_tick, x, small_tick);
                for (float x = (int)-2.1f + 0.5f; x <= 2.1f; x += 1)
                    e.Graphics.DrawLine(thin_pen, x, -big_tick, x, big_tick);

                e.Graphics.DrawLine(thin_pen, 0, -2.1f, 0, 2.1f);
                for (float y = (int)-2.1f; y <= 2.1f; y += 1)
                    e.Graphics.DrawLine(thin_pen, -small_tick, y, small_tick, y);
                for (float y = (int)-2.1f + 0.5f; y <= 2.1f; y += 1)
                    e.Graphics.DrawLine(thin_pen, -big_tick, y, big_tick, y);

                // Draw the graph.
                DrawGraph(e.Graphics);
            }
        }

        // Draw the graph on a Bitmap.
        private void DrawGraph(Graphics gr)
        {
            // Generate the points.
            double t = 0;
            const double dt = Math.PI / 100.0;
            const double two_pi = 2 * Math.PI;
            List<PointF> points = new List<PointF>();
            while (t <= two_pi)
            {
                double r = 2 * Math.Sin(5 * t);
                float x = (float)(r * Math.Cos(t));
                float y = (float)(r * Math.Sin(t));
                points.Add(new PointF(x, y));
                t += dt;
            }

            // Draw the curve.
            using (Pen thin_pen = new Pen(Color.Red, 0))
            {
                gr.DrawPolygon(thin_pen, points.ToArray());
            }
        }








    }
}
