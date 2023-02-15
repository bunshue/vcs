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

namespace vcs_CommandLine1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox2.KeyUp += new KeyEventHandler(richTextBox2_KeyUp);

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
            dy = 65;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox2.Location = new Point(x_st + dx * 4 - 130, y_st + dy * 1);
            label1.Location = new Point(x_st + dx * 4 - 130, y_st + dy * 0 + 20);
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
            if (command.ToLower() == "cmd")
            {
                output = null;
                error = null;
                return;
            }

            try
            {
                Process process = new Process();    //創建一個進程用於調用外部程序

                process.StartInfo.FileName = command;   //設定欲執行的命令或程式名稱
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.RedirectStandardOutput = true;
                process.StartInfo.RedirectStandardError = true;
                process.StartInfo.CreateNoWindow = true;

                process.Start();    //啟動進程

                //准備讀出輸出流和錯誤流
                string outputData = string.Empty;
                string errorData = string.Empty;
                process.BeginOutputReadLine();
                process.BeginErrorReadLine();

                process.OutputDataReceived += (ss, ee) =>
                {
                    outputData += ee.Data;
                };

                process.ErrorDataReceived += (ss, ee) =>
                {
                    errorData += ee.Data;
                };

                //等待退出
                process.WaitForExit();

                //關閉進程
                process.Close();

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
            Process process = new Process();    //創建一個進程用於調用外部程序

            //Process類有一個StartInfo屬性，這個是ProcessStartInfo類，包括了一些屬性和方法，下面我們用到了他的幾個屬性：

            process.StartInfo.FileName = "cmd.exe"; //設定欲執行的命令或程式名稱
            //process.StartInfo.Arguments = "/c " command; //設定程式執行參數
            process.StartInfo.UseShellExecute = false; //關閉Shell的使用
            process.StartInfo.RedirectStandardInput = true; //重定向標準輸入
            process.StartInfo.RedirectStandardOutput = true; //重定向標準輸出
            process.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process.StartInfo.CreateNoWindow = true; //設置不顯示窗口

            process.Start();    //啟動進程

            //process.StandardInput.WriteLine(command); //也可以用這種方式輸入要執行的命令
            //process.StandardInput.WriteLine("exit"); //不過要記得加上Exit要不然下一行程式執行的時候會當機
            return process.StandardOutput.ReadToEnd(); //從輸出流取得命令執行結果
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //執行外部.EXE檔 並獲取結果
            //相當於輸入 cmd/netstat -an, 並獲取輸出的結果

            Process process = new Process();    //創建一個進程用於調用外部程序

            ProcessStartInfo startInfo = new ProcessStartInfo("cmd.exe");
            startInfo.UseShellExecute = false;
            process.StartInfo = startInfo;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;

            process.Start();    //啟動進程

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
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            psi.UseShellExecute = false;
            psi.FileName = exePath;
            psi.Arguments = parameters;

            Process process = Process.Start(psi);   //創建一個進程用於調用外部程序

            StreamReader outputStreamReader = process.StandardOutput;
            StreamReader errStreamReader = process.StandardError;
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
            Process process = new Process();    //創建一個進程用於調用外部程序

            process.StartInfo.FileName = exePath;   //設定欲執行的命令或程式名稱
            process.StartInfo.Arguments = parameters;
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.RedirectStandardOutput = true;

            process.Start();    //啟動進程

            process.BeginOutputReadLine();
            process.OutputDataReceived += new DataReceivedEventHandler(processOutputDataReceived);
        }

        private void processOutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            MessageBox.Show(e.Data);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //cmd 1

            //c# 執行外部程式(.exe，.bat…)

            string exe_filename = "cmd.exe";    //要執行的程序名稱
            Process process = new Process();    //創建一個進程用於調用外部程序

            //Process類有一個StartInfo屬性，這個是ProcessStartInfo類，包括了一些屬性和方法，下面用到了幾個屬性：
            process.StartInfo.FileName = exe_filename; //設定要啟動的程式
            //process.StartInfo.Arguments = "/c" + FullBatPath; //設定程式執行參數" /c " 執行完以下命令後停止
            process.StartInfo.UseShellExecute = false; //關閉Shell的使用
            process.StartInfo.RedirectStandardInput = true; //重定向標準輸入
            process.StartInfo.RedirectStandardOutput = true; //重定向標準輸出
            process.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process.StartInfo.CreateNoWindow = false; //true設置不顯示窗口
            process.StartInfo.RedirectStandardError = true;
            process.Start(); //啟動
            while (!process.HasExited)
            {
                process.WaitForExit(1000); //等待10秒
            }
            process.Dispose();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //cmd 2
            //隱式操作CMD命令行窗口
            /*
            MS的CMD命令行是一種重要的操作界面，
            一些在C#中不那麼方便完成的功能，在CMD中幾個簡單的命令或許就可以輕松搞定，
            如果能在C#中能完成CMD窗口的功能，那一定可以使我們的程序簡便不少。

            下面介紹一種常用的在C#程序中調用CMD.exe程序，並且不顯示命令行窗口界面，來完成CMD中各種功能的簡單方法。
            */

            string exe_filename = "cmd.exe";    //要執行的程序名稱
            Process process = new Process();    //創建一個進程用於調用外部程序
            process.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.RedirectStandardInput = true;//可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardOutput = true;//由調用程序獲取輸出信息
            process.StartInfo.CreateNoWindow = true;//不顯示程序窗口
            process.Start();//啟動程序
            //向CMD窗口發送輸入信息：
            //process.StandardInput.WriteLine("shutdown -r t 10"); //10秒後重啟（C#中可不好做哦）
            process.StandardInput.WriteLine("ver"); //10秒後重啟（C#中可不好做哦）
            //獲取CMD窗口的輸出信息：
            string sOutput = process.StandardOutput.ReadToEnd();

            richTextBox1.Text += sOutput + "\n";

            //有啦以下代碼，就可以神不知鬼不覺的操作CMD啦。總之，Process類是一個非常有用的類，它十分方便的利用第三方的程序擴展了C#的功能。

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //cmd 3


            string exe_filename = "cmd.exe";    //要執行的程序名稱

            Process process = new Process();    //創建一個進程用於調用外部程序

            process.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.CreateNoWindow = false;

            richTextBox1.Text += "啟動程式\n";
            process.Start(); //啟動進程

            //準備讀出輸出流和錯誤流
            string outputData = string.Empty;
            string errorData = string.Empty;
            process.BeginOutputReadLine();
            process.BeginErrorReadLine();

            process.OutputDataReceived += (ss, ee) =>
            {
                outputData += ee.Data;
            };

            process.ErrorDataReceived += (ss, ee) =>
            {
                errorData += ee.Data;
            };

            //等待退出
            process.WaitForExit();

            //關閉進程
            process.Close();

            richTextBox1.Text += "使用者關閉程式\n";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //cmd 4

            Process process = new Process();    //創建一個進程用於調用外部程序
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.CreateNoWindow = true;

            process.Start();

            //process.StandardInput.WriteLine(@"netstat -a -n > c:\dddddddddd\port.txt");
            process.StandardInput.WriteLine(@"dir > some_data.txt");

            
        }


        private void button8_Click(object sender, EventArgs e)
        {
            //取得系統開啟的端口和狀態

            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.StandardInput.WriteLine(@"netstat -a -n > port.txt");

            Application.DoEvents();

            richTextBox1.Text += "取得系統開啟的端口和狀態\n";
            try
            {
                string path = "port.txt";
                using (StreamReader sr = new StreamReader(path, Encoding.Default))
                {
                    while (sr.Peek() >= 0)
                    {
                        this.richTextBox1.Text += sr.ReadLine() + "\r\n";
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {

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

                process.Start();    //啟動進程

                //System.Threading.Thread.Sleep(1000);        //等一秒
                process.StandardInput.AutoFlush = true;           //輸入命令
                process.StandardInput.WriteLine(command);
                process.StandardInput.WriteLine("exit");          //等待結束  //一定要關閉

                //same
                //richTextBox2.AppendText(process.StandardOutput.ReadToEnd());  //直接顯示出來

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
