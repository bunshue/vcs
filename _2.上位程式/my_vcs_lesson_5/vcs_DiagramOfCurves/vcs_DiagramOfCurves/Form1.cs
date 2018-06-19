using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DiagramOfCurves
{
    public partial class Form1 : Form
    {
        Graphics g;    //設定一個畫布g
        public Form1()
        {
            InitializeComponent();
            g = this.CreateGraphics();	//這個視窗，就是畫布
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Pen pen = new Pen(Color.Black, 8);
            pen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;  //EndCap設定 這支筆的結尾會是個箭頭

            g.DrawLine(pen, 50, 400, 50, 100);  //畫出X軸及y軸
            g.DrawLine(pen, 50, 400, 350, 400);

            pen = new Pen(Color.Blue, 6);   //重新設定pp的線條樣式
            //pp.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot; //DashStyle設定線條 點
            //pp.StartCap = System.Drawing.Drawing2D.LineCap.RoundAnchor; //設定為圓頭

            pen.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;

            //gg.DrawLine(pp, 50, 50, 250, 250);//只畫一條
            g.DrawLines(pen, new Point[] {//一次畫好多條
            new Point(70,350),
            new Point(100,280),
            new Point(120,300),
            new Point(200,220),
            new Point(250,260),
            new Point(340,150)});


        }
    }
}
