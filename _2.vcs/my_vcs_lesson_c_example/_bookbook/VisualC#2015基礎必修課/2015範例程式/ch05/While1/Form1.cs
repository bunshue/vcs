using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace While1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int i = 0, sum = 0;
            string str1;
            while (i < 10)
            {
                i++;
                sum += i;
            }
            str1 = Convert.ToString(sum);
            MessageBox.Show(str1);
            Application.Exit();
        }
    }
}
