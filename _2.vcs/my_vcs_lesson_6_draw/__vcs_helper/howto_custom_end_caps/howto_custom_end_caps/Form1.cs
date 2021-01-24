using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_custom_end_caps
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a GraphicsPath to define the start cap.
            using (GraphicsPath start_path = new GraphicsPath())
            {
                start_path.AddArc(-2, 0, 4, 4, 180, 180);

                // Make the start cap.
                using (CustomLineCap start_cap =
                    new CustomLineCap(null, start_path))
                {
                    // Make a GraphicsPath to define the end cap.
                    using (GraphicsPath end_path = new GraphicsPath())
                    {
                        end_path.AddLine(0, 0, -2, -2);
                        end_path.AddLine(0, 0, 2, -2);

                        // Make the end cap.
                        using (CustomLineCap end_cap =
                            new CustomLineCap(null, end_path))
                        {
                            // Make a pen that uses the custom caps.
                            using (Pen the_pen = new Pen(Color.Blue, 5))
                            {
                                the_pen.CustomStartCap = start_cap;
                                the_pen.CustomEndCap = end_cap;

                                // Draw a line.
                                e.Graphics.DrawLine(the_pen, 40, 40, 200, 40);

                                // Draw a polygon.
                                PointF[] points = new PointF[] 
                                {
                                    new PointF(40, 80),
                                    new PointF(120, 100),
                                    new PointF(230, 70),
                                };
                                the_pen.Color = Color.Green;
                                e.Graphics.DrawLines(the_pen, points);

                                // Draw a transformed arc.
                                e.Graphics.ScaleTransform(3, 1);
                                the_pen.Color = Color.Red;
                                e.Graphics.DrawArc(the_pen, 20, 120, 70, 60, 180, 270);
                            }
                        }
                    }
                }
            }
        }
    }
}
