using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Media;
using System.Drawing.Drawing2D;

namespace howto_bouncing_ball
{
    public partial class Form1 : Form
    {
        // Some drawing parameters.
        private const int BallWidth = 50;
        private const int BallHeight = 50;
        private int BallX, BallY;   // Position.
        private int BallVx, BallVy; // Velocity.

        public Form1()
        {
            InitializeComponent();
        }

        // Initialize some random stuff.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Pick a random start position and velocity.
            Random rnd = new Random();
            BallVx = rnd.Next(1, 4);
            BallVy = rnd.Next(1, 4);
            BallX = rnd.Next(0, ClientSize.Width - BallWidth);
            BallY = rnd.Next(0, ClientSize.Height - BallHeight);

            // Use double buffering to reduce flicker.
            this.SetStyle(
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint |
                ControlStyles.DoubleBuffer,
                true);
            this.UpdateStyles();
        }

        // Draw the ball at its current location.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(BackColor);
            e.Graphics.FillEllipse(Brushes.Blue, BallX, BallY, BallWidth, BallHeight);
            e.Graphics.DrawEllipse(Pens.Black, BallX, BallY, BallWidth, BallHeight);
        }

        // Update the ball's position, bouncing if necessary.
        private void tmrMoveBall_Tick(object sender, EventArgs e)
        {
            BallX += BallVx;
            if (BallX < 0)
            {
                BallVx = -BallVx;
                Boing();
            }
            else if (BallX + BallWidth > ClientSize.Width)
            {
                BallVx = -BallVx;
                Boing();
            }

            BallY += BallVy;
            if (BallY < 0)
            {
                BallVy = -BallVy;
                Boing();
            }
            else if (BallY + BallHeight > ClientSize.Height)
            {
                BallVy = -BallVy;
                Boing();
            }

            Refresh();
        }

        // Play the boing sound file resource.
        private void Boing()
        {
            using (SoundPlayer player = new SoundPlayer(Properties.Resources.boing))
            {
                //player.Play();
            }
        }
    }
}
