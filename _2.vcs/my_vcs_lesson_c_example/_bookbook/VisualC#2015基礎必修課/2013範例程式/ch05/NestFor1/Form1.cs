using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NestFor1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string show = "";
            for (int y = 1; y <= 3; y++)
            {
                for (int x = 1; x <= 5; x++)
                    show += "*";
                show += '\n';
            }
            MessageBox.Show(show);
            Application.Exit();
        }
    }
}
