using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace WindowsFormsApplication1dddd
{
    public partial class Form1 : Form
    {
        private Rectangle rectSelected = Rectangle.Empty;

        private bool isClipping = false;

        private Bitmap screen;

        private Bitmap coverLayer = null;

        private Color coverColor;

        private Brush rectBrush = null;

        private Bitmap resultBmp = null;



        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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
            /*
            Graphics g = e.Graphics;

            g.DrawImage(screen, 0, 0);

            g.DrawImage(coverLayer, 0, 0);

            PaintRectangle();
            */
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
    

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
