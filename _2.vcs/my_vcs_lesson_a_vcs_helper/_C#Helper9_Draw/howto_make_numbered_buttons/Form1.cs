using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Drawing.Text;

namespace howto_make_numbered_buttons
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display a sample.
        private void ShowSample()
        {
            // Display a sample.
            picSample.Image = MakeNumberBitmap((int)nudWidth.Value,
                picBackground.BackColor, picForeground.BackColor,
                (int)nudBorderThickness.Value, lblFontSample.Font,
                nudMax.Value.ToString());
        }

        // Make a bitmap containing the indicated text.
        private Bitmap MakeNumberBitmap(int width,
            Color bg_color, Color fg_color,
            int border_thickness, Font fg_font, string txt)
        {
            // Size the bitmap.
            Bitmap bm = new Bitmap(width, width);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.SmoothingMode = SmoothingMode.AntiAlias;
                gr.TextRenderingHint = TextRenderingHint.AntiAlias;

                // Make the background transparent.
                gr.Clear(Color.Transparent);

                // Fill the background.
                float margin = 2 + border_thickness / 2f;
                RectangleF rect = new RectangleF(margin, margin,
                    width - 2 * margin, width - 2 * margin);
                using (LinearGradientBrush bg_brush = new LinearGradientBrush(
                    rect, Color.White, bg_color, LinearGradientMode.BackwardDiagonal))
                {
                    gr.FillEllipse(bg_brush, rect);
                }

                // Outline the background.
                if (border_thickness > 0)
                {
                    using (LinearGradientBrush bg_brush = new LinearGradientBrush(
                        rect, bg_color, Color.White, LinearGradientMode.ForwardDiagonal))
                    {
                        using (Pen bg_pen = new Pen(bg_brush, border_thickness))
                        {
                            gr.DrawEllipse(bg_pen, rect);
                        }
                    }
                }

                // Draw the button text.
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    using (Brush fg_brush = new SolidBrush(fg_color))
                    {
                        gr.DrawString(txt, fg_font, fg_brush, rect, string_format);
                    }
                }
            }

            return bm;
        }

        // Set some defaults and show an initial sample.
        private void Form1_Load(object sender, EventArgs e)
        {
            picBackground.BackColor = Color.Blue;
            picForeground.BackColor = Color.Black;
            lblFontSample.Text = lblFontSample.Font.Name + ", " +
                lblFontSample.Font.Size.ToString() + "pt";

            ShowSample();
        }

        // Let the user select a new background color.
        private void picBackground_Click(object sender, EventArgs e)
        {
            cdColor.Color = picBackground.BackColor;
            if (cdColor.ShowDialog() == DialogResult.OK)
            {
                picBackground.BackColor = cdColor.Color;
                ShowSample();
            }
        }

        // Let the user select a new foreground color.
        private void picForeground_Click(object sender, EventArgs e)
        {
            cdColor.Color = picForeground.ForeColor;
            if (cdColor.ShowDialog() == DialogResult.OK)
            {
                picForeground.BackColor = cdColor.Color;
                ShowSample();
            }
        }

        // Let the user select a font.
        private void lblFontSample_Click(object sender, EventArgs e)
        {
            fdFont.Font = lblFontSample.Font;
            if (fdFont.ShowDialog() == DialogResult.OK)
            {
                lblFontSample.Font = fdFont.Font;
                lblFontSample.Text = lblFontSample.Font.Name + ", " +
                    lblFontSample.Font.Size.ToString() + "pt";
                ShowSample();
            }
        }

        // Display a sample with the new values.
        private void chkBorder_CheckedChanged(object sender, EventArgs e)
        {
            ShowSample();
        }
        private void nud_ValueChanged(object sender, EventArgs e)
        {
            ShowSample();
        }
        private void nud_Scroll(object sender, ScrollEventArgs e)
        {
            ShowSample();
        }
        private void nud_KeyUp(object sender, KeyEventArgs e)
        {
            ShowSample();
        }

        // Make the files.
        private void btnMakeFiles_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            Refresh();

            // Make the files.
            for (decimal i = nudMin.Value; i <= nudMax.Value; i++)
            {
                // Make the file.
                Bitmap bm = MakeNumberBitmap((int)nudWidth.Value,
                    picBackground.BackColor, picForeground.BackColor,
                    (int)nudBorderThickness.Value, lblFontSample.Font,
                    i.ToString());

                // Save the file.
                bm.Save("Number" + i.ToString() + ".png", ImageFormat.Png);
            }

            MessageBox.Show("Done", "Done", MessageBoxButtons.OK);
            Cursor = Cursors.Default;
        }
    }
}
