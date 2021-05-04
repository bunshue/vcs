using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class GC_2D_Wander
    {
        Bitmap myBitmap; // 圖形

        public PointF pos = new Point(300, 200);  // 座標
        public double Angle_Offset = 90; //-Math.PI / 2;  // 開始的旋轉矯正徑度
        public PointF Wander_Center = new Point(400, 400); // 漫遊的中心點
        public double Wander_Radius = 200; // 漫遊的半徑距離
        public int Speed = 5; // 漫遊的速度

        double Angle = 0; // 目前的旋轉角度
        Random rd = new Random(); // 亂數

        public GC_2D_Wander(Bitmap myBitmap)
        {
            this.myBitmap = myBitmap;
        }

        public void Update()
        {
            // NPC 和 漫遊中心點 的 夾角向量
            PointF vectorToCenter = new PointF(Wander_Center.X - pos.X, Wander_Center.Y - pos.Y);
            // NPC 和 漫遊中心點 的距離
            double len = Math.Sqrt((Wander_Center.X - pos.X) * (Wander_Center.X - pos.X) +
                                   (Wander_Center.Y - pos.Y) * (Wander_Center.Y - pos.Y));

            if (len > 5 * Wander_Radius) // 在 5 倍 的漫遊半徑距離 外
            {
                // NPC 和 漫遊中心點 的角度
                double Yaw2 = Math.Atan2(vectorToCenter.Y, vectorToCenter.X);

                // Yaw2 和 NPC 角度 的 角度差
                double diff = Yaw2 - Angle;

                Angle = Angle + diff; // 一次就 矯正 回來
            }
            else if (len > Wander_Radius) // 在 漫遊的半徑距離 外
            {
                // NPC 和 漫遊中心點 的角度
                double Yaw2 = Math.Atan2(vectorToCenter.Y, vectorToCenter.X);

                // Yaw2 和 NPC 角度 的 角度差
                double diff = Yaw2 - Angle;

                // 欲矯正的角度
                double r;
                r = 0.01 * Math.PI * len / Wander_Radius; // NPC 和 漫遊中心點 距離愈遠 矯正的角度愈大

                if (diff < -r) diff = -r; // 慢慢把 角度差 矯正回來
                else if (diff > r) diff = r;

                Angle = Angle + (diff + (rd.NextDouble() * 0.001)); // 再加一點點 亂數
            }
            else // 在 漫遊的半徑距離 內
            {
                double rate = rd.NextDouble() * 0.06 - 0.03; // 一些 亂數 改變 角度
                Angle += rate;
            }

            while (Angle < -Math.PI) Angle += Math.PI * 2; // 確定  Angle 是在 -Math.PI ~ Math.PI 之間
            while (Angle > Math.PI) Angle -= Math.PI * 2;

            pos.X += (float)(Speed * Math.Cos(Angle)); // NPC 新的座標
            pos.Y += (float)(Speed * Math.Sin(Angle));
        }

        public void Draw(Graphics G)
        {
            G.ResetTransform();  // 重設 畫布的轉換矩陣
            G.TranslateTransform(pos.X, pos.Y); // 平移 畫布 的中心點
            G.RotateTransform((float)(Angle_Offset + (Angle * 180.0 / Math.PI))); // 旋轉 畫布 
            G.DrawImage(myBitmap, 0 - myBitmap.Width / 2, 0 - myBitmap.Height / 2, myBitmap.Width, myBitmap.Height); //繪出 圖形
            G.ResetTransform(); // 重設 畫布的轉換矩陣
        }
    }
}
