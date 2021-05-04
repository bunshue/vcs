using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MultiForm_2
{
    public partial class frmMenu : Form
    {
        public frmMenu()
        {
            InitializeComponent();
        }

        private void btnBuy_Click(object sender, EventArgs e)
        {
            frmBuy f1;
            f1 = new frmBuy();
            f1.Show();
        }
 
        private void btnSale_Click(object sender, EventArgs e)
        {
            frmSale f2;
            f2 = new frmSale();
            f2.Show();
        }
        
        private void btnEnd_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

      
    }
}
