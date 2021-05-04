using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class G2D_DraggingRect
    {
        public Color color;
        public Rectangle rect;

        public G2D_DraggingRect(Color color, Rectangle rect)
        {
            this.color = color;
            this.rect = rect;
        }

        public void Draw(Graphics G)
        {
            G.FillRectangle(new SolidBrush(color), rect);
        }
    }
}
