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
        private Color[] color =
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
            return color[rand.Next(0, color.Length)];
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
            float r = 50;
            Circle circle0 = new Circle(x, y, r);

            int i;
            for (i = 50; i < 300; i += 50)
            {
                x = i;
                y = i;
                r = i/2;


                using (Brush the_brush = new SolidBrush(RandomColor()))
                {
                    circle0 = new Circle(x, y, r);
                    circle0.Draw(e.Graphics, the_brush);    //畫實心
                    richTextBox1.Text += "circle info : " + circle0.ToString() + "\n";
                }

                circle0 = new Circle(x, y, r + 10);
                Pen p = new Pen(Color.Red, 5);

                //circle0.Draw(e.Graphics, Pens.Red); //畫空心, 未設定筆寬, 即筆寬為1
                circle0.Draw(e.Graphics, p); //畫空心
                richTextBox1.Text += "circle info : " + circle0.ToString() + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }
    }
}
