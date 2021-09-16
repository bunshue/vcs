using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace xCh5_4_2_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process currentProcess = Process.GetCurrentProcess();
            MessageBox.Show(
                 "電腦名稱：" + currentProcess.MachineName +
                 Environment.NewLine +
                 "處理序名稱：" + currentProcess.ProcessName);
        }

        private void button2_Click(object sender, EventArgs e)
        {
                process1 = Process.Start("Notepad.exe");
                for (int i = 0; i < 5; i++)
                {
                    if (!process1.HasExited)
                    {
                        process1.Refresh();

                        textBox1.AppendText(
                            "實體記憶體的耗用： "+ 
                            process1.WorkingSet64.ToString()+
                            Environment.NewLine
                            );

                        process1.WaitForExit(3000);
                    }
                    else
                    {
                        break;
                    }
                }
                process1.CloseMainWindow();
                textBox1.AppendText("執行了CloseMainWindow()方法");
                textBox1.AppendText(Environment.NewLine);

                process1.Close();
                textBox1.AppendText("執行了Close()方法");
        }
    }
}
