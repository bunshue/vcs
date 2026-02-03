using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;
using System.Drawing.Drawing2D;

namespace vcs_Draw6_String3
{
    public partial class Form1 : Form
    {
        // Text justification.
        public enum TextJustification
        {
            Left,
            Right,
            Center,
            Full
        }

        TextJustification justification = TextJustification.Left;

        // Arrangement parameters.
        private Padding TextMargin = new Padding(5);
        private const float ParagraphIndent = 40f;
        private const float LineSpacing = 1f;
        private const float ExtraParagraphSpacing = 0.5f;

        // The text to display.
        private const string MessageText =
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse lobortis blandit mauris, a sagittis libero. Proin a posuere justo, vel scelerisque risus.\n" +
            "Sed condimentum suscipit est in sagittis. Maecenas ac nulla in metus gravida feugiat nec vel odio. Aenean vulputate urna vel gravida rhoncus.\n" +
            "Etiam vel lacinia urna, non ultrices arcu. Curabitur eget neque nec felis facilisis lacinia. Donec sit amet neque vel ligula scelerisque cursus et quis nisl.\n" +
            "Proin convallis metus elit, eu condimentum nunc ultrices vel. Maecenas elementum orci tellus, quis pretium risus fringilla non.\n" +
            "Quisque eget diam a erat vestibulum cursus ut nec nisi. Duis non velit quis augue mattis consectetur pharetra sed dolor.\n" +
            "Pellentesque luctus tempor ornare.\n" +
            "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin pellentesque dolor in leo porttitor, dignissim sollicitudin nulla bibendum.\n" +
            "Nullam sit amet faucibus nunc, nec laoreet orci. Etiam nec rutrum mauris. Integer sapien felis, placerat id orci eu, fermentum porta dui.\n" +
            "Nam in pharetra orci, sed sollicitudin urna. Suspendisse sit amet tellus sagittis, lobortis ante quis, consectetur est.\n" +
            "Aliquam tempor ligula in augue facilisis, vehicula fermentum sem elementum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox3.Paint += new PaintEventHandler(pictureBox3_Paint);
            pictureBox3.Resize += new EventHandler(pictureBox3_Resize);
        }

        // Draw justified text on the PictureBox.
        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.Clear(pictureBox3.BackColor);
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

            // Draw within a rectangle excluding the margins.
            RectangleF rect = new RectangleF(TextMargin.Left, TextMargin.Top,
                pictureBox3.ClientSize.Width - TextMargin.Left - TextMargin.Right,
                pictureBox3.ClientSize.Height - TextMargin.Top - TextMargin.Bottom);

            /*
            // Get the desired alignment.
            TextJustification justification = TextJustification.Left;
            if (chkCenter.Checked)
                justification = TextJustification.Center;
            else if (chkRight.Checked)
                justification = TextJustification.Right;
            else if (chkFull.Checked)
                justification = TextJustification.Full;
            */

            // Draw the text.
            using (Font font = new Font("Times New Roman", 10))
            {
                if ((justification == TextJustification.Right) || (justification == TextJustification.Center))
                {
                    rect = DrawParagraphs(e.Graphics, rect, font, Brushes.Green, MessageText, justification,
                        LineSpacing, 0, ExtraParagraphSpacing);
                }
                else
                {
                    rect = DrawParagraphs(e.Graphics, rect, font, Brushes.Green, MessageText, justification,
                        LineSpacing, ParagraphIndent, ExtraParagraphSpacing);
                }
            }

