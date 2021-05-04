using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Ellipse
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g;               //宣告畫布物件 g
            g = this.CreateGraphics();    //將表單當成畫布
                                          //建立畫筆物件 p, 畫筆顏色綠色, 畫筆寬度2
            Pen p = new Pen(Color.Green, 2);
            //Rectangle rec = new Rectangle(50, 60, 100, 70);
            //g.DrawEllipse(p, rec);
            //上面兩行敘述可合併成下面一行敘述
            g.DrawEllipse(p, 50, 60, 100, 70);

        }
    }
}
