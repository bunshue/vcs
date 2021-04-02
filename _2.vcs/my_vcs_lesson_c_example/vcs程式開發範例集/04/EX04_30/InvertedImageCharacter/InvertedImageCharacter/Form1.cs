using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace InvertedImageCharacter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = panel1.CreateGraphics();//建立控制元件的Graphics類別
            g.Clear(Color.White);//以指定的顏色清除控件背景
            Brush Var_Brush_Back = Brushes.Gray;//設置前景色
            Brush Var_Brush_Fore = Brushes.Black;//設置背景色
            Font Var_Font = new Font("細明體", 40);//設置字體樣式
            string Var_Str = "倒影效果的文字";//設置字符串
            SizeF Var_Size = g.MeasureString(Var_Str, Var_Font);//獲取字符串的大小
            g.DrawString(Var_Str, Var_Font, Var_Brush_Fore, 0, 0);//繪製文本
            g.ScaleTransform(1, -1.0F);//縮放變換矩陣
            g.DrawString(Var_Str, Var_Font, Var_Brush_Back, 0, -Var_Size.Height * 1.6F);//繪製倒影文本
        }
    }
}
