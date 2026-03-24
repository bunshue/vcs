using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class G2D_Line
    {
        Point Center;  // 中心圓的位置
        float Angle;   // 旋轉角度
        double w1, w2; // 兩邊端點離中心圓的距離
        public Point p1 = new Point(); // 兩邊端點的位置
        public Point p2 = new Point();

        bool CenterMoving = false; // 是否正在移動 中心圓
        int CenterD = 5; // 中心圓的半徑
        Point CenterOffset; // 中心圓 和 滑鼠游標 的 偏移值

        bool p1Moving = false; // 是否正在移動 p1 端點
        int p1D = 5; // p1 端點的半徑
        Point p1Offset;// p1 端點 和 滑鼠游標 的 偏移值

        bool p2Moving = false;
        int p2D = 5;
        Point p2Offset;

        public G2D_Line(Point Center, float Angle, double w1, double w2)
        {
            this.Center = Center; // new Point(200, 200);  // 中心圓的位置
            this.Angle = Angle; // 0;
            this.w1 = w1; // 100;  // p1 端點 離中心圓的距離
            this.w2 = w2; // 100;

            p1.X = (int)(Center.X + w1 * Math.Cos(Angle)); // p1 端點的位置
            p1.Y = (int)(Center.Y + w1 * Math.Sin(Angle));

            p2.X = (int)(Center.X + w2 * Math.Cos(Angle + Math.PI));
            p2.Y = (int)(Center.Y + w2 * Math.Sin(Angle + Math.PI));
        }

        public void Draw(Graphics G)
        {
            G.DrawRectangle(Pens.Red, p1.X - p1D, p1.Y - p1D, 10, 10); // 繪出 p1 端點
            G.DrawRectangle(Pens.Green, p2.X - p2D, p2.Y - p2D, 10, 10);

            G.DrawLine(Pens.Black, p1, p2); // 繪出直線
            // 繪出 中心圓
            G.FillEllipse(Brushes.Blue, Center.X - CenterD, Center.Y - CenterD, 2 * CenterD, 2 * CenterD);
        }

        public void MouseDown(Point e)
        {
            double dis = Math.Sqrt((e.X - Center.X) * (e.X - Center.X) + (e.Y - Center.Y) * (e.Y - Center.Y));
            if (dis <= CenterD) // 點選到 中心圓
            {
                CenterMoving = true;
                CenterOffset.X = e.X - Center.X;
                CenterOffset.Y = e.Y - Center.Y;
                return;
            }

            dis = Math.Sqrt((e.X - p1.X) * (e.X - p1.X) + (e.Y - p1.Y) * (e.Y - p1.Y));
            if (dis <= p1D) // 點選到 p1 端點
            {
                p1Moving = true;
                p1Offset.X = e.X - p1.X;
                p1Offset.Y = e.Y - p1.Y;
                return;
            }

            dis = Math.Sqrt((e.X - p2.X) * (e.X - p2.X) + (e.Y - p2.Y) * (e.Y - p2.Y));
            if (dis <= p2D) // 點選到 p2 端點
            {
                p2Moving = true;
                p2Offset.X = e.X - p2.X;
                p2Offset.Y = e.Y - p2.Y;
                return;
            }
        }

        public void MouseUp(Point e)
        {
            CenterMoving = false;
            p1Moving = false;
            p2Moving = false;
        }

        public bool MouseMove(Point e)
        {
            if (CenterMoving == true)
            {
                Center.X = e.X - CenterOffset.X; // 中心圓 移動
                Center.Y = e.Y - CenterOffset.Y;

                p1.X = (int)(Center.X + w1 * Math.Cos(Angle)); // p1 端點 跟著移動
                p1.Y = (int)(Center.Y + w1 * Math.Sin(Angle));

                p2.X = (int)(Center.X + w2 * Math.Cos(Angle + Math.PI)); // p2 端點 跟著移動
                p2.Y = (int)(Center.Y + w2 * Math.Sin(Angle + Math.PI));

                //this.Invalidate();
                return true;
            }
            else if (p1Moving == true) 
            {
                p1.X = e.X - p1Offset.X; // p1 端點 移動
                p1.Y = e.Y - p1Offset.Y;
                // 重新計算 離中心圓的距離 以便 p2 端點 移動時 p1 可以重新定位
                w1 = Math.Sqrt((Center.X - p1.X) * (Center.X - p1.X) + (Center.Y - p1.Y) * (Center.Y - p1.Y));

                Angle = (float)Math.Atan2(p1.Y - Center.Y, p1.X - Center.X); // 重新計算 角度
                p2.X = (int)(Center.X + w2 * Math.Cos(Angle + Math.PI)); // p2 端點 要跟著 旋轉
                p2.Y = (int)(Center.Y + w2 * Math.Sin(Angle + Math.PI));

                //this.Invalidate();
                return true;
            }
            else if (p2Moving == true)
            {
                p2.X = e.X - p2Offset.X;
                p2.Y = e.Y - p2Offset.Y;
                w2 = Math.Sqrt((Center.X - p2.X) * (Center.X - p2.X) + (Center.Y - p2.Y) * (Center.Y - p2.Y));

                Angle = (float)(Math.Atan2(p2.Y - Center.Y, p2.X - Center.X) - Math.PI);
                p1.X = (int)(Center.X + w1 * Math.Cos(Angle ));
                p1.Y = (int)(Center.Y + w1 * Math.Sin(Angle ));

                //this.Invalidate();
                return true;
            }

            return false;
        }

        public void UpdateP1(Point p)
        {
            p1 = p;

            w1 = Math.Sqrt((Center.X - p1.X) * (Center.X - p1.X) + (Center.Y - p1.Y) * (Center.Y - p1.Y));

            Angle = (float)Math.Atan2(p1.Y - Center.Y, p1.X - Center.X); // 重新計算 角度
            p2.X = (int)(Center.X + w2 * Math.Cos(Angle + Math.PI)); // p2 端點 要跟著 旋轉
            p2.Y = (int)(Center.Y + w2 * Math.Sin(Angle + Math.PI));
        }

        public void UpdateP2(Point p)
        {
            p2 = p;

            w2 = Math.Sqrt((Center.X - p2.X) * (Center.X - p2.X) + (Center.Y - p2.Y) * (Center.Y - p2.Y));

            Angle = (float)(Math.Atan2(p2.Y - Center.Y, p2.X - Center.X) - Math.PI);
            p1.X = (int)(Center.X + w1 * Math.Cos(Angle));
            p1.Y = (int)(Center.Y + w1 * Math.Sin(Angle));
        }
    }
}
