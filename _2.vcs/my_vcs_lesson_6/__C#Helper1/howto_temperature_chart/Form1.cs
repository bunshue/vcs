using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Printing;
using System.Drawing.Text;

namespace howto_temperature_chart
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void pdocChart_PrintPage(object sender, PrintPageEventArgs e)
        {
            const float font_size = 12;
            const float dy = font_size * 1.5f;
            float x0 = e.MarginBounds.Left + 0.5f * 100;
            float x1 = x0 + 0.75f * 100;
            float y = e.MarginBounds.Top;
            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            using (Font font = new Font("Times New Roman", font_size))
            {
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;

                    e.Graphics.DrawString("Celsius", font, Brushes.Blue, x0, y, sf);
                    e.Graphics.DrawString("Fahrenheit", font, Brushes.Blue, x1, y, sf);
                    y += dy;

                    for (int celsius = 60; celsius <= 250; celsius += 5)
                    {
                        float fahrenheit = celsius * 9f / 5f + 32;
                        e.Graphics.DrawString(celsius.ToString(),
                            font, Brushes.Black, x0, y, sf);
                        e.Graphics.DrawString(fahrenheit.ToString("0"),
                            font, Brushes.Black, x1, y, sf);
                        y += dy;
                    }

                    y = e.MarginBounds.Top;
                    float x2 = x1 + 1.2f * 100;
                    float x3 = x2 + 0.75f * 100;
                    e.Graphics.DrawString("Fahrenheit", font, Brushes.Blue, x2, y, sf);
                    e.Graphics.DrawString("Celsius", font, Brushes.Blue, x3, y, sf);
                    y += dy;

                    for (int fahrenheit = 140; fahrenheit <= 500; fahrenheit += 10)
                    {
                        float celsius = (fahrenheit - 32) * 5f / 9f;
                        e.Graphics.DrawString(fahrenheit.ToString(),
                            font, Brushes.Black, x2, y, sf);
                        e.Graphics.DrawString(celsius.ToString("0"),
                            font, Brushes.Black, x3, y, sf);
                        y += dy;
                    }
                }
            }
        }

        private void btnCreateChart_Click(object sender, EventArgs e)
        {
            ppdChart.ShowDialog();
        }
    }
}
