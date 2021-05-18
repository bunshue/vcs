using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

// http://zh.wikipedia.org/zh-tw/%E6%A9%A2%E5%9C%93
namespace vcs_Draw3C
{
    class G2D_EllipsePath
    {
        PointF center;
        float a, b;

        public G2D_EllipsePath(PointF center, float a, float b) // 中心點 加上 兩個半徑
        {
            this.center = center;
            this.a = a;
            this.b = b;
        }

        public G2D_EllipsePath(PointF LeftUp, PointF RightDown) // 左上  右下
        {
            this.center.X = (RightDown.X + LeftUp.X) / 2;
            this.center.Y = (RightDown.Y + LeftUp.Y) / 2;

            this.a = (RightDown.X - LeftUp.X) / 2;
            this.b = (RightDown.Y - LeftUp.Y) / 2;
        }

        public PointF GetPath(float theta)
        {
            PointF ret = new PointF();
            ret.X = (float)(center.X + a * Math.Cos(theta));
            ret.Y = (float)(center.Y + b * Math.Sin(theta));
            return ret;
        }

        public void Draw(Graphics G)
        {
            PointF p;
            for (int i = 0; i < 360; i++)
            {
                p = GetPath((float)(i * Math.PI / 180));
                G.DrawEllipse(Pens.Silver, p.X , p.Y, 1, 1);
            }
        }

    }
}
