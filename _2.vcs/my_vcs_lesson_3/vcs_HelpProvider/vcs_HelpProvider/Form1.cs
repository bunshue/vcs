using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
this.HelpButton = true;
this.MaximizeBox = false;
this.MinimizeBox = false;
*/

namespace vcs_HelpProvider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string strpath = Application.StartupPath.Substring(0, Application.StartupPath.Substring(0, Application.StartupPath.LastIndexOf("\\")).LastIndexOf("\\"));
            strpath += @"\AMCap.chm";
            helpProvider1.HelpNamespace = strpath;

            richTextBox1.Text += "filename = " + strpath + "\n";

            //------------------------------------------------------------  # 60個

            helpProvider2.SetShowHelp(textBox_id, true);
            helpProvider2.SetHelpString(textBox_id, "請輸入帳號！");

            helpProvider2.SetShowHelp(textBox_password, true);
            helpProvider2.SetHelpString(textBox_password, "請輸入密碼！");

            helpProvider2.SetShowHelp(bt_login, true);
            helpProvider2.SetHelpString(bt_login, "帳號輸入後，點這裡喔！");

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "先按上面的問號\n";
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


