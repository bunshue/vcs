using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // for GraphicsPath

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath gp = new GraphicsPath();
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區的中心點
            int Cy = this.ClientSize.Height / 2;

            int D = 20;    // 每格 寬
            int x = Cx;    // 心臟的起始點
            int y = Cy - 2 * D;

            //心臟右邊的曲線 由上往下
            PointF[] pt = new PointF[]{
                          new PointF(x, y),
                          new PointF(x+3*D, y - 1.5f*D),
                          new PointF(x+5*D, y),
                          new PointF(x+4*D, y+3*D),
                          new PointF(x, y+ 7 *D),
                          };
            gp.AddCurve(pt, 0.6f);

            //心臟左邊的曲線 順時間方向 由下往上 定義點的座標
            PointF[] pt2 = new PointF[]{
                          new PointF(x, y+ 7 *D),
                          new PointF(x-4*D, y+3*D),
                          new PointF(x-5*D, y),
                          new PointF(x-3*D, y - 1.5f*D),
                          new PointF(x, y),
                          };
            gp.AddCurve(pt2, 0.6f);

            if (comboBox1.SelectedIndex == 0)  // 單色塗刷
                e.Graphics.FillPath(Brushes.Red, gp); // 填滿形狀區域
            else if (comboBox1.SelectedIndex == 1) // 樣式塗刷一
            {
                HatchBrush myBrush1 = new HatchBrush(HatchStyle.DiagonalCross, Color.Yellow, Color.Blue);
                e.Graphics.FillPath(myBrush1, gp); //填滿形狀區域
            }
            else if (comboBox1.SelectedIndex == 2) // 樣式塗刷二
            {
                HatchBrush myBrush2 = new HatchBrush(HatchStyle.SolidDiamond, Color.Yellow, Color.Blue);
                e.Graphics.FillPath(myBrush2, gp); //填滿形狀區域
            }
            else if (comboBox1.SelectedIndex == 3) // 使用圖形塗刷
            {
                Bitmap bm = new Bitmap(Properties.Resources.Butterfly);
                TextureBrush myBrush3 = new TextureBrush(bm);  // 圖形塗刷
                e.Graphics.FillPath(myBrush3, gp); //填滿形狀區域
            }
            e.Graphics.DrawPath(Pens.Black, gp); //繪出圖形軌跡

        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        // ComboBox元件 更新選項事件
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }
}