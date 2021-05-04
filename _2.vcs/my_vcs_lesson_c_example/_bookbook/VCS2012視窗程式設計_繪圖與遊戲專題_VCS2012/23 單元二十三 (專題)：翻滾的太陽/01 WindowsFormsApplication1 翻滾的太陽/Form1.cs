using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        // 矩形區塊 動態陣列 用來儲存 sin 軌跡
        List<Rectangle> myRectList = new List<Rectangle>();
        int myRectListIndex = 0; // 目前的 矩形區塊索引值
        int myRectListIndex_D = 1; // 矩形區塊索引值 的遞增值
        int Radius = 200; // sin 軌跡的 高度
        Image myImage; // 2D 圖形
        float Angle = 0; // 2D 圖形的旋轉角度
        float Angle_D = 10; // 2D 圖形旋轉角度的遞增值

        public Form1()
        {
            InitializeComponent();
            UpdateMyRectList();
            myImage = new Bitmap(Properties.Resources.Sun128);
        }

        // 視窗寬高更新事件
        private void Form1_Resize(object sender, EventArgs e)
        {
            UpdateMyRectList();
            this.Invalidate();
        }

        // 更新 sin 軌跡 的 矩形區塊 動態陣列 
        void UpdateMyRectList()
        {
            myRectList.Clear();

            int x, y;
            Rectangle rect = new Rectangle();
            // 設定視窗寬為360度  算出視窗寬的每一個像素代表幾度
            double unit = 360.0 / this.ClientSize.Width;

            for (int i = 0; i <= this.ClientSize.Width; i = i + 10)
            {
                x = i;
                y = this.ClientSize.Height / 2 - (int)(Radius * Math.Sin(i * unit * Math.PI / 180));

                rect.X = x;
                rect.Y = y;
                rect.Width = 2;
                rect.Height = 2;
                myRectList.Add(rect);
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 繪出 sin 軌跡
            for (int i = 0; i < myRectList.Count - 1; i++)
            {
                e.Graphics.DrawEllipse(Pens.Black, myRectList[i]);
            }

            // 繪出翻滾中的圖形
            if (myRectListIndex >= 0 && myRectListIndex <= myRectList.Count - 1)
            {
                // 畫布原點 平移
                e.Graphics.TranslateTransform(myRectList[myRectListIndex].X + 1,
                                              myRectList[myRectListIndex].Y + 1);
                // 畫布座標旋轉
                e.Graphics.RotateTransform(Angle);

                e.Graphics.DrawImage(myImage, -myImage.Width / 2, -myImage.Height / 2);
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            // 更新 sin 軌跡的 高度
            if (e.KeyData == Keys.Up)
            {
                Radius += 2;
                UpdateMyRectList();
            }

            if (e.KeyData == Keys.Down)
            {
                Radius -= 2;
                UpdateMyRectList();
            }

            // 空白鍵 更新矩形區塊索引值的遞增值 => 改變圖形的行進方向
            if (e.KeyData == Keys.Space)
            {
                myRectListIndex_D = -myRectListIndex_D;
            }

            // 更新蜘蛛的翻滾速度
            if (e.KeyData == Keys.Right)
            {
                Angle_D += 2;
            }
            if (e.KeyData == Keys.Left)
            {
                Angle_D -= 2;
            }
        }

        // 計時器 定時更新矩形區塊索引值 呈現來回行進
        // 計時器 定時更新圖形的翻滾旋轉角度
        private void timer1_Tick(object sender, EventArgs e)
        {
            myRectListIndex += myRectListIndex_D;
            if (myRectListIndex == myRectList.Count - 1 || myRectListIndex == 0)
                myRectListIndex_D = -myRectListIndex_D;

            Angle += Angle_D;
            this.Invalidate();
        }
    }
}