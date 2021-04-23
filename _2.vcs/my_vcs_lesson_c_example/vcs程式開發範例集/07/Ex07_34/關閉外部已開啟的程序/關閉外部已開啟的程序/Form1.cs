using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace 關閉外部已開啟的程序
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            Process[] myProcesses = Process.GetProcesses();
            foreach (Process myProcess in myProcesses)
            {
                if (myProcess.MainWindowTitle.Length > 0)
                {
                    listBox1.Items.Add(myProcess.ProcessName.ToString().Trim());
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process[] myProcesses = Process.GetProcessesByName(listBox1.SelectedItem.ToString().Trim());
            foreach (Process myProcess in myProcesses)
            {
                myProcess.CloseMainWindow();
            }

            //remove this process in listbox
            listBox1.Items.Remove(listBox1.SelectedItem);//從listBox1中移除listBox1中選定的項

            MessageBox.Show("程序已關閉", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
