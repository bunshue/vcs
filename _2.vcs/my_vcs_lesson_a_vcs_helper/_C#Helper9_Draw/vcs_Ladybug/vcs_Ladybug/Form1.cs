using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_Ladybug
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            //pictureBox2.Size = new Size(1920 / 2, 1080 / 2);
            //pictureBox2.Location = new Point(0, 0);

        }

        //漫遊演算法 ST
        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            //cir.CheckSelected(e.X, e.Y);
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            //cir.Update(e.X, e.Y);
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            //cir.dragging = false;
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
        }

        //漫遊演算法 SP
    }
}


