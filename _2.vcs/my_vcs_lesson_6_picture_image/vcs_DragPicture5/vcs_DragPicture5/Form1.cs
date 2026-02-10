using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture5
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        Bitmap bitmap0; //放底圖
        Bitmap bitmap1; //放貼上的小圖
        Graphics g;

        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        bool flag_mouse_down = false;
        Point pt_picture_position = Point.Empty;
        int W = 0;
        int H = 0;
        int w = 0;
        int h = 0;

        PictureBox pictureBox1 = new PictureBox();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox1.Width = 1200;
            pictureBox1.Height = 800;
            pictureBox1.Location = new Point(0, 0);
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.BackColor = SystemColors.ControlLight;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            // 加入事件
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);

            this.Controls.Add(pictureBox1);	// 將控件加入表單

            pt_picture_position = new Point(0, 0);

            W = pictureBox1.Width;
            H = pictureBox1.Height;

            bitmap0 = new Bitmap(W, H);

            g = Graphics.FromImage(bitmap0);
            g.Clear(SystemColors.ControlLight);

            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            w = bitmap1.Width;
            h = bitmap1.Height;

            /*
            int x_st = (W - w) / 2;
            int y_st = (H - h) / 2;
            g.DrawImage(bitmap1, x_st, y_st, bitmap1.Width, bitmap1.Height);
            */

            g.DrawImage(bitmap1, pt_picture_position.X, pt_picture_position.Y, bitmap1.Width, bitmap1.Height);

            /*
            int i;
            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Red, i, 0, i, H);
            }
            for (i = 0; i <= H; i += 100)
            {
                g.DrawLine(Pens.Red, 0, i, W, i);
            }
            */

            pictureBox1.Image = bitmap0;
        }

        void show_item_location()
        {
            richTextBox1.Location = new Point(1650, 10);
            //richTextBox1.Visible = false;

            pictureBox1.Size = new Size(1600, 900);
            pictureBox1.Location = new Point(10, 10);

            //控件位置
            //bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            //離開按鈕的寫法
            bt_exit_setup();

            //最小化按鈕的寫法
            bt_minimize_setup();
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

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_mouse_down = true;
                pt_st = e.Location; //起始點座標
                //richTextBox1.Text += "Down : " + e.Location.ToString() + "\n";
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if ((e.Location.X >= pt_picture_position.X) && (e.Location.X <= (pt_picture_position.X + bitmap1.Width))
                && (e.Location.Y >= pt_picture_position.Y) && (e.Location.Y <= (pt_picture_position.Y + bitmap1.Height)))
            {
                Cursor = Cursors.Hand;
            }
            else
            {
                Cursor = Cursors.Default;
            }

            if (flag_mouse_down == false)
            {
                return;
            }

            pt_sp = e.Location; //終點座標
            //richTextBox1.Text += "Up : " + e.Location.ToString() + "\n";
            //richTextBox1.Text += "ST : " + pt_st.ToString() + "\n";
            //richTextBox1.Text += "SP : " + pt_sp.ToString() + "\n";

            int dx = pt_sp.X - pt_st.X;
            int dy = pt_sp.Y - pt_st.Y;

            //richTextBox1.Text += "old : " + pt_picture_position.ToString() + "\n";
            pt_picture_position = new Point(pt_picture_position.X + dx, pt_picture_position.Y + dy);

            //richTextBox1.Text += "dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            //richTextBox1.Text += "new : " + pt_picture_position.ToString() + "\n";

            //bitmap0 = new Bitmap(W, H);

            //g = Graphics.FromImage(bitmap0);
            g.Clear(SystemColors.ControlLight);


            g.DrawImage(bitmap1, pt_picture_position.X, pt_picture_position.Y, bitmap1.Width, bitmap1.Height);

            /*
            int i;
            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Red, i, 0, i, H);
            }
            for (i = 0; i <= H; i += 100)
            {
                g.DrawLine(Pens.Red, 0, i, W, i);
            }
            */

            pictureBox1.Image = bitmap0;

            pt_st = e.Location;
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == false)
            {
                return;
            }
            flag_mouse_down = false;

            pt_sp = e.Location; //終點座標
            //richTextBox1.Text += "Up : " + e.Location.ToString() + "\n";
            //richTextBox1.Text += "ST : " + pt_st.ToString() + "\n";
            //richTextBox1.Text += "SP : " + pt_sp.ToString() + "\n";

            int dx = pt_sp.X - pt_st.X;
            int dy = pt_sp.Y - pt_st.Y;

            //richTextBox1.Text += "old : " + pt_picture_position.ToString() + "\n";
            pt_picture_position = new Point(pt_picture_position.X + dx, pt_picture_position.Y + dy);

            //richTextBox1.Text += "dx = " + dx.ToString() + ", dy = " + dy.ToString() + "\n";
            //richTextBox1.Text += "new : " + pt_picture_position.ToString() + "\n";

            bitmap0 = new Bitmap(W, H);

            g = Graphics.FromImage(bitmap0);

            g.DrawImage(bitmap1, pt_picture_position.X, pt_picture_position.Y, bitmap1.Width, bitmap1.Height);
            /*
            int i;
            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Red, i, 0, i, H);
            }
            for (i = 0; i <= H; i += 100)
            {
                g.DrawLine(Pens.Red, 0, i, W, i);
            }
            */

            pictureBox1.Image = bitmap0;

            pt_st = e.Location;
        }
    }
}
