using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Drawing.Drawing2D;

namespace vcs_Draw3C
{
    class G2D_Butterfly
    {
        PointF pos = new PointF(400, 400);  // 蝴蝶線的中心點座標
        float theta = 0; // 旋轉角度
        float theta_D = 0; // 旋轉角度 差異值

        int d;  // 蝴蝶線的半徑
        int n = 1; // 畫幾圈

        GraphicsPath gp; // 圖形軌跡物件
        int speed = 10; // 速度

        public G2D_Butterfly(int n, int d)
        {
            this.n = n;
            this.d = d;
            setVertex();
        }

        // 計算出 360 * n 個蝴蝶線的座標點
        public void setVertex()
        {
            double t;  // 極座標的θ
            double r;  // 極座標的 r
            PointF[] pt = new PointF[360 * n];

            // 計算出 360 * n 個座標點
            for (int k = 0; k < 360 * n; k++)
            {
                t = k * Math.PI / 180;
                r = d * (Math.Pow(Math.E, Math.Cos(t)) - 2 * Math.Cos(4 * t) - Math.Pow(Math.Sin(t / 12), 5));

                pt[k].X = (float)(r * Math.Sin(t));
                pt[k].Y = (float)(r * Math.Cos(t));
            }

            gp = new GraphicsPath();
            gp.AddLines(pt);
            gp.CloseFigure();
        }

        // 蝴蝶 往 座標點 (eX, eY) 走
        public void Update(int eX, int eY)
        {
            theta_D = (float)(Math.Atan2(eY - pos.Y, eX - pos.X) * 180 / Math.PI) - theta;
            
            if (theta_D > 180)   // 避免走遠路
                theta_D = -(360 - theta_D);
            else if (theta_D < -180)
                theta_D = 360 + theta_D;
        }

        // 繪出 蝴蝶圖案
        public void Draw(Graphics G)
        {
            theta = theta + theta_D * 0.1f;
            theta = theta % 360; // 保持在 360 度內

            pos.X = (float)(pos.X + speed * Math.Cos(theta * Math.PI / 180));
            pos.Y = (float)(pos.Y + speed * Math.Sin(theta * Math.PI / 180));
            
            G.ResetTransform();
            G.RotateTransform(theta - 90); // 先旋轉
            G.TranslateTransform(pos.X, pos.Y, MatrixOrder.Append); // 再平移
            G.DrawPath(Pens.Black, gp);
        }
    }
}
