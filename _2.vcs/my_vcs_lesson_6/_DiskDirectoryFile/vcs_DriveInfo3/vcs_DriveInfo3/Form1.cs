using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;


namespace vcs_DriveInfo3
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

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_DriveInfo3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //通过GetVolumeInformation获取
            var diskID = GetdiskID();
            Console.WriteLine("GetVolumeInformation C={diskID}");
            Console.WriteLine(diskID);

            CmdResult result;
            //获取进程所在盘符序列号
            result = CmdExecute(new string[] { "vol" });
            Console.WriteLine("Output={result.OutputData}");
            Console.WriteLine(result.OutputData);

            Console.WriteLine("Error={result.ErrorData}");
            Console.WriteLine(result.ErrorData);

            //获取c盘序列号
            result = CmdExecute(new string[] { "c:", "vol" });
            Console.WriteLine("Output={result.OutputData}");
            Console.WriteLine(result.OutputData);

            Console.WriteLine("Error={result.ErrorData}");
            Console.WriteLine(result.ErrorData);

            //获取d盘序列号
            result = CmdExecute(new string[] { "d:", "vol" });
            Console.WriteLine("Output={result.OutputData}");
            Console.WriteLine(result.OutputData);

            Console.WriteLine("Error={result.ErrorData}");
            Console.WriteLine(result.ErrorData);

            Console.WriteLine("回车退出程序");
            Console.ReadLine();

        }


        /// <summary>
        /// GetVolumeInformation
        /// </summary>
        /// <param name="lpRootPathName">欲获取信息的那个卷的根路径</param>
        /// <param name="lpVolumeNameBuffer">用于装载卷名（卷标）的一个字串 </param>
        /// <param name="nVolumeNameSize">lpVolumeNameBuffer字串的长度</param>
        /// <param name="lpVolumeSerialNumber">用于装载磁盘卷序列号的变量</param>
        /// <param name="lpMaximumComponentLength">指定一个变量，用于装载文件名每一部分的长度。例如，在“c:\component1\component2.ext”的情况下，它就代表component1或component2名称的长度 .</param>
        /// <param name="lpFileSystemFlags">用于装载一个或多个二进制位标志的变量。对这些标志位的解释如下：
        /// FS_CASE_IS_PRESERVED 文件名的大小写记录于文件系统
        /// FS_CASE_SENSITIVE 文件名要区分大小写
        /// FS_UNICODE_STORED_ON_DISK 文件名保存为Unicode格式
        /// FS_PERSISTANT_ACLS 文件系统支持文件的访问控制列表（ACL）安全机制
        /// FS_FILE_COMPRESSION 文件系统支持逐文件的进行文件压缩
        /// FS_VOL_IS_COMPRESSED 整个磁盘卷都是压缩的
        ///</param>
        /// <param name="lpFileSystemNameBuffer">指定一个缓冲区,用于装载文件系统的名称（如FAT，NTFS以及其他）       </param>
        /// <param name="nFileSystemNameSize">lpFileSystemNameBuffer字串的长度</param>
        /// <returns></returns>
        [DllImport("Kernel32.dll", CharSet = CharSet.Auto)]
        public static extern bool GetVolumeInformation(string lpRootPathName, string lpVolumeNameBuffer, int nVolumeNameSize, ref int lpVolumeSerialNumber, int lpMaximumComponentLength, int lpFileSystemFlags, string lpFileSystemNameBuffer, int nFileSystemNameSize);
        /// <summary>
        /// 获取硬盘ID
        /// </summary>
        /// <returns></returns>
        public static string GetdiskID()
        {

            const int MAX_FILENAME_LEN = 256;
            int retVal = 0;
            int a = 0;
            int b = 0;
            string str1 = null;
            string str2 = null;


            GetVolumeInformation(
                @"C:\",
                str1,
                MAX_FILENAME_LEN,
                ref retVal,
                a,
                b,
                str2,
                MAX_FILENAME_LEN);

            return Convert.ToString(retVal, 16).ToUpper();

        }
        /// <summary>
        /// 执行DOS命令
        /// </summary>
        /// <param name="commands">顺序执行命令列表</param>
        /// <param name="timeoutSecond">等待命令执行的时间（单位：秒），如果设定为0，则无限等待</param>
        /// <returns></returns>
        static CmdResult CmdExecute(string[] commands, int timeoutSecond = 0)
        {
            var output = new StringBuilder();
            var error = new StringBuilder();
            if (commands != null)
            {
                try
                {
                    using (var process = new Process())
                    {
                        var startInfo = new ProcessStartInfo();
                        startInfo.FileName = "cmd.exe";
                        //设定需要执行的命令
                        startInfo.UseShellExecute = false;
                        //不使用系统外壳程序启动
                        startInfo.RedirectStandardInput = true;
                        //重定向输入
                        startInfo.RedirectStandardOutput = true;
                        var filter = new Regex(@"^(Microsoft Windows|版权所有|(\(c\) \d{4} Microsoft Corporation)|([a-zA-Z]:(\\[^\\]*)+)\>)", RegexOptions.IgnoreCase | RegexOptions.ExplicitCapture);
                        process.OutputDataReceived += (object s, DataReceivedEventArgs e) =>
                        {
                            if (e.Data == null || filter.IsMatch(e.Data)) return;
                            output.Append(e.Data);
                        };
                        startInfo.RedirectStandardError = true;
                        process.ErrorDataReceived += (object s, DataReceivedEventArgs e) =>
                        {
                            if (e.Data == null) return;
                            error.Append(e.Data);
                        };
                        //重定向输出
                        startInfo.CreateNoWindow = true;
                        //不创建窗口
                        process.StartInfo = startInfo;
                        if (process.Start())
                        {
                            process.BeginOutputReadLine();
                            process.BeginErrorReadLine();
                            foreach (var command in commands)
                            {
                                process.StandardInput.WriteLine(command);
                            }
                            process.StandardInput.WriteLine("exit");
                            if (timeoutSecond == 0)
                            {
                                process.WaitForExit();
                            }
                            else
                            {
                                process.WaitForExit(timeoutSecond);
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    error.Append(ex.ToString());
                }
            }
            return new CmdResult()
            {
                OutputData = output.ToString(),
                ErrorData = error.ToString()
            };
        }
        /// <summary>
        /// cmd执行结果
        /// </summary>
        class CmdResult
        {
            /// <summary>
            /// 程序正常输出
            /// </summary>
            public string OutputData { get; set; }
            /// <summary>
            /// 异常输出
            /// </summary>
            public string ErrorData { get; set; }
        }


        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
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

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

