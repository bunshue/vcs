using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace ProjectionCharacter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = panel1.CreateGraphics();//實例化panel1控件的Graphics類
            g.Clear(Color.White);//以白色清空panel1的背景
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.ClearTypeGridFit;//設置文本輸出的質量
            g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;//消除繪製時出現的鋸齒
            Font Var_Font = new Font("細明體", 48);//定義文字的字體
            Matrix Var_Matrix = new Matrix();//實例化Matrix類
            Var_Matrix.Shear(-1.4F, 0.0F);//設置投影
            Var_Matrix.Scale(1, 0.5F);//設置縮放
            Var_Matrix.Translate(168, 118);//設置平移
            g.Transform = Var_Matrix;//設置坐標平面變換
            SolidBrush Var_Brush_1 = new SolidBrush(Color.Gray);//設置文字的畫刷
            SolidBrush Var_Brush_2 = new SolidBrush(Color.SlateBlue);//設置投影的畫刷
            string Var_Str = "投影效果文字";//設置文字
            g.DrawString(Var_Str, Var_Font, Var_Brush_1, new PointF(0, 60));//繪製投影
            g.ResetTransform();//變換矩陣重置為單位矩陣
            g.DrawString(Var_Str, Var_Font, Var_Brush_2, new PointF(0, 60));//繪製文字
        }
    }
}
