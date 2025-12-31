using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCrop6
{
    public partial class Form1 : Form
    {
        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        private Graphics g1 = null;
        private Graphics g2 = null;
        private bool MadeSelection = false;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.bmp";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);

            bitmap1 = new Bitmap(pictureBox1.Image);

            this.KeyPreview = true;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 305 + 10;
            dy = 400 + 10;

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);

        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        // Start selecting an area.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            // Save the starting point.
            flag_select_area = true;
            pt_st = e.Location; //起始點座標

            // Make the selected image.
            bitmap2 = new Bitmap(bitmap1);
            g2 = Graphics.FromImage(bitmap2);
            pictureBox1.Image = bitmap2;
        }

        // Continue selecting an area.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
                return;

            pt_sp = e.Location; //終點座標

            select_rectangle = MakeRectangle(pt_st, pt_sp);

            // Generate the new image with the selection rectangle.
            // Copy the original image.
            g2.DrawImage(bitmap1, 0, 0);

            // Draw the selection rectangle.
            Pen select_pen = new Pen(Color.Red);
            select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            g2.DrawRectangle(select_pen, select_rectangle);
            pictureBox1.Refresh();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
            {
                return;
            }

            flag_select_area = false;

            // Stop selecting.
            g2 = null;

            // Convert the points into a Rectangle.
            select_rectangle = MakeRectangle(pt_st, pt_sp);
            MadeSelection = ((select_rectangle.Width > 0) && (select_rectangle.Height > 0));

            richTextBox1.Text += "選取區域 : " + select_rectangle.ToString() + "\n";
        }

        // If the user presses Escape, cancel.
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 27)
            {
                if (flag_select_area == false)
                    return;
                flag_select_area = false;

                // Stop selecting.
                bitmap2 = null;
                g2 = null;
                pictureBox1.Image = bitmap1;
                pictureBox1.Refresh();

                // There is no selection.
                MadeSelection = false;
            }
        }

        //複製選取部分到剪貼簿
        private void CopyToClipboard(Rectangle src_rect)
        {
            // Make a bitmap for the selected area's image.
            Bitmap bm = new Bitmap(src_rect.Width, src_rect.Height);

            // Copy the selected area into the bitmap.
            using (Graphics g2 = Graphics.FromImage(bm))
            {
                //目標矩形
                Rectangle dest_rect = new Rectangle(0, 0, src_rect.Width, src_rect.Height);
                g2.DrawImage(bitmap1, dest_rect, src_rect, GraphicsUnit.Pixel);
                g2.DrawRectangle(Pens.Red, dest_rect);
            }

            //複製影像到剪貼簿
            Clipboard.SetImage(bm);
        }

       private void button5_Click(object sender, EventArgs e)
        {
            //複製選取部分到剪貼簿
            CopyToClipboard(select_rectangle);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (!Clipboard.ContainsImage())
            {
                richTextBox1.Text += "剪貼簿內 無影像\n";
                return;
            }
            richTextBox1.Text += "剪貼簿內 有影像\n";

            //取得剪貼簿內的影像
            Image clipboard_image = Clipboard.GetImage();

            Graphics g = this.pictureBox2.CreateGraphics();
            g.DrawRectangle(Pens.Red, 50, 50, 200, 200);

            //來源矩形
            int sx = 0;
            int sy = 0;
            int sw = clipboard_image.Width;
            int sh = clipboard_image.Height;
            Rectangle src_rect = new Rectangle(sx, sy, sw, sh);

            //目標矩形
            int dx = 0;
            int dy = 0;
            int dw = sw;
            int dh = sh;
            Rectangle dest_rect = new Rectangle(dx, dy, dw, dh);

            g.DrawImage(clipboard_image, dest_rect, src_rect, GraphicsUnit.Pixel);
            g.DrawRectangle(Pens.Magenta, dest_rect);

            pictureBox1.Image = bitmap1;
            MadeSelection = false;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //挖空
            Graphics g2 = Graphics.FromImage(bitmap1);
            SolidBrush br = new SolidBrush(pictureBox1.BackColor);
            g2.FillRectangle(br, select_rectangle);
            pictureBox1.Image = bitmap1;

            MadeSelection = false;//???
        }
    }
}
