using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;  // for GraphicsPath

namespace vcs_ScreenCapture3
{
    public partial class FullScreenForm : Form
    {
        private Rectangle rectSelected = Rectangle.Empty;
        private bool isClipping = false;
        private Bitmap screen;
        private Bitmap coverLayer = null;
        private Color coverColor;
        private Brush rectBrush = null;
        private Bitmap resultBmp = null;

        public FullScreenForm(Bitmap screen)
        {
            InitializeComponent();

            int width = Screen.PrimaryScreen.Bounds.Width;
            int height = Screen.PrimaryScreen.Bounds.Height;
            coverLayer = new Bitmap(width, height);
            coverColor = Color.FromArgb(50, 200, 0, 0);
            rectBrush = new SolidBrush(coverColor);

            using (Graphics g = Graphics.FromImage(coverLayer))
            {
                g.Clear(coverColor);
            }

            this.Bounds = new Rectangle(0, 0, width, height);

            this.screen = screen;

            this.DoubleBuffered = true;
        }

        private void FullScreenForm_Load(object sender, EventArgs e)
        {

        }


        protected override void OnMouseDown(MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isClipping = true;
                rectSelected.Location = e.Location;
            }
            else if (e.Button == MouseButtons.Right)
            {
                this.DialogResult = DialogResult.OK;
                this.Close();
            }
        }

        protected override void OnMouseMove(MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left && isClipping)
            {
                rectSelected.Width = e.X - rectSelected.X;
                rectSelected.Height = e.Y - rectSelected.Y;

                this.Invalidate();
            }
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left && isClipping)
            {
                rectSelected.Width = e.X - rectSelected.X;
                rectSelected.Height = e.Y - rectSelected.Y;
                this.Invalidate();

                resultBmp = new Bitmap(rectSelected.Width, rectSelected.Height);
                using (Graphics g = Graphics.FromImage(resultBmp))
                {
                    g.DrawImage(screen, new Rectangle(0, 0, rectSelected.Width, rectSelected.Height), rectSelected, GraphicsUnit.Pixel);
                }
                this.DialogResult = DialogResult.OK;
            }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.DrawImage(screen, 0, 0);
            g.DrawImage(coverLayer, 0, 0);
            PaintRectangle();
        }

        protected override void OnPaintBackground(PaintEventArgs e)
        {

        }

        protected override void OnKeyDown(KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)
            {
                this.DialogResult = DialogResult.Cancel;
            }
        }

        private void PaintRectangle()
        {
            using (Graphics g = Graphics.FromImage(coverLayer))
            {
                g.Clear(coverColor);
                GraphicsPath path = new GraphicsPath();
                path.AddRectangle(this.Bounds);
                path.AddRectangle(rectSelected);
                g.FillPath(rectBrush, path);
                g.DrawRectangle(Pens.Blue, rectSelected);
            }
        }

        public Bitmap ResultBitmap
        {
            get { return resultBmp; }
        }
    }
}



/*

接下來為了方便在這之上進行截圖，有一個很重要的設計實現方式：
用全屏幕窗體代替現有真實屏幕，
這樣就可以把截圖過程的所有操作都在那個窗體上實現（該窗體設置成無邊框，高寬等於屏幕大小即可），
另外為了顯示掩蔽效果（只能正常顯示選擇的部分屏幕內容，而其實部分用一個如半透明層覆蓋），
就添加一層半透明位置位圖。




*/

