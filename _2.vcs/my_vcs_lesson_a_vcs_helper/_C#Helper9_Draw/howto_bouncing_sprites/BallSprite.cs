using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Media;

namespace howto_bouncing_sprites
{
    class BallSprite
    {
        public Rectangle Location;
        public Point Velocity;
        public Color BackColor, ForeColor;
        public int MaxX, MaxY;

        // Constructor that initializes randomly.
        private static Random rand = new Random();
        public BallSprite(int min_r, int max_r, int max_x, int max_y, int min_v, int max_v)
        {
            MaxX = max_x;
            MaxY = max_y;
            int width = rand.Next(min_r, max_r);
            Location = new Rectangle(
                rand.Next(0, max_x - width),
                rand.Next(0, max_y - width),
                width, width);

            int vx = rand.Next(min_v, max_v);
            int vy = rand.Next(min_v, max_v);
            if (rand.Next(0, 2) == 0) vx = -vx;
            if (rand.Next(0, 2) == 0) vy = -vy;
            Velocity = new Point(vx, vy);

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

        // Move the ball.
        public void Move()
        {
            // Move the ball.
            int new_x = Location.X + Velocity.X;
            int new_y = Location.Y + Velocity.Y;
            bool bounced = ((new_x < 0) || (new_y < 0) ||
                (new_x + Location.Width > MaxX) ||
                (new_y + Location.Height > MaxY));
            if (new_x < 0) Velocity.X = -Velocity.X;
            else if (new_x + Location.Width > MaxX) Velocity.X = -Velocity.X;
            if (new_y < 0) Velocity.Y = -Velocity.Y;
            else if (new_y + Location.Height > MaxY) Velocity.Y = -Velocity.Y;

            if (bounced) Boing();

            Location = new Rectangle(
                new_x, new_y,
                Location.Width,
                Location.Height);
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
            using (SolidBrush the_brush = new SolidBrush(BackColor))
            {
                gr.FillEllipse(the_brush, Location);
            }
            using (Pen the_pen = new Pen(ForeColor))
            {
                gr.DrawEllipse(the_pen, Location);
            }
        }
    }
}

