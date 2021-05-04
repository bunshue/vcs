/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassBomb
    {
        int W, H; // 視窗的寬高
        int BX, EX; // 開始的 X 軸 座標、結束的X軸 座標
        double Distance; // 起點 和 終點 的距離
        double step = 1; // 炸彈每次前進的距離

        public bool Falling = true; // 是否下降中
        int FallingCount = 0; // 下降次數的計數

        int DX; // 起點座標 和 終點座標 之間在X軸的距離
        int DY; // 起點座標 和 終點座標 之間在Y軸的距離

        public int X, Y; // 目前的 位置 
        public static int ToButtomCount = 0; // 成功抵達視窗下緣的次數

        Pen[] myPen = new Pen[] // 定義六枝筆的顏色 與 寬度
			{
				new Pen(Color.Red, 3),
				new Pen(Color.Lime, 3),
				new Pen(Color.Blue, 3),
				new Pen(Color.Fuchsia, 3),
				new Pen(Color.Yellow, 3),
				new Pen(Color.Aqua, 3)
			};
        int myPen_Index; // 筆陣列 的索引
        Random rd = new Random();

        public ClassBomb(int W, int H, int BX, int EX)
        {
            this.W = W; // 視窗的寬
            this.H = H; // 視窗的高

            this.BX = BX; // 開始的 X軸 座標
            this.EX = EX; // 結束的 X軸 座標

            // 起點座標 和 終點座標 之間的距離
            Distance = Math.Sqrt((BX - EX) * (BX - EX) + H * H);
            DX = EX - BX;  // 起點座標 和 終點座標 之間在X軸的距離
            DY = H; // 起點座標 和 終點座標 之間在Y軸的距離

            myPen_Index = rd.Next(6);  // 隨機取得一枝筆
            foreach (Pen p in myPen) // 六枝筆的樣式都為 點線
                p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
        }

        public void Draw(Graphics G)
        {
            if (!Falling) return; // 如果已經不繼續下降 就不畫了

            FallingCount++; //下降次數的計數 加一
            // 直線的終點 (X, Y),  起點是 (BX, 0)
            X = BX + (int)(FallingCount * (step / Distance) * DX);
            Y = (int)(FallingCount * (step / Distance) * DY);
            G.DrawLine(myPen[myPen_Index], BX, 0, X, Y);
            // 在直線的終點 畫一個 圓點
            G.FillEllipse(Brushes.White, X - 5, Y - 5, 10, 10);
            // 如果已經畫到 視窗的下緣 就 不需要再畫了
            if (FallingCount * step >= Distance)
            {
                Falling = false;
                ToButtomCount++;
            }
        }
    }
}
