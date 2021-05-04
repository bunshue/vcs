using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Line
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g;               //宣告畫布物件g
            g = this.CreateGraphics();   // 將表單當成畫布
            //建立畫筆物件p, 畫筆顏色綠色, 畫筆寬度5
            // Pen p = new Pen(Color.Green, 5);
            // p.Color = Color.Green;   // 畫筆顏色設為綠色
            //g.DrawLine(p, 50, 50, 200, 150); // 在畫布上繪製線條
            //上面三行可合併成下面一行
            g.DrawLine(new Pen(Color.Green, 5), 50, 50, 200, 150);
        }
    }
}
