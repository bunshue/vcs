using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Clock5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private LedText TimeLedText, DateLedText;
        private void Form1_Load(object sender, EventArgs e)
        {
            const float cell_width = 50;
            const float cell_height = 80;
            const float led_thickness = 7;
            const float gap = 1.5f;
            TimeLedText = new LedText(cell_width,
                cell_height, led_thickness, gap);

            const float scale = 0.95f;
            DateLedText = new LedText(scale * cell_width,
                scale * cell_height, scale * led_thickness,
                scale * gap);
        }

        private void tmrTick_Tick(object sender, EventArgs e)
        {
            picClock.Refresh();
        }

        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            ShowTime(e.Graphics);
        }

        // Display the time.
        private void ShowTime(Graphics gr)
        {
            gr.Clear(Color.Black);
            gr.SmoothingMode = SmoothingMode.AntiAlias;

            const float margin = 5f;
            PointF position = new PointF(margin, margin);
            using (Brush unused_brush = new SolidBrush(Color.FromArgb(0, 40, 0)))
            {
                // Draw the time.
                Brush bg_brush = Brushes.Black;
                Brush used_brush = Brushes.Lime;
                Pen used_pen = Pens.Transparent;
                Pen unused_pen = Pens.Transparent;

                TimeLedText.DrawText(gr, bg_brush,
                    used_brush, used_pen,
                    unused_brush, unused_pen,
                    position, 1.2f,
                    DateTime.Now.ToLongTimeString());
            }

            using (Brush unused_brush = new SolidBrush(Color.FromArgb(0, 0, 60)))
            {
                // Draw the time.
                Brush bg_brush = Brushes.Black;
                Brush used_brush = Brushes.Blue;
                Pen used_pen = Pens.Transparent;
                Pen unused_pen = Pens.Transparent;

                position.Y += TimeLedText.CellHeight +
                    4 * TimeLedText.LedThickness;

                // Draw the day and date.
                string date_string =
                    DateTime.Now.DayOfWeek.ToString();
                date_string = date_string.ToUpper().Substring(0, 3);
                date_string += " " +
                    DateTime.Now.Day.ToString() + "/" +
                    DateTime.Now.Year.ToString().Substring(0, 2);
                DateLedText.DrawText(gr, bg_brush,
                    used_brush, used_pen,
                    unused_brush, unused_pen,
                    position, 1.2f,
                    date_string);
            }
        }
    }
}
