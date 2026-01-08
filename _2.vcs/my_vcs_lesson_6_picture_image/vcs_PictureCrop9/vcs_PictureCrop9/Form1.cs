using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat, PixelFormat

namespace vcs_PictureCrop9
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點

        int X1, Y1, X2, Y2;
        Rectangle rect = new Rectangle(0, 0, 0, 0);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
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
            dx = 200 + 10;
            dy = 60 + 10;

            pictureBox1.Size = new Size(850, 600);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox2.Size = new Size(380, 600);
            pictureBox2.Location = new Point(x_st + dx * 4 + 20, y_st + dy * 0);

            lb_x.Text = "x_st";
            lb_y.Text = "y_st";
            lb_w.Text = "w";
            lb_h.Text = "h";
            int ddy = 35;
            lb_x.Location = new Point(x_st + dx * 6, y_st + dy * 0 + ddy * 0);
            lb_y.Location = new Point(x_st + dx * 6, y_st + dy * 0 + ddy * 1);
            lb_w.Location = new Point(x_st + dx * 6, y_st + dy * 0 + ddy * 2);
            lb_h.Location = new Point(x_st + dx * 6, y_st + dy * 0 + ddy * 3);
            int ddx = 50;
            tb_x.Location = new Point(x_st + dx * 6 + ddx, y_st + dy * 0 + ddy * 0);
            tb_y.Location = new Point(x_st + dx * 6 + ddx, y_st + dy * 0 + ddy * 1);
            tb_w.Location = new Point(x_st + dx * 6 + ddx, y_st + dy * 0 + ddy * 2);
            tb_h.Location = new Point(x_st + dx * 6 + ddx, y_st + dy * 0 + ddy * 3);

            button1.Location = new Point(x_st + dx * 7 - 20, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 464);
            richTextBox1.Location = new Point(x_st + dx * 6 + 10, y_st + dy * 2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1620, 690);
            this.Text = "vcs_PictureCrop9";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void draw_grid(Graphics g)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            for (int i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);//垂直線
            }
            for (int j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);//水平線
            }
        }

        void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                pt_st = e.Location;//起始點座標
                pt_sp = e.Location;
                pictureBox1.Refresh();

                X1 = X2 = e.X;
                Y1 = Y2 = e.Y;
                flag_select_area = true;
            }
            else if (e.Button == MouseButtons.Right)
            {
                richTextBox1.Text += "滑鼠右鍵\t準備貼上選取的部分\n";
            }
        }

        void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_select_area==false)
            {
                return;
            }

            pt_sp = e.Location; //終點座標

            pictureBox1.Refresh();

            // Update the new circle's second corner.
            X2 = e.X;
            Y2 = e.Y;

            // Redraw.
            this.pictureBox1.Invalidate();
        }

        void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_select_area==false)
            {
                return;
            }
            flag_select_area = false;

            pictureBox1.Refresh();

            // Redraw.
            this.pictureBox1.Invalidate();
        }

        void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            //richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            e.Graphics.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);

            //e.Graphics.Clear(pictureBox1.BackColor);

            if (pt_st != pt_sp)
            {
                //e.Graphics.DrawRectangle(Pens.Black, pt_st, pt_sp);
                e.Graphics.DrawLine(Pens.Black, pt_st, pt_sp);
            }

            int width = 0;
            int height = 0;
            rect = new Rectangle(X1, Y1, width, height);
            if (X2 > X1)
            {
                rect.Width = X2 - X1;
            }
            else
            {
                rect.X = X2;
                rect.Width = X1 - X2;
            }
            if (Y2 > Y1)
            {
                rect.Height = Y2 - Y1;
            }
            else
            {
                rect.Y = Y2;
                rect.Height = Y1 - Y2;
            }

            draw_grid(e.Graphics);
            e.Graphics.DrawRectangle(Pens.Red, rect);

            tb_x.Text = rect.X.ToString();
            tb_y.Text = rect.Y.ToString();
            tb_w.Text = rect.Width.ToString();
            tb_h.Text = rect.Height.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += rect.ToString() + "\n";

            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);

            PixelFormat format = bitmap1.PixelFormat;
            //Bitmap cloneBitmap = bitmap1.Clone(rect, PixelFormat.DontCare);//PixelFormat.Format32bppArgb
            Bitmap cloneBitmap = bitmap1.Clone(rect, format);//PixelFormat.Format32bppArgb
            pictureBox2.Image = cloneBitmap;
        }
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個

