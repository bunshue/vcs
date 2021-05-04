/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class BallInNet  // 在多點網格 移動的小球
    {
        PointF position;
        int speed; // 球的速度 (注意：每一次的更新 速度是要加三次)
        public int Ball_Width = 10; // 球的半徑
        SolidBrush myBrush = new SolidBrush(Color.Blue);
        int stepNo = 0;
        List<ClassMovingPoint> mpList = new List<ClassMovingPoint>(); // 可移動點的動態陣列
        List<int> pathList = new List<int>(); // 小球 在 可移動點動態陣列 的路徑
        int nodeNo = 0;

        public BallInNet(List<ClassMovingPoint> mpList,
                         List<int> pathList,
                         int speed,
                         int Ball_Width,
                         Color color)
        {
            this.mpList = mpList;
            this.pathList = pathList;
            this.speed = speed; // 球的速度
            this.Ball_Width = Ball_Width;  // 球的半徑
            myBrush.Color = color;  // 球的顏色
        }

        // 繪出小球
        public void Draw(Graphics G)
        {
            G.FillEllipse(myBrush, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
            G.DrawEllipse(Pens.Black, position.X - Ball_Width, position.Y - Ball_Width, Ball_Width * 2, Ball_Width * 2);
        }

        // 更新小球的座標 
        // 輸入開始 結束點的座標點 N1, N2
        // 到達 N2 就傳回 false
        public void Update()
        {
            PointF N1 = mpList[pathList[nodeNo]].pos;
            PointF N2;
            if (nodeNo < pathList.Count - 1)
                N2 = mpList[pathList[nodeNo + 1]].pos;
            else
                N2 = mpList[pathList[0]].pos;

            stepNo++;
            PointF vector = G2D_PointAndLine.VectorNormalize(N1, N2);
            position.X = N1.X + stepNo * speed * vector.X;
            position.Y = N1.Y + stepNo * speed * vector.Y;

            PointF v = new PointF(N2.X - N1.X, N2.Y - N1.Y);
            double v_Length = Math.Sqrt(v.X * v.X + v.Y * v.Y);

            if (stepNo * speed >= v_Length)
            {
                position = N2;
                nodeNo++;
                if (nodeNo > pathList.Count - 1)
                    nodeNo = 0;
                stepNo = 0;
            }

        }

    }
}
