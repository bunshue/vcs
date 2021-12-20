using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for Process

namespace vcs_CommandLine
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            //button
            x_st = 12;
            y_st = 12;
            dx = 210;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //執行一條command命令 並取得其結果
            string result = string.Empty;

            GetCommandLineResult(out result);
            richTextBox1.Text = result + "\n";
        }

        /// <summary>
        /// 獲取視頻的幀寬度和幀高度
        /// </summary>
        /// <returns>null表示獲取寬度或高度失敗</returns>
        public static void GetCommandLineResult(out string result)
        {
            try
            {
                //執行命令獲取該文件的一些信息 
                string command = "systeminfo";

                string output;
                string error;
                ExecuteCommand(command, out output, out error);

                result = output;
            }
            catch (Exception)
            {
                //width = null;
                //height = null;
                result = null;
            }
        }

        /// <summary>
        /// 執行一條command命令
        /// </summary>
        /// <param name="command">需要執行的Command</param>
        /// <param name="output">輸出</param>
        /// <param name="error">錯誤</param>
        public static void ExecuteCommand(string command, out string output, out string error)
        {
            try
            {
                //創建一個進程
                Process pc = new Process();
                pc.StartInfo.FileName = command;
                pc.StartInfo.UseShellExecute = false;
                pc.StartInfo.RedirectStandardOutput = true;
                pc.StartInfo.RedirectStandardError = true;
                pc.StartInfo.CreateNoWindow = true;

                //啟動進程
                pc.Start();

                //准備讀出輸出流和錯誤流
                string outputData = string.Empty;
                string errorData = string.Empty;
                pc.BeginOutputReadLine();
                pc.BeginErrorReadLine();

                pc.OutputDataReceived += (ss, ee) =>
                {
                    outputData += ee.Data;
                };

                pc.ErrorDataReceived += (ss, ee) =>
                {
                    errorData += ee.Data;
                };

                //等待退出
                pc.WaitForExit();

                //關閉進程
                pc.Close();

                //返回流結果
                output = outputData;
                error = errorData;
            }
            catch (Exception)
            {
                output = null;
                error = null;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //C#中利用process類調用外部程序以及執行dos命令
            //C#中利用process類調用外部程序以及執行dos命令
            //TBD

            //C#中利用process類調用外部程序以及執行dos命令
            //string result = RunCmd("cmd");
            //richTextBox1.Text += result + "\n";
        }

        /*
        C#中的Process類可方便的調用外部程序，所以我們可以通過調用cmd.exe程序
        加入參數 "/c " 要執行的命令來執行一個DOS命令
        （/c代表執行參數指定的命令後關閉cmd.exe /k參數則不關閉cmd.exe）
        */

        private string RunCmd(string command)
        {
            //實例一個Process類，啟動一個獨立進程
            Process p = new Process();

            //Process類有一個StartInfo屬性，這個是ProcessStartInfo類，包括了一些屬性和方法，下面我們用到了他的幾個屬性：

            p.StartInfo.FileName = "cmd.exe"; //設定程序名
            //p.StartInfo.Arguments = "/c " command; //設定程式執行參數
            p.StartInfo.UseShellExecute = false; //關閉Shell的使用
            p.StartInfo.RedirectStandardInput = true; //重定向標準輸入
            p.StartInfo.RedirectStandardOutput = true; //重定向標準輸出
            p.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            p.StartInfo.CreateNoWindow = true; //設置不顯示窗口

            p.Start(); //啟動

            //p.StandardInput.WriteLine(command); //也可以用這種方式輸入要執行的命令
            //p.StandardInput.WriteLine("exit"); //不過要記得加上Exit要不然下一行程式執行的時候會當機
            return p.StandardOutput.ReadToEnd(); //從輸出流取得命令執行結果
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //執行外部.EXE檔 並獲取結果
            //相當於輸入 cmd/netstat -an, 並獲取輸出的結果

            Process process = new Process();
            ProcessStartInfo startInfo = new ProcessStartInfo("cmd.exe");
            startInfo.UseShellExecute = false;
            process.StartInfo = startInfo;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.Start();

            process.StandardInput.WriteLine("netstat -an");
            process.StandardInput.WriteLine("exit");

            string netMessage = process.StandardOutput.ReadToEnd();
            process.WaitForExit();
            process.Close();

            richTextBox1.Text += netMessage + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //調用外部程序，並獲取輸出和錯誤信息
            richTextBox1.Text += "目前只有異步模式可用\n";
            string cmd = "cmd";
            string parameter = "ver";
            exec_async(cmd, parameter);
        }

        //C# 調用外部程序，並獲取輸出和錯誤信息
        //1. 同步模式
        public void exec_sync(string exePath, string parameters)
        {
            System.Diagnostics.ProcessStartInfo psi =
            new System.Diagnostics.ProcessStartInfo();
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            psi.UseShellExecute = false;
            psi.FileName = exePath;
            psi.Arguments = parameters;
            System.Diagnostics.Process process = System.Diagnostics.Process.Start(psi);
            System.IO.StreamReader outputStreamReader = process.StandardOutput;
            System.IO.StreamReader errStreamReader = process.StandardError;
            process.WaitForExit(2000);
            if (process.HasExited)
            {
                string output = outputStreamReader.ReadToEnd();
                string error = errStreamReader.ReadToEnd();
                MessageBox.Show(output);
                MessageBox.Show(error);
            }
        }

        //2.異步模式
        public void exec_async(string exePath, string parameters)
        {
            Process process = new System.Diagnostics.Process();
            process.StartInfo.FileName = exePath;
            process.StartInfo.Arguments = parameters;
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.Start();
            process.BeginOutputReadLine();
            process.OutputDataReceived += new DataReceivedEventHandler(processOutputDataReceived);
        }

        private void processOutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            MessageBox.Show(e.Data);
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}

