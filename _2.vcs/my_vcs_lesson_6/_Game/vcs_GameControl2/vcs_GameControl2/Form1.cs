using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace vcs_GameControl2
{
    public partial class Form1 : Form
    {
        Bitmap earth = Properties.Resources.earth2;
        Bitmap sky = Properties.Resources.sky;
        int X = 0;

        Bitmap grass = Properties.Resources.BBB;
        Bitmap grass1 = Properties.Resources.B;

        int windX = 0;
        int windX_D = 1;

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(640, 480);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle dest = new Rectangle(0, 280, 640, 200);
            Rectangle src = new Rectangle(0, 0, 640, 200);
            e.Graphics.DrawImage(earth, dest, src, GraphicsUnit.Pixel);

            if (X <= this.ClientSize.Width / 2)
            {
                dest = new Rectangle(0, 0, 640, 280);
                src = new Rectangle(X, 0, 640, 280);
                e.Graphics.DrawImage(sky, dest, src, GraphicsUnit.Pixel);
            }
            else
            {
                int w = sky.Width - X;
                dest = new Rectangle(0, 0, w, 280);
                src = new Rectangle(X, 0, w, 280);
                e.Graphics.DrawImage(sky, dest, src, GraphicsUnit.Pixel);

                int w2 = this.ClientSize.Width - w;
                dest = new Rectangle(w, 0, w2, 280);
                src = new Rectangle(0, 0, w2, 280);
                e.Graphics.DrawImage(sky, dest, src, GraphicsUnit.Pixel);
            }

            dest = new Rectangle(100, 180, 200, 100);
            src = new Rectangle(0, 0, 200, 100);
            e.Graphics.DrawImage(grass, dest, src, GraphicsUnit.Pixel);

            dest = new Rectangle(200, 180, 50, 100);

            Point[] pt = new Point[3];
            pt[0] = new Point(200 + windX, 180);
            pt[1] = new Point(250 + windX, 180);
            pt[2] = new Point(200, 280);

            Matrix A = new Matrix(dest, pt);

            src = new Rectangle(0, 0, 50, 100);

            e.Graphics.Transform = A;

            e.Graphics.DrawImage(grass1, dest, src, GraphicsUnit.Pixel);

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            X++;
            if (X > sky.Width) X = X - sky.Width;
            this.Invalidate();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            windX = windX + windX_D;

            if (windX > 20 || windX < -20) windX_D = -windX_D;
            this.Invalidate();
        }
    }
}
