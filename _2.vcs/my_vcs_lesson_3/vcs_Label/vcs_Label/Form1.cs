using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Text;  //for TextRenderingHint
using System.Drawing.Drawing2D; //for MatrixOrder

namespace vcs_Label
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Hide the labels that position the rotated text.
        private void Form1_Load(object sender, EventArgs e)
        {
            lblRotated1.Visible = false;
            lblRotated2.Visible = false;
            lblRotated3.Visible = false;
        }

        // Draw rotated text.
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;

                e.Graphics.TextRenderingHint =
                    TextRenderingHint.AntiAliasGridFit;
                DrawSidewaysText(e.Graphics, Font, Brushes.Black,
                    lblRotated1.Bounds, string_format, "Row 1");
                DrawSidewaysText(e.Graphics, Font, Brushes.Black,
                    lblRotated2.Bounds, string_format, "Row 2");
                DrawSidewaysText(e.Graphics, Font, Brushes.Black,
                    lblRotated3.Bounds, string_format, "Row 3");
            }
        }

        // Draw sideways text in the indicated rectangle.
        private void DrawSidewaysText(Graphics gr, Font font, Brush brush, Rectangle bounds, StringFormat string_format, string txt)
        {
            // Make a rotated rectangle at the origin.
            Rectangle rotated_bounds = new Rectangle(
                0, 0, bounds.Height, bounds.Width);

            // Rotate.
            gr.ResetTransform();
            gr.RotateTransform(-90);

            // Translate to move the rectangle to the correct position.
            gr.TranslateTransform(bounds.Left, bounds.Bottom, MatrixOrder.Append);

            // Draw the text.
            gr.DrawString(txt, font, brush, rotated_bounds, string_format);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            lb_moving.Left -= 2;
            if (lb_moving.Right < 0)
            {
                lb_moving.Left = this.Width;
            }
        }
    }
}
