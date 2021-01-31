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

        int W = 230;
        int H = 230;

        float rotating_angle = 0;

        private const int Period = 21;
        // Initialize the colors.
        private Color[] Colors = new Color[]
        {
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

        #region pictureBox_butterfly butterfly
        private const int period = 24;
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            redraw_all();

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

            label1.Location = new Point(x_st + dx * 0 - 20, y_st + dy * 0 - 30);
            numericUpDown1.Location = new Point(x_st + dx * 0 + 40, y_st + dy * 0 - 30);
            numericUpDown1.Value = 0;

            bt_save.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_exit.Location = new Point(x_st + dx * 0, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            richTextBox1.Size = new Size(richTextBox1.Size.Width - 70, this.Height - richTextBox1.Size.Height - 20);

            pictureBox_hex.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox_Chrysanthemum.Size = new Size(W, H);
            pictureBox_dragon.Size = new Size(W, H);
            pictureBox_dragon4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox_Chrysanthemum2.Size = new Size(W, H);
            pictureBox_polar.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox13.BackColor = Color.LightSalmon;
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox_snowflake.Size = new Size(W, H);
            pictureBox_snowflake2.Size = new Size(W, H);
            pictureBox_fractal1.Size = new Size(W, H);
            pictureBox_fractal2.Size = new Size(W, H);
            pictureBox_fractal3.Size = new Size(W, H);
            pictureBox22.Size = new Size(W, H);
            pictureBox_butterfly.Size = new Size(W, H);
            pictureBox_butterfly.BackColor = Color.Black;
            pictureBox_sierpinski1.Size = new Size(W, H);
            pictureBox_sierpinski2.Size = new Size(W, H);

            x_st = 10;
            y_st = 10;
            dx = W + 70;
            dy = H + 45;

            pictureBox_Chrysanthemum.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox_Chrysanthemum2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox_hex.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox_snowflake.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox_snowflake2.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            pictureBox_butterfly.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox_polar.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            pictureBox_dragon.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox_dragon4.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 5, y_st + dy * 1);

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
            pictureBox_fractal3.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            pictureBox22.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            pictureBox_sierpinski1.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            pictureBox_sierpinski2.Location = new Point(x_st + dx * 5, y_st + dy * 3);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
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

        private void pictureBox_Chrysanthemum_Paint(object sender, PaintEventArgs e)
        {
            pictureBox_Chrysanthemum.BackColor = Color.Black;

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

        private void timer_change_Tick(object sender, EventArgs e)
        {
            numericUpDown1.Value++;
            if (numericUpDown1.Value == 5)
                numericUpDown1.Value = 0;
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

            pictureBox22.Refresh();
        }

        private void pictureBox_fractal1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void pictureBox_fractal2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void pictureBox_fractal3_Paint(object sender, PaintEventArgs e)
        {

        }


        #region sierpinski

        // Draw the carpet.
        private void DrawGasket1()
        {
            int Level = (int)numericUpDown1.Value;

            Bitmap bm = new Bitmap(
                pictureBox_sierpinski1.ClientSize.Width,
                pictureBox_sierpinski1.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(Color.White);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the top-level carpet.
                const float margin = 10;
                RectangleF rect = new RectangleF(
                    margin, margin,
                    pictureBox_sierpinski1.ClientSize.Width - 2 * margin,
                    pictureBox_sierpinski1.ClientSize.Height - 2 * margin);
                DrawRectangle(gr, Level, rect);
            }

            // Display the result.
            pictureBox_sierpinski1.Image = bm;

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

        #region pictureBox_butterfly butterfly

        // Draw the butterfly.
        private void pictureBox_butterfly_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(this.pictureBox_butterfly.BackColor);

            // Scale and translate.
            RectangleF world_rect =
                new RectangleF(-4.0f, -4.4f, 8.0f, 7.3f);
            float cx = (world_rect.Left + world_rect.Right) / 2;
            float cy = (world_rect.Top + world_rect.Bottom) / 2;

            // Center the world coordinates at origin.
            e.Graphics.TranslateTransform(-cx, -cy);

            // Scale to fill the form.
            float scale = Math.Min(
                this.pictureBox_butterfly.ClientSize.Width / world_rect.Width,
                this.pictureBox_butterfly.ClientSize.Height / world_rect.Height);
            e.Graphics.ScaleTransform(scale, scale, MatrixOrder.Append);

            // Move the result to center on the form.
            e.Graphics.TranslateTransform(
                this.pictureBox_butterfly.ClientSize.Width / 2,
                this.pictureBox_butterfly.ClientSize.Height / 2, MatrixOrder.Append);

            // Generate the points.
            PointF pt0, pt1;
            double t = 0;
            double expr =
                Math.Exp(Math.Cos(t))
                - 2 * Math.Cos(4 * t)
                - Math.Pow(Math.Sin(t / 12), 5);
            pt1 = new PointF(
                (float)(Math.Sin(t) * expr),
                (float)(-Math.Cos(t) * expr));
            using (Pen the_pen = new Pen(Color.Blue, 0))
            {
                const long num_lines = 5000;
                for (long i = 0; i < num_lines; i++)
                {
                    t = i * period * Math.PI / num_lines;
                    expr =
                        Math.Exp(Math.Cos(t))
                        - 2 * Math.Cos(4 * t)
                        - Math.Pow(Math.Sin(t / 12), 5);
                    pt0 = pt1;
                    pt1 = new PointF(
                        (float)(Math.Sin(t) * expr),
                        (float)(-Math.Cos(t) * expr));
                    the_pen.Color = GetColor(t);
                    e.Graphics.DrawLine(the_pen, pt0, pt1);
                }
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
    
    }
}
