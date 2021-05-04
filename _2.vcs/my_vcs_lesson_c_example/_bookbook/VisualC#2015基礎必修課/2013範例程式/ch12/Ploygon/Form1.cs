using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ploygon
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g;                  //宣告畫布物件g
            g = this.CreateGraphics();   //將表單當成畫布

            //建立畫筆物件p, 畫筆顏色綠色, 畫筆寬度2
            Pen p = new Pen(Color.Green, 2);

            //建立多邊形物件pts端點
            Point[] pts = new Point[] {new Point(100, 50), new Point(70, 75), 
                          new Point(80, 100), new Point(120, 100), new Point(130, 75)};
            //繪製五邊形，pts為頂點的集合，其中有五個點座標
            g.DrawPolygon(p, pts); 
        }
    }
}
