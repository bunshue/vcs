using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_21_ListBox4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int ItemMargin = 5;
        private const float PictureHeight = 100f;

        // Create some objects.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Make the LIstBox owner drawn.
            listBox1.DrawMode = DrawMode.OwnerDrawVariable;

            listBox1.Items.Add(new Planet("Mercury", Properties.Resources.Mercury, "Distance: 0.39 AU, Radius: 0.38, Mass: 0.05, Day: 59 days, Year: 88 days"));
            listBox1.Items.Add(new Planet("Venus", Properties.Resources.Venus, "Distance: 0.72 AU, Radius: 0.95, Mass: 0.89, Day: 243 days, Year: 224 days"));
            listBox1.Items.Add(new Planet("Earth", Properties.Resources.Earth, "Distance: 1 AU, Radius: 1, Mass: 1, Day: 1 day, Year: 365 days"));
            listBox1.Items.Add(new Planet("Mars", Properties.Resources.Mars, "Distance: 1.5 AU, Radius: 0.53, Mass: 0.11, Day: 1.026 days, Year: 687 days"));
            listBox1.Items.Add(new Planet("Jupiter", Properties.Resources.Jupiter, "Distance: 5.2 AU, Radius: 11, Mass: 318, Day: 0.411 days, Year: 11.8 years"));
            listBox1.Items.Add(new Planet("Saturn", Properties.Resources.Saturn, "Distance: 9.5 AU, Radius: 9, Mass: 95, Day: 0.43 days, Year: 29.5 years"));
            listBox1.Items.Add(new Planet("Uranus", Properties.Resources.Uranus, "Distance: 19.2 AU, Radius: 4, Mass: 17, Day: 0.75 days, Year: 84 years"));
            listBox1.Items.Add(new Planet("Neptune", Properties.Resources.Neptune, "Distance: 30.1 AU, Radius: 4, Mass: 17, Day: 0.8 days, Year: 165 years"));
            listBox1.Items.Add(new Planet("Pluto", Properties.Resources.Pluto, "Distance: 39.5 AU, Radius: 0.18, Mass: 0.002, Day: 0.27 days, Year: 248 years"));
        }

        // Return enough space for the item.
        private void listBox1_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            e.ItemHeight = (int)(PictureHeight + 2 * ItemMargin);
        }

        // Draw the item.
        private void listBox1_DrawItem(object sender, DrawItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            Planet planet = (Planet)lst.Items[e.Index];

            // Draw the background.
            e.DrawBackground();

            // Draw the picture.
            float scale = PictureHeight / planet.Picture.Height;
            RectangleF source_rect = new RectangleF(
                0, 0, planet.Picture.Width, planet.Picture.Height);
            float picture_width = scale * planet.Picture.Width;
            RectangleF dest_rect = new RectangleF(
                e.Bounds.Left + ItemMargin, e.Bounds.Top + ItemMargin,
                picture_width, PictureHeight);
            e.Graphics.DrawImage(planet.Picture, dest_rect, source_rect, GraphicsUnit.Pixel);

            // See if the item is selected.
            Brush br;
            if ((e.State & DrawItemState.Selected) == DrawItemState.Selected)
                br = SystemBrushes.HighlightText;
            else
                br = new SolidBrush(e.ForeColor);

            // Find the area in which to put the text.
            float x = e.Bounds.Left + picture_width + 3 * ItemMargin;
            float y = e.Bounds.Top + ItemMargin;
            float width = e.Bounds.Right - ItemMargin - x;
            float height = e.Bounds.Bottom - ItemMargin - y;
            RectangleF layout_rect = new RectangleF(x, y, width, height);

            // Draw the text.
            string txt = planet.Name + '\n' + planet.Stats;
            e.Graphics.DrawString(txt, this.Font, br, layout_rect);

            // Outline the text.
            e.Graphics.DrawRectangle(Pens.Red, Rectangle.Round(layout_rect));

            // Draw the focus rectangle if appropriate.
            e.DrawFocusRectangle();
        }
    }
}
