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
using RemotingClass;
using System.IO;

namespace RemotingClient
{
    public partial class RemotingClientForm : Form
    {
        FarClass fc;
        public RemotingClientForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
              StreamReader sr = new StreamReader(fc.GetFile(textBox1.Text));
              StreamWriter sw = new StreamWriter(textBox2.Text);
              sw.Write(sr.ReadToEnd());
              sr.Close();
              sw.Close();
        }

        private void RemotingClientForm_Load(object sender, EventArgs e)
        {
            RemotingConfiguration.Configure("RemotingClient.exe.Config",false);
            fc = new FarClass();
        }
    }
}