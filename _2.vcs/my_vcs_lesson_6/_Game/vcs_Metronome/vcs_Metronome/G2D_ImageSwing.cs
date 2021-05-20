using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing; //  for Bitmap
using System.Drawing.Drawing2D; // for Matrix
using System.Windows.Forms;

namespace vcs_Metronome
{
    class G2D_ImageSwing
    {
        Bitmap bitmap ;  // 貼圖
        public float theta = 0; // 貼圖的旋轉角度
        public Point pos; // 圖形中心點

        SolidBrush myBrush = new SolidBrush(Color.FromArgb(128, 255, 0, 0));  // 標示 圖形中心點
        SolidBrush myBrush2 = new SolidBrush(Color.FromArgb(128, 255, 255, 0));  // 標示 圖形中心點

        public Point pivot; // 旋轉中心點
        Matrix aMatrix;

        public G2D_ImageSwing(Bitmap bitmap, Point pos, Point pivot)
        {
            this.bitmap = bitmap;
            this.pos = pos;
            //pivot = new Point(bitmap.Width / 2, bitmap.Height / 2);
            this.pivot = pivot;
        }

        public void Draw(Graphics G)
        {
            G.SmoothingMode = SmoothingMode.AntiAlias; // 消除鋸齒狀

            G.ResetTransform();
            aMatrix = new Matrix();
            aMatrix.Translate(-pivot.X, -pivot.Y, MatrixOrder.Append); // 將 圖形中心點 (旋轉中心點) 當作原點
            aMatrix.Rotate(theta, MatrixOrder.Append); // 旋轉 theta 角度
            aMatrix.Translate(pos.X, pos.Y, MatrixOrder.Append); // 擺到 (pos.X, pos.Y) (圖形中心點 = 旋轉中心點)
            G.Transform = aMatrix;
            G.DrawImage(bitmap, 0, 0, bitmap.Width, bitmap.Height);

            Matrix A = new Matrix();  
            A.Translate(pos.X, pos.Y, MatrixOrder.Append);
            G.Transform = A;
            G.FillEllipse(myBrush, -10, -10, 20, 20); // 中心點
        }
    }
}
