using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime;
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Services;
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
            //TcpChannel chan = new TcpChannel(9999);
            //ChannelServices.RegisterChannel(chan);
            //FarClass fc = new FarClass();
            //ObjRef obj = RemotingServices.Marshal(fc, "Tcpservice");
            //RemotingServices.Unmarshal(obj);
            //FarClass fc = new FarClass();
            //MessageBox.Show("遠程類對像被第" + fc.GetTime().ToString() + "次呼叫");
            RemotingConfiguration.Configure("RemotingServer.exe.Config", false);
            this.label1.Text = "服務端已啟動";
        }
    }
}