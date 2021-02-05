using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TabControl2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The size of the X in each tab's upper right corner.
        private int Xwid = 8;
        private const int tab_margin = 3;

        private void Form1_Load(object sender, EventArgs e)
        {
            // We will draw the tabs.
            tabMenu.DrawMode = TabDrawMode.OwnerDrawFixed;

            // SizeMode must be Fixed to change tab size.
            tabMenu.SizeMode = TabSizeMode.Fixed;

            // Set the size for the tabs.
            Size tab_size = tabMenu.ItemSize;
            tab_size.Width = 100;
            tab_size.Height += 6;
            tabMenu.ItemSize = tab_size;
        }

        // Draw a tab.
        private void tabMenu_DrawItem(object sender, DrawItemEventArgs e)
        {
            Brush txt_brush, box_brush;
            Pen box_pen;

            // We draw in the TabRect rather than on e.Bounds
            // so we can use TabRect later in MouseDown.
            Rectangle tab_rect = tabMenu.GetTabRect(e.Index);

            // Draw the background.
            // Pick appropriate pens and brushes.
            if (e.State == DrawItemState.Selected)
            {
                e.Graphics.FillRectangle(Brushes.DarkOrange, tab_rect);
                e.DrawFocusRectangle();

                txt_brush = Brushes.Yellow;
                box_brush = Brushes.Silver;
                box_pen = Pens.DarkBlue;
            }
            else
            {
                e.Graphics.FillRectangle(Brushes.PaleGreen, tab_rect);

                txt_brush = Brushes.DarkBlue;
                box_brush = Brushes.LightGray;
                box_pen = Pens.DarkBlue;
            }

            // Allow room for margins.
            RectangleF layout_rect = new RectangleF(
                tab_rect.Left + tab_margin,
                tab_rect.Y + tab_margin,
                tab_rect.Width - 2 * tab_margin,
                tab_rect.Height - 2 * tab_margin);
            using (StringFormat string_format = new StringFormat())
            {
                // Draw the tab # in the upper left corner.
                using (Font small_font = new Font(this.Font.FontFamily, 6, FontStyle.Bold))
                {
                    string_format.Alignment = StringAlignment.Near;
                    string_format.LineAlignment = StringAlignment.Near;
                    e.Graphics.DrawString(
                        e.Index.ToString(),
                        small_font,
                        txt_brush,
                        layout_rect,
                        string_format);
                }

                // Draw the tab's text centered.
                using (Font big_font = new Font(this.Font, FontStyle.Bold))
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    e.Graphics.DrawString(
                        tabMenu.TabPages[e.Index].Text,
                        big_font,
                        txt_brush,
                        layout_rect,
                        string_format);
                }

                // Draw an X in the upper right corner.
                Rectangle rect = tabMenu.GetTabRect(e.Index);
                e.Graphics.FillRectangle(box_brush,
                    layout_rect.Right - Xwid,
                    layout_rect.Top,
                    Xwid,
                    Xwid);
                e.Graphics.DrawRectangle(box_pen,
                    layout_rect.Right - Xwid,
                    layout_rect.Top,
                    Xwid,
                    Xwid);
                e.Graphics.DrawLine(box_pen,
                    layout_rect.Right - Xwid,
                    layout_rect.Top,
                    layout_rect.Right,
                    layout_rect.Top + Xwid);
                e.Graphics.DrawLine(box_pen,
                    layout_rect.Right - Xwid,
                    layout_rect.Top + Xwid,
                    layout_rect.Right,
                    layout_rect.Top);
            }
        }

        // If the mouse is over an X, close the tab.
        private void tabMenu_MouseDown(object sender, MouseEventArgs e)
        {
            // See if this is over a tab.
            for (int i = 0; i < tabMenu.TabPages.Count; i++)
            {
                // Get the TabRect plus room for margins.
                Rectangle tab_rect = tabMenu.GetTabRect(i);
                RectangleF rect = new RectangleF(
                    tab_rect.Left + tab_margin,
                    tab_rect.Y + tab_margin,
                    tab_rect.Width - 2 * tab_margin,
                    tab_rect.Height - 2 * tab_margin);
                if (e.X >= rect.Right - Xwid &&
                    e.X <= rect.Right &&
                    e.Y >= rect.Top &&
                    e.Y <= rect.Top + Xwid)
                {
                    Console.WriteLine("Tab " + i);
                    tabMenu.TabPages.RemoveAt(i);
                    return;
                }
            }
        }
    }
}
