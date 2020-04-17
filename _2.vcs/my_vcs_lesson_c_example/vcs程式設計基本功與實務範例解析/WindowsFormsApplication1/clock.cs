using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class clock : Form
    {

        int h, m, s;  // 方法二

        public clock()
        {
            InitializeComponent();
        }

        private void clock_Load(object sender, EventArgs e)
        {
             // 方法二
             DateTime dt = DateTime.Now;
             h = dt.Hour;
             m = dt.Minute;
             s = dt.Second;

             lblHour.Text = h.ToString();
             lblMin.Text = m.ToString();
             lblSec.Text = s.ToString();
           

            /*
            // 方法一
            DateTime dt = DateTime.Now;
            lblHour.Text = dt.Hour.ToString();
            lblMin.Text = dt.Minute.ToString();
            lblSec.Text = dt.Second.ToString();
            */
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            
            // 方法二
            s = s + 1;
            if (s >= 60)
            {
                m++;
                s = 0;
            }
            if (m >= 60)
            {
                h++;
                m = 0;
            }
            if (h >= 24) h = 0;
            lblHour.Text = h.ToString();
            lblMin.Text = m.ToString();
            lblSec.Text = s.ToString();
            

            /*
            // 方法一
            DateTime dt = DateTime.Now;
            lblHour.Text = dt.Hour.ToString();
            lblMin.Text = dt.Minute.ToString();
            lblSec.Text = dt.Second.ToString();
            */
        }
    }
}
