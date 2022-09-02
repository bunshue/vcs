using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_bobblehead
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Bitmap BmHead, BmBody, BmCombined;
        private PointF Chin, Origin;
        private float Ar, Aa, Fr, Fa;
        private float T = 0;
        private const float Dampen = 0.95f;

        private void Form1_Load(object sender, EventArgs e)
        {
            // The body is scaled by 0.5 so the head looks big.
            const float BodyScale = 0.5f;

            // Make the body image.
            Bitmap bm_body = (Bitmap)picBody.Image;
            int body_wid = (int)(bm_body.Width * BodyScale);
            int body_hgt = (int)(bm_body.Height * BodyScale);
            BmBody = new Bitmap(body_wid, body_hgt);
            using (Graphics gr = Graphics.FromImage(BmBody))
            {
                Point[] dest_points =
                {
                    new Point(0, 0),
                    new Point(body_wid, 0),
                    new Point(0, body_hgt),
                };
                gr.DrawImage(bm_body, dest_points);
            }

            // Make the head image, using the upper left
            // corner's color as the transparent color.
            BmHead = (Bitmap)picHead.Image;
            Color transparent = BmHead.GetPixel(0, 0);
            BmHead.MakeTransparent(transparent);

            // The tip of chin is at (273, 383) in scaled coordinates.
            Chin = new PointF(273 * BodyScale, 383 * BodyScale);

            // Origin is where we need to draw the upper left
            // corner of the head to place it on the tip of the chin.
            Origin = new PointF(
                Chin.X - BmHead.Width / 2,
                Chin.Y - BmHead.Height + 15);

            // Draw the head.
            DrawHead(0, 0);

            // Size the form to fit.
            ClientSize = new Size(
                picBobble.Right + picBobble.Left,
                picBobble.Bottom + picBobble.Top);
        }

        // Start bobbling.
        private Random Rand = new Random();
        private void picBobble_Click(object sender, EventArgs e)
        {
            Ar = Rand.Next(10, 20);
            if (Rand.Next(0, 2) == 0) Ar = -Ar;
            Aa = Rand.Next(10, 20);
            if (Rand.Next(0, 2) == 0) Aa = -Aa;
            Fr = Rand.Next(7, 15) / 10f;
            Fa = Rand.Next(7, 15) / 10f;

            T = 0;
            tmrBobble.Enabled = true;
        }

        // A*Cos(2*pi*f*t)
        private void tmrBobble_Tick(object sender, EventArgs e)
        {
            float r = (float)(Ar * Math.Cos(2 * Math.PI * Fr * T));
            float theta = (float)(Aa * Math.Cos(2 * Math.PI * Fa * T));
            DrawHead(r, theta);

            T += 0.1f;
            Ar *= Dampen;
            Aa *= Dampen;

            if ((Math.Abs(Ar) < 0.1) && (Math.Abs(Aa) < 0.1f))
                tmrBobble.Enabled = false;
        }

        // Draw the head at the indicated position.
        private void DrawHead(float r, float theta)
        {
            BmCombined = (Bitmap)BmBody.Clone();
            using (Graphics gr = Graphics.FromImage(BmCombined))
            {
                gr.TranslateTransform(-Chin.X, -Chin.Y, MatrixOrder.Append);
                gr.RotateTransform(theta, MatrixOrder.Append);
                gr.TranslateTransform(0, r, MatrixOrder.Append);
                gr.TranslateTransform(Chin.X, Chin.Y, MatrixOrder.Append);

                gr.DrawImage(BmHead, Origin);
            }
            picBobble.Image = BmCombined;
            picBobble.Refresh();
        }
    }
}
