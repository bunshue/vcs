using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        ClassBall ball1, ball2;
        bool BarEnabled = false;
        Point MousePos;
        Pen myPen = new Pen(Color.Brown, 3);
        Point[] HoleList = new Point[4];

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(800, 400);
            ball1 = new ClassBall(new Point(this.ClientSize.Width * 3 / 4, this.ClientSize.Height / 2),
                new Point(0, 0),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                30,
                Color.White);

            ball2 = new ClassBall(new Point(this.ClientSize.Width / 4, this.ClientSize.Height / 2),
                new Point(0, 0),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                30,
                Color.Red);
            Compute_HolePos();
        }

        void Compute_HolePos()
        {
            HoleList[0] = new Point(10, 10);
            HoleList[1] = new Point(this.ClientSize.Width - 10, 10);
            HoleList[2] = new Point(10, this.ClientSize.Height - 10);
            HoleList[3] = new Point(this.ClientSize.Width - 10, this.ClientSize.Height - 10);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            for (int i = 0; i < 4; i++)
                e.Graphics.FillEllipse(Brushes.Black, HoleList[i].X - 50, HoleList[i].Y - 50, 100, 100);

            if (!ball1.Dead)
                ball1.Draw(e.Graphics);
            if (!ball2.Dead)
                ball2.Draw(e.Graphics);

            if (!ball1.Dead && !ball2.Dead && BarEnabled)
            {
                e.Graphics.DrawLine(myPen, MousePos.X, MousePos.Y, (int)(ball1.position.X), (int)(ball1.position.Y));
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ClassBallCollide ballCollide = new ClassBallCollide(ball2, ball1);
            ballCollide.performBallCollide();

            double d;
            for (int i = 0; i < 4; i++)
            {
                d = Math.Sqrt((HoleList[i].X - ball1.position.X) * (HoleList[i].X - ball1.position.X) +
                     (HoleList[i].Y - ball1.position.Y) * (HoleList[i].Y - ball1.position.Y));
                if (d <= 50)
                {
                    ball1.Dead = true;
                    timer1.Enabled = false;
                    this.Invalidate();
                    MessageBox.Show("白球入袋！ (新局請按空白鍵)");
                }


                d = Math.Sqrt((HoleList[i].X - ball2.position.X) * (HoleList[i].X - ball2.position.X) +
                     (HoleList[i].Y - ball2.position.Y) * (HoleList[i].Y - ball2.position.Y));
                if (d <= 50)
                {
                    ball2.Dead = true;
                    timer1.Enabled = false;
                    this.Invalidate();
                    MessageBox.Show("紅球入袋！ (新局請按空白鍵)");
                }
            }

            this.Invalidate();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            BarEnabled = true;
            MousePos.X = e.X;
            MousePos.Y = e.Y;
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            BarEnabled = false;
            ball1.velocity.X = (ball1.position.X - MousePos.X) * 0.1f;
            ball1.velocity.Y = (ball1.position.Y - MousePos.Y) * 0.1f;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (BarEnabled)
            {
                MousePos.X = e.X;
                MousePos.Y = e.Y;
                this.Invalidate();
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Space)
            {
                ball1.Dead = false;
                ball1.position = new Point(this.ClientSize.Width * 3 / 4, this.ClientSize.Height / 2);
                ball1.velocity = new PointF(0, 0);

                ball2.Dead = false;
                ball2.position = new Point(this.ClientSize.Width / 4, this.ClientSize.Height / 2);
                ball2.velocity = new PointF(0, 0);
                timer1.Enabled = true;
            }
        }
    }
}