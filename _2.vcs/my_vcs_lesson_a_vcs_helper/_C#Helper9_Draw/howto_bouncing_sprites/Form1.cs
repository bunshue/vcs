using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_bouncing_sprites
{
    public partial class Form1 : Form
    {
        // The sprites.
        private BallSprite[] Sprites;
        private Size FormSize;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make random balls.
            Random rand = new Random();
            const int num_balls = 10;
            Sprites = new BallSprite[num_balls];
            for (int i = 0; i < num_balls; i++)
            {
                Sprites[i] = new BallSprite(10, 40, ClientSize.Width, ClientSize.Height, 2, 10);
            }

            // Save the form's size.
            FormSize = ClientSize;

            // Use double buffering to reduce flicker.
            this.SetStyle(
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint |
                ControlStyles.DoubleBuffer,
                true);
            this.UpdateStyles();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        // Redraw.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(BackColor);
            foreach (BallSprite sprite in Sprites)
            {
                sprite.Draw(e.Graphics);
            }
        }

        // Move the balls and refresh.
        private void tmrMoveBall_Tick(object sender, EventArgs e)
        {
            foreach (BallSprite sprite in Sprites)
            {
                sprite.Move();
            }
            Refresh();
        }
    }
}
