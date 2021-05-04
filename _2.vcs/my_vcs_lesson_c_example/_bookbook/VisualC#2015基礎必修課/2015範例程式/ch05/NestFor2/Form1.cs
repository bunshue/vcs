using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NestFor2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            for (int y = 1; y <= 3; y++)
            {
                for (int x = 1; x <= 5; x++)
                    label1.Text += "*";
                label1.Text += '\n';
            }
        }
    }
}
