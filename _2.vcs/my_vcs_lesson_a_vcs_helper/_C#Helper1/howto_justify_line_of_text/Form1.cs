using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;

namespace howto_justify_line_of_text
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Text justification.
        public enum TextJustification
        {
            Left,
            Right,
            Center,
            Full
        }

        // Arrangement parameters.
        private Padding TextMargin = new Padding(5);
        private const float ParagraphIndent = 40f;
        private const float LineSpacing = 1f;
        private const float ExtraParagraphSpacing = 0.5f;

        // The text to display.
        private const string MessageText =
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";

        // Draw justified text on the PictureBox.
        private void pictureBox_justify1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox_justify1.BackColor);
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            // Draw within a rectangle excluding the margins.
            RectangleF rect = new RectangleF(
                TextMargin.Left, TextMargin.Top,
                pictureBox_justify1.ClientSize.Width - TextMargin.Left - TextMargin.Right,
                pictureBox_justify1.ClientSize.Height - TextMargin.Top - TextMargin.Bottom);

            // Draw the text.
            using (Font font = new Font("Times New Roman", 10))
            {
                DrawJustifiedLine(e.Graphics, rect,
                    font, Brushes.Blue, MessageText);
            }

            // Show the text drawing area.
            e.Graphics.DrawRectangle(Pens.Silver, Rectangle.Round(rect));
        }
        private void pictureBox_justify1_Resize(object sender, EventArgs e)
        {
            pictureBox_justify1.Refresh();
        }

        // Draw justified text on the Graphics object
        // in the indicated Rectangle.
        private void DrawJustifiedLine(Graphics gr, RectangleF rect,
            Font font, Brush brush, string text)
        {
            // Break the text into words.
            string[] words = text.Split(' ');

            // Add a space to each word and get their lengths.
            float[] word_width = new float[words.Length];
            float total_width = 0;
            for (int i = 0; i < words.Length; i++)
            {
                // See how wide this word is.
                SizeF size = gr.MeasureString(words[i], font);
                word_width[i] = size.Width;
                total_width += word_width[i];
            }

            // Get the additional spacing between words.
            float extra_space = rect.Width - total_width;
            int num_spaces = words.Length - 1;
            if (words.Length > 1) extra_space /= num_spaces;

            // Draw the words.
            float x = rect.Left;
            float y = rect.Top;
            for (int i = 0; i < words.Length; i++)
            {
                // Draw the word.
                gr.DrawString(words[i], font, brush, x, y);

                // Move right to draw the next word.
                x += word_width[i] + extra_space;
            }
        }
    }
}
