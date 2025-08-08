using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ImageProcessing6
{
    public partial class Form1 : Form
    {
        // Select an area.
        private Point pt_st1 = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp1 = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private int StartX1 = -1;
        private int StartY1 = -1;
        private Bitmap BoxBitmap1 = null;
        private Graphics BoxGraphics1 = null;
        private Bitmap CurrentBitmap1 = null;

        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            pictureBox0.Image = Image.FromFile(filename);
            pictureBox1.Image = Image.FromFile(filename);
            pictureBox2.Image = Image.FromFile(filename);
            pictureBox3.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            CurrentBitmap1 = bitmap1.Clone() as Bitmap;
            pictureBox1.Image = bitmap1.Clone() as Image;
        }

        void show_item_location()
        {
            int W = 500;
            int H = 400;
            int x_st = 20;
            int y_st = 20;
            int dx = W + 50;
            int dy = H + 100;
            int dd1 = 40;
            int dd2 = 85;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label3.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_reset1.Location = new Point(x_st + dx * 1 + W - 60, y_st + dy * 0);

            label0.Text = "原圖";
            label1.Text = "選取區域做 Pixellate, 模糊化, 馬賽克化";
            label2.Text = "Gamma";
            label3.Text = "亮度";

            pictureBox0.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd2);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd2);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd2);
            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd2);

            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx * 2 + 150, y_st + dy * 0 + dd2);
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (CurrentBitmap1 == null)
                return;

            pt_st1 = e.Location;
            StartX1 = e.X;
            StartY1 = e.Y;

            // Make the selected image.
            BoxBitmap1 = new Bitmap(CurrentBitmap1);
            BoxGraphics1 = Graphics.FromImage(BoxBitmap1);
            pictureBox1.Image = BoxBitmap1;
        }

        // Continue selecting the area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (StartX1 < 0)
                return;

            // Restore the current image.
            BoxGraphics1.DrawImage(CurrentBitmap1, 0, 0);

            // Draw the selection rectangle.
            using (Pen select_pen = new Pen(Color.Red))
            {
                select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                Rectangle rect = MakeRectangle(StartX1, StartY1, e.X, e.Y);
                BoxGraphics1.DrawRectangle(select_pen, rect);
            }
            pictureBox1.Refresh();
        }

        // Pixellate the selected area and save the result.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (StartX1 < 0)
                return;

            PixellateRectangle(MakeRectangle(StartX1, StartY1, e.X, e.Y));

            // Remember we're not selecting any more.
            StartX1 = -1;
            StartY1 = -1;
            BoxGraphics1.Dispose();
            BoxGraphics1 = null;
            BoxBitmap1.Dispose();
            BoxBitmap1 = null;
        }

        // Pixellate the indicated rectangle.
        private void PixellateRectangle(Rectangle rect)
        {
            // Restrict the rectangle to fit on the image.
            int W = CurrentBitmap1.Width;
            int H = CurrentBitmap1.Height;
            rect = Rectangle.Intersect(rect, new Rectangle(0, 0, W, H));

            // Process the rectangle.
            const int box_wid = 8;
            using (Graphics gr = Graphics.FromImage(CurrentBitmap1))
            {
                int start_y = box_wid * (int)(rect.Top / box_wid);
                int start_x = box_wid * (int)(rect.Left / box_wid);
                for (int y = start_y; y <= rect.Bottom; y += box_wid)
                {
                    for (int x = start_x; x <= rect.Right; x += box_wid)
                    {
                        // Pixellate the area with upper left corner (x, y).

                        // Get the average of the pixels' color component values.
                        int total_r = 0, total_g = 0, total_b = 0, num_pixels = 0;
                        for (int dy = 0; dy < box_wid; dy++)
                        {
                            if (y + dy >= H) break;
                            for (int dx = 0; dx < box_wid; dx++)
                            {
                                if (x + dx >= W) break;
                                Color pixel_color = CurrentBitmap1.GetPixel(x + dx, y + dy);
                                total_r += pixel_color.R;
                                total_g += pixel_color.G;
                                total_b += pixel_color.B;
                                num_pixels++;
                            }
                        }
                        byte r = (byte)(total_r / num_pixels);
                        byte g = (byte)(total_g / num_pixels);
                        byte b = (byte)(total_b / num_pixels);
                        Color new_color = Color.FromArgb(255, r, g, b);

                        // Give all pixels in the box this color.
                        using (Brush br = new SolidBrush(new_color))
                        {
                            gr.FillRectangle(br, x, y, box_wid, box_wid);
                        }
                    }
                }

                // Refresh to show the new image.
                pictureBox1.Image = CurrentBitmap1;
                pictureBox1.Refresh();
            }
        }

        private void bt_reset1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = new Bitmap(filename);
            CurrentBitmap1 = bitmap1.Clone() as Bitmap;
            pictureBox1.Image = bitmap1.Clone() as Image;
        }
    }
}
