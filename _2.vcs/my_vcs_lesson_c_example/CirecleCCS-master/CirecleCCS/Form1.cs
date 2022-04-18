using System;
using System.Drawing;
using System.Windows.Forms;

namespace CirecleCCS
{
    public partial class Form1 : Form
    {
        CcsGo ccs = new CcsGo();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            ccs.ResizePinSize = 10;
            ccs.Create();

            string filename = @"C:\______test_files\elephant.jpg";
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            ccs.DrawRubberBand(pictureBox1, e);
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            ccs.StartPoint(pictureBox1, e);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            ccs.TrackRubberBand(pictureBox1, e);
            label_xval.Text = "E->X:" + e.X.ToString();
            label_yval.Text = "E->Y:" + e.Y.ToString();
            labelccsX.Text = "CcsX:" + ccs.X.ToString();
            label_CcsY.Text = "CcsY:" + ccs.Y.ToString();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            ccs.EndPoint(pictureBox1, e);
        }

        bool IsInELP(Point Cusorpostion, Point ElpCenter, int radius)
        {
            int elpX = ElpCenter.X;
            int elpY = ElpCenter.Y;
            int csX = Cusorpostion.X;
            int csY = Cusorpostion.Y;
            if (!((elpX - csX) * (elpX - csX) + (elpY - csY) * (elpY - csY) >= radius * radius))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
