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
        Process process_async = new Process();    //創建一個進程用於調用外部程序

        //一維List for string
        List<string> cmd_output_data = new List<string>();

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
            //執行CommandLine指令, 並取回結果 1

            string exe_filename = "cmd.exe";    //要執行的程式名稱
            string command = "systeminfo";      //向要執行的程式發送的命令
            //string command = "ipconfig /all"; //向要執行的程式發送的命令, 並加參數
            string output_data = run_command_line_process(exe_filename, command);//程式+命令, 程式+命令+參數
            richTextBox1.Text += output_data + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //執行CommandLine指令, 並取回結果 2

            string filename = @"..\..\my_script.bat";
            string output_data = run_command_line_process_psi(filename, null);  //若是batch檔案, 直接傳入即可
            richTextBox1.Text += output_data + "\n";

            //調用系統IPCONFIG獲取本機局域網IP以及其他相關信息
            //執行一條command命令 並取得其結果
            //調用ipconfig ,並傳入參數: /all 
            string command1 = "ipconfig";
            string command2 = "/all";
            output_data = run_command_line_process_psi(command1, command2);
            richTextBox1.Text += output_data + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //關閉與重啟計算機(偽)

            //僅執行命令, 不管結果

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
        }

        int show_result_index = 0;
        private void button5_Click(object sender, EventArgs e)
        {
            //燒錄映像檔

            string exe_filename = @"../../aaaa.exe";
            string parameters = "aa bb cc dd ee";

            run_command_line_process_async(exe_filename, parameters);
        }

        //標準版 非同步 Process使用
        void run_command_line_process_async(string exe_filename, string command)
        {
            cmd_output_data.Clear();
            show_result_index = 0;
            //timer_get_result.Enabled = true;

            process_async.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            //process_async.StartInfo.Arguments = "/c " + command; //設定程式執行參數, 也可直接把command寫在這裡, 就不用後面的 StandardInput.WriteLine 了, 要加/c
            //process_async.StartInfo.Arguments = "/c systeminfo";  //可, 要加/c
            process_async.StartInfo.Arguments = command;
            //process_async.StandardInput.AutoFlush = true;

            process_async.StartInfo.UseShellExecute = false;  //false, 關閉Shell的使用, 是否指定操作系統外殼進程啟動程序, 可能接受來自調用程序的輸入信息
            process_async.StartInfo.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            process_async.StartInfo.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            process_async.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process_async.StartInfo.CreateNoWindow = true; //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體
            process_async.StartInfo.ErrorDialog = false;
            //process_async.StartInfo.WindowStyle = ProcessWindowStyle.Normal;  //測不出來
            //process_async.StartInfo.WindowStyle = ProcessWindowStyle.Hidden,

            //設定非同步資料處理 output and error handlers
            process_async.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
            process_async.ErrorDataReceived += new DataReceivedEventHandler(OutputHandler);

            process_async.Start();    //啟動程式

            //啟動讀取資料輸出與錯誤輸出
            process_async.BeginOutputReadLine();
            process_async.BeginErrorReadLine();
            richTextBox1.Text += "等待程式結束.......\n";
            process_async.WaitForExit();	//等待退出
            richTextBox1.Text += "程式結束\n";
        }

        void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            if (process_async.HasExited == false)
            {
                Console.WriteLine("process.HasExited = " + process_async.HasExited.ToString());
                // Write to console
                Console.WriteLine(outLine.Data);

                cmd_output_data.Add(outLine.Data);
            }
            else
            {
                cmd_output_data.Add("已結束");
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //非同步測試2
            //richTextBox1.Text += "process_async.HasExited = " + process_async.HasExited.ToString() + "\n";

            if (cmd_output_data.Count > 0)
                richTextBox1.Text += "共有 " + cmd_output_data.Count.ToString() + " 筆資料要存\n";

            int i;
            for (i = 0; i < cmd_output_data.Count; i++)
            {
                //richTextBox1.Text += "cmd_output_data[" + i.ToString() + "] = " + cmd_output_data[i] + "\n";
                if (cmd_output_data[i] == "")
                {
                    richTextBox1.Text += "xxxxxi = " + i.ToString() + "\t" + cmd_output_data[i].Length.ToString() + "\n";
                }
                else
                {
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + cmd_output_data[i] + "\n";
                }
                //richTextBox1.Text += "len = " + cmd_output_data[i].Length.ToString() + "\n";

            }


        }

        //標準版Process使用
        string run_command_line_process(string exe_filename, string command)
        {
            //string exe_filename = "cmd.exe";    //要執行的程式名稱

            Process process = new Process();    //創建一個進程用於調用外部程序

            process.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            //process.StartInfo.Arguments = "/c " + command; //設定程式執行參數, 也可直接把command寫在這裡, 就不用後面的 StandardInput.WriteLine 了, 要加/c
            //process.StartInfo.Arguments = "/c systeminfo";  //可, 要加/c
            //process.StartInfo.Arguments = command;
            //process.StandardInput.AutoFlush = true;

            process.StartInfo.UseShellExecute = false;  //false, 關閉Shell的使用, 是否指定操作系統外殼進程啟動程序, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            process.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process.StartInfo.CreateNoWindow = true; //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體
            process.StartInfo.ErrorDialog = false;
            //process.StartInfo.WindowStyle = ProcessWindowStyle.Normal;  //測不出來
            //process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;

            process.Start();    //啟動程式

            //向要啟動的程式發送輸入信息
            process.StandardInput.WriteLine(command);

            process.StandardInput.WriteLine("exit");	//一定要關閉, 不然會當機

            //從輸出流取得命令執行結果
            StreamReader output_sr = process.StandardOutput;
            string output_data = output_sr.ReadToEnd();
            StreamReader error_sr = process.StandardError;
            string error_data = error_sr.ReadToEnd();
            //richTextBox1.Text += "輸出 :\n" + output_data + "\n";
            //richTextBox1.Text += "錯誤 :\n" + error_data + "\n";

            process.WaitForExit();	//等待退出
            process.Close();	//關閉進程

            return output_data;
        }

        string run_command_line_process_psi(string cmd1, string cmd2)
        {
            //不用另外設定 "cmd.exe"

            ProcessStartInfo psi = new ProcessStartInfo(cmd1, cmd2);

            psi.CreateNoWindow = true;      //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體
            psi.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            psi.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            psi.RedirectStandardError = true; //重定向錯誤輸出

            psi.UseShellExecute = false;

            //Process process = Process.Start(psi); //same, 拆成以下3行

            Process process = new Process();
            process.StartInfo = psi;
            process.Start();    //啟動程式


            //從輸出流取得命令執行結果
            StreamReader output_sr = process.StandardOutput;
            string output_data = output_sr.ReadToEnd();
            StreamReader error_sr = process.StandardError;
            string error_data = error_sr.ReadToEnd();
            //richTextBox1.Text += "輸出 :\n" + output_data + "\n";
            //richTextBox1.Text += "錯誤 :\n" + error_data + "\n";

            // Clean up.
            output_sr.Close();
            error_sr.Close();
            process.Close();

            return output_data;
        }


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
            process.StartInfo.CreateNoWindow = true; //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體

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
                process.StartInfo.CreateNoWindow = true;            //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體

                process.Start();    //啟動程式

                //System.Threading.Thread.Sleep(1000);        //等一秒
                process.StandardInput.AutoFlush = true;           //輸入命令

                //向要啟動的程式發送輸入信息
                process.StandardInput.WriteLine(command);
                process.StandardInput.WriteLine("exit");	//一定要關閉, 不然會當機

                //same
                //獲取要啟動的程式的輸出信息
                //從輸出流取得命令執行結果
                StreamReader output_sr = process.StandardOutput;
                string output_data = output_sr.ReadToEnd();
                StreamReader error_sr = process.StandardError;
                string error_data = error_sr.ReadToEnd();
                //richTextBox1.Text += "輸出 :\n" + output_data + "\n";
                //richTextBox1.Text += "錯誤 :\n" + error_data + "\n";

                richTextBox2.Text += output_data + "\n";
                //獲取要啟動的程式的輸出信息
                //從輸出流取得命令執行結果
                StreamReader reader = process.StandardOutput;
                string output = reader.ReadLine();//每次讀取一行

                while (!reader.EndOfStream) //怎知輸出已到結尾?!?!
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

        private void timer_get_result_Tick(object sender, EventArgs e)
        {
            //if (cmd_output_data.Count > 0)
            //richTextBox1.Text += "共有 " + cmd_output_data.Count.ToString() + " 筆資料要存\n";

            if (show_result_index < cmd_output_data.Count)
            {
                int i;
                int count = cmd_output_data.Count - show_result_index;
                richTextBox1.Text += count.ToString() + " ";
                for (i = 0; i < count; i++)
                {
                    //richTextBox1.Text += "i = " + i.ToString() + "\t" + cmd_output_data[show_result_index] + "\n";
                    //Application.DoEvents();
                }
                show_result_index = cmd_output_data.Count;
            }
        }
    }
}
