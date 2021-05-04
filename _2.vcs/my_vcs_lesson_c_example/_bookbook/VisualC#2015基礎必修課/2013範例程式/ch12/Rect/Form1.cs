using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Rect
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g;                   //宣告畫布物件 g
            g = this.CreateGraphics();    //將表單當成畫布
            Pen p = new Pen(Color.Green, 2);
            //Rectangle rec = new Rectangle(30, 40, 100, 70);
            //g.DrawRectangle(p, rec);
            g.DrawRectangle(p, 30, 40, 100, 70);
        }
    }
}
