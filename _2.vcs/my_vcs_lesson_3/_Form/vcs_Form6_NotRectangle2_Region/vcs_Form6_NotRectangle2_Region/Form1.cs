using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_Form6_NotRectangle2_Region
{
    public partial class Form1 : Form
    {
        int mode = 3;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
            this.BackColor = Color.Pink;

            //測試region
            this.Region = null;

            if (mode == 0)
            {
                //用GP製作非矩形視窗

                //先製作非矩形的GP
                GraphicsPath gp = new GraphicsPath();
                gp.AddPie(0, 0, this.Width, this.Height * 2, 190, 160);

                //將此GP設定給表單的Region參數

                //Region的用法
                Region region = new Region(gp);
                this.Region = region;
                //this.Region = new Region(gp); //same
            }
            else if (mode == 1)
            {
                //繪製圓角表單
                this.Region = null;
                SetWindowRegion();
            }
            else if (mode == 2)
            {
                //不規則表單 Region
                //通過設置窗體的Region屬性，製作不規則窗體。
                int W = this.ClientSize.Width;
                int H = this.ClientSize.Height / 2;

                GraphicsPath gp = new GraphicsPath();
                Rectangle rect = new Rectangle(0, 0, W, H);
                gp.AddEllipse(rect);
                Region r = new Region(gp);
                this.Region = r;
                //this.Region = new Region(gp); same
            }
            else if (mode == 3)
            {
                create_irregular_form();
            }
        }

        public void SetWindowRegion()
        {
            Rectangle rect = new Rectangle(0, 22, this.Width, this.Height - 22);

            GraphicsPath FormPath = GetRoundedRectPath(rect, 30);
            this.Region = new Region(FormPath);
        }

        private GraphicsPath GetRoundedRectPath(Rectangle rect, int radius)
        {
            int diameter = radius;
            Rectangle arcRect = new Rectangle(rect.Location, new Size(diameter, diameter));
            GraphicsPath path = new GraphicsPath();
            // 左上
            path.AddArc(arcRect, 180, 90);
            // 右上
            arcRect.X = rect.Right - diameter;
            path.AddArc(arcRect, 270, 90);
            // 右下
            arcRect.Y = rect.Bottom - diameter;
            path.AddArc(arcRect, 0, 90);
            // 左下
            arcRect.X = rect.Left;
            path.AddArc(arcRect, 90, 90);
            path.CloseFigure();
            return path;
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
                pts[i] = new PointF((float)(cx + r1 * Math.Cos(theta)), (float)(cy + r1 * Math.Sin(theta)));
                theta += dtheta;
                pts[i + 1] = new PointF((float)(cx + r2 * Math.Cos(theta)), (float)(cy + r2 * Math.Sin(theta)));
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
    }
}
