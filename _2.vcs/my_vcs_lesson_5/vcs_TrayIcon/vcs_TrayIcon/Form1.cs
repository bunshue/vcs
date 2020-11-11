using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TrayIcon
{
    public partial class Form1 : Form
    {
        private Icon mNetTrayIcon = new Icon(@"C:\_git\vcs\_2.vcs\______test_files\_material\ims.ico");
        private Bitmap MyImage = null;
        private NotifyIcon TrayIcon;
        private ContextMenu notifyiconMnu;

        public Form1()
        {
            InitializeComponent();

            TrayIcon = new NotifyIcon();
            TrayIcon.Icon = mNetTrayIcon;
            TrayIcon.Text = "製作TrayIcon";
            TrayIcon.Visible = true;

        }
    }
}
