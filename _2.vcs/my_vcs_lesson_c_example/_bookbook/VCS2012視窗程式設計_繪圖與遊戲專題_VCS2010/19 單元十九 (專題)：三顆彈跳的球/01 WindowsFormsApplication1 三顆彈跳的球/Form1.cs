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
        ClassBall ball1, ball2, ball3;
        public Form1()
        {
            InitializeComponent();
            ball1 = new ClassBall(new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2),
                new Point(3, 5),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                30,
                Color.Red);

            ball2 = new ClassBall(new Point(this.ClientSize.Width / 4, this.ClientSize.Height / 4),
                new Point(-3, 5),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                30,
                Color.Blue);

            ball3 = new ClassBall(new Point(this.ClientSize.Width / 4, this.ClientSize.Height / 2),
                new Point(3, -8),
                new Size(this.ClientSize.Width, this.ClientSize.Height),
                30,
                Color.Green);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            ball1.Draw(e.Graphics);
            ball2.Draw(e.Graphics);
            ball3.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            ball1.Move();
            ball2.Move();
            ball3.Move();

            if (Collides(ball1, ball2)) Swap(ball1, ball2);
            if (Collides(ball2, ball3)) Swap(ball2, ball3);
            if (Collides(ball1, ball3)) Swap(ball1, ball3);

            this.Invalidate();
        }

        /*
        bool Collides(ClassBall A, ClassBall B)
        {
            if (A.position.X + A.Ball_Width > B.position.X - B.Ball_Width &&
                A.position.X - A.Ball_Width < B.position.X + B.Ball_Width &&
                A.position.Y + A.Ball_Width > B.position.Y - B.Ball_Width &&
                A.position.Y - A.Ball_Width < B.position.Y + B.Ball_Width)
                return true;
            else
                return false;
        }
        */

        bool Collides(ClassBall A, ClassBall B)
        {
            Double D = Math.Sqrt(
            (A.position.X - B.position.X) * (A.position.X - B.position.X) +
            (A.position.Y - B.position.Y) * (A.position.Y - B.position.Y));

            if (D <= A.Ball_Width + B.Ball_Width)
                return true;
            else
                return false;
        }


        void Swap(ClassBall A, ClassBall B)
        {
            Point temp = A.velocity;
            A.velocity = B.velocity;
            B.velocity = temp;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            ball1.clientSize = this.ClientSize;
            ball2.clientSize = this.ClientSize;
            ball3.clientSize = this.ClientSize;
            this.Invalidate();
        }
    }
}