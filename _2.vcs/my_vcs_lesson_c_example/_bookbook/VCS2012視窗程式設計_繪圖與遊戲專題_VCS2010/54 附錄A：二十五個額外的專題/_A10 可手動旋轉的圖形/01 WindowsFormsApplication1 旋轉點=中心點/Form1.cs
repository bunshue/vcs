using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bitmap = Properties.Resources.p120;  // 貼圖
        float theta = 0; // 貼圖的旋轉角度
        bool actionTurning = false; // 是否 進入 旋轉模式
        Point pos; // 圖形中心點 = 旋轉中心點
        int mx, my; // 滑鼠游標位置
        double disInBitmap;  // 滑鼠游標能夠選到 圖形 的最大距離
        double disInPos = 10; // 滑鼠游標能夠選到 圖形中心點 的最大距離
        int dx, dy;  // 滑鼠游標和 圖形中心點 的偏移值
        bool actionMoving = false;  // 是否 進入 移動模式
        float Inertia; // 旋轉角度 慣性
        SolidBrush myBrush = new SolidBrush(Color.FromArgb(128, 255, 0, 0));  // 標示 圖形中心點

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(600, 600);
            pos = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            disInBitmap = (bitmap.Width / 2.0) * 1.4142; // 根號 2 
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias; // 消除鋸齒狀

            Matrix A = new Matrix();
            A.Translate(-bitmap.Width / 2, -bitmap.Height / 2, MatrixOrder.Append); // 將 圖形中心點 當作原點
            A.Rotate(theta, MatrixOrder.Append); // 旋轉 theta 角度
            A.Translate(pos.X, pos.Y, MatrixOrder.Append); // 擺到 (pos.X, pos.Y) (圖形中心點 = 旋轉中心點)
            e.Graphics.Transform = A;
            e.Graphics.DrawImage(bitmap, 0, 0, bitmap.Width, bitmap.Height);

            A = new Matrix();
            A.Translate(pos.X, pos.Y, MatrixOrder.Append);
            e.Graphics.Transform = A;
            e.Graphics.FillEllipse(myBrush, - 10, - 10, 20, 20);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            // 滑鼠游標位置 和 圖形中心點 的距離
            double dis = Math.Sqrt((e.X - pos.X) * (e.X - pos.X) +
                                   (e.Y - pos.Y) * (e.Y - pos.Y));

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
                my = e.Y ;
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (actionMoving) // 在移動模式
            {
                pos.X = e.X - dx; // 圖形中心點 新的位置
                pos.Y = e.Y - dy;
                this.Invalidate();
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
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
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

        private void timer1_Tick(object sender, EventArgs e)
        {
            theta += Inertia;
            this.Invalidate();

            Inertia = 0.99f * Inertia; // 旋轉慣性 愈來愈小
            if (Inertia < 0.01f && Inertia > -0.01f) timer1.Enabled = false;
        }
    }
}
