using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        int x0 = 30;  // 左上角座標定位點
        int y0 = 30;

        Rectangle rectRed, rectGreen, rectBlue;
        bool dragging = false;
        int dx, dy;

        List<G2D_DraggingRect> rectList = new List<G2D_DraggingRect>();
        G2D_DraggingRect rectSelected;
        
        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(720, 660);

            rectRed = new Rectangle(650, 60, 30, 30);
            rectGreen = new Rectangle(650, 100, 30, 30);
            rectBlue = new Rectangle(650, 140, 30, 30);

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.FillRectangle(Brushes.Red, rectRed);
            e.Graphics.FillRectangle(Brushes.Green, rectGreen);
            e.Graphics.FillRectangle(Brushes.Blue, rectBlue);

            for (int i = 0; i < rectList.Count; i++)
            {
                rectList[i].Draw(e.Graphics);
            }

            for (int i = 0; i <= 20; i++)
            {
                e.Graphics.DrawLine(Pens.Black, x0 + i * 30, y0, x0 + i * 30, y0 + 600);
                e.Graphics.DrawLine(Pens.Black, x0, y0 + i * 30, x0 + 600, y0 + i * 30);
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            G2D_DraggingRect rectNew;

            if (rectRed.Contains(e.Location))
            {
                dragging = true;
                rectNew = new G2D_DraggingRect(Color.Red, rectRed);
                rectList.Add(rectNew);
                rectSelected = rectNew;
                dx = e.X - rectSelected.rect.X;
                dy = e.Y - rectSelected.rect.Y;
            }
            else if (rectGreen.Contains(e.Location))
            {
                dragging = true;
                rectNew = new G2D_DraggingRect(Color.Green, rectGreen);
                rectList.Add(rectNew);
                rectSelected = rectNew;
                dx = e.X - rectSelected.rect.X;
                dy = e.Y - rectSelected.rect.Y;
            }
            else if (rectBlue.Contains(e.Location))
            {
                dragging = true;
                rectNew = new G2D_DraggingRect(Color.Blue, rectBlue);
                rectList.Add(rectNew);
                rectSelected = rectNew;
                dx = e.X - rectSelected.rect.X;
                dy = e.Y - rectSelected.rect.Y;
            }
            else
            {
                for (int i = 0; i < rectList.Count; i++)
                {
                    if (rectList[i].rect.Contains(e.Location))
                    {
                        dragging = true;
                        rectSelected = rectList[i];
                        dx = e.X - rectSelected.rect.X;
                        dy = e.Y - rectSelected.rect.Y;
                    }
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                rectSelected.rect = new Rectangle(e.X - dx, e.Y - dy, 30, 30);
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
           dragging = false;

           //int x = (int)(Math.Round((rectSelected.rect.X - x0) / 30.0));
           //int y = (int)(Math.Round((rectSelected.rect.Y - y0) / 30.0));

           int x = (int)((rectSelected.rect.X - x0) / 30);
           int y = (int)((rectSelected.rect.Y - y0) / 30);
           rectSelected.rect = new Rectangle(x * 30 + x0, y * 30 + y0, 30, 30);
           this.Invalidate();
        }
    }
}
