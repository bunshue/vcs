using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
namespace 繪製面形圖
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Graphics g;//建立Graphics對像
        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bt = new Bitmap(panel1.Width, panel1.Height);//實例化一個Bitmap對像
            int flag = (panel1.Width-4 )/ 6;//X軸的增值
            g = Graphics.FromImage(bt);//實例化Graphics對像
            Pen p = new Pen(Color.Black, 1);//設定Pen對像
            g.DrawLine(p, new Point(0, 0), new Point(0, panel1.Height-20));//繪製Y軸
            g.DrawLine(p, new Point(0, panel1.Height - 20), new Point(panel1.Width - 4, panel1.Height - 20));//繪製X軸
            //宣告一個用於繪製顏色的數組
            Color[] cl = new Color[] { Color.Red, Color.Blue, Color.YellowGreen, Color.Yellow, Color.RoyalBlue, Color.Violet, Color .Tomato};
            int[] points = { 20,70,80,60,40,100,10};//宣告一個計算走勢峰值的數組
            Point pt1 = new Point(0, panel1.Height - 20 - points[0]);//記錄繪製四邊形的第一個點
            Point pt2 = new Point(0, panel1.Height - 20);//記錄繪製四邊形的第二個點
            for (int i = 0; i <= 6; i++)//透過for循環繪製月份和面形圖
            {
                PointF p1 = new PointF(flag * i, panel1.Height - 20);//計算每個月份數字的座標
                //繪製顯示月份的數字
                g.DrawString(i.ToString(), new Font("細明體", 9), new SolidBrush(Color.Black), new PointF(p1.X - 2, p1.Y));
                //記錄繪製四邊形的第三個點
                Point pt3 = new Point(flag * i, panel1.Height - 20);
                //記錄繪製四邊形的第四個點
                Point pt4 = new Point(flag * i, panel1.Height - 20 - points[i]);
                Point[] pt={pt1,pt2,pt3,pt4};//宣告一個Point數組
                g.FillPolygon(new SolidBrush(cl[i]), pt);//填充四邊形的顏色
                //當繼續繪製下一個四邊形時，前一個四邊形的最後兩個點作為下一個四邊形的起始點
                pt1 = pt4;
                pt2 = pt3;
            }
            panel1.BackgroundImage = bt;//顯示繪製的面形圖
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
