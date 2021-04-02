using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace Cachet
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Font Var_Font = new Font("Arial", 12, FontStyle.Bold);//定義字符串的字體樣式
        Rectangle rect = new Rectangle(10, 10, 160, 160);//實例化Rectangle類

        private void button1_Click(object sender, EventArgs e)
        {
            int tem_Line = 0;//記錄圓的直徑
            int circularity_W = 4;//設置圓畫筆的粗細
            if (panel1.Width >= panel1.Height)//如果panel1控件的寬度大於等於高度
                tem_Line = panel1.Height;//設置高度為圓的直徑
            else
                tem_Line = panel1.Width;//設置寬度為圓的直徑
            rect = new Rectangle(circularity_W, circularity_W, tem_Line - circularity_W * 2, tem_Line - circularity_W * 2);//設置圓的繪製區域
            Font star_Font = new Font("Arial", 30, FontStyle.Regular);//設置星號的字體樣式
            string star_Str = "★";
            Graphics g = this.panel1.CreateGraphics();//實例化Graphics類
            g.SmoothingMode = SmoothingMode.AntiAlias;//消除繪製圖形的鋸齒
            g.Clear(Color.White);//以白色清空panel1控件的背景
            Pen myPen = new Pen(Color.Red, circularity_W);//設置畫筆的顏色
            g.DrawEllipse(myPen, rect); //繪製圓 
            SizeF Var_Size = new SizeF(rect.Width, rect.Width);//實例化SizeF類
            Var_Size = g.MeasureString(star_Str, star_Font);//對指定字符串進行測量
            //要指定的位置繪製星號
            g.DrawString(star_Str, star_Font, myPen.Brush, new PointF((rect.Width / 2F) + circularity_W - Var_Size.Width / 2F, rect.Height / 2F - Var_Size.Width / 2F));
            Var_Size = g.MeasureString("專用章", Var_Font);//對指定字符串進行測量
            //繪製文字
            g.DrawString("專用章", Var_Font, myPen.Brush, new PointF((rect.Width / 2F) + circularity_W - Var_Size.Width / 2F, rect.Height / 2F + Var_Size.Height * 2));
            string tempStr = "省明日科技有限公司";
            int len = tempStr.Length;//獲取字符串的長度
            float angle = 180 + (180 - len * 20) / 2;//設置文字的旋轉角度
            for (int i = 0; i < len; i++)//將文字以指定的弧度進行繪製
            {
                //將指定的平移添加到g的變換矩陣前         
                g.TranslateTransform((tem_Line + circularity_W / 2) / 2, (tem_Line + circularity_W / 2) / 2);
                g.RotateTransform(angle);//將指定的旋轉用於g的變換矩陣   
                Brush myBrush = Brushes.Red;//定義畫刷
                g.DrawString(tempStr.Substring(i, 1), Var_Font, myBrush, 60, 0);//顯示旋轉文字
                g.ResetTransform();//將g的全局變換矩陣重置為單位矩陣
                angle += 20;//設置下一個文字的角度
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
