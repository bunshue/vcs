using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;       //for Process

namespace vcs_Process_CommandLine
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

            richTextBox2.KeyUp += new KeyEventHandler(richTextBox2_KeyUp);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            //button
            x_st = 15;
            y_st = 22;
            dx = 200;
            dy = 70;

            groupBox1.Location = new Point(10, 10);

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            richTextBox1.Location = new Point(10 + dx * 1 + 60, 10);
            richTextBox2.Location = new Point(10 + dx * 4 - 90 + 60, 10 + 30);
            label1.Location = new Point(10 + dx * 4 - 90 + 60, 10);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //執行一條command命令 並取得其結果
            string exe_filename = "cmd.exe";    //要執行的程式名稱
            string command = "systeminfo";             //向要執行的程式發送的命令
            //string command = "ver";             //向要執行的程式發送的命令
            string output_data = string.Empty;

            output_data = run_command_line_process(exe_filename, command);
            richTextBox1.Text += output_data + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //關閉與重啟計算機(偽)

            /*
            //關閉
            string exe_filename = "cmd.exe";    //要執行的程式名稱
            string command1 = "shutdown -s -t 0";             //向要執行的程式發送的命令    //執行關機命令 0秒後

            richTextBox1.Text += "關閉計算機(偽)\n";
            //偽執行
            //run_command_line_process(exe_filename, command1);

            //重啟
            string command2 = "shutdown -r -t 0";             //向要執行的程式發送的命令    //執行重啟計算機命令 0秒後
            richTextBox1.Text += "重啟計算機(偽)\n";
            //偽執行
            //run_command_line_process(exe_filename, command2);
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //執行CommandLine指令, 並取回結果
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..\\hello.bat"));

            ProcessStartInfo start_info = new ProcessStartInfo(filename);
            start_info.UseShellExecute = false;
            start_info.CreateNoWindow = true;
            start_info.RedirectStandardOutput = true;
            start_info.RedirectStandardError = true;

            // Make the process and set its start information.
            using (Process process = new Process())
            {
                process.StartInfo = start_info;

                // Start the process.
                process.Start();

                // Attach to stdout and stderr.
                using (StreamReader std_out = process.StandardOutput)
                {
                    using (StreamReader std_err = process.StandardError)
                    {
                        // Display the results.
                        richTextBox1.Text += "輸出 :\n" + std_out.ReadToEnd() + "\n";
                        richTextBox1.Text += "錯誤 :\n" + std_err.ReadToEnd() + "\n";

                        // Clean up.
                        std_err.Close();
                        std_out.Close();
                        process.Close();
                    }
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //檢測網絡連接（主要是局域網）
            //檢測網絡連接問題，都是通過與外網（或者局域網服務器）傳遞信息檢測的。

            //string ip = "10.1.148.1";
            //string ip = "192.192.132.229";
            string ip_address = "www.google.com";

            string exe_filename = "cmd.exe";    //要執行的程式名稱
            string command = "ping -n 1 " + ip_address;

            string output_data = run_command_line_process(exe_filename, command);

            string ping_result = string.Empty;

            if (output_data.IndexOf("(0% loss)") != -1)
                ping_result = "連接";
            else if (output_data.IndexOf("Destination host unreachable.") != -1)
                ping_result = "無法到達目的主機";
            else if (output_data.IndexOf("Request timed out.") != -1)
                ping_result = "超時";
            else if (output_data.IndexOf("Unknown host") != -1)
                ping_result = "無法解析主機";
            else
                ping_result = output_data;

            richTextBox1.Text += ping_result;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //調用系統IPCONFIG獲取本機局域網IP以及其他相關信息

            //執行一條command命令 並取得其結果
            string exe_filename = "cmd.exe";    //要執行的程式名稱
            string command = "ipconfig /all";             //向要執行的程式發送的命令
            //string command = "ver";             //向要執行的程式發送的命令
            string output_data = string.Empty;

            output_data = run_command_line_process2(exe_filename, command);
            richTextBox1.Text += output_data + "\n";
        }

        string run_command_line_process2(string exe_filename, string command)
        {
            //調用ipconfig ,並傳入參數: /all 
            ProcessStartInfo psi = new ProcessStartInfo("ipconfig", "/all");

            psi.CreateNoWindow = true;
            psi.RedirectStandardOutput = true;
            psi.UseShellExecute = false;

            Process process = Process.Start(psi);

            return process.StandardOutput.ReadToEnd();
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        //標準版Process使用
        string run_command_line_process(string exe_filename, string command)
        {
            //隱式操作CMD命令行窗口
            /*
            MS的CMD命令行是一種重要的操作界面，
            一些在C#中不那麼方便完成的功能，在CMD中幾個簡單的命令或許就可以輕松搞定，
            如果能在C#中能完成CMD窗口的功能，那一定可以使我們的程序簡便不少。

            下面介紹一種常用的在C#程序中調用CMD.exe程序，並且不顯示命令行窗口界面，來完成CMD中各種功能的簡單方法。
            */

            //string exe_filename = "cmd.exe";    //要執行的程式名稱
            string output_data = string.Empty;

            Process process = new Process();    //創建一個進程用於調用外部程序

            process.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            //process.StartInfo.Arguments = "/c " command; //設定程式執行參數
            //process.StartInfo.Arguments = command; //也可直接把command寫在這裡, 就不用後面的 StandardInput.WriteLine 了
            //process.StartInfo.Arguments = "/c" + FullBatPath; //設定程式執行參數" /c " 執行完以下命令後停止
            //process.StartInfo.Arguments = "ping -n   1" + ip_address;
            //process.StandardInput.AutoFlush = true;

            process.StartInfo.UseShellExecute = false;  //false, 關閉Shell的使用, 是否指定操作系統外殼進程啟動程序, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            process.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process.StartInfo.CreateNoWindow = true; //true, 設置不顯示程式窗口, 用T/F測不出差異
            //psi.CreateNoWindow = true; //若為false，則會出現cmd的黑窗體 
            process.StartInfo.ErrorDialog = false;

            process.Start();    //啟動程式

            //向要啟動的程式發送輸入信息
            process.StandardInput.WriteLine(command);

            process.StandardInput.WriteLine("exit");	//一定要關閉, 不然會當機

            //獲取要啟動的程式的輸出信息
            output_data = process.StandardOutput.ReadToEnd();	//從輸出流取得命令執行結果

            process.WaitForExit();	//等待退出
            process.Close();	//關閉進程

            return output_data;
        }

        /*  tmp
        C#中的Process類可方便的調用外部程序，所以我們可以通過調用cmd.exe程序
        加入參數 "/c " 要執行的命令來執行一個DOS命令
        （/c代表執行參數指定的命令後關閉cmd.exe /k參數則不關閉cmd.exe）
        */
        /*

                            //psi.WindowStyle = ProcessWindowStyle.Hidden;

                    //獲取要啟動的程式的輸出信息
                    StreamReader outputStreamReader = process.StandardOutput;
                    StreamReader errStreamReader = process.StandardError;
                    process.WaitForExit(2000);
                    if (process.HasExited)
                    {
                        string output = outputStreamReader.ReadToEnd();
                        string error = errStreamReader.ReadToEnd();

                        richTextBox1.Text += "output:\n" + output + "\n";
                        richTextBox1.Text += "error:\n" + error + "\n";
                    }
                */

        /*
                            process.Start();    //啟動程式

                    while (!process.HasExited)
                    {
                        richTextBox1.Text += "a ";
                        process.WaitForExit(1000); //等待10秒
                    }
                    process.Dispose();
        */

        public void exec_async(string exe_filename, string parameters)
        {
            Process process = new Process();    //創建一個進程用於調用外部程序

            process.StartInfo.FileName = exe_filename; //設定要啟動的程式
            process.StartInfo.Arguments = parameters;

            process.StartInfo.UseShellExecute = false;  //false, 關閉Shell的使用, 是否指定操作系統外殼進程啟動程序, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            process.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process.StartInfo.CreateNoWindow = true; //true, 設置不顯示程式窗口

            process.Start();    //啟動程式

            process.BeginOutputReadLine();
            process.OutputDataReceived += new DataReceivedEventHandler(processOutputDataReceived);
        }

        private void processOutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            Console.WriteLine("取得資料: " + e.Data);
        }

        private void richTextBox2_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                int count = richTextBox2.Lines.Length;
                if (count == 0)
                {
                    return;
                }

                while (count > 0 && (string.IsNullOrEmpty(richTextBox2.Lines[count - 1])))
                {
                    count--;
                }
                if (count > 0)// && !string.IsNullOrEmpty(richTextBox2.Lines[count - 1]))
                {
                    ExecuteCmd(richTextBox2.Lines[count - 1]);
                }
            }
        }

        /// <summary>
        /// 執行Cmd命令
        /// </summary>
        public void ExecuteCmd(string command)
        {
            if (command.ToLower() == "cmd")
            {
                return;
            }

            try
            {
                Process process = new Process();    //創建一個進程用於調用外部程序

                process.StartInfo.FileName = "cmd.exe";     //設定欲執行的命令或程式名稱
                process.StartInfo.UseShellExecute = false;  //是否指定操作系統外殼進程啟動程序

                //可能接受來自調用程序的輸入信息
                process.StartInfo.RedirectStandardInput = true;   //重定向標准輸入
                process.StartInfo.RedirectStandardOutput = true;  //重定向標准輸出
                process.StartInfo.RedirectStandardError = true;   //重定向錯誤輸出
                process.StartInfo.CreateNoWindow = true;          //不顯示程序窗口

                process.Start();    //啟動程式

                //System.Threading.Thread.Sleep(1000);        //等一秒
                process.StandardInput.AutoFlush = true;           //輸入命令

                //向要啟動的程式發送輸入信息
                process.StandardInput.WriteLine(command);
                process.StandardInput.WriteLine("exit");	//一定要關閉, 不然會當機

                //same
                //獲取要啟動的程式的輸出信息
                string output_data = process.StandardOutput.ReadToEnd();	//從輸出流取得命令執行結果
                richTextBox2.Text += output_data + "\n";

                //獲取要啟動的程式的輸出信息
                StreamReader reader = process.StandardOutput;//截取輸出流
                string output = reader.ReadLine();//每次讀取一行

                while (!reader.EndOfStream)
                {
                    richTextBox2.Text += output + "\n";
                    output = reader.ReadLine();
                }
                process.WaitForExit();
                process.Close();
            }
            catch (Exception)
            {
            }
        }
    }
}
