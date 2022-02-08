using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace vcs_ColorMixer2
{
    class G2D_ColorRect  // 顏色矩形類別
    {
        int Cx, Cy; // 矩形的 中心點
        int w, h;   // 矩形的 寬高
        public Color color; // 矩形的 顏色

        public bool drag = false; // 矩形是否拖曳中 
        int dx, dy;  // 記錄 矩形的中心點 和滑鼠游標的 距離


        public G2D_ColorRect(int Cx, int Cy, int w, int h, Color color)
        {
            this.Cx = Cx;
            this.Cy = Cy;

            this.w = w;
            this.h = h;

            this.color = color;
        }

        // 看看滑鼠游標 是否選到 顏色矩形物件
        public void check(int eX, int eY)
        {
            Rectangle rect = GetRect();

            if (rect.Contains(eX, eY))  // 如果選到
            {
                drag = true;  // 就記錄為 拖曳中
                dx = eX - Cx;
                dy = eY - Cy;
            }
        }

        public void update(int eX, int eY)
        {
            if (drag) // 如果 拖曳中
            {
                Cx = eX - dx;  // 就 更新 矩形的 中心點
                Cy = eY - dy;
            }
        }

        // 得到 矩形的 區域
        public Rectangle GetRect()
        {
            Rectangle rect = new Rectangle(Cx - w/ 2, Cy - h / 2, w, h);
            return rect;
        }

        // 矩形繪出
        public void Draw(Graphics G)
        {
            SolidBrush myBrush = new SolidBrush(color);

            G.FillRectangle(myBrush, GetRect());
            G.DrawRectangle(Pens.Black, GetRect());
        }
    }
}
