using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        int k = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (k == 0)
            {
                label1.Text = "春有百花秋有月";
                k++;
            }
            else if (k == 1)
            {
                label1.Text = "夏有涼風冬有雪";
                k++;
            }
            else if (k == 2)
            {
                label1.Text = "若無閒事掛心頭";
                k++;
            }
            else if (k == 3)
            {
                label1.Text = "便是人間好時節";
                k=0;
            }

        }
    }
}
