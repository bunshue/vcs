using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_set_picturebox_region
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Restrict pictureBox3 and pictureBox4 to a circular region.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Make a Rectangle that defines the circular area.
            Rectangle rect = new Rectangle(7, 4, 90 - 7, 87 - 4);

            // Make a GraphicsPath and add the circle.
            GraphicsPath path = new GraphicsPath();
            path.AddEllipse(rect);

            // Convert the GraphicsPath into a Region.
            Region region = new Region(path);

            // Restrict the PictureBoxes to the Region.
            pictureBox3.Region = region;
            pictureBox4.Region = region;
        }

        // Draw two overlapping images.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawImage(Properties.Resources.Volleyball, 12, 25);
            e.Graphics.DrawImage(Properties.Resources.Volleyball, 52, 65);
        }

        // Display the name of the clicked PictureBox.
        private void PictureBox_Click(object sender, EventArgs e)
        {
            PictureBox pic = sender as PictureBox;
            MessageBox.Show(pic.Name);
        }
    }
}
