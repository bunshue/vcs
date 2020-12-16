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
            x_st = 1050;
            y_st = 10;
            dx = 130;
            dy = 55;

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
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 25);

            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(button2.Right + 10, richTextBox1.Bottom + 10);    //自動表單邊界
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




    }
}
