using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace ShadeCharacter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = panel1.CreateGraphics();//建立控制元件的Graphics類
            g.Clear(Color.White);//以指定的顏色清除控制元件背景
            Color Var_Color_Up = Color.Red;//設定前景色
            Color Var_Color_Down = Color.Yellow;//設定背景色
            Font Var_Font = new Font("細明體", 40);//設定字體樣式
            string Var_Str = "漸變效果的文字";//設定字串
            SizeF Var_Size = g.MeasureString(Var_Str, Var_Font);//取得字串的大小
            PointF Var_Point = new PointF(5, 5);
            RectangleF Var_Rect = new RectangleF(Var_Point, Var_Size);
            LinearGradientBrush Var_LinearBrush = new LinearGradientBrush(Var_Rect, Var_Color_Up, Var_Color_Down, LinearGradientMode.Horizontal);
            g.DrawString(Var_Str, Var_Font, Var_LinearBrush, Var_Point);
        }
    }
}
