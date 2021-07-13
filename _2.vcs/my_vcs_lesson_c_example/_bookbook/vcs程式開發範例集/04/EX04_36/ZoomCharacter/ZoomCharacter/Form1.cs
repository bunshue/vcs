using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace ZoomCharacter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //button1_Click(sender, e);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = panel1.CreateGraphics();//建立控制元件的Graphics類
            g.Clear(Color.White);//以指定的顏色清除控制元件背景
            Brush Var_Back = Brushes.Black;//設定畫刷
            FontFamily Var_FontFamily = new FontFamily("細明體");//設定字體樣式
            string Var_Str = "縮放文字";//設定字串

            //SizeF Var_Size = g.MeasureString(Var_Str, Var_Font);//取得字串的大小
            //int Var_X = (panel1.Width - Convert.ToInt32(Var_Size.Width)) / 2;//設定平移的X座標
            //int Var_Y = (panel1.Height - Convert.ToInt32(Var_Size.Height)) / 2;////設定平移的Y座標

            GraphicsPath Var_Path = new GraphicsPath();//實例化GraphicsPath對像
            Var_Path.AddString(Var_Str, Var_FontFamily, (int)FontStyle.Regular, 50, new Point(0, 0), new StringFormat());//在路徑中新增文字
            PointF[] Var_PointS = Var_Path.PathPoints;//取得路徑中的點
            Byte[] Car_Types = Var_Path.PathTypes;//取得對應點的類型

            //Matrix Var_Matrix = new Matrix(Convert.ToSingle(textBox1.Text), 0.0F, 0.0F, Convert.ToSingle(textBox1.Text), 0.0F, 0.0F);//設定仿射矩陣
            Matrix Var_Matrix = new Matrix((float)numericUpDown1.Value, 0.0F, 0.0F, (float)numericUpDown1.Value, 0.0F, 0.0F);//設定仿射矩陣
            Var_Matrix.TransformPoints(Var_PointS);
            GraphicsPath Var_New_Path = new GraphicsPath(Var_PointS, Car_Types);
            g.FillPath(Var_Back, Var_New_Path);
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            button1_Click(sender, e);
        }
    }
}
