using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Chess3
{
    public partial class Form1 : Form
    {
        int D = 10; // 格子寬
        Point Center = new Point(); // 格線中心點
        bool Dragging = false;      // 是否 拖曳 格線中
        Point MousePos = new Point(); // 紀錄 滑鼠游標位置

        Image image = new Bitmap(Properties.Resources.ChamferBox);
        List<ClassX> ImageSet = new List<ClassX>(); // 動態陣列

        public Form1()
        {
            InitializeComponent();
            // 加入滾輪事件
            this.MouseWheel += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseWheel);

            int w = this.ClientSize.Width;
            int h = this.ClientSize.Height;
            Center = new Point(w / 2, h / 2);  // 預設格線中心點
        }

        // 滾輪事件 函數
        private void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            if (e.Delta > 0) // 滾輪往前
            {
                D++; // 格子變大
            }
            else if (e.Delta < 0) // 滾輪往後
            {
                D--; // 格子變小
                if (D < 2) D = 2; // 格子最小的單位
            }
            this.Invalidate();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left) // 滑鼠左鍵
            {
                // 加入 物件
                ClassX temp = new ClassX(image);
                temp.SetPos((e.X - Center.X) / (float)D, (e.Y - Center.Y) / (float)D);
                temp.SetScale(0.2f);

                ImageSet.Add(temp);
            }
            else if (e.Button == MouseButtons.Middle) // 滑鼠中鍵
            {
                Dragging = true; // 開始拖曳 格子座標
                MousePos = e.Location; // 紀錄滑鼠游標座標
                this.Cursor = Cursors.NoMove2D; // 更新滑鼠游標 
            }
            this.Invalidate(); // 重繪
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int w = this.ClientSize.Width;
            int h = this.ClientSize.Height;

            // 繪出 格子
            //grid.Draw(w, h, D, Center, e.Graphics);
            Grid.Draw(w, h, D, Center, e.Graphics);

            // 繪出 全部 物件
            foreach (ClassX k in ImageSet)
            {
                k.Draw(e.Graphics, D, Center);
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            Dragging = false; // 停止拖曳
            this.Cursor = Cursors.Default; // 更新滑鼠游標
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (Dragging) // 拖曳中
            {
                // 計算 新的格子中心點
                Center.X = Center.X + (e.X - MousePos.X);
                Center.Y = Center.Y + (e.Y - MousePos.Y);

                MousePos = e.Location;
                this.Invalidate();
            }
        }
    }
}
