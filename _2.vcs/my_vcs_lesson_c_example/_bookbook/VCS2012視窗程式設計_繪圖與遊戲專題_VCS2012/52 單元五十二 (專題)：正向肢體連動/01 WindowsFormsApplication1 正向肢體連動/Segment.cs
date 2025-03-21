﻿using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class Segment  // 肢節 的 類別
    {
        PointF pin1 = new PointF(); // 上節點的座標
        Size size = new Size(200, 40); // 肢節 的 寬高
        public float Angle = 30; // 角度
        Color color; // 肢節 的 顏色

        public Segment(int Width, int Height, Color color)
        {
            size.Width = Width; // 上節點 到 下節點 的 距離
            size.Height = Height; // 肢節 的 高
            this.color = color;
        }

        // 設定 上節點 的座標
        public void SetPos(PointF p)
        {
            pin1.X = p.X;
            pin1.Y = p.Y;
        }

        // 繪出 肢節
        public void Draw(Graphics G)
        {
            // 矩形區域 往上下節點 兩側延伸
            Rectangle rect = new Rectangle();
            rect.X = -size.Height / 2;
            rect.Y = -size.Height / 2;
            rect.Width = size.Width + size.Height;
            rect.Height = size.Height;

            int D = 10;  // 上下節點 圓孔 的直徑

            G.ResetTransform();
            G.TranslateTransform(pin1.X, pin1.Y); // 畫布原點移到上節點
            G.RotateTransform(Angle);  // 畫布旋轉，以度為單位

            // 繪出肢節 和 圓孔
            SolidBrush brush = new SolidBrush(color);
            G.FillRectangle(brush, rect);
            G.FillEllipse(Brushes.White, -D / 2, -D / 2, D, D);
            G.FillEllipse(Brushes.White, size.Width - D / 2, -D / 2, D, D);

            // 繪出邊框
            Pen pen = new Pen(Color.Black);
            G.DrawRectangle(pen, rect);
            G.DrawEllipse(pen, -D / 2, -D / 2, D, D);
            G.DrawEllipse(pen, size.Width - D / 2, -D / 2, D, D);
        }

        // 計算出第二個節點
        public PointF GetPin2()
        {
            PointF P = new PointF();
            P.X = pin1.X + (float)(size.Width * Math.Cos(Angle * Math.PI / 180));
            P.Y = pin1.Y + (float)(size.Width * Math.Sin(Angle * Math.PI / 180));

            return P;
        }
    }
}
