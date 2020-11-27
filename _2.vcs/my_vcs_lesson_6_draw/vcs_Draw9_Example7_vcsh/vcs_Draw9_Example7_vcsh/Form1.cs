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
            x_st = 850;
            y_st = 10;
            dx = 110;
            dy = 45;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            bt_save.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(button2.Right + 20, richTextBox1.Bottom + 20);    //自動表單邊界
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
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
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



    }
}
