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
            x_st = 1500;
            y_st = 10;
            dx = 110;
            dy = 45;

            bt_save.Location = new Point(x_st + dx * 4, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            //pictureBox1.Location = new Point(10, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //ClientSize = new Size(button4.Right + 20, richTextBox1.Bottom + 20);    //自動表單邊界

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

        private void button2_Click(object sender, EventArgs e)
        {

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
