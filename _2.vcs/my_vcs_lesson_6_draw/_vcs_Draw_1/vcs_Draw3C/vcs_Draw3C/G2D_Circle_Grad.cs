using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace vcs_Draw3C
{
    class G2D_Circle_Grad  // 矩形 W 寬
    {
        public Bitmap bitmap;
        public G2D_Circle_Grad(int W, float r, Color myColor)  //  r = 0.25f
        {
            bitmap = new Bitmap(W, W);
            Color color;
            float dis;
            float R = r * W; //中間實心的圓 的半徑

            for (int x =0; x < W;x++)
                for (int y = 0; y < W; y++)
                {
                    dis = (float)(Math.Sqrt((x - W / 2) * (x - W / 2) + (y - W / 2) * (y - W / 2)));
                    if (dis < R)
                        color = Color.FromArgb(255, myColor.R, myColor.G, myColor.B); // 白色 完全不透明
                    else if (dis > W / 2)
                        color = Color.FromArgb(0, 0, 0, 0); // 完全透明
                    else
                    {
                        byte f = (byte)(255 * (1f - (dis - R) / (W / 2 - R)));
                        color = Color.FromArgb(f, myColor.R, myColor.G, myColor.B); // 灰色 漸層 不透明 
                    }
                    bitmap.SetPixel(x, y, color);
                }
        }
    }
}
