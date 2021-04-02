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
using System.Reflection;
using System.Diagnostics;
using System.Linq;
using RemotingClass;
using System.IO;

namespace RemotingClient
{
    public partial class RemotingClientForm : Form
    {
        FarClass fc;
        DataTable table;
        public RemotingClientForm()
        {
            InitializeComponent();
        }

        private void RemotingClientForm_Load(object sender, EventArgs e)
        {
            //ChannelServices.RegisterChannel(new TcpChannel());
            //WellKnownClientTypeEntry RemotingConfing = new WellKnownClientTypeEntry(typeof(FarClass), "tcp://localhost:9999/TcpService");
            //RemotingConfiguration.RegisterWellKnownClientType(RemotingConfing);
            RemotingConfiguration.Configure("RemotingClient.exe.Config",false);
            fc = new FarClass();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            table = new DataTable();
            table = fc.GetDataTable("student");
            this.dataGridView1.DataSource = table;
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            fc.UpdateDataTable(table, "student");
        }
    }
}