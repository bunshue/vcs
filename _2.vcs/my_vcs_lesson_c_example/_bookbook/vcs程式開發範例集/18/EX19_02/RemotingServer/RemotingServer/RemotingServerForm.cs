using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.Remoting;
using RemotingClass;
namespace RemotingServer
{
    public partial class RemotingServerForm : Form
    {
        public RemotingServerForm()
        {
            InitializeComponent();
        }

        private void RemotingServerForm_Load(object sender, EventArgs e)
        {
            RemotingConfiguration.Configure("RemotingServer.exe.Config",false);
            label1.Text = "伺服器端已啟動";
        }
    }
}