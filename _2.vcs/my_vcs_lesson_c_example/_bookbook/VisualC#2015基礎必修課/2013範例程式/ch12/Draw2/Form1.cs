using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Draw2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = this.CreateGraphics();  //建立畫布物件g
            //藍色外框，內部無色
            g.DrawEllipse(new Pen(Color.Blue, 4), 20, 20, 50, 70);
            //內部填肉色，外框無色
            g.FillEllipse(Brushes.Pink, 120, 20, 50, 70);     //先繪藍色外框     
            g.DrawEllipse(new Pen(Color.Blue, 4), 220, 20, 50, 70);
            g.FillEllipse(Brushes.Pink, 220, 20, 50, 70);     //再填內部肉色
            g.FillEllipse(Brushes.Pink, 320, 20, 50, 70);     //先填滿內部，再畫外框
            g.DrawEllipse(new Pen(Color.Blue, 4), 320, 20, 50, 70);
            //以拋物線的曲線來安排放置Visual C# 文字列的x與y座標
            int i, s, x, y;
            for (i = 1; i <= 5; i++)
            {
                s = 6 + i * 3;
                x = i * 30;
                y = i * (6 + i * 2) + 130;
                //建立Font字型物件f，字體為新細明體, 大小s，樣式為加底線
                Font f = new Font("新細明體", s, FontStyle.Underline);
                //在畫布上繪製文字Visual C#
                g.DrawString("Visual C#", f, Brushes.Blue, x, y);
            }
        }
    }
}
