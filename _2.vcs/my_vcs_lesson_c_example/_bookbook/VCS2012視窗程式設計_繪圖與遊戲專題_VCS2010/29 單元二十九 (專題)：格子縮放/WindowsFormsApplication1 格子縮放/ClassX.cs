/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class ClassX // 圖形定位與繪出類別
    {
        Image image;     // 圖形影像
        PointF pos = new PointF();  // 和 格子中心點的 相對位置
        float scale = 1; // 縮放比例

        public ClassX(Image image) // 建構元
        {
            this.image = image; // 得到圖形影像
        }

        //  設定位置
        public void SetPos(float X, float Y)
        {
            pos.X = X;
            pos.Y = Y;
        }

        //  設定圖形的縮放比例
        public void SetScale(float scale)
        {
            this.scale = scale;
        }

        //  繪出
        public void Draw(Graphics G, int D, Point Center)
        {
            //  圖形當時的寬高 (和 D 有關) 除以 20 是刻意要縮小
            int imageWidth = (int)(image.Width * scale * D / 20);
            int imageHeight = (int)(image.Height * scale * D / 20);

            Rectangle rect = new Rectangle(
                              (int)((Center.X + pos.X * D) - imageWidth / 2),
                              (int)((Center.Y + pos.Y * D) - imageHeight / 2),
                              imageWidth,
                              imageHeight);

            G.DrawImage(image, rect);
        }
    }
}
