using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;

namespace vcs_test_all_04_Font3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // List the fonts.
        private void Form1_Load(object sender, EventArgs e)
        {
            InstalledFontCollection fonts = new InstalledFontCollection();
            var font_names =
                from family in fonts.Families
                select family.Name;
            cboFonts.DataSource = font_names.ToArray();
        }

        // Draw font samples.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(this.BackColor);

            int x = 20;
            int y = cboFonts.Bottom + 5;
            DrawSamples(e.Graphics, TextRenderingHint.AntiAlias, x, ref y);

            y += 10;
            DrawSamples(e.Graphics, TextRenderingHint.AntiAliasGridFit, x, ref y);

            y += 10;
            DrawSamples(e.Graphics, TextRenderingHint.ClearTypeGridFit, x, ref y);

            x += 250;
            y = cboFonts.Bottom + 5;
            DrawSamples(e.Graphics, TextRenderingHint.SingleBitPerPixel, x, ref y);

            y += 10;
            DrawSamples(e.Graphics, TextRenderingHint.SingleBitPerPixelGridFit, x, ref y);

            y += 10;
            DrawSamples(e.Graphics, TextRenderingHint.SystemDefault, x, ref y);
        }

        private void DrawSamples(Graphics gr, TextRenderingHint hint, int x, ref int y)
        {
            gr.TextRenderingHint = TextRenderingHint.AntiAlias;
            gr.DrawString(hint.ToString(), this.Font, Brushes.Blue, x - 10, y);
            y += 20;
            gr.TextRenderingHint = hint;
            for (int font_size = 6; font_size <= 16; font_size += 2)
            {
                DrawSample(gr, font_size, x, ref y);
            }
        }

        // Draw a sample of the indicated text.
        private void DrawSample(Graphics gr, float font_size, int x, ref int y)
        {
            try
            {
                using (Font font = new Font(cboFonts.Text, font_size))
                {
                    string text = cboFonts.Text + ", " + font_size.ToString();
                    gr.DrawString(text, font, Brushes.Black, x, y);
                    y = (int)(y + font_size) + 10;
                }
            }
            catch
            {
            }
        }

        // Redraw the samples using the new font.
        private void cboFonts_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.Refresh();
        }
    }
}
