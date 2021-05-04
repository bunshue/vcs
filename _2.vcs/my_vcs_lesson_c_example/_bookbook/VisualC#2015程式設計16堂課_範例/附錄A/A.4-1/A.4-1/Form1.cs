using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using gameItems;

namespace _15._4_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Pen p;
        private Rectangle[] walls;
        private Block[] blocks;
        private Ball ball;

        private void Form1_Load(object sender, EventArgs e)
        {
            this.p = new Pen(Color.Black);
            this.ball = new Ball(new Rectangle(25, 25, 15, 15), Color.Blue, 2, 2);
            this.walls = new Rectangle[4] {
                new Rectangle(10, 10, 10, 240),
                new Rectangle(360, 10, 10, 240),
                new Rectangle(20, 10, 340, 10),
                new Rectangle(20, 240, 340, 10)
            };
            this.blocks = new Block[3] {
                new Block(new Rectangle(90, 70, 20, 20), Color.Red),
                new Block(new Rectangle(180, 180, 20, 20), Color.Green),
                new Block(new Rectangle(270, 70, 20, 20), Color.Blue)
            };
            timer1.Enabled = true;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Left)
                this.ball.increaseVx(-1);
            if (e.KeyData == Keys.Right)
                this.ball.increaseVx(1);
            if (e.KeyData == Keys.Up)
                this.ball.increaseVy(-1);
            if (e.KeyData == Keys.Down)
                this.ball.increaseVy(1);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.ball.step();

            bool left_collision = this.ball.getposition().X <= this.walls[0].X+this.walls[0].Width;
            bool right_collision = this.ball.getposition().X+this.ball.getposition().Width >= this.walls[1].X;
            bool top_collision = this.ball.getposition().Y <= this.walls[2].Y+this.walls[2].Height;
            bool bottom_collision = this.ball.getposition().Y+this.ball.getposition().Height >= this.walls[3].Y;
            if (left_collision || right_collision)
                this.ball.collisionVx();
            if (top_collision || bottom_collision)
                this.ball.collisionVy();

            for (int i=0; i<this.blocks.Length; ++i) {
                bool x_inside1 = this.ball.getposition().X + this.ball.getposition().Width/2 >= this.blocks[i].getposition().X;
                bool x_inside2 = this.ball.getposition().X + this.ball.getposition().Width/2 <= this.blocks[i].getposition().X + this.blocks[i].getposition().Width;
                bool y_inside1 = this.ball.getposition().Y + this.ball.getposition().Height/2 >= this.blocks[i].getposition().Y;
                bool y_inside2 = this.ball.getposition().Y + this.ball.getposition().Height/2 <= this.blocks[i].getposition().Y + this.blocks[i].getposition().Height;
                if (x_inside1 && x_inside2 && y_inside1 && y_inside2)
                    this.ball.setcolor(this.blocks[i].getcolor());
            }
            this.Refresh();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.DrawRectangles(this.p, this.walls);
            g.FillEllipse(new SolidBrush(this.ball.getcolor()), this.ball.getposition());
            for (int i=0; i<this.blocks.Length; ++i) {
                Brush b = new SolidBrush(this.blocks[i].getcolor());
                g.FillRectangle(b, this.blocks[i].getposition());
            }
            g.Dispose();
            base.OnPaint(e);
        }

    }
}
