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
        int mode = 4;

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
                //簡易圓形Region
                GraphicsPath gp = new GraphicsPath();
                gp.AddEllipse(this.ClientRectangle);

                //將此GP設定給表單的Region參數
                //Region的用法
                Region region = new Region(gp);//Make a region from the path
                this.Region = region;
                //this.Region = new Region(gp); //same
            }
            else if (mode == 1)
            {
                //用GP製作非矩形視窗

                //先製作非矩形的GP
                GraphicsPath gp = new GraphicsPath();
                gp.AddPie(0, 0, this.Width, this.Height * 2, 190, 160);

                //將此GP設定給表單的Region參數
                //Region的用法
                Region region = new Region(gp);//Make a region from the path
                this.Region = region;
                //this.Region = new Region(gp); //same
            }
            else if (mode == 2)
            {
            }
            else if (mode == 3)
            {
                //不規則表單 Region
                //通過設置窗體的Region屬性，製作不規則窗體。
                int W = this.ClientSize.Width;
                int H = this.ClientSize.Height / 2;

                GraphicsPath gp = new GraphicsPath();
                Rectangle rect = new Rectangle(0, 0, W, H);
                gp.AddEllipse(rect);
                Region region = new Region(gp);
                this.Region = region;
                //this.Region = new Region(gp);  // same
            }
            else if (mode == 4)
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
                GraphicsPath gp = new GraphicsPath();
                gp.AddPolygon(pts);

                // Make a region from the path.
                Region region = new Region(gp);

                // Restrict the form to the region.
                this.Region = region;
            }
        }

    }
}
