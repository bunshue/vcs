using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;


        public Form1()
        {
            InitializeComponent();
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;

            if ((cnt % 4) == 0)
            {
                p0.BackColor = Color.Blue;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 1)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Blue;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 2)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Blue;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 3)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Blue;
            }



        
        
        
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = panel1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g.Clear(Color.Red);             //useless??
            panel1.BackColor = Color.Pink;

        }

    }
}
