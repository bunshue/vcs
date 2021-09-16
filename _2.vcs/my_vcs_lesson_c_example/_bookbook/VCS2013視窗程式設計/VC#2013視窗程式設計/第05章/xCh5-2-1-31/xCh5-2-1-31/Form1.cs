using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_2_1_31
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            helpProvider1.SetShowHelp(textBox1, true);
            helpProvider1.SetHelpString(textBox1, "請輸入帳號！");

            helpProvider1.SetShowHelp(textBox2, true);
            helpProvider1.SetHelpString(textBox2, "請輸入密碼！");

            helpProvider1.SetShowHelp(button1, true);
            helpProvider1.SetHelpString(button1, "帳號輸入後，點這裡喔！");
        }
    }
}



