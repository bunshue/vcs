using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic.PowerPacks;//匯入VB向量繪圖功能     需要加入參考dll與using此行

namespace vcs_Chess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        byte[,] S;        //對應棋盤狀態的陣列：0為空格，1為黑子，2為白子
        //Bitmap bmp;
        //Graphics g;
        ShapeContainer CVS; //畫布物件(棋盤)

        //繪製棋盤與加入畫布
        private void Form1_Load(object sender, EventArgs e)
        {
            Bitmap bmp = new Bitmap(570, 570);          //棋盤影像物件
            Graphics g = Graphics.FromImage(bmp);       //棋盤影像繪圖物件
            g.Clear(Color.White);                       //設白色為背景色
            int i;
            int j;
            for (i = 15; i <= 555; i += 30)             //畫19條垂直線
            {
                g.DrawLine(Pens.Black, i, 15, i, 555);
            }
            for (j = 15; j <= 555; j += 30)             //畫19條水平線
            {
                g.DrawLine(Pens.Black, 15, j, 555, j);
            }
            panel1.BackgroundImage = bmp;               //貼上棋盤影像為panel1的背景
            CVS = new ShapeContainer();                //宣告畫布物件
            panel1.Controls.Add(CVS);                  //畫布物件加入panel1
            S = new byte[19, 19];                      //宣告棋盤資訊陣列 
        }

        //畫棋子的副程序
        void Chess(int i, int j, Color BW)
        {
            int w = 26;
            int h = 26;
            int x_st = i * 30 + 2;
            int y_st = j * 30 + 2;

            OvalShape C = new OvalShape();  //建立一個圓形的Shape物件
            C.Width = w;                    //寬度(略小於棋格)
            C.Height = h;                   //高度
            C.Left = x_st;                  //左邊座標
            C.Top = y_st;                   //頂部座標
            C.FillStyle = FillStyle.Solid;  //實心填滿
            C.FillColor = BW;               //填黑或白色
            C.Parent = CVS;                 //將圓形Shape加入畫布(棋盤)
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            int i = e.X / 30;   //算出是第幾個水平向的棋格
            int j = e.Y / 30;   //算出是第幾個垂直向的棋格
            if (S[i, j] == 0)
            {
                Chess(i, j, Color.Black);   //畫黑子
                S[i, j] = 1;                //記為黑子
            }
        }

        //清除
        private void button1_Click(object sender, EventArgs e)
        {
            CVS.Shapes.Clear();             //清除棋子
            S = new byte[19, 19];           //清除棋盤資訊
        }
    }
}
