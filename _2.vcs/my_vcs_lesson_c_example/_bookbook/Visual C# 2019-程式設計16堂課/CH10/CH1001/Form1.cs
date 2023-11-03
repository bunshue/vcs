using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1001
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void btnOK_Click(object sender, EventArgs e)
        {
            if (txtName.Text != "")
            {
                string name = $"Hi! {txtName.Text}";
                MessageBox.Show(name);
            }
        }
    }
}
