using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

// Added a bitmap resource named happy to the program.

namespace howto_owner_drawn_tooltip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Set a multi-line tooltip in code.
        private void Form1_Load(object sender, EventArgs e)
        {
            tipButtons.SetToolTip(btnWhatever,
                "Whatever...\nWhatever...\nWhatever...");
        }

        private const int Margin = 10;

        // Set the tooltip's bounds.
        private void tipButtons_Popup(object sender, PopupEventArgs e)
        {
            int image_wid = 2 * Margin +
                Properties.Resources.happy.Width;
            int image_hgt = 2 * Margin +
                Properties.Resources.happy.Height;

            int wid = e.ToolTipSize.Width + 2 * Margin + image_wid;
            int hgt = e.ToolTipSize.Height;
            if (hgt < image_hgt) hgt = image_hgt;

            e.ToolTipSize = new Size(wid, hgt);
        }

        // Draw the tooltip.
        private void tipButtons_Draw(object sender, DrawToolTipEventArgs e)
        {
            // Draw the background and border.
            e.DrawBackground();
            e.DrawBorder();

            // Draw the image.
            e.Graphics.DrawImage(Properties.Resources.happy, Margin, Margin);

            // Draw the text.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Center;

                int image_wid = 2 * Margin +
                    Properties.Resources.happy.Width;

                Rectangle rect = new Rectangle(
                    image_wid, 0,
                    e.Bounds.Width - image_wid, e.Bounds.Height);
                e.Graphics.DrawString(
                    e.ToolTipText, e.Font, Brushes.Green, rect, sf);
            }
        }

        private void btnClickMe_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Clicked!", "Clicked", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnDontClick_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Just kidding!", "Kidding", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnWhatever_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Whatever...", "Whatever", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
