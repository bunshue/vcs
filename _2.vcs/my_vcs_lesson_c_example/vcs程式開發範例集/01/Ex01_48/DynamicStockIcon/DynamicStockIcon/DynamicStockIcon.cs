using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DynamicStockIcon
{
    public partial class DynamicStockIcon : Form
    {
        public DynamicStockIcon()
        {
            InitializeComponent();
        }

        #region 本程序声明的变量
        public static bool flag=false ;
        #endregion

        private void flicker_Click(object sender,EventArgs e)
        {
            stocktimer.Enabled = true;
        }

        private void cease_Click(object sender,EventArgs e)
        {
            stocktimer.Enabled = false;
            stockIcon.Icon = Properties.Resources._1;
        }

        private void stocktimer_Tick(object sender,EventArgs e)
        {
            if(flag == false)
            {
                stockIcon.Icon = Properties.Resources._1;
                flag = true;
            }
            else
            {
                stockIcon.Icon = Properties.Resources._2;
                flag = false;
            }
        }
    }
}
