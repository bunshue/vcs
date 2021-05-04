using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    static class G2D_PointAndLine  // 點線關係類別
    {
        // 測試 點 是 位於 向量 的 哪一側 
        // 注意：這裡是 使用 Y 軸向下 的座標系統 
        public static short IsPointInVector(PointF p1, PointF p2, PointF q1)
        {
            PointF p1p2 = new PointF(p2.X - p1.X, p2.Y - p1.Y);
            PointF p1q1 = new PointF(q1.X - p1.X, q1.Y - p1.Y);

            double Product = p1p2.X * p1q1.Y - p1q1.X * p1p2.Y;

            if (Product > 0) return 1; // 右側，在正常的 2D 座標系統 是左側 return -1
            else if (Product < 0) return -1; // 左側，在正常的 2D 座標系統 是右側 return 1
            else // Product == 0  在 向量的延伸線 上
            {
                float MaxX = (p1.X > p2.X ? p1.X : p2.X);
                float MinX = (p1.X < p2.X ? p1.X : p2.X);
                float MaxY = (p1.Y > p2.Y ? p1.Y : p2.Y);
                float MinY = (p1.Y < p2.Y ? p1.Y : p2.Y);
                if (q1.X <= MaxX && q1.X >= MinX && 
                    q1.Y <= MaxY && q1.Y >= MinY) // q1 在 向量上
                    return 0; // q1 在 向量上
                else
                    return -101; // q1 在 向量的延伸線 上
            }
        }

        // 測試 點 是否 位於 三角形 內部 
        // 只要 測試 點 是否 位於 三角形 三個邊 的同一側(左邊 或 右邊) 即可
        // 注意：這裡是 使用 Y 軸向下 的座標系統 
        public static bool IsPointInTriangle(PointF p1, PointF p2, PointF p3, PointF q1)
        {
            PointF p1p2 = new PointF(p2.X - p1.X, p2.Y - p1.Y);
            PointF p1q1 = new PointF(q1.X - p1.X, q1.Y - p1.Y);
            double Product_p1p2p1q1 = p1p2.X * p1q1.Y - p1q1.X * p1p2.Y;

            PointF p2p3 = new PointF(p3.X - p2.X, p3.Y - p2.Y);
            PointF p2q1 = new PointF(q1.X - p2.X, q1.Y - p2.Y);
            double Product_p2p3p2q1 = p2p3.X * p2q1.Y - p2q1.X * p2p3.Y;

            PointF p3p1 = new PointF(p1.X - p3.X, p1.Y - p3.Y);
            PointF p3q1 = new PointF(q1.X - p3.X, q1.Y - p3.Y);
            double Product_p3p1p3q1 = p3p1.X * p3q1.Y - p3q1.X * p3p1.Y;

            if (Product_p1p2p1q1 <= 0 && Product_p2p3p2q1 <= 0 && Product_p3p1p3q1 <= 0)
                return true;
            else if (Product_p1p2p1q1 >= 0 && Product_p2p3p2q1 >= 0 && Product_p3p1p3q1 >= 0)
                return true;
            else
                return false;
        }

        // 計算 點 q1 至 直線 p1 p2 的 直線距離D、交叉點H、及對側點 q2的座標
        // 注意：這裡是 使用 Y 軸向下 的座標系統 
        public static void PointToLine(PointF p1, PointF p2, PointF q1, ref double D, ref PointF H, ref PointF q2)
        {
            // 由 p1 和 p2 兩點 找到 直線方程式  Ax + By + C = 0
            float A = p1.Y - p2.Y;
            float B = p2.X - p1.X;
            float C = p2.Y * (p1.X - p2.X) - p2.X * (p1.Y - p2.Y);

            double S = A * A + B * B;
            double L = A * q1.X + B * q1.Y + C;
            D = Math.Abs(L) / Math.Sqrt(S);
            H = new PointF((float)(q1.X - A * L / S), (float)(q1.Y - B * L / S));
            q2 = new PointF((float)(q1.X - 2*A * L / S), (float)(q1.Y - 2*B * L / S));
        }

        // 向量正規化   由一個向量 => 一個長度為 1 的向量
        public static PointF VectorNormalize(PointF v)
        {
            double v_Length = Math.Sqrt(v.X * v.X + v.Y * v.Y);
            return new PointF((float)(v.X / v_Length), (float)(v.Y / v_Length));
        }

        // 向量正規化  由兩個點 => p1 p2 向量 => 一個長度為 1 的向量
        public static PointF VectorNormalize(PointF p1, PointF p2)
        {
            PointF v = new PointF(p2.X - p1.X, p2.Y - p1.Y);
            double v_Length = Math.Sqrt(v.X * v.X + v.Y * v.Y);
            return new PointF((float)(v.X / v_Length), (float)(v.Y / v_Length));
        }
    }
}
