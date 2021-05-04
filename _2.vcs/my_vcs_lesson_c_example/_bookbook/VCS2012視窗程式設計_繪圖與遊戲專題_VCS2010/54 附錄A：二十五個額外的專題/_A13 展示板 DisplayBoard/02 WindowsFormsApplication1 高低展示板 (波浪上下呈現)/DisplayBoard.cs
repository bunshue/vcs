// 高低訊號展示板類別
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class DisplayBoard
    {
        PointF pt = new PointF(); // 展示板 左上角的座標
        PointF[,] pts; // 展示板 內 每個小方塊 左上角的座標
        int[] values;  // 展示板 內 每行小方塊的高度
        float W, H;    // 展示板 的 寬高
        int col, row;  // 展示板 內 小方塊 的行列數目
        float sW, sH;  // 展示板 內 每個小方塊 的寬高
        float gapW, gapH; // 展示板 內 每個小方塊 間隔的寬高

        // gapWs 小格間隔的寬 / 小格的寬 
        public DisplayBoard(PointF pt, float W, float H, int col, int row, float gapWs, float gapHs)
        {
            // gapWs 是 小方塊間隔的寬 / 小方塊的寬 
            // gapHs 是 小方塊間隔的高 / 小方塊的高
            pts = new PointF[col, row]; // 總共有這麼多的  小方塊
            values = new int[col];  // 展示板 內 每行的高度

            this.pt = pt;
            this.W = W;
            this.H = H;
            this.col = col;
            this.row = row;
            sW = W / (col + (col + 1) * gapWs);  // 展示板 內 每個小方塊 的寬
            sH = H / (row + (row + 1) * gapHs);  // 展示板 內 每個小方塊 的高

            gapW = sW * gapWs;  // 展示板 內 每個小方塊間隔 的寬
            gapH = sH * gapHs;  // 展示板 內 每個小方塊間隔 的高

            // 展示板 內 每個小方塊 左上角的座標
            for (int i = 0; i < col; i++)
                for (int j = 0; j < row; j++)
                {
                    pts[i, j].X = pt.X + gapW + i * (sW + gapW);
                    pts[i, j].Y = pt.Y + gapH + j * (sH + gapH);
                }
        }

        // 更新 每行的高度
        public void Update(int[] values)
        {
            this.values = values;
        }

        // 繪出
        public void Draw(Graphics G)
        {
            // 繪出 外框
            G.DrawRectangle(Pens.Black, pt.X, pt.Y, W, H);

            // 依據 每行的高度 填滿必要的小方塊
            for (int i = 0; i < col; i++)
                for (int j = 0; j < row; j++)
                {
                    if (j >= (row - values[i]))  // 
                        G.FillRectangle(Brushes.Red, pts[i, j].X, pts[i, j].Y, sW, sH);
                }

            // 繪出 每個小方塊 的 外框
            for (int i = 0; i < col; i++)
                for (int j = 0; j < row; j++)
                {
                    G.DrawRectangle(Pens.Black, pts[i, j].X, pts[i, j].Y, sW, sH);
                }
        }
    }
}
