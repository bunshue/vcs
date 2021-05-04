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

        Rectangle rectRed, rectGreen, rectBlue; // 三個顏色方塊 出發點
        bool dragging = false; // 是否拖曳中
        int dx, dy;  // 滑鼠偏移值

        List<G2D_DraggingRect> rectList = new List<G2D_DraggingRect>(); // 方塊清單
        G2D_DraggingRect rectSelected; // 被選中的方塊
        int rectListNow; // 被選中的方塊 的編號  刪除時要用的

        int Grid = 20; // 格子數目
        int Gwidth; // 格子寬
        
        public Form1()
        {
            InitializeComponent();

            InitialGrid();
        }

        void InitialGrid() // 初始化 格子
        {
            Gwidth = 600 / Grid; // 格子寬
            rectRed = new Rectangle(650, y0, Gwidth, Gwidth);
            rectGreen = new Rectangle(650, y0 + Gwidth + 10, Gwidth, Gwidth);
            rectBlue = new Rectangle(650, y0 + 2 * Gwidth + 20, Gwidth, Gwidth);
            this.ClientSize = new Size(650 + Gwidth + 20, 660); // 視窗客戶區的寬
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 繪出 三個顏色方塊
            e.Graphics.FillRectangle(Brushes.Red, rectRed);
            e.Graphics.FillRectangle(Brushes.Green, rectGreen);
            e.Graphics.FillRectangle(Brushes.Blue, rectBlue);

            // 依序 繪出 小方塊
            for (int i = 0; i < rectList.Count; i++)
            {
                rectList[i].Draw(e.Graphics);
            }

            // 繪出格子
            for (int i = 0; i <= Grid; i++)
            {
                e.Graphics.DrawLine(Pens.Black, x0 + i * Gwidth, y0, x0 + i * Gwidth, y0 + Gwidth * Grid);
                e.Graphics.DrawLine(Pens.Black, x0, y0 + i * Gwidth, x0 + Gwidth * Grid, y0 + i * Gwidth);
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            G2D_DraggingRect rectNew;

            if (rectRed.Contains(e.Location)) // 選到 紅色方塊
            {
                dragging = true;
                rectNew = new G2D_DraggingRect(Color.Red, rectRed);
                rectList.Add(rectNew); // 新增一個 紅色方塊
                rectSelected = rectNew;
                rectListNow = rectList.Count - 1; // 被選中的方塊 的編號 
                dx = e.X - rectSelected.rect.X;
                dy = e.Y - rectSelected.rect.Y;
            }
            else if (rectGreen.Contains(e.Location)) // 選到 綠色方塊
            {
                dragging = true;
                rectNew = new G2D_DraggingRect(Color.Green, rectGreen);
                rectList.Add(rectNew); // 新增一個 綠色方塊
                rectSelected = rectNew;
                rectListNow = rectList.Count - 1; // 被選中的方塊 的編號 
                dx = e.X - rectSelected.rect.X;
                dy = e.Y - rectSelected.rect.Y;
            }
            else if (rectBlue.Contains(e.Location)) // 選到 藍色方塊
            {
                dragging = true;
                rectNew = new G2D_DraggingRect(Color.Blue, rectBlue);
                rectList.Add(rectNew); // 新增一個 藍色方塊
                rectSelected = rectNew;
                rectListNow = rectList.Count - 1; // 被選中的方塊 的編號 
                dx = e.X - rectSelected.rect.X;
                dy = e.Y - rectSelected.rect.Y;
            }
            else
            {
                for (int i = rectList.Count - 1; i >= 0; i--)  // 從後面開始找 因為後面的會蓋在上面
                {
                    if (rectList[i].rect.Contains(e.Location))
                    {
                        dragging = true;
                        rectSelected = rectList[i];
                        rectListNow = i;
                        dx = e.X - rectSelected.rect.X;
                        dy = e.Y - rectSelected.rect.Y;
                        break;
                    }
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (dragging)
            {
                rectSelected.rect = new Rectangle(e.X - dx, e.Y - dy, Gwidth, Gwidth);
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
           dragging = false;

           int x = (int)((rectSelected.rect.X - x0) / Gwidth);
           int y = (int)((rectSelected.rect.Y - y0) / Gwidth);

           if (x < 0 || x >= Grid || y < 0 || y >= Grid) // 拖到外面 就刪除 
           {
               rectList.RemoveAt(rectListNow);
           }
           else // 拖到裡面 就 就定位 
           {
               rectSelected.rect = new Rectangle(x * Gwidth + x0, y * Gwidth + y0, Gwidth, Gwidth);
           }

           this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Up) // 增加格子數目 
            {
                if (Grid < 20) Grid++;
                InitialGrid();
                rectList.Clear();
                this.Invalidate();
            }
            else if (e.KeyData == Keys.Down) // 減少格子數目 
            {
                if (Grid > 3) Grid--;
                InitialGrid();
                rectList.Clear();
                this.Invalidate();
            }
            else if (e.KeyData == Keys.Space)  // 清空
            {
                rectList.Clear();
                this.Invalidate();
            }
        }
    }
}
