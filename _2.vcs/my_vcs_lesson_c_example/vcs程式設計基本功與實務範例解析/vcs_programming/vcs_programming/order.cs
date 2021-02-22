using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class order : Form
    {
        public order()
        {
            InitializeComponent();
        }

        private void btnOrder_Click(object sender, EventArgs e)
        {
            int totalAmount = 0;

            if (chkFish.Checked) totalAmount += 59;
            if (chkChicken.Checked) totalAmount += 69;
            if (chkSPizza.Checked) totalAmount += 259;
            if (chkBPizza.Checked) totalAmount += 429;

            if (chkFries.Checked)
            {
                // §j¡¶/§p¡¶
                if (rdbSmall.Checked)
                    totalAmount += 25;
                else
                    totalAmount += 35;
            }

            if (chkDrink.Checked)
            {
                if (rdbCoke.Checked) totalAmount += 25;
                else if(rdbCoffee.Checked) totalAmount += 30;
                else totalAmount += 20;
            }
            
            lblOutput.Text = "NT $ " + totalAmount;
        } 
    }
}