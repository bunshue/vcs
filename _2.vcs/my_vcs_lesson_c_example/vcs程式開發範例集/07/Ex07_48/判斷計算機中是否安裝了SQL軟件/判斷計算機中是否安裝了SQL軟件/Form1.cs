using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.ServiceProcess;
namespace 判斷電腦中是否安裝了SQL軟體
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        public bool ExitSQL()
        {
            bool sqlFlag = false;
            ServiceController[] services = ServiceController.GetServices();
            for (int i = 0; i < services.Length; i++)
            {
                if (services[i].DisplayName.ToString() == "MSSQLSERVER")
                    sqlFlag = true;
            }
            return sqlFlag;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (ExitSQL())
            {
                label1.Text = "本機電腦中已經安裝SQL軟體";
            }
            else
            {
                label1.Text = "本機電腦中沒有安裝SQL軟體";
            }
        }
    }
}