            // Show the text drawing area.
            rect = new RectangleF(TextMargin.Left, TextMargin.Top,
                pictureBox3.ClientSize.Width - TextMargin.Left - TextMargin.Right,
                pictureBox3.ClientSize.Height - TextMargin.Top - TextMargin.Bottom);
            e.Graphics.DrawRectangle(Pens.Silver, Rectangle.Round(rect));
        }
        private void pictureBox3_Resize(object sender, EventArgs e)
        {
            pictureBox3.Refresh();
        }

        // Draw justified text on the Graphics object in the indicated Rectangle.
        private RectangleF DrawParagraphs(Graphics gr, RectangleF rect, Font font, Brush brush, string text,
            TextJustification justification, float line_spacing, float indent, float paragraph_spacing)
        {
            // Split the text into paragraphs.
            string[] paragraphs = text.Split('\n');

            // Draw each paragraph.
            foreach (string paragraph in paragraphs)
            {
                // Draw the paragraph keeping track of remaining space.
                rect = DrawParagraph(gr, rect, font, brush, paragraph, justification, line_spacing, indent, paragraph_spacing);

                // See if there's any room left.
                if (rect.Height < font.Size)
                {
                    break;
                }
            }
            return rect;
        }

        // Draw a paragraph by lines inside the Rectangle.
        // Return a RectangleF representing any unused
        // space in the original RectangleF.
        private RectangleF DrawParagraph(Graphics gr, RectangleF rect, Font font, Brush brush, string text,
            TextJustification justification, float line_spacing, float indent, float extra_paragraph_spacing)
        {
            // Get the coordinates for the first line.
            float y = rect.Top;

            // Break the text into words.
            string[] words = text.Split(' ');
            int start_word = 0;

            // Repeat until we run out of text or room.
            for (; ; )
            {
                // See how many words will fit.
                // Start with just the next word.
                string line = words[start_word];

                // Add more words until the line won't fit.
                int end_word = start_word + 1;
                while (end_word < words.Length)
                {
                    // See if the next word fits.
                    string test_line = line + " " + words[end_word];
                    SizeF line_size = gr.MeasureString(test_line, font);
                    if (line_size.Width + indent > rect.Width)
                    {
                        // The line is too wide. Don't use the last word.
                        end_word--;
                        break;
                    }
                    else
                    {
                        // The word fits. Save the test line.
                        line = test_line;
                    }

                    // Try the next word.
                    end_word++;
                }

                // See if this is the last line in the paragraph.
                if ((end_word == words.Length) && (justification == TextJustification.Full))
                {
                    // This is the last line. Don't justify it.
                    DrawLine(gr, line, font, brush, rect.Left + indent, y, rect.Width - indent, TextJustification.Left);
                }
                else
                {
                    // This is not the last line. Justify it.
                    DrawLine(gr, line, font, brush, rect.Left + indent, y, rect.Width - indent, justification);
                }

                // Move down to draw the next line.
                y += font.Height * line_spacing;

                // Make sure there's room for another line.
                if (font.Size > rect.Height)
                {
                    break;
                }

                // Start the next line at the next word.
                start_word = end_word + 1;
                if (start_word >= words.Length)
                {
                    break;
                }

                // Don't indent subsequent lines in this paragraph.
                indent = 0;
            }

            // Add a gap after the paragraph.
            y += font.Height * extra_paragraph_spacing;

            // Return a RectangleF representing any unused
            // space in the original RectangleF.
            float height = rect.Bottom - y;
            if (height < 0)
            {
                height = 0;
            }
            return new RectangleF(rect.X, y, rect.Width, height);
        }

        // Draw a line of text.
        private void DrawLine(Graphics gr, string line, Font font, Brush brush, float x, float y, float width, TextJustification justification)
        {
            // Make a rectangle to hold the text.
            RectangleF rect = new RectangleF(x, y, width, font.Height);

            // See if we should use full justification.
            if (justification == TextJustification.Full)
            {
                // Justify the text.
                DrawJustifiedLine(gr, rect, font, brush, line);
            }
            else
            {
                // Make a StringFormat to align the text.
                using (StringFormat sf = new StringFormat())
                {
                    // Use the appropriate alignment.
                    switch (justification)
                    {
                        case TextJustification.Left:
                            sf.Alignment = StringAlignment.Near;
                            break;
                        case TextJustification.Right:
                            sf.Alignment = StringAlignment.Far;
                            break;
                        case TextJustification.Center:
                            sf.Alignment = StringAlignment.Center;
                            break;
                    }
                    gr.DrawString(line, font, brush, rect, sf);
                }
            }
        }

        // Draw justified text on the Graphics object
        // in the indicated Rectangle.
        private void DrawJustifiedLine(Graphics gr, RectangleF rect, Font font, Brush brush, string text)
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
            if (words.Length > 1)
            {
                extra_space /= num_spaces;
            }

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

        /*
        // Uncheck the othuer ToolStripButtons and redraw the text.
        private void chkAlignment_Click(object sender, EventArgs e)
        {
            // Uncheck the other buttons.
            ToolStripButton btn = sender as ToolStripButton;
            ToolStripButton[] buttons = { chkLeft, chkCenter, chkRight, chkFull };
            foreach (ToolStripButton test_button in buttons)
            {
                if (test_button != btn) test_button.Checked = false;
            }

            // Redraw the text.
            pictureBox3.Refresh();
        }
        */

        private void btn_alignment(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            if (btn.Name == "button1")
                justification = TextJustification.Left;
            else if (btn.Name == "button2")
                justification = TextJustification.Center;
            else if (btn.Name == "button3")
                justification = TextJustification.Right;
            else if (btn.Name == "button4")
                justification = TextJustification.Full;

            // Redraw the text.
            pictureBox3.Refresh();
        }
    }
}
