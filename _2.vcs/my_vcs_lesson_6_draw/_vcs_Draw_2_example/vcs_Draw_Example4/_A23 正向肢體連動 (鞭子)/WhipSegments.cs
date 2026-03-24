using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsApplication1
{
    class WhipSegments
    {
        public SegmentEnd01 Handler;  // 手把
        public Segment[] Whip ; // 鞭子
        public float cycle = 0;  // 旋轉角度
        public float cycle_Delta = 0.005f;  // 角度遞增值
        public int HandlerRange = 45; // 手把擺動的角度
        public int WhipRange = 5;     // 鞭子擺動的角度

        public int HandlerBaseAngle = 0;  // 手把起始的角度
        public int WhipBaseAngle = 0;     // 鞭子起始的角度

        public double WhipDelayAngle = Math.PI / 4;  // 鞭子遞延的角度 (徑度)

        // new WhipSegments(15, 80, 20, Color.Red, 40, 20, Color.Blue);
        public WhipSegments(int WhipCount,
                            int HandlerWidth, int HandlerHeight, Color HandlerColor,
                            int WhipWidth, int WhipHeight, Color WhipColor)
        {
            Whip = new Segment[WhipCount]; // 鞭子的節數
            // 手把
            Handler = new SegmentEnd01(HandlerWidth, HandlerHeight, HandlerColor);
            // 鞭子的子節
            for (int i = 0; i < Whip.Length; i++)
                Whip[i] = new Segment(WhipWidth, WhipHeight, WhipColor);
        }

        public void Draw(Graphics G)
        {
            // 繪出 手把
            Handler.Draw(G);

            // 繪出 鞭子
            for (int i = 0; i < Whip.Length; i++)
                Whip[i].Draw(G);
        }

        public void Update(PointF HandlerPos)
        {
            cycle += cycle_Delta; // 0.05f;

            // 手把的擺盪角度 是介於 -45度 ~ 45度
            float angle = (float)(Math.Sin(cycle) * HandlerRange + HandlerBaseAngle);
            Handler.Angle = angle;

            float angle2 = (float)(Math.Sin(cycle - WhipDelayAngle) * WhipRange + WhipBaseAngle);
            Whip[0].Angle = Handler.Angle + angle2;

            Handler.SetPos(HandlerPos); // 手把的 位置 
            Whip[0].SetPos(Handler.GetPin2()); // 鞭子 位置 在 手把的下節點

            for (int i = 0; i < Whip.Length - 1; i++)
            {
                angle2 = (float)(Math.Sin(cycle - WhipDelayAngle) * WhipRange + WhipBaseAngle);
                Whip[i + 1].Angle = Whip[i].Angle + angle2;
                Whip[i + 1].SetPos(Whip[i].GetPin2()); // 鞭子 連續的編排
            }
        }
    }
}
