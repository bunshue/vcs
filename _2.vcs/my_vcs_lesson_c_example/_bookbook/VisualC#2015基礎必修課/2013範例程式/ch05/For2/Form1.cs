using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace For2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int sum1 = 0, sum2 = 0;
            for (int i = 1, k = 10; i <= 5 && k >= 2; i++, k -= 2)
            {
                sum1 += i;
                sum2 += k;
            }
            //for (int i = 1, k = 10; i <= 5 && k >= 2; i++, k -= 2)
            //{
            //    sum1 += i;
            //    sum2 += k;
            //}
            MessageBox.Show(sum1.ToString() + "," + sum2.ToString());
            Application.Exit();
        }
    }
}
