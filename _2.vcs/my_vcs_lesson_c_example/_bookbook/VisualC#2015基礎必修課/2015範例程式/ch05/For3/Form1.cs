using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace For3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            double sum = 0.0;
            for (double k = 0.5; k <= 5; k += 0.5)
                sum += k;
            MessageBox.Show(Convert.ToString(sum));
            Application.Exit();
        }
    }
}
