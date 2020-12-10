using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawD_Map
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        // The hotspots.
        private List<Rectangle> Hotspots = new List<Rectangle>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 3);

            pictureBox1.Image = vcs_DrawD_Map.Properties.Resources.大峽谷國家公園;
            pictureBox1.ClientSize = new Size(pictureBox1.Image.Size.Width, pictureBox1.Image.Size.Height);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            this.Size = new Size(pictureBox1.Image.Size.Width + 200, pictureBox1.Image.Size.Height + 50);
            button1.Location = new Point(pictureBox1.Image.Width + 20, 10);
            richTextBox1.Location = new Point(pictureBox1.Image.Width + 20, 40);
            richTextBox1.Size = new Size(150, pictureBox1.Size.Height - 40);

            // The hotspots.
            // Initialize the hotspots.
            Hotspots.Add(new Rectangle(88, 509, 22, 22));
            Hotspots.Add(new Rectangle(140, 577, 20, 20));
            Hotspots.Add(new Rectangle(161, 609, 20, 20));
            Hotspots.Add(new Rectangle(630, 138, 20, 20));
            Hotspots.Add(new Rectangle(447, 626, 20, 20));
            Hotspots.Add(new Rectangle(966, 179, 20, 20));
            Hotspots.Add(new Rectangle(958, 214, 20, 20));
            Hotspots.Add(new Rectangle(1062, 301, 20, 20));
            Hotspots.Add(new Rectangle(1109, 581, 20, 20));
            Hotspots.Add(new Rectangle(1099, 621, 20, 20));
            Hotspots.Add(new Rectangle(1247, 262, 20, 16));
            Hotspots.Add(new Rectangle(1314, 224, 20, 20));
            Hotspots.Add(new Rectangle(1344, 651, 20, 20));
            Hotspots.Add(new Rectangle(1098, 753, 20, 20));
            Hotspots.Add(new Rectangle(655, 797, 20, 20));
            Hotspots.Add(new Rectangle(549, 846, 20, 20));
            Hotspots.Add(new Rectangle(449, 935, 20, 20));
            Hotspots.Add(new Rectangle(826, 876, 20, 20));
            Hotspots.Add(new Rectangle(991, 930, 20, 20));
            Hotspots.Add(new Rectangle(1095, 900, 20, 20));
            Hotspots.Add(new Rectangle(1249, 942, 20, 20));
            Hotspots.Add(new Rectangle(254, 1079, 20, 20));
            Hotspots.Add(new Rectangle(298, 1110, 20, 20));
            Hotspots.Add(new Rectangle(1234, 1076, 16, 18));
        }

        private void button1_Click(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();


            int len = Hotspots.Count;
            //richTextBox1.Text += "len = " + len.ToString() + "\n";
            /*  same
            int i;
            for (i = 0; i < len; i++)
            {
                g.DrawRectangle(p, Hotspots[i]);
            }
            */
            //same
            foreach (Rectangle hotspot in Hotspots)
            {
                g.FillRectangle(Brushes.Red, hotspot);
            }
        }

        // See if we clicked a hotspot.
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            int i = HotspotAtPoint(e.Location);
            if (i >= 0)
                richTextBox1.Text += "你點中景點 " + i.ToString() + "\n";
        }

        // See if we're over a hotspot.
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            // See if we're over a hotspot.
            int i = HotspotAtPoint(e.Location);
            if (i >= 0)
            {
                //richTextBox1.Text += "你經過景點 " + i.ToString() + "\n";
                pictureBox1.Cursor = Cursors.Hand;
            }
            else
                pictureBox1.Cursor = Cursors.Default;
        }

        // Return the index of the hotspot at this point
        // or -1 if there is no hotspot there.
        private int HotspotAtPoint(Point mouse_point)
        {
            //richTextBox1.Text += "(" + mouse_point.X.ToString() + ", " + mouse_point.Y.ToString() + ") ";

            // Check the hotspots.
            //return Hotspots.FindIndex(hotspot => hotspot.Contains(mouse_point));

            for (int i = 0; i < Hotspots.Count; i++)
                if (Hotspots[i].Contains(mouse_point)) return i;

            // We didn't find a hotspot that contains the point.
            return -1;
        }



    }
}
