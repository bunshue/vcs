using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ToolTip2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolTip1.OwnerDraw = true;
            toolTip1.SetToolTip(button1, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            toolTip1.SetToolTip(button2, "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB");
            toolTip1.SetToolTip(button3, "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCC");
        }

        private const int Margin = 10;

        private void toolTip1_Popup(object sender, PopupEventArgs e)
        {
            int image_wid = 2 * Margin + Properties.Resources.burn.Width;
            int image_hgt = 2 * Margin +
                Properties.Resources.burn.Height;

            int wid = e.ToolTipSize.Width + 2 * Margin + image_wid;
            int hgt = e.ToolTipSize.Height;
            if (hgt < image_hgt)
                hgt = image_hgt;

            e.ToolTipSize = new Size(wid, hgt);
        }

        private void toolTip1_Draw(object sender, DrawToolTipEventArgs e)
        {
            // Draw the background and border.
            e.DrawBackground();
            e.DrawBorder();

            // Draw the image.
            e.Graphics.DrawImage(Properties.Resources.burn, Margin, Margin);

            // Draw the text.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Center;

                int image_wid = 2 * Margin +
                    Properties.Resources.burn.Width;

                Rectangle rect = new Rectangle(
                    image_wid, 0,
                    e.Bounds.Width - image_wid, e.Bounds.Height);
                e.Graphics.DrawString(e.ToolTipText, e.Font, Brushes.Green, rect, sf);
            }
        }
    }
}
