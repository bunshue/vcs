using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bitmap = Properties.Resources.p120;   // 貼圖
        Bitmap bitmap2 = Properties.Resources.p135;  // 貼圖
        G2D_ImageRotateBias image01, image02;

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(600, 600);
            Point pos = new Point(this.ClientSize.Width / 4, this.ClientSize.Height / 4);
            image01 = new G2D_ImageRotateBias(bitmap, pos, new Point(bitmap.Width / 2, bitmap.Height / 2));

            pos = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            image02 = new G2D_ImageRotateBias(bitmap2, pos, new Point(bitmap2.Width *3/ 4, bitmap2.Height *3/ 4));
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            image01.Draw(e.Graphics);
            image02.Draw(e.Graphics);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            image01.MouseDown(e.Location);
            image02.MouseDown(e.Location);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            image01.MouseMove(e.Location);
            image02.MouseMove(e.Location);
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            image01.MouseUp();
            image02.MouseUp();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                image01.StopRotate();
                image02.StopRotate();
            }
        }
    }
}
