using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Tictactoe6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Pen black_pen, red_pen, blue_pen;
        private bool[] isCircle, isCross;
        private int step;

        private void Form1_Load(object sender, EventArgs e)
        {
            this.black_pen = new Pen(Color.Black);
            this.red_pen = new Pen(Color.Red);
            this.blue_pen = new Pen(Color.Blue);
            this.isCircle = new bool[9];
            this.isCross = new bool[9];
            reset();
        }

        private void reset() {
            this.step = 0;
            for (int i=0; i<9; ++i) {
                this.isCircle[i] = false;
                this.isCross[i] = false;
            }
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            if(e.Button == MouseButtons.Right || step == 9)
                reset();
            else if(e.Button == MouseButtons.Left){
                int num = e.X/100 + 3*(e.Y/100);
                if(!this.isCircle[num] && !this.isCross[num]){
                    if(this.step % 2 == 0)
                        this.isCircle[num] = true;
                    else
                        this.isCross[num] = true;
                    ++step;
                }
            }
            this.Refresh();
        }

        protected override void OnPaint(PaintEventArgs e) {
            Graphics g = e.Graphics;
            g.DrawLine(this.black_pen, 0, 100, 300, 100);
            g.DrawLine(this.black_pen, 0, 200, 300, 200);
            g.DrawLine(this.black_pen, 100, 0, 100, 300);
            g.DrawLine(this.black_pen, 200, 0, 200, 300);
            
            for(int i=0; i<9; ++i){
                int x = i%3;
                int y = i/3;
                if (this.isCircle[i])
                    g.DrawEllipse(this.red_pen, x*100+5, y*100+5, 90, 90);
                else if (this.isCross[i]) {
                    g.DrawLine(this.blue_pen, x*100+5, y*100+5, (x+1)*100-5, (y+1)*100-5);
                    g.DrawLine(this.blue_pen, (x+1)*100-5, y*100+5, x*100+5, (y+1)*100-5);
                }
            }
            g.Dispose();
            base.OnPaint(e);
        }

    }
}
