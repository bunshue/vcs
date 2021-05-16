using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureCrop1
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        //private int w = 0;  //擷取圖的寬
        //private int h = 0;  //擷取圖的高

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            W = bitmap1.Width;
            H = bitmap1.Height;
            pictureBox1.ClientSize = new Size(W, H);
            pictureBox2.ClientSize = new Size(W, H);
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

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_select_area = true;
                pt_st = e.Location; //起始點座標
            }
            else if (e.Button == MouseButtons.Right)
            {
                richTextBox1.Text += "滑鼠右鍵\t準備貼上選取的部分\n";
            }
        }

        // Continue selecting.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
                return;

            pt_sp = e.Location; //終點座標

            select_rectangle = MakeRectangle(pt_st, pt_sp);

            // Make a Bitmap to display the selection rectangle.
            Bitmap bmp = new Bitmap(bitmap1);

            // Draw the selection rectangle.
            using (Graphics g = Graphics.FromImage(bmp))
            {
                Pen select_pen = new Pen(Color.Green);
                select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                g.DrawRectangle(select_pen, select_rectangle);
            }
            // Display the temporary bitmap.
            pictureBox1.Image = bmp;
        }

        // Finish selecting the area.
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            // Do nothing if we're not selecting an area.
            if (flag_select_area == false)
                return;
            flag_select_area = false;

            // Display the original image.
            //pictureBox1.Image = bitmap1;  //仍應保留選取區域

            int w = select_rectangle.Width;
            int h = select_rectangle.Height;

            if (w < 1)
                return;
            if (h < 1)
                return;

            bitmap2 = new Bitmap(w, h);  //擷取部分位圖Bitmap
            using (Graphics g2 = Graphics.FromImage(bitmap2))
            {
                Rectangle dest_rectangle = new Rectangle(0, 0, w, h);
                g2.DrawImage(bitmap1, dest_rectangle, select_rectangle, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox2.Image = bitmap2;

            richTextBox1.Text += "select_rectangle = " + select_rectangle.ToString() + "\n";
        }

        // If the user presses Escape, cancel.
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //若有RichTextBox則此功能失效
            if (e.KeyChar == 27)
            {
                if (flag_select_area == false)
                    return;
                flag_select_area = false;

                // Stop selecting.
                bitmap2 = null;
                //g2 = null;
                pictureBox1.Image = bitmap1;
                pictureBox1.Refresh();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (bitmap2 != null)
            {
                string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                try
                {
                    bitmap2.Save(filename, ImageFormat.Bmp);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }

            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pt_st = " + pt_st.ToString() + "\n";
            richTextBox1.Text += "pt_sp = " + pt_sp.ToString() + "\n";
            int w = Math.Abs(pt_sp.X - pt_st.X) + 1;
            int h = Math.Abs(pt_sp.Y - pt_st.Y) + 1;
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";
        }

        // Copy the selected area to the clipboard.
        private void CopyToClipboard(Rectangle src_rect)
        {
            // Make a bitmap for the selected area's image.
            Bitmap bm = new Bitmap(src_rect.Width, src_rect.Height);

            // Copy the selected area into the bitmap.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                Rectangle dest_rect = new Rectangle(0, 0, src_rect.Width, src_rect.Height);
                gr.DrawImage(bitmap1, dest_rect, src_rect, GraphicsUnit.Pixel);
            }

            // Copy the selection image to the clipboard.
            Clipboard.SetImage(bm);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // Copy the selected area to the clipboard
            // and blank that area.

            //清空所選取的區域
            if (bitmap2 != null)
            {

                if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
                {
                    richTextBox1.Text += "未選定區域，無法剪下圖片\n";
                    return;
                }

                // Copy the selection to the clipboard.
                CopyToClipboard(select_rectangle);

                // Blank the selected area in the original image.
                using (Graphics gr = Graphics.FromImage(bitmap1))
                {
                    using (SolidBrush br = new SolidBrush(pictureBox1.BackColor))
                    {
                        gr.FillRectangle(br, select_rectangle);
                    }
                }

                // Display the result.
                bitmap2 = new Bitmap(bitmap1);
                pictureBox1.Image = bitmap2;

            }
            else
            {
                richTextBox1.Text += "無選取區域\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
            {
                richTextBox1.Text += "未選定區域，無法複製圖片\n";
                return;
            }

            // Copy the selected area to the clipboard.
            CopyToClipboard(select_rectangle);
            richTextBox1.Text += "已複製圖片\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Reset
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            W = bitmap1.Width;
            H = bitmap1.Height;
            pictureBox1.ClientSize = new Size(W, H);
            pictureBox2.ClientSize = new Size(W, H);
        }
    }
}
