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
        string filename = @"C:\______test_files\elephant.jpg";

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

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
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            this.UpdateStyles();
            //以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            W = bitmap1.Width;
            H = bitmap1.Height;

            nud_w.Maximum = W;
            nud_h.Maximum = H;
            nud_x_st.Maximum = W;
            nud_y_st.Maximum = H;
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int pbx_W = 420;
            int pbx_H = 420;

            x_st = 10;
            y_st = 10;
            dx = pbx_W + 10;
            dy = pbx_H + 10;

            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox2.Size = new Size(pbx_W, pbx_H);
            //pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            //pictureBox2.SizeMode = PictureBoxSizeMode.Normal;

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

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_select_area = true;
                pt_st = e.Location; //起始點座標

                nud_x_st.Value = 0;
                nud_y_st.Value = 0;
                nud_w.Value = 0;
                nud_h.Value = 0;
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

            //richTextBox1.Text += "select_rectangle = " + select_rectangle.ToString() + "\n";

            nud_x_st.Value = select_rectangle.X;
            nud_y_st.Value = select_rectangle.Y;
            nud_w.Value = select_rectangle.Width;
            nud_h.Value = select_rectangle.Height;


            this.Text = "選取區域 : " + select_rectangle.ToString();
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

        private void button6_Click(object sender, EventArgs e)
        {
            if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
                return;

            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;
            String filename = Application.StartupPath + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            Bitmap bitmap = new Bitmap(pictureBox1.Image);
            select_rectangle = new Rectangle(x_st, y_st, w, h);
            //richTextBox1.Text += select_rectangle.ToString() + "\n";
            Bitmap cloneBitmap = bitmap.Clone(select_rectangle, PixelFormat.DontCare);
            cloneBitmap.Save(filename, ImageFormat.Bmp);
            richTextBox1.Text += "存截圖，存檔檔名：" + filename + "\n";
        }

        private void select_crop_area(object sender, EventArgs e)
        {
            if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
                return;

            int x_st = (int)nud_x_st.Value;
            int y_st = (int)nud_y_st.Value;
            int w = (int)nud_w.Value;
            int h = (int)nud_h.Value;

            Rectangle select_rectangle2 = new Rectangle(x_st, y_st, w, h);

            // Make a Bitmap to display the selection rectangle.
            Bitmap bmp = new Bitmap(bitmap1);

            // Draw the selection rectangle.
            using (Graphics g = Graphics.FromImage(bmp))
            {
                Pen select_pen = new Pen(Color.Red);
                select_pen.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                g.DrawRectangle(select_pen, select_rectangle2);
            }
            // Display the temporary bitmap.
            pictureBox1.Image = bmp;
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            if ((select_rectangle.Width <= 0) || (select_rectangle.Height <= 0))
                return;

            try
            {
                Graphics graphics = this.CreateGraphics();
                Bitmap bitmap = new Bitmap(pictureBox1.Image);
                Bitmap cloneBitmap = bitmap.Clone(select_rectangle, PixelFormat.DontCare);
                graphics.DrawImage(cloneBitmap, e.X, e.Y);
                Graphics g = pictureBox1.CreateGraphics();
                //SolidBrush myBrush = new SolidBrush(Color.White);
                //g.FillRectangle(myBrush, select_rectangle);   //將原圖剪下
            }
            catch
            { }
        }
    }
}
