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

namespace vcs_Draw9_Example6_vcsh_text
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        int W = 250;
        int H = 250;

        //可以變大變小的Label 與 動態文字
        int label_size_w_old = 0;
        int label_size_h_old = 0;
        // The PictureBox's current size.
        private float StartWidth;
        private int StartHeight;
        private float EndWidth = 260;
        private float Dx, CurrentWidth;
        private int TicksToGo, TotalTicks;
        // Information about the string to draw.
        private const string LabelText = "群曜醫電股份有限公司";
        //private const string LabelText = "C# Programming";
        private Font TextFont;
        private float[] CharacterWidths;
        private float TotalCharacterWidth;

        #region rotate_brush
        // The polygon's points.
        private PointF[] PolygonPoints;

        // The path.
        private GraphicsPath Path;

        // The rectangle where we will draw.
        private Rectangle DrawingArea;

        // Offset when assigning colors.
        private int ColorOffset = 0;
        #endregion

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the labels display only borders.
            //label1.Text = "";
            label2.Text = "";
            label1.BackColor = Color.Transparent;
            label2.BackColor = Color.Transparent;

            // (Alternatively just hide them.)
            label1.Visible = true;  //畫label的框
            label2.Visible = true;  //畫label的框

            show_item_location();


            //可以變大變小的Label 與 動態文字
            label_size_w_old = label_size.Size.Width;
            label_size_h_old = label_size.Size.Height;

            // Set the initial size.
            StartWidth = pictureBox_stretching.Size.Width;
            StartHeight = pictureBox_stretching.Size.Height;
            CurrentWidth = StartWidth;

            // Stretch for 2 seconds.
            TotalTicks = 2 * 1000 / timer_text.Interval;
            Dx = (EndWidth - StartWidth) / TotalTicks;

            // Make the font and measure the characters.
            CharacterWidths = new float[LabelText.Length];
            TextFont = new Font("Times New Roman", 16);
            using (Graphics gr = this.CreateGraphics())
            {
                for (int i = 0; i < LabelText.Length; i++)
                {
                    SizeF ch_size = gr.MeasureString(LabelText.Substring(i, 1), TextFont);
                    CharacterWidths[i] = ch_size.Width;
                }
            }
            TotalCharacterWidth = CharacterWidths.Sum();

            CurrentWidth = StartWidth;
            pictureBox_stretching.Size = new Size((int)StartWidth, pictureBox_stretching.Size.Height);
            pictureBox_stretching.Refresh();
            TicksToGo = TotalTicks;

            #region rotate_brush
            // Make points that define a polygon.
            // Double buffer to prevent flicker.
            this.DoubleBuffered = true;

            // Make the drawing area rectangle.
            const int margin = 10;
            DrawingArea = new Rectangle(
                margin, margin,
                pictureBox_rotate_brush.ClientSize.Width - 2 * margin,
                pictureBox_rotate_brush.ClientSize.Height - 2 * margin);

            // Make the polygon's points.
            PolygonPoints = MakePolygon(22, DrawingArea);

            // Make the brush's path.
            Path = new GraphicsPath();
            Path.AddPolygon(DoublePoints(PolygonPoints));
            #endregion
            ShowSample1();
            ShowSample2();
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
            x_st = 1530;
            y_st = 10;
            dx = 130;
            dy = 55;

            button0.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            bt_save.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            bt_exit.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 25);

            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W * 7 / 4, H);

            pictureBox_rotate_brush.Size = new Size(W * 2, H);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            pictureBox_rotate_brush.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox_image_string.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox_filled_text.Location = new Point(x_st + dx * 2, y_st + dy * 1 + 150);
            pictureBox_rainbow_text.Location = new Point(x_st + dx * 2 + 450, y_st + dy * 1 + 150);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //ClientSize = new Size(button2.Right + 10, richTextBox1.Bottom + 10);    //自動表單邊界
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;


        }

        private void button1_Click(object sender, EventArgs e)
        {
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
            // Draw a string with character bounds.
            int x_st = 100;
            int y_st = 570;
            int w = 450;
            int h = 120;
            int dy = h + 10;
            e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            Rectangle rect = new Rectangle(x_st, y_st, w, h);
            e.Graphics.DrawRectangle(new Pen(Color.Gray, 1), rect);
            using (Font font = new Font("Times New Roman", 60, FontStyle.Italic))
            {
                DrawStringWithCharacterBounds(e.Graphics, "Lion-mouse", font, rect);
            }

            w = 250;
            y_st += dy;
            rect = new Rectangle(x_st, y_st, w, h);
            e.Graphics.DrawRectangle(new Pen(Color.Gray, 1), rect);
            using (Font font = new Font("Times New Roman", 60, FontStyle.Regular))
            {
                DrawStringWithCharacterBounds(e.Graphics, "Lion", font, rect);
            }

            w = 250;
            x_st += 260;
            rect = new Rectangle(x_st, y_st, w, h);
            e.Graphics.DrawRectangle(new Pen(Color.Gray, 1), rect);
            using (Font font = new Font("Times New Roman", 60, FontStyle.Italic))
            {
                DrawStringWithCharacterBounds(e.Graphics, "Mouse", font, rect);
            }



            //利用label所在位置畫字，把字畫成直的
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;

                e.Graphics.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;

                DrawSidewaysText(e.Graphics, Font, Brushes.Black, label2.Bounds, string_format, "利用label所在位置畫字，把字畫成直的");
            }
        }

        // Draw sideways text in the indicated rectangle.
        private void DrawSidewaysText(Graphics gr, Font font, Brush brush, Rectangle bounds, StringFormat string_format, string txt)
        {
            // Make a rotated rectangle at the origin.
            Rectangle rotated_bounds = new Rectangle(0, 0, bounds.Height, bounds.Width);

            // Rotate.
            gr.ResetTransform();
            gr.RotateTransform(-90);

            // Translate to move the rectangle to the correct position.
            gr.TranslateTransform(bounds.Left, bounds.Bottom, System.Drawing.Drawing2D.MatrixOrder.Append);

            // Draw the text.
            gr.DrawString(txt, font, brush, rotated_bounds, string_format);
        }

        // Draw the string and the bounds for its characters.
        private void DrawStringWithCharacterBounds(Graphics gr, string text, Font font, Rectangle rect)
        {
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;

                // Draw the string.
                gr.DrawString(text, font, Brushes.Blue, rect, string_format);

                // Make a CharacterRange for the string's characters.
                List<CharacterRange> range_list = new List<CharacterRange>();
                for (int i = 0; i < text.Length; i++)
                {
                    range_list.Add(new CharacterRange(i, 1));
                }
                string_format.SetMeasurableCharacterRanges(range_list.ToArray());

                // Measure the string's character ranges.
                Region[] regions = gr.MeasureCharacterRanges(
                    text, font, rect, string_format);

                // Draw the character bounds.
                for (int i = 0; i < text.Length; i++)
                {
                    Rectangle char_rect = Rectangle.Round(regions[i].GetBounds(gr));
                    gr.DrawRectangle(Pens.Red, char_rect);
                }
            }
        }

        private float GradientStart = 0;
        private float Delta = 5f;

        // Make the PictureBox redraw.
        private void timer_moving_Tick(object sender, EventArgs e)
        {
            pictureBox_gradient.Refresh();
            pictureBox_text.Refresh();
        }

        // Draw the background with text on top.
        private void pictureBox_gradient_Paint(object sender, PaintEventArgs e)
        {
            // Shade the background.
            int wid = pictureBox_gradient.ClientSize.Width;
            ShadeRect(e.Graphics, GradientStart, GradientStart + wid);

            // Increase the start position.
            GradientStart += Delta;
            if (GradientStart >= wid) GradientStart = 0;

            // Draw some text.
            using (Font font = new Font("Times New Roman", 18, FontStyle.Bold))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    e.Graphics.DrawString("群曜醫電 Insight Medical Solutions Inc.",
                        font, Brushes.Black,
                        pictureBox_gradient.ClientSize.Width / 2,
                        pictureBox_gradient.ClientSize.Height / 2,
                        string_format);
                }
            }
        }

        // Fill the rectangle with a gradient that
        // shades from red to white to red.
        private void ShadeRect(Graphics gr, float xmin, float xmax)
        {
            using (LinearGradientBrush br = new LinearGradientBrush(
                new PointF(xmin, 0), new PointF(xmax, 0),
                Color.Red, Color.Red))
            {
                br.WrapMode = WrapMode.Tile;
                ColorBlend color_blend = new ColorBlend();
                color_blend.Colors = new Color[] { Color.Red, Color.White, Color.Red };
                color_blend.Positions = new float[] { 0, 0.5f, 1 };

                br.InterpolationColors = color_blend;
                gr.FillRectangle(br, pictureBox_gradient.ClientRectangle);
            }
        }

        // Draw the background with text on top.
        private void pictureBox_text_Paint(object sender, PaintEventArgs e)
        {
            // Clear the background.
            int wid = pictureBox_text.ClientSize.Width;
            e.Graphics.Clear(Color.White);

            // Make the gradient brush.
            using (LinearGradientBrush brush = new LinearGradientBrush(
                new PointF(GradientStart, 0),
                new PointF(GradientStart + wid, 0),
                Color.Red, Color.Red))
            {
                brush.WrapMode = WrapMode.Tile;
                ColorBlend color_blend = new ColorBlend();
                color_blend.Colors = new Color[]
                {
                    Color.Blue, Color.Blue,
                    Color.White, Color.Blue, Color.Blue
                };
                color_blend.Positions =
                    new float[] { 0, 0.4f, 0.5f, 0.6f, 1 };
                brush.InterpolationColors = color_blend;

                // Use the brush to draw some text.
                using (Font font = new Font("Times New Roman", 18, FontStyle.Bold))
                {
                    using (StringFormat string_format = new StringFormat())
                    {
                        string_format.Alignment = StringAlignment.Center;
                        string_format.LineAlignment = StringAlignment.Center;
                        e.Graphics.DrawString("群曜醫電 Insight Medical Solutions Inc.",
                            font, brush,
                            pictureBox_text.ClientSize.Width / 2,
                            pictureBox_text.ClientSize.Height / 2,
                            string_format);
                    }
                }
            }

            // Increase the start position.
            GradientStart += Delta;
            if (GradientStart >= wid) GradientStart = 0;
        }

        private int ProgressMinimum = 0;
        private int ProgressMaximum = 100;
        private int ProgressValue = 0;

        private void timer_progressbar_Tick(object sender, EventArgs e)
        {
            ProgressValue += 1;
            if (ProgressValue > ProgressMaximum)
            {
                ProgressValue = 0;
                //tmrWork.Enabled = false;
            }
            pictureBox_progressbar.Refresh();
        }

        // Show the progress.
        private void pictureBox_progressbar_Paint(object sender, PaintEventArgs e)
        {
            // Clear the background.
            e.Graphics.Clear(pictureBox_progressbar.BackColor);

            // Draw the progress bar.
            float fraction = (float)(ProgressValue - ProgressMinimum) / (ProgressMaximum - ProgressMinimum);
            int wid = (int)(fraction * pictureBox_progressbar.ClientSize.Width);
            e.Graphics.FillRectangle(Brushes.LightGreen, 0, 0, wid, pictureBox_progressbar.ClientSize.Height);

            // Draw the text.
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Center;
                sf.LineAlignment = StringAlignment.Center;
                int percent = (int)(fraction * 100);
                e.Graphics.DrawString(percent.ToString() + "%", this.Font, Brushes.Black, pictureBox_progressbar.ClientRectangle, sf);
            }
        }

        // Draw the text on the control.
        private void pictureBox_stretching_Paint(object sender, PaintEventArgs e)
        {
            // Use AntiAlias for the best result.
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAlias;
            e.Graphics.Clear(pictureBox_stretching.BackColor);

            SpaceTextToFit(e.Graphics, pictureBox_stretching.ClientRectangle,
                TextFont, Brushes.Red, LabelText);

        }

        // Draw text inserting space between characters
        // to make it fill the indicated width.
        private void SpaceTextToFit(Graphics gr, Rectangle rect, Font font, Brush brush, string text)
        {
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Near;
                string_format.LineAlignment = StringAlignment.Near;

                // Calculate the spacing.
                float space = (rect.Width - TotalCharacterWidth) / (text.Length - 1);

                // Draw the characters.
                PointF point = new PointF(rect.X, rect.Y);
                for (int i = 0; i < text.Length; i++)
                {
                    gr.DrawString(text[i].ToString(), font, brush, point);
                    point.X += CharacterWidths[i] + space;
                }
            }
        }

        int dw = 0;
        int dh = 0;
        private void timer_text_Tick(object sender, EventArgs e)
        {
            /*
             * 可以變大變小的Label
             * 屬性
             * BackColor
             * BorderStype 改 FixedSingle
             * AutoSize 改 False
             * 改 Size
            */
            dw++;
            dh++;
            if (dw > 50)
                dw = 0;
            if (dh > 50)
                dh = 0;
            label_size.Size = new Size(label_size_w_old + dw, label_size_h_old + dh);

            CurrentWidth += Dx;
            pictureBox_stretching.Size = new Size((int)CurrentWidth, StartHeight);
            pictureBox_stretching.Refresh();

            // If we're done moving, disable the Timer.
            if (--TicksToGo <= 0)
            {
                timer_text.Enabled = false;
                //TicksToGo = TotalTicks;
            }
        }

        #region rotate_brush
        // Return PointFs to define a polygon.
        private PointF[] MakePolygon(int num_points, Rectangle bounds)
        {
            // Make room for the points.
            PointF[] pts = new PointF[num_points];

            float sqrt2 = (float)Math.Sqrt(2.0);
            float rx = bounds.Width / 2f * sqrt2;
            float ry = bounds.Height / 2f * sqrt2;
            float cx = bounds.X + bounds.Width / 2f;
            float cy = bounds.Y + bounds.Height / 2f;

            // Start at the top.
            float theta = (float)(-Math.PI / 2.0);
            float dtheta = (float)(2.0 * Math.PI / num_points);
            for (int i = 0; i < num_points; i++)
            {
                pts[i] = new PointF((float)(cx + rx * Math.Cos(theta)), (float)(cy + ry * Math.Sin(theta)));
                theta += dtheta;
            }
            return pts;
        }

        // Insert a point between each of the polygon's points.
        private PointF[] DoublePoints(PointF[] points)
        {
            List<PointF> new_points = new List<PointF>();
            for (int i = 0; i < points.Length - 1; i++)
            {
                new_points.Add(points[i]);
                new_points.Add(PointBetween(points[i], points[i + 1]));
            }
            new_points.Add(points[points.Length - 1]);
            new_points.Add(PointBetween(points[0], points[points.Length - 1]));

            // Return the new points.
            return new_points.ToArray();
        }

        // Return a point between two points.
        private PointF PointBetween(PointF point1, PointF point2)
        {
            return new PointF(
                (point1.X + point2.X) / 2,
                (point1.Y + point2.Y) / 2);
        }

        // Draw the polygon.
        private void pictureBox_rotate_brush_Paint(object sender, PaintEventArgs e)
        {
            // Make a path gradient brush.
            using (PathGradientBrush br = new PathGradientBrush(Path))
            {
                // Define edge colors.
                Color[] edge_colors = new Color[PolygonPoints.Length * 2];
                Color[] color_series = new Color[]
                {
                    Color.Green,
                    Color.LightGreen,
                    Color.White,
                    Color.LightGreen,
                };
                for (int i = 0; i < edge_colors.Length; i++)
                {
                    edge_colors[i] = color_series[(i + ColorOffset) % color_series.Length];
                }
                br.SurroundColors = edge_colors;
                br.CenterColor = Color.White;
                ColorOffset++;

                // Fill the polygon.
                //e.Graphics.FillPolygon(br, PolygonPoints);
                e.Graphics.FillRectangle(br, DrawingArea);

                // Draw text over the background.
                using (Font font = new Font("Times New Roman", 30, FontStyle.Bold))
                {
                    using (StringFormat sf = new StringFormat())
                    {
                        sf.Alignment = StringAlignment.Center;
                        sf.LineAlignment = StringAlignment.Center;
                        e.Graphics.DrawString(LabelText, font, Brushes.Blue, DrawingArea, sf);
                    }
                }
            }
        }

        private void timer_rotate_brush_Tick(object sender, EventArgs e)
        {
            pictureBox_rotate_brush.Refresh();
        }
        #endregion


        #region 自動字型大小
        private void txtSample_TextChanged(object sender, EventArgs e)
        {
            ShowSample1();
            ShowSample2();
        }

        // Display the sample text as large as possible.
        private void ShowSample1()
        {
            string text = txtSample.Text;
            if (text.Length == 0) return;

            float font_size = GetFontSize(
                lblSample1, text, 10, 1, 1000);
            lblFontSize1.Text = font_size.ToString("0.0");
            lblSample1.Font = new Font(lblSample1.Font.FontFamily, font_size);
            lblSample1.Text = text;
        }

        // Return the largest font size that lets the text fit in the Label.
        private float GetFontSize(Label label, string text,
            int margin, float min_size, float max_size)
        {
            // Only bother if there's text.
            if (text.Length == 0) return min_size;

            // See how much room we have, allowing a bit
            // for the Label's internal margin.
            int wid = label.DisplayRectangle.Width - margin;
            int hgt = label.DisplayRectangle.Height - margin;

            // Make a Graphics object to measure the text.
            using (Graphics gr = label.CreateGraphics())
            {
                while (max_size - min_size > 0.1f)
                {
                    float pt = (min_size + max_size) / 2f;
                    using (Font test_font = new Font(label.Font.FontFamily, pt))
                    {
                        // See if this font is too big.
                        SizeF text_size = gr.MeasureString(text, test_font);
                        if ((text_size.Width > wid) || (text_size.Height > hgt))
                            max_size = pt;
                        else
                            min_size = pt;
                    }
                }
                return min_size;
            }
        }

        // Display the sample text as large as possible.
        private void ShowSample2()
        {
            string text = txtSample.Text;
            if (text.Length == 0) return;

            float font_size = GetFontSize2(
                lblSample2, text, 10, 1, 1000);
            lblFontSize2.Text = font_size.ToString("0.0");
            lblSample2.Font = new Font(lblSample2.Font.FontFamily, font_size);
            lblSample2.Text = text;
        }

        // Return the largest font size that lets the text fit in the Label.
        private float GetFontSize2(Label label, string text,
            int margin, float min_size, float max_size)
        {
            // Only bother if there's text.
            if (text.Length == 0) return min_size;

            // See how much room we have, allowing a bit
            // for the Label's internal margin.
            int wid = label.DisplayRectangle.Width - margin;
            int hgt = label.DisplayRectangle.Height - margin;

            // Make a Graphics object to measure the text.
            using (Graphics gr = label.CreateGraphics())
            {
                while (max_size - min_size > 0.1f)
                {
                    float pt = (min_size + max_size) / 2f;
                    using (Font test_font = new Font(label.Font.FontFamily, pt))
                    {
                        // See if this font is too big.
                        SizeF text_size = gr.MeasureString(text, test_font, wid);
                        if ((text_size.Width > wid) || (text_size.Height > hgt))
                            max_size = pt;
                        else
                            min_size = pt;
                    }
                }
                return min_size;
            }
        }
        #endregion


        #region 字串任意顏色
        // Return a random color.
        private Random rand = new Random();
        private Color[] colors =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
        };
        private Color RandomColor()
        {
            return colors[rand.Next(0, colors.Length)];
        }

        // Draw some text with each letter in a random color.
        private void pictureBox_random_color_Paint(object sender, PaintEventArgs e)
        {
            const string txt = "群曜醫電股份有限公司";

            // Make the font.
            using (Font the_font = new Font("Times New Roman", 30,
                FontStyle.Bold | FontStyle.Italic))
            {
                // Make a StringFormat object to use for text layout.
                using (StringFormat string_format = new StringFormat())
                {
                    // Center the text.
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    string_format.FormatFlags = StringFormatFlags.NoClip;

                    // Make CharacterRanges to indicate which
                    // ranges we want to measure.
                    CharacterRange[] ranges = new CharacterRange[txt.Length];
                    for (int i = 0; i < txt.Length; i++)
                    {
                        ranges[i] = new CharacterRange(i, 1);
                    }
                    string_format.SetMeasurableCharacterRanges(ranges);

                    // Measure the text to see where each character range goes.
                    Region[] regions =
                        e.Graphics.MeasureCharacterRanges(
                            txt, the_font, this.pictureBox_random_color.ClientRectangle,
                            string_format);

                    // Draw the characters one at a time.
                    for (int i = 0; i < txt.Length; i++)
                    {
                        // See where this character would be drawn.
                        RectangleF rectf = regions[i].GetBounds(e.Graphics);
                        Rectangle rect = new Rectangle(
                            (int)rectf.X, (int)rectf.Y,
                            (int)rectf.Width, (int)rectf.Height);

                        // Make a brush with a random color.
                        using (Brush the_brush = new SolidBrush(RandomColor()))
                        {
                            // Draw the character.
                            e.Graphics.DrawString(txt.Substring(i, 1),
                                the_font, the_brush, rectf, string_format);
                        }
                    }
                }
            }
        }
        #endregion


        #region 用圖片寫文字
        private void pictureBox_image_string_Paint(object sender, PaintEventArgs e)
        {
            // Make text filled with a single big image.
            // Make a brush containing the picture.
            using (TextureBrush the_brush = new TextureBrush(Properties.Resources.ColoradoFlowers))
            {
                // Draw the text.
                using (Font the_font = new Font("Times New Roman", 60, FontStyle.Bold))
                {
                    e.Graphics.DrawString("群曜醫電", the_font, the_brush, 0, 0);
                }
            }

            // Make text filled with a tiled image.
            // Make a brush containing the picture.
            using (TextureBrush the_brush = new TextureBrush(Properties.Resources.Smiley))
            {
                // Draw the text.
                using (Font the_font = new Font("Times New Roman", 40, FontStyle.Bold))
                {
                    e.Graphics.DrawString("股份有限公司", the_font, the_brush, 60, 90);
                }
            }
        }
        #endregion

        #region 文字內填滿文字
        private void pictureBox_filled_text_Paint(object sender, PaintEventArgs e)
        {
            // Make things smoother.
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Create the text path.
            GraphicsPath path = new GraphicsPath(FillMode.Alternate);

            // Draw text using a StringFormat to center it on the form.
            using (FontFamily font_family = new FontFamily("Times New Roman"))
            {
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;
                    sf.LineAlignment = StringAlignment.Center;
                    path.AddString("群曜醫電", font_family,
                        (int)FontStyle.Bold, 80,
                        this.pictureBox_filled_text.ClientRectangle, sf);
                }
            }

            // Make a bitmap containing the small brush's text.
            using (Font small_font = new Font("Times New Roman", 8))
            {
                // See how big the text will be.
                SizeF text_size = e.Graphics.MeasureString("Text", small_font);

                // Make a Bitmap to hold the text.
                Bitmap bm = new Bitmap(
                    (int)(2 * text_size.Width),
                    (int)(2 * text_size.Height));
                using (Graphics gr = Graphics.FromImage(bm))
                {
                    gr.Clear(Color.LightBlue);
                    gr.DrawString("Insight Medical Solutions Inc.", small_font, Brushes.Red, 0, 0);
                    gr.DrawString("Insight Medical Solutions Inc.", small_font, Brushes.Green, text_size.Width, 0);
                    gr.DrawString("Insight Medical Solutions Inc.", small_font, Brushes.Blue, -text_size.Width / 2, text_size.Height);
                    gr.DrawString("Insight Medical Solutions Inc.", small_font, Brushes.DarkOrange, text_size.Width / 2, text_size.Height);
                    gr.DrawString("Insight Medical Solutions Inc.", small_font, Brushes.Blue, 1.5f * text_size.Width, text_size.Height);
                }

                // Fill the path.
                using (TextureBrush br = new TextureBrush(bm))
                {
                    e.Graphics.FillPath(br, path);
                }
            }

            // Outline the path.
            using (Pen pen = new Pen(Color.Black, 3))
            {
                e.Graphics.DrawPath(pen, path);
            }

        }
        #endregion


        //彩色文字 ST
        private void pictureBox_rainbow_text_Paint(object sender, PaintEventArgs e)
        {
            const string Txt = "群曜醫電";

            // Make the result smoother.
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            // Make a font.
            using (Font the_font = new Font("Times New Roman", 80, FontStyle.Bold, GraphicsUnit.Pixel))
            {
                // Get the font's metrics.
                FontInfo font_info = new FontInfo(e.Graphics, the_font);

                // See how big the text is.
                SizeF text_size = e.Graphics.MeasureString(Txt, the_font);
                int x0 = (int)((this.pictureBox_rainbow_text.ClientSize.Width - text_size.Width) / 2);
                int y0 = (int)((this.pictureBox_rainbow_text.ClientSize.Height - text_size.Height) / 2);

                // Get the Y coordinates that the brush should span.
                int brush_y0 = (int)(y0 + font_info.InternalLeadingPixels);
                int brush_y1 = (int)(y0 + font_info.AscentPixels);

                // Fudge the brush down a smidgen.
                brush_y0 += (int)(font_info.InternalLeadingPixels);
                brush_y1 += 5;

                // Make a brush to color the area.
                using (LinearGradientBrush the_brush = new LinearGradientBrush(
                    new Point(x0, brush_y0),
                    new Point(x0, brush_y1),
                    Color.Red, Color.Violet))
                {
                    Color[] colors = new Color[]
                    {
                        Color.FromArgb(255, 0, 0),
                        Color.FromArgb(255, 0, 0),
                        Color.FromArgb(255, 128, 0),
                        Color.FromArgb(255, 255, 0),
                        Color.FromArgb(0, 255, 0),
                        Color.FromArgb(0, 255, 128),
                        Color.FromArgb(0, 255, 255),
                        Color.FromArgb(0, 128, 255),
                        Color.FromArgb(0, 0, 255),
                        Color.FromArgb(0, 0, 255),
                    };
                    int num_colors = colors.Length;
                    float[] blend_positions = new float[num_colors];
                    for (int i = 0; i < num_colors; i++)
                    {
                        blend_positions[i] = i / (num_colors - 1f);
                    }

                    ColorBlend color_blend = new ColorBlend();
                    color_blend.Colors = colors;
                    color_blend.Positions = blend_positions;
                    the_brush.InterpolationColors = color_blend;

                    // Draw the text.
                    e.Graphics.DrawString(Txt, the_font, the_brush, x0, y0);
                }
            }
        }
        //彩色文字 SP

        //把字體旋轉90度 ST
        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            using (Font the_font = new Font("Comic Sans MS", 20))
            {

                int x_st = 5;
                int y_st = 220;
                int dx;

                dx = 35;
                DrawRotatedTextAt(e.Graphics, -90, "January", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "February", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "March", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "April", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "May", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "June", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "July", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "August", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "September", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "October", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "November", x_st, y_st, the_font, Brushes.Red);
                x_st += dx;
                DrawRotatedTextAt(e.Graphics, -90, "December", x_st, y_st, the_font, Brushes.Red);
            }

        }

        // Draw a rotated string at a particular position.
        private void DrawRotatedTextAt(Graphics gr, float angle, string txt, int x, int y, Font the_font, Brush the_brush)
        {
            // Save the graphics state.
            GraphicsState state = gr.Save();
            gr.ResetTransform();

            // Rotate.
            gr.RotateTransform(angle);

            // Translate to desired position. Be sure to append
            // the rotation so it occurs after the rotation.
            gr.TranslateTransform(x, y, MatrixOrder.Append);

            // Draw the text at the origin.
            gr.DrawString(txt, the_font, the_brush, 0, 0);

            // Restore the graphics state.
            gr.Restore(state);
        }
        //把字體旋轉90度 SP

    
    }
}
