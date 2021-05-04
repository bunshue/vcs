using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing; //  for Bitmap
using System.Drawing.Drawing2D; // for Matrix
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    class G2D_ImageRotate
    {
        Bitmap bitmap ;  // 貼圖
        float theta = 0; // 貼圖的旋轉角度
        bool actionTurning = false; // 是否 進入 旋轉模式
        public Point pos; // 圖形中心點 = 旋轉中心點
        int mx, my; // 滑鼠游標位置
        double disInBitmap;  // 滑鼠游標能夠選到 圖形 的最大距離
        double disInPos = 10; // 滑鼠游標能夠選到 圖形中心點 的最大距離
        int dx, dy;  // 滑鼠游標和 圖形中心點 的偏移值
        bool actionMoving = false;  // 是否 進入 移動模式
        float Inertia; // 旋轉角度 慣性
        SolidBrush myBrush = new SolidBrush(Color.FromArgb(128, 255, 0, 0));  // 標示 圖形中心點

        Timer timer1 = new Timer();

        public G2D_ImageRotate(Bitmap bitmap, Point pos)
        {
            this.bitmap = bitmap;
            this.pos = pos;

            disInBitmap = (bitmap.Width / 2.0) * 1.4142;
            timer1.Enabled = false;
            timer1.Interval = 10;
            timer1.Tick += new System.EventHandler(timer1_Tick);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta += Inertia;
            //this.Invalidate();  // ..............

            Inertia = 0.99f * Inertia; // 旋轉慣性 愈來愈小
            if (Inertia < 0.01f && Inertia > -0.01f) timer1.Enabled = false;
        }

        public void Draw(Graphics G)
        {
            G.SmoothingMode = SmoothingMode.AntiAlias; // 消除鋸齒狀

            Matrix A = new Matrix();
            A.Translate(-bitmap.Width / 2, -bitmap.Height / 2, MatrixOrder.Append); // 將 圖形中心點 當作原點
            A.Rotate(theta, MatrixOrder.Append); // 旋轉 theta 角度
            A.Translate(pos.X, pos.Y, MatrixOrder.Append); // 擺到 (pos.X, pos.Y) (圖形中心點 = 旋轉中心點)
            G.Transform = A;
            G.DrawImage(bitmap, 0, 0, bitmap.Width, bitmap.Height);

            A = new Matrix();
            A.Translate(pos.X, pos.Y, MatrixOrder.Append);
            G.Transform = A;
            G.FillEllipse(myBrush, -10, -10, 20, 20);
        }

        public void MouseDown(Point e)
        {
            // 滑鼠游標位置 和 圖形中心點 的距離
            double dis = Math.Sqrt((e.X - pos.X) * (e.X - pos.X) +
                                   (e.Y - pos.Y) * (e.Y - pos.Y));
            // bool MouseInBitmap = e.X < <== 因為有旋轉 所以矩形區域不管用

            if (dis < disInPos) // 滑鼠游標在 圖形中心點 => 要移動圖形
            {
                actionMoving = true; // 進入移動模式
                dx = e.X - pos.X;
                dy = e.Y - pos.Y;
            }
            else if (dis < disInBitmap) // 滑鼠游標在 圖形上 => 要旋轉圖形
            {
                Inertia = 0;  // 取消 旋轉慣性 
                timer1.Enabled = false;
                actionTurning = true; // 進入旋轉模式
                mx = e.X;  // 記錄 滑鼠游標 位置
                my = e.Y;
            }
        }

        public void MouseUp()
        {
            if (actionMoving)
            {
                actionMoving = false;
            }
            else if (actionTurning) // 在旋轉模式 要有 慣性 的效果
            {
                actionTurning = false;
                Inertia = 1 * Inertia;  // 1 是持續旋轉係數
                timer1.Enabled = true; // 以計時器 呈現 慣性 的效果
            }
        }

        public void MouseMove(Point e)
        {
            if (actionMoving) // 在移動模式
            {
                pos.X = e.X - dx; // 圖形中心點 新的位置
                pos.Y = e.Y - dy;
                //this.Invalidate();   // ..............
            }
            else if (actionTurning) // 在旋轉模式
            {
                // 算出兩個座標的夾角徑度
                double A = Math.Atan2((e.Y - pos.Y), (e.X - pos.X));
                double B = Math.Atan2((my - pos.Y), (mx - pos.X));
                Inertia = (float)((A - B) * 180.0 / Math.PI); // 夾角徑度 轉為 角度
                theta += Inertia; // 更新 旋轉 角度

                mx = e.X; // 記錄新的 滑鼠游標 位置
                my = e.Y;
                //this.Invalidate();   // ..............
            }
        }


        public void StopRotate()
        {
            timer1.Enabled = false;
            theta = 0; // 貼圖的旋轉角度
        }
    }
}
