using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ColorPalette
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MakeColorPalette(this, 10, 10, Color_Click);
        }

        // Make a color palette on the given parent.
        private void MakeColorPalette(Control parent, int x, int y, System.EventHandler event_handler)
        {
            Color[] colors = 
            {
                Color.White,
                Color.FromArgb(255, 255, 192, 192),
                Color.FromArgb(255, 255, 224, 192),
                Color.FromArgb(255, 255, 255, 192),
                Color.FromArgb(255, 192, 255, 192),
                Color.FromArgb(255, 192, 255, 255),
                Color.FromArgb(255, 192, 192, 255),
                Color.FromArgb(255, 255, 192, 255),
                Color.FromArgb(255, 224, 224, 224),
                Color.FromArgb(255, 255, 128, 128),
                Color.FromArgb(255, 255, 192, 128),
                Color.FromArgb(255, 255, 255, 128),
                Color.FromArgb(255, 128, 255, 128),
                Color.FromArgb(255, 128, 255, 255),
                Color.FromArgb(255, 128, 128, 255),
                Color.FromArgb(255, 255, 128, 255),
                Color.Silver,
                Color.Red,
                Color.FromArgb(255, 255, 128, 0),
                Color.Yellow,
                Color.Lime,
                Color.Cyan,
                Color.Blue,
                Color.Fuchsia,
                Color.Gray,
                Color.FromArgb(255, 192, 0, 0),
                Color.FromArgb(255, 192, 64, 0),
                Color.FromArgb(255, 192, 192, 0),
                Color.FromArgb(255, 0, 192, 0),
                Color.FromArgb(255, 0, 192, 192),
                Color.FromArgb(255, 0, 0, 192),
                Color.FromArgb(255, 192, 0, 192),
                Color.FromArgb(255, 64, 64, 64),
                Color.Maroon,
                Color.FromArgb(255, 128, 64, 0),
                Color.Olive,
                Color.Green,
                Color.Teal,
                Color.Navy,
                Color.Purple,
                Color.Black,
                Color.FromArgb(255, 64, 0, 0),
                Color.FromArgb(255, 128, 64, 64),
                Color.FromArgb(255, 64, 64, 0),
                Color.FromArgb(255, 0, 64, 0),
                Color.FromArgb(255, 0, 64, 64),
                Color.FromArgb(255, 0, 0, 64),
                Color.FromArgb(255, 64, 0, 64),
            };
            const int num_rows = 6;
            const int num_columns = 8;
            const int pbx_width = 60;
            const int pbx_height = 60;
            const int spacing = 4;

            int row_y = y;
            for (int row = 0; row < num_rows; row++)
            {
                int column_x = x;
                for (int column = 0; column < num_columns; column++)
                {
                    PictureBox pbx = new PictureBox();
                    pbx.Parent = parent;
                    pbx.Click += event_handler;
                    pbx.BackColor = colors[row * num_columns + column];
                    pbx.Size = new Size(pbx_width, pbx_height);
                    pbx.Location = new Point(column_x, row_y);
                    pbx.BorderStyle = BorderStyle.Fixed3D;
                    column_x += pbx_width + spacing;
                }
                row_y += pbx_height + spacing;
            }
        }

        // The user clicked a color. Apply it.
        private void Color_Click(object sender, EventArgs e)
        {
            PictureBox pic = sender as PictureBox;
            this.BackColor = pic.BackColor;
        }

    }
}
