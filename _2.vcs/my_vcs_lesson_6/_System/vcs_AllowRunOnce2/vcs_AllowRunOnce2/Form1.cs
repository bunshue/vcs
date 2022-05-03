using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_AllowRunOnce2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 判斷是否已有程式在執行
            string proc = Process.GetCurrentProcess().ProcessName;
            Process[] processes = Process.GetProcessesByName(proc);

            //richTextBox1.Text += "ProcessName : " + proc + "\tlen = " + processes.Length.ToString() + "\n";
            if (processes.Length > 1)
            {
                MessageBox.Show("PrintScreen " + proc + " 已經在執行", "重複執行錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                Close();
            }

        }
    }
}
