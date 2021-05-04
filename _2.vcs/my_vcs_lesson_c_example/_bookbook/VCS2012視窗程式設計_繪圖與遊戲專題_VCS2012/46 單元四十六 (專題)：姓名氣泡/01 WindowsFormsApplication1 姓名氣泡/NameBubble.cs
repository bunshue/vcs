using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;

namespace WindowsFormsApplication1
{
    class NameBubble
    {
        public Point pos; // 氣泡 中心點座標
        public Point vec; // 氣泡速度
        string str;  // 氣泡的字串
        public SizeF strSize; // 氣泡字串的寬高
        SolidBrush myBrush1, myBrush2; // 氣泡的塗刷和字串的塗刷
        Font myFont = new Font("標楷體", 18);

        public NameBubble(Point pos, Point vec, string str, Color color)
        {
            this.pos = pos;
            this.vec = vec;
            this.str = str;
            myBrush1 = new SolidBrush(color); // myBrush2 是 myBrush1 的互補色
            myBrush2 = new SolidBrush(Color.FromArgb(255 - color.R, 255 - color.G,255 - color.B));
        }

        public void Update(int w, int h)
        {
            pos.X += vec.X;
            pos.Y += vec.Y;

            if (pos.X < strSize.Width / 2) // 左側碰撞
            {
                pos.X = (int)(strSize.Width/2);
                vec.X = -vec.X;
            }
            else if (pos.X > w - strSize.Width / 2) // 右側碰撞
            {
                pos.X = (int)(w - strSize.Width / 2);
                vec.X = -vec.X;
            }

            /* 上下緣的 碰撞不需要
            if (pos.Y < strSize.Width / 2)
            {
                pos.Y = (int)(strSize.Width / 2);
                vec.Y = -vec.Y;
            }
            else if (pos.Y > h - strSize.Width / 2)
            {
                pos.Y = (int)(h - strSize.Width / 2);
                vec.Y = -vec.Y;
            } 
             * */
        }

        public void Draw(Graphics G)
        {
            // 計算氣泡字串的寬高
            strSize = G.MeasureString(str, myFont);

            // 氣泡內部 填色
            G.FillEllipse(myBrush1,
                pos.X - strSize.Width / 2, pos.Y - strSize.Width / 2,
                strSize.Width, strSize.Width);
            // 氣泡外緣繪出
            G.DrawEllipse(Pens.Black,
                pos.X - strSize.Width / 2, pos.Y - strSize.Width / 2,
                strSize.Width, strSize.Width);
            // 氣泡字串繪出
            G.DrawString(str, myFont, myBrush2,
                pos.X - strSize.Width / 2, pos.Y - strSize.Height / 2);
        }
    }
}
