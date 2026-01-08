using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCropA
{
    public partial class Form1 : Form
    {
        private List<Point> Points = null;
        private bool flag_select_area = false;  //開始選取的旗標
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1;

            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
        }

        void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Points = new List<Point>();
            flag_select_area = true;
        }

        void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_select_area == false)
                return;
            Points.Add(new Point(e.X, e.Y));
            pictureBox1.Invalidate();
        }

        void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_select_area = false;

            richTextBox1.Text += "點數 : " + Points.Count.ToString() + "\n";
        }

        void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if ((Points != null) && (Points.Count > 1))
            {
                using (Pen dashed_pen = new Pen(Color.Red))
                {
                    dashed_pen.DashPattern = new float[] { 5, 5 };
                    e.Graphics.DrawLines(Pens.White, Points.ToArray());
                    e.Graphics.DrawLines(dashed_pen, Points.ToArray());
                }
            }

        }
    }
}

