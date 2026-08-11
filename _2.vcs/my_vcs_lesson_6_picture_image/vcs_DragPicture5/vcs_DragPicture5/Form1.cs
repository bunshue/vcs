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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            // 加入事件
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);

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
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            pictureBox1.Size = new Size(800, 690);
            pictureBox1.Location = new Point(10, 10);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(820, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1150, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


