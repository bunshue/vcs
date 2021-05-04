using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for Matrix, MatrixOrder

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        float shearX = 0; // X 軸水平分歧因數
        float shearY = 0; // Y 軸垂直分歧因數
        Point MP; // 滑鼠游標座標

        public Form1()
        {
            InitializeComponent();
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區正中心點
            int Cy = this.ClientSize.Height / 2;//
            int D = 100; // 球本身的半徑

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣
            e.Graphics.DrawEllipse(Pens.Silver, Cx - D, Cy - D, 2 * D, 2 * D); //畫出開始的圓

            shearX = (MP.X - Cx) / (float)D; // X 軸水平分歧因數
            shearY = (MP.Y - Cy) / (float)D; // Y 軸水平分歧因數

            this.Text = "切變矩陣 (" + shearX.ToString() + ", " + shearY.ToString() + ")";

            Matrix A = new Matrix(); // 轉換矩陣
            A.Shear(shearX, shearY, MatrixOrder.Append);// shearX, shearY, MatrixOrder.Append);  // 乘上 切變矩陣
            A.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = A;  // 畫布的矩陣 = 矩陣 A
            e.Graphics.DrawEllipse(Pens.Red, 0 - D, 0 - D, 2 * D, 2 * D); //畫出縮放後的圓 
        }


        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            MP = e.Location; // 紀錄滑鼠游標座標
            this.Invalidate();// 要求表單重畫
        }
    }
}
