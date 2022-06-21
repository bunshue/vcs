using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_Form6_NotRectangle6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            create_irregular_form();

            bt_exit.Location = new Point(200, 200);
        }

        void create_irregular_form()
        {
            //建立一個不規則的表單
            // Make points to define a polygon for the form.
            PointF[] pts = new PointF[10];
            float cx = (float)(this.ClientSize.Width * 0.5);
            float cy = (float)(this.ClientSize.Height * 0.5);
            float r1 = (float)(this.ClientSize.Height * 0.45);
            float r2 = (float)(this.ClientSize.Height * 0.25);
            float theta = (float)(-Math.PI / 2);
            float dtheta = (float)(2 * Math.PI / 10);
            for (int i = 0; i < 10; i += 2)
            {
                pts[i] = new PointF(
                    (float)(cx + r1 * Math.Cos(theta)),
                    (float)(cy + r1 * Math.Sin(theta)));
                theta += dtheta;
                pts[i + 1] = new PointF(
                    (float)(cx + r2 * Math.Cos(theta)),
                    (float)(cy + r2 * Math.Sin(theta)));
                theta += dtheta;
            }

            // Use the polygon to define a GraphicsPath.
            GraphicsPath path = new GraphicsPath();
            path.AddPolygon(pts);

            // Make a region from the path.
            Region form_region = new Region(path);

            // Restrict the form to the region.
            this.Region = form_region;

        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}

