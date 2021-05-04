// 透明度漸變的影像類別   -- 鄞永傳老師 2012-08
// 用來繪出兩張透明度漸變的影像 (一張淡出、一張淡入)
// 主程式要這樣使用
/*
G2D_ImageFadeinFadeout2 imageObject;
imageObject = new G2D_ImageFadeinFadeout2(bitmap1, bitmap2);  // 產生淡入淡出物件
imageObject.Init(new Point(100, 100), 5000); //從 完全透明-> 完全不透明->完全透明  用了5秒

private void timer1_Tick(object sender, EventArgs e)
 {
   this.Invalidate();
   if (imageObject.isTimeUp())
      {
        timer1.Enabled = false;
      }
 }
 
imageObject.Draw(e.Graphics); // 畫出
 * */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Drawing.Imaging;

namespace WindowsFormsApplication1
{
    class G2D_ImageFadeinFadeout2
    {
        Point m_pos = new Point();
        Bitmap m_bitmap1 = null; // 淡出的圖片
        Bitmap m_bitmap2 = null; // 淡入的圖片
        G2D_Anim ani;
        float[][] m_cmArray = // 色彩調整矩陣
               {
                  new float[] {1, 0, 0, 0,    0},
                  new float[] {0, 1, 0, 0,    0},
                  new float[] {0, 0, 1, 0,    0},
                  new float[] {0, 0, 0, 0.5f, 0},
                  new float[] {0, 0, 0, 0,    1}
               };

        public G2D_ImageFadeinFadeout2(Bitmap m_bitmap1, Bitmap m_bitmap2)  // 建構元
        {
            this.m_bitmap1 = m_bitmap1;  // 第一張淡出
            this.m_bitmap2 = m_bitmap2;  // 第二張淡入
        }

        public void Init(Point m_pos, int time)
        {
            this.m_pos = m_pos;
            ani = new G2D_Anim(3, time, false, AnimType.AT_Linear);
            ani.SetKeyValue(0, 0.0f, 1); //第 0 個關鍵值  在 0.0f 比例時間的位置 值是 1
            ani.SetKeyValue(1, 0.5f, 0); //第 1 個關鍵值  在 0.5f 比例時間的位置 值是 0
            ani.SetKeyValue(2, 1.0f, 0); //第 1 個關鍵值  在 1.0f 比例時間的位置 值是 0

            ani.BeginAnimation();
        }

        public bool isTimeUp()
        {
            if (ani.isTimeup())
                return true;
            else
                return false;
        }

        public void Draw(Graphics G)  // 畫出
        {
            m_cmArray[3][3] = ani.GetValue();

            ColorMatrix cm = new ColorMatrix(m_cmArray);
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm,
                ColorMatrixFlag.Default,
                ColorAdjustType.Bitmap);

            // 淡出的圖片
            if (m_bitmap1 != null)
            {
                Rectangle rect = new Rectangle(m_pos.X - m_bitmap1.Width / 2, m_pos.Y - m_bitmap1.Height / 2, m_bitmap1.Width, m_bitmap1.Height);
                G.DrawImage(m_bitmap1,
                    rect,
                    0, 0, m_bitmap1.Width, m_bitmap1.Height,
                    GraphicsUnit.Pixel, ia);
            }

            m_cmArray[3][3] = 1 - m_cmArray[3][3];
            cm = new ColorMatrix(m_cmArray);
            ia = new ImageAttributes();
            ia.SetColorMatrix(cm,
                ColorMatrixFlag.Default,
                ColorAdjustType.Bitmap);

            // 淡入的圖片
            if (m_bitmap2 != null)
            {
                Rectangle rect = new Rectangle(m_pos.X - m_bitmap2.Width / 2, m_pos.Y - m_bitmap2.Height / 2, m_bitmap2.Width, m_bitmap2.Height);
                G.DrawImage(m_bitmap2,
                    rect,
                    0, 0, m_bitmap2.Width, m_bitmap2.Height,
                    GraphicsUnit.Pixel, ia);
            }
        }
    }
}
