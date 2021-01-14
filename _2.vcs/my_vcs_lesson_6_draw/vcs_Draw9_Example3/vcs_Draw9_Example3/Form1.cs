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

namespace vcs_Draw9_Example3
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
            lblStatus.Text = "";
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
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 4, y_st + dy * 2);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 4, y_st + dy * 3);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button24.Location = new Point(x_st + dx * 4, y_st + dy * 4);

            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button28.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button29.Location = new Point(x_st + dx * 4, y_st + dy * 5);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button34.Location = new Point(x_st + dx * 4, y_st + dy * 6);

            button35.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button36.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button39.Location = new Point(x_st + dx * 4, y_st + dy * 7);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button41.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 8);

            bt_save.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            bt_exit.Location = new Point(x_st + dx * 4, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            ClientSize = new Size(button4.Right + 20, richTextBox1.Bottom + 20);    //自動表單邊界
        }

        // Drawing objects.
        private const int EllipseMargin = 10;
        private int EllipseCx, EllipseCy, EllipseWidth, EllipseHeight;
        private List<PointF> LinePoints = null;

        private void button0_Click(object sender, EventArgs e)
        {
            MakeDrawingObjects();

            if ((EllipseWidth <= 0) || (EllipseHeight <= 0))
                return;

            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Fill and outline the ellipse.
            g.FillEllipse(Brushes.LightBlue, EllipseMargin, EllipseMargin, EllipseWidth, EllipseHeight);
            g.DrawEllipse(Pens.Blue, EllipseMargin, EllipseMargin, EllipseWidth, EllipseHeight);

            // Draw the lines.
            g.DrawLines(Pens.Blue, LinePoints.ToArray());
        }

        // Make the drawing objects.
        private void MakeDrawingObjects()
        {
            // Calculate the ellipse parameters.
            EllipseWidth = this.pictureBox1.ClientSize.Width - 2 * EllipseMargin;
            EllipseHeight = this.pictureBox1.ClientSize.Height - 2 * EllipseMargin;

            // Make random lines connecting points
            // on the edge of the ellipse.
            EllipseCx = this.pictureBox1.ClientSize.Width / 2;
            EllipseCy = this.pictureBox1.ClientSize.Height / 2;
            Random rand = new Random();
            double circumference = 2 * Math.PI * Math.Sqrt(
                (EllipseWidth * EllipseWidth + EllipseHeight * EllipseHeight) / 2);
            int num_points = (int)(circumference / 40);
            LinePoints = new List<PointF>();
            for (int i = 0; i < num_points; i++)
            {
                double theta1 = 2 * Math.PI * rand.NextDouble();
                float x1 = (float)(EllipseCx + Math.Cos(theta1) * EllipseWidth / 2);
                float y1 = (float)(EllipseCy + Math.Sin(theta1) * EllipseHeight / 2);
                LinePoints.Add(new PointF(x1, y1));

                double theta2 = 2 * Math.PI * rand.NextDouble();
                float x2 = (float)(EllipseCx + Math.Cos(theta2) * EllipseWidth / 2);
                float y2 = (float)(EllipseCy + Math.Sin(theta2) * EllipseHeight / 2);
                LinePoints.Add(new PointF(x2, y2));
            }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            Color color_background = Color.Blue;
            Color color_foreground = Color.Black;
            Font f = new Font("Times New Roman", 20F);
            int width = 50;
            int boder_size = 5; //寫0為無邊框

            richTextBox1.Text += "製作數字球並存檔\n";
            richTextBox1.Text += "背景色\t" + color_background + "\n";
            richTextBox1.Text += "前景色\t" + color_foreground + "\n";
            richTextBox1.Text += "字型\t" + f.Name + ", " + f.Size.ToString() + "\n";
            richTextBox1.Text += "大小\t" + width + "\n";
            richTextBox1.Text += "框線大小\t" + boder_size.ToString() + "\n";

            int first = 3;
            int last = 6;

            pictureBox1.Image = MakeNumberBitmap(width, color_background, color_foreground, boder_size, f, last.ToString());

            int i;
            // Make the files.
            for (i = first; i <= last; i++)
            {
                // Make the file.
                Bitmap bm = MakeNumberBitmap(width, color_background, color_foreground, boder_size, f, i.ToString());

                // Save the file.
                bm.Save("Number" + i.ToString() + ".png", ImageFormat.Png);
            }
            richTextBox1.Text += "完成\n";
        }

        // Make a bitmap containing the indicated text.
        private Bitmap MakeNumberBitmap(int width, Color bg_color, Color fg_color, int border_size, Font fg_font, string txt)
        {
            // Size the bitmap.
            Bitmap bm = new Bitmap(width, width);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.TextRenderingHint = TextRenderingHint.AntiAlias;

                // Make the background transparent.
                gr.Clear(Color.Transparent);

                // Fill the background.
                Rectangle rect;
                const int margin = 2;
                int rect_width;


                if (border_size == 0)
                {
                    rect = new Rectangle(2, 2, width - 4, width - 4);
                }
                else
                {
                    rect_width = width - 2 * margin;
                    if (rect_width < 1) rect_width = 1;
                    rect = new Rectangle(margin, margin, rect_width, rect_width);
                }
                using (LinearGradientBrush bg_brush = new LinearGradientBrush(rect, Color.White, bg_color, LinearGradientMode.BackwardDiagonal))
                {
                    gr.FillEllipse(bg_brush, rect);
                }

                if (border_size == 0)
                {
                    // Outline the background.
                    if (border_size > 0)
                    {
                        using (Pen bg_pen = new Pen(bg_color))
                        {
                            gr.DrawEllipse(bg_pen, rect);
                        }
                    }
                }
                else
                {
                    rect_width = width - 2 * (margin + border_size);
                    if (rect_width < 1) rect_width = 1;
                    Rectangle inner_rect = new Rectangle(margin + border_size, margin + border_size, rect_width, rect_width);
                    using (LinearGradientBrush bg_brush = new LinearGradientBrush(inner_rect, bg_color, Color.White, LinearGradientMode.BackwardDiagonal))
                    {
                        gr.FillEllipse(bg_brush, inner_rect);
                    }
                }

                // Draw the sample text.
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    using (Brush fg_brush = new SolidBrush(fg_color))
                    {
                        gr.DrawString(txt, fg_font, fg_brush, rect, string_format);
                    }
                }
            }
            return bm;
        }


        private void button2_Click(object sender, EventArgs e)
        {
            DrawTranslucentText();
        }

        void DrawTranslucentText()
        {
            string filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bm = new Bitmap(filename);

            using (Graphics gr = Graphics.FromImage(bm))
            {
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;

                    int dy = (int)(gr.MeasureString("X", this.Font).Height * 1.5);
                    int x = bm.Width / 2;
                    int y = 30;

                    for (int opacity = 20; opacity <= 80; opacity += 10)
                    {
                        string txt = "透明度 " + opacity.ToString();
                        using (Brush brush = new SolidBrush(Color.FromArgb(opacity, 0, 0, 0)))
                        {
                            gr.DrawString(txt, this.Font, brush, x, y, string_format);
                        }
                        using (Brush brush = new SolidBrush(Color.FromArgb(opacity, 255, 255, 255)))
                        {
                            gr.DrawString(txt, this.Font, brush, x - 2, y - 2, string_format);
                        }
                        y += dy;
                    }
                }
                pictureBox1.Image = bm;
            }
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

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void button42_Click(object sender, EventArgs e)
        {
        }

        private void button43_Click(object sender, EventArgs e)
        {
        }

        private void button44_Click(object sender, EventArgs e)
        {
        }

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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // Tile the image.
            using (TextureBrush brush = new TextureBrush(new Bitmap(@"C:\______test_files\_material\ims2.bmp")))
            {
                e.Graphics.FillRectangle(brush, this.ClientRectangle);
            }
        }

        /*
        // Draw a rectangle in the indicated Rectangle
        // rounding the indicated corners.
        private GraphicsPath MakeRoundedRect(
            RectangleF rect, float xradius, float yradius,
            bool round_ul, bool round_ur, bool round_lr, bool round_ll)
        {
            // 在畫電池那邊
        }
        */


    }
}
