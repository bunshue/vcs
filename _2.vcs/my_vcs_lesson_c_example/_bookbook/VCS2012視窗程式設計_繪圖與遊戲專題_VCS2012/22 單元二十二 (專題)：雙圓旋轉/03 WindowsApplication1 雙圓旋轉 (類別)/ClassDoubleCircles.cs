using System;
using System.Collections.Generic;
//using System.Linq;
using System.Text;
using System.Drawing;
using System.Windows.Forms;

namespace WindowsApplication1
{
    class ClassDoubleCircles
    {
        Pen pen01 = new Pen(Color.Red, 4); // 內圓 的筆刷
        Pen pen02 = new Pen(Color.Blue, 4);// 外圓 的筆刷

        double angle = 0;            // 內圓 的角度
        double angle2 = Math.PI;     // 外圓 的角度
        double angleDelta = 0.1;     // 旋轉的角度遞增值

        int inner = 100; // 內圓 的半徑
        int outer = 200; // 外圓 的半徑
        int innerNo = 1; // 內圓 的小圓球數目
        int outerNo = 1; // 外圓 的小圓球數目

        int x0=0, y0=0;

        public ClassDoubleCircles(int x0, int y0, int inner, int outer)
        {
            this.x0 = x0;
            this.y0 = y0;

            this.inner = inner;
            this.outer = outer;
            // 內外圓 的筆刷樣式設定
            pen01.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            pen02.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
        }

        public void Draw(Graphics G)
        {
            // 視窗客戶區 中心點
            //int x0 = this.ClientSize.Width / 2;
            //int y0 = this.ClientSize.Height / 2;

            G.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出內外圓 的大圓
            G.DrawEllipse(pen01, x0 - inner, y0 - inner, inner * 2, inner * 2);
            G.DrawEllipse(pen02, x0 - outer, y0 - outer, outer * 2, outer * 2);

            int x, y;
            // 繪出內圓 的旋轉小圓球
            for (int i = 0; i < innerNo; i++)
            {
                // 依旋轉角度angle算出 座標
                x = x0 + (int)((inner - 10) * Math.Cos(angle + i * (Math.PI * 2 / innerNo)));
                y = y0 + (int)((inner - 10) * Math.Sin(angle + i * (Math.PI * 2 / innerNo)));
                G.FillEllipse(Brushes.Red, x - 10, y - 10, 20, 20);
            }

            // 繪出外圓 的旋轉小圓球
            for (int i = 0; i < outerNo; i++)
            {
                // 依旋轉角度angle2算出 座標
                x = x0 + (int)((outer - 10) * Math.Cos(angle2 + i * (Math.PI * 2 / outerNo)));
                y = y0 + (int)((outer - 10) * Math.Sin(angle2 + i * (Math.PI * 2 / outerNo)));
                G.FillEllipse(Brushes.Blue, x - 10, y - 10, 20, 20);
            }
        }

        public void UpdateNumber(MouseButtons button, int mouseX, int mouseY)
        {
            //int x0 = this.ClientSize.Width / 2;
            //int y0 = this.ClientSize.Height / 2;
            double dist = Math.Sqrt((mouseX - x0) * (mouseX - x0) + (mouseY - y0) * (mouseY - y0));

            if (dist < inner) // 滑鼠在內圓按下
            {
                if (button == MouseButtons.Left)  // 滑鼠左鍵 增加小圓球
                    innerNo++;
                else if (button == MouseButtons.Right) // 滑鼠右鍵 減少小圓球
                {
                    if (innerNo > 0)
                        innerNo--;
                }
            }
            else if (dist < outer) // 滑鼠在外圓按下
            {
                if (button == MouseButtons.Left)
                    outerNo++;
                else if (button == MouseButtons.Right)
                {
                    if (outerNo > 0)
                        outerNo--;
                }
            }
        }

        public void Update()
        {
            angle = angle + angleDelta;
            angle2 = angle2 - angleDelta;
        }

    }
}
