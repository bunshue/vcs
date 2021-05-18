using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;  // for SolidBrush, Pen
using System.Windows.Forms; // for Control

namespace vcs_GameControl1
{
    class G2D_Image_Plane
    {
        //double interval = 10;       // 更新變數值的間隔時間 
        //double cumulatedTime = 0;   // 計算一次間隔累計的時間

        //SolidBrush myBrush = new SolidBrush(Color.FromArgb(192, 192, 0)); // 亮黃色
        //Pen myPen = new Pen(Color.FromArgb(0, 0, 0), 3);  // 黑色
        Form1 form1;

        Bitmap m_bitmap;  // 圖片
        Point m_pos;      // 圖片位置

        public G2D_Image_Plane(Form1 form1, Bitmap m_bitmap, Point m_pos)
        {
            this.form1 = form1;  // 可以用來適時的取得 Form1 的寬高
            this.m_bitmap = m_bitmap;
            this.m_pos = m_pos;
        }

        public void Update(double elapsedTime)
        {
            //cumulatedTime += elapsedTime;   // 時間累計
            //if (cumulatedTime >= interval)  // 累計的時間 超過了 一個更新畫面的時間
            //{
            //    cumulatedTime = 0;  // 重新累計
            //}

            int speed = Convert.ToInt32(elapsedTime * 0.5);
            // 鍵盤控制
            if (G2D_KeyListener.IsKeyPushedDown(Keys.Right))
                this.m_pos.X += speed; // 更新位置
            if (G2D_KeyListener.IsKeyPushedDown(Keys.Left))
                this.m_pos.X -= speed; // 更新位置

            if (G2D_KeyListener.IsKeyPushedDown(Keys.Up))
                this.m_pos.Y -= speed; // 更新位置
            if (G2D_KeyListener.IsKeyPushedDown(Keys.Down))
                this.m_pos.Y += speed; // 更新位置
        }

        public void Draw(Graphics G)
        {
            // 繪出
            G.DrawImage(m_bitmap, m_pos.X - m_bitmap.Width / 2, m_pos.Y - m_bitmap.Height / 2, m_bitmap.Width, m_bitmap.Height);
        }
    }
}