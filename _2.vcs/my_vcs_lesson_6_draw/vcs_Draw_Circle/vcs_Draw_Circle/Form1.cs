using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Circle
{
    public partial class Form1 : Form
    {
        // Return a random color.
        private Random rand = new Random();
        private Color[] Colors15 =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
            Color.Yellow,
            Color.LightGreen,
            Color.LightBlue,
            Color.Cyan,
        };

        private Color RandomColor()
        {
            return Colors15[rand.Next(0, Colors15.Length)];
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            float x = 100;
            float y = 100;
            float r = 100;
            Circle circle0 = new Circle(x, y, r);

            int i;
            for (i = 0; i < 50; i += 20)
            {
                x += i;
                y += i;
                r += i;
                circle0 = new Circle(x, y, r+5);
                circle0.Draw(e.Graphics, Pens.Red); //畫空心

                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    circle0 = new Circle(x, y, r);
                    circle0.Draw(e.Graphics, the_brush);    //畫實心
                }
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }
    }
}
