using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1ball
{
    public partial class Form1 : Form
    {
        Graphics g;                 // 繪圖區
        Pen pen;                    // 畫筆
        public Form1()
        {
            InitializeComponent();
            this.FormBorderStyle = FormBorderStyle.None;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            g = this.CreateGraphics();

            //g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(0, 0, 100, 100));

            
        }

        private void button1_Click(object sender, EventArgs e)
        {

            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(0, 0, 100, 100));

            this.Size = new Size(265, 602);
        }

        int x_st = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //if (x_st < 600)
            {
                x_st += 50;
                g.Clear(System.Drawing.SystemColors.ControlLight);
                g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(x_st, 0, 50, 50));
                if (x_st == 600)
                    x_st = 0;
            }
        }
    }
}
