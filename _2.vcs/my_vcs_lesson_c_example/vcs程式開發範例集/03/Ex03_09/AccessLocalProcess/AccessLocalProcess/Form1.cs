using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace AccessLocalProcess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            process1.StartInfo.FileName = "notepad.exe";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            process1.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
             System.Diagnostics.Process[] myProcesses;
            myProcesses =  System.Diagnostics.Process.GetProcessesByName("Notepad");
               foreach (System.Diagnostics.Process instance in myProcesses)
               {
                  instance.CloseMainWindow();
                  instance.WaitForExit(3000);
                  instance.Close();
               }
        }

     
    }
}