using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Media;

namespace vcs_Draw9_Example8_vcsh
{
    class BallSprite
    {
        public PointF Center;
        public Vector2D Velocity;
        public float Radius;
        public Color BackColor, ForeColor;
        public int MaxX, MaxY;

        // Constructor that initializes randomly.
        private static Random rand = new Random();
        public BallSprite(int min_r, int max_r, int max_x, int max_y, int min_v, int max_v)
        {
            MaxX = max_x;
            MaxY = max_y;
            Radius = rand.Next(min_r, max_r);
            int radius = (int)Radius;
            Center = new PointF(
                rand.Next(radius, max_x - radius),
                rand.Next(radius, max_y - radius));

            int vx = rand.Next(min_v, max_v);
            int vy = rand.Next(min_v, max_v);
            if (rand.Next(0, 2) == 0) vx = -vx;
            if (rand.Next(0, 2) == 0) vy = -vy;
            Velocity = new Vector2D(vx, vy);

            BackColor = RandomColor();
            ForeColor = RandomColor();
        }

        // Return a random color.
        private Color[] colors =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
        };
        private Color RandomColor()
        {
            return colors[rand.Next(0, colors.Length)];
        }

        // Return the ball's bounds.
        public RectangleF GetBounds()
        {
            return new RectangleF(
                Center.X - Radius, Center.Y - Radius,
                2 * Radius, 2 * Radius);
        }

        // Move the ball.
        public void Move()
        {
            // Move the ball.
            Center += Velocity;

            bool bounced = false;
            if ((Center.X < Radius) ||
                (Center.X + Radius > MaxX))
            {
                Velocity.X = -Velocity.X;
                bounced = true;
            }
            if ((Center.Y < Radius) ||
                (Center.Y + Radius > MaxY))
            {
                Velocity.Y = -Velocity.Y;
                bounced = true;
            }

            if (bounced)
                Boing();
        }

        // Play the boing sound file resource.
        private static void Boing()
        {
            using (SoundPlayer player = new SoundPlayer(Properties.Resources.boing))
            {
                //player.Play();
            }
        }

        // Draw the ball.
        public void Draw(Graphics gr)
        {
            RectangleF bounds = GetBounds();
            using (SolidBrush the_brush = new SolidBrush(BackColor))
            {
                gr.FillEllipse(the_brush, bounds);
            }
            using (Pen the_pen = new Pen(ForeColor))
            {
                gr.DrawEllipse(the_pen, bounds);
            }
        }
    }
}
