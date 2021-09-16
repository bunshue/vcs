using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinApCallWs
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                ServiceReference1.WebService1SoapClient ws =
                    new ServiceReference1.WebService1SoapClient();
                double d1, d2;
                d1 = double.Parse(textBox1.Text);
                d2 = double.Parse(textBox2.Text);
                MessageBox.Show("兩數相加為 " + ws.Add(d1, d2).ToString());
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }
    }
}
