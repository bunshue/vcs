using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_CommandLine3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.KeyUp += new KeyEventHandler(richTextBox1_KeyUp);
        }

        private void richTextBox1_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                int count = richTextBox1.Lines.Length;

                if (count == 0)
                {
                    return;
                }

                while (count > 0 && (string.IsNullOrEmpty(richTextBox1.Lines[count - 1])))
                {
                    count--;
                }

                if (count > 0)// && !string.IsNullOrEmpty(txtCmdInput.Lines[count - 1]))
                {
                    ExecuteCmd(richTextBox1.Lines[count - 1]);
                }
            }
        }

        public void ExecuteCmd(string cmd)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();                                  //設置自動刷新緩沖並更新   
            p.StandardInput.AutoFlush = true;           //寫入命令     
            p.StandardInput.WriteLine(cmd);
            p.StandardInput.WriteLine("exit");          //等待結束  
            richTextBox1.AppendText(p.StandardOutput.ReadToEnd());
            p.WaitForExit();
            p.Close();
        }
    }
}

