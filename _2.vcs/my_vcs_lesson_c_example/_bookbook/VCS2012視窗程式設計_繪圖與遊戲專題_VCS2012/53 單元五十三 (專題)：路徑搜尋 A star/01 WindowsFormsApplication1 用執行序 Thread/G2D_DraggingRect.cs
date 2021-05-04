using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_DraggingRect
    {
        public Point pos; // 中心點
        short D; // 半徑
        SolidBrush brush;

        public G2D_DraggingRect(Point pos, Color color, short D)
        {
            this.pos = pos;
            this.D = D;
            brush = new SolidBrush(color);
        }

        public Rectangle GetRect()
        {
           return new Rectangle(pos.X - D, pos.Y - D, D* 2, D * 2);
        }

        public void Draw(Graphics G)
        {
            Rectangle rect = new Rectangle(pos.X - (D - 2), pos.Y - (D - 2), (D - 2) * 2, (D - 2) * 2);
            G.FillRectangle(brush, rect);
        }
    }
}
