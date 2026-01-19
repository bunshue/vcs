using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode

// 滑鼠操作畫圖相關

namespace vcs_MousePaint2
{
    public partial class Form1 : Form
    {
        //pictureBox0 直線連線 ST
        Point[] pt = new Point[300];
        int pt_index = -1;
        bool flag_mouse_down = false;
        //pictureBox0 直線連線 SP

        private List<Point> Points = new List<Point>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;
        }

        void show_item_location()
        {
            int W = 460;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "直線連線";
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_clear1.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_clear1.Size.Width, pictureBox1.Location.Y + pictureBox1.Size.Height - bt_clear1.Size.Height);

            this.Size = new Size(1740, 940);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;

            if (pt_index < (pt.Length - 1)) // 如果一維陣列內的 100 個位置還沒裝滿
            {
                pt_index++;  // 一維陣列 的索引往前
                pt[pt_index] = new Point(e.X, e.Y); // 存入 滑鼠游標位置
                this.pictureBox0.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            /*
            for (int i = 0; i <= pt_index; i++)
            {
                e.Graphics.DrawImage(img,
                pt[i].X - img.Width / 2, pt[i].Y - img.Height / 2, //影像左上角在表單的位置
                img.Width, img.Height); //影像的寬高
            }
            */
            //richTextBox1.Text += "index " + pt_index.ToString() + "\n";

            if (pt_index < 1)
            {
                return;
            }

            Point[] pt2 = new Point[pt_index + 1];
            int i;
            for (i = 0; i <= pt_index; i++)
            {
                pt2[i] = pt[i];
            }

            e.Graphics.DrawLines(new Pen(Color.Red, 2), pt2);

            /*
            //richTextBox1.Text += "idx = " + pt_index.ToString() + "\n";
                //Point[] pt2 = new Point[pt_index + 1];
                int i;
                for (i = 0; i <= pt_index; i++)
                {
                    //richTextBox1.Text += "draw i = " + i.ToString() + "\n";
                    e.Graphics.DrawEllipse(new Pen(Color.Red, 1), pt[i].X, pt[i].Y, 20, 20);
                }
            */
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Points.Add(e.Location);
            Refresh();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Draw the points.
            foreach (Point point in Points)
            {
                e.Graphics.FillEllipse(Brushes.Black, point.X - 3, point.Y - 3, 5, 5);
            }
            if (Points.Count < 2)
            {
                return;
            }

            // Draw the curve.
            e.Graphics.DrawCurve(Pens.Red, Points.ToArray());

        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            // Start a new point list.
            Points = new List<Point>();
            Refresh();
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
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


/*  可搬出

*/
