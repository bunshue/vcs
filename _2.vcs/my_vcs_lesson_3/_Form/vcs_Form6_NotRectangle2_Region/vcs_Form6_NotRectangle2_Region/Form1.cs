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

            /*
            //用GP製作非矩形視窗

            //先製作非矩形的GP
            GraphicsPath gp = new GraphicsPath();
            gp.AddPie(0, 0, this.Width, this.Height * 2, 190, 160);

            //將此GP設定給表單的Region參數

            //Region的用法
            Region region = new Region(gp);
            this.Region = region;
            //this.Region = new Region(gp); //same
            */

            //繪製圓角表單
            //SetWindowRegion();
            this.Region = null;
            SetWindowRegion();
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
    }
}
