using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace howto_password_tracker
{
    public partial class frmChangeMaster : Form
    {
        public frmChangeMaster()
        {
            InitializeComponent();
        }

        private void frmChangeMaster_Load(object sender, EventArgs e)
        {
            SettingStuff.RestoreFormPosition(this, "MasterForm");
        }

        private void frmChangeMaster_FormClosing(object sender, FormClosingEventArgs e)
        {
            SettingStuff.SaveFormPosition(this, "MasterForm");
        }
    }
}
