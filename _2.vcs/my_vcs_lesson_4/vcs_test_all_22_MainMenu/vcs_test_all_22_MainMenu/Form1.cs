using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_test_all_22_MainMenu
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const string FONT_NAME = "Times New Roman";
        private const float FONT_SIZE = 12;
        private const FontStyle FONT_STYLE = FontStyle.Bold;
        private const string MENU_CAPTION = "Say Hi";


        // Tell Windows how big to make the menu item.
        private void mnuFileSayHi_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            // Create the font we will use to draw the text.
            using (Font menu_font = new Font(
                FONT_NAME, FONT_SIZE, FONT_STYLE))
            {
                // See how big the text will be.
                SizeF text_size =
                    e.Graphics.MeasureString(MENU_CAPTION, menu_font);

                // Set the necessary size.
                e.ItemHeight = (int)text_size.Height;
                e.ItemWidth = (int)text_size.Width;
            }
        }

        // Draw the menu item.
        private void mnuFileSayHi_DrawItem(object sender, DrawItemEventArgs e)
        {
            // Create the font we will use to draw the text.
            using (Font menu_font = new Font(
                FONT_NAME, FONT_SIZE, FONT_STYLE))
            {
                // See if the mouse is over the menu item.
                if ((e.State & DrawItemState.Selected) != DrawItemState.None)
                {
                    // The mouse is over the item.
                    // Draw a shaded background.
                    using (Brush menu_brush =
                        new LinearGradientBrush(
                            e.Bounds, Color.Red, Color.Black, 90))
                    {
                        e.Graphics.FillRectangle(menu_brush, e.Bounds);
                    }

                    // Draw the text.
                    e.Graphics.DrawString(MENU_CAPTION, menu_font,
                        System.Drawing.Brushes.AliceBlue,
                        e.Bounds.X, e.Bounds.Y);
                }
                else
                {
                    // The mouse is not over the item.
                    // Erase the background.
                    e.Graphics.FillRectangle(
                        System.Drawing.Brushes.LightGray,
                        e.Bounds.X, e.Bounds.Y,
                        e.Bounds.Width, e.Bounds.Height);

                    // Draw the text.
                    e.Graphics.DrawString(MENU_CAPTION, menu_font,
                        System.Drawing.Brushes.Black,
                        e.Bounds.X, e.Bounds.Y);
                }
            }
        }


        private void mnuFileSayHi_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Hi");
        }

        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
