using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace StartupInterface
{
    public partial class StartupInterface : Form
    {
        public StartupInterface()
        {
            InitializeComponent();
        }

        private void StartupInterface_FormClosing(object sender,FormClosingEventArgs e)
        {
            Application.Exit();  //退出应用程序
        }
    }
}
