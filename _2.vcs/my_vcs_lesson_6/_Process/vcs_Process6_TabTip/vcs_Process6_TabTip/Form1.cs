using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;

namespace vcs_Process6_TabTip
{
    public partial class Form1 : Form
    {
        string progFiles = string.Empty;
        string keyboardPath = string.Empty;
        Process myProcess = new Process();

        int focus_at = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            progFiles = @"C:\Program Files\Common Files\Microsoft Shared\ink";
            keyboardPath = Path.Combine(progFiles, "TabTip.exe");

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (focus_at == 1)
            {
                richTextBox1.Focus();
            }
            else if (focus_at == 2)
            {
                richTextBox2.Focus();
            }
            else if (focus_at == 3)
            {
                richTextBox3.Focus();
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            focus_at = 1;
            //System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/osk.exe");
            //OR
            //System.Diagnostics.Process.Start("osk.exe");


            myProcess = Process.Start(keyboardPath);


        }

        private void button2_Click(object sender, EventArgs e)
        {
            focus_at = 2;
            myProcess = Process.Start(keyboardPath);

        }

        private void button3_Click(object sender, EventArgs e)
        {

            focus_at = 3;
            myProcess = Process.Start(keyboardPath);
        }
    }
}
