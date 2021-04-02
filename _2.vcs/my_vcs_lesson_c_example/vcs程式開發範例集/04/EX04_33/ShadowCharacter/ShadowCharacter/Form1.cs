using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ShadowCharacter
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
            Brush Var_Brush_Back = Brushes.Gray;//設定前景色
            Brush Var_Brush_Fore = Brushes.Black;//設定背景色
            Font Var_Font = new Font("黑體", 40,FontStyle.Bold);//設定字體樣式
            string Var_Str = "陰影效果的文字";//設定字串
            SizeF Var_Size = g.MeasureString(Var_Str, Var_Font);//取得字串的大小
            int Var_X = (panel1.Width - Convert.ToInt32(Var_Size.Width)) / 2;//設定平移的X座標
            int Var_Y = (panel1.Height - Convert.ToInt32(Var_Size.Height)) / 2;////設定平移的Y座標
            g.DrawString(Var_Str, Var_Font, Var_Brush_Back, Var_X + 3, Var_Y + 2);
            g.DrawString(Var_Str, Var_Font, Var_Brush_Fore, Var_X, Var_Y);
        }
    }
}
