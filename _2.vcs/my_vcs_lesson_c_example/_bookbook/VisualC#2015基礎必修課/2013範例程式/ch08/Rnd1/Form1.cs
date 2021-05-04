using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Rnd1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Random rnd = new Random();
            label1.Text = "";
            for (int i = 1; i <= 5; i++)
            {
                label1.Text += "第" + i.ToString() + "個亂數: "
                  + rnd.Next(3, 15).ToString() + "\n";
            }
        }
    }
}
