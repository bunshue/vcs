using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;        //for Directory, File
using System.Diagnostics;   //for Process
using System.Threading;
using System.Threading.Tasks;

using System.Collections.Concurrent;    //for ConcurrentQueue

namespace vcs_LOG
{
    public partial class Form1 : Form
    {
        private string LogFileName;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            LogFileName = Application.StartupPath + "\\log_" + DateTime.Now.ToString("yyyyMMdd") + ".txt";
            richTextBox1.Text += "用Timer1自動存Log中.....\n";

            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            _que = new ConcurrentQueue<FlashLogMessage>();
            _mre = new ManualResetEvent(false);

            Register();

            LogAPI.InitLogAPI(Application.StartupPath, "aaaaaaa.log");


        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Process.GetCurrentProcess().Kill(); //程序的退出
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        int aa = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            aa++;
            string str = "加入LOG aa = " + aa.ToString();
            EventLog.Write(str);
            richTextBox1.Text += str + "\n";
        }

        // If the file exceeds max_size bytes, move it to a new file
        // with .1 appended to the name and bump down older versions.
        // (E.g. log.txt.1, log.txt.2, etc.)
        // Then write the text into the main log file. 
        private void WriteToLog(string new_text, string file_name, long max_size, int num_backups)
        {
            // See if the file is too big.
            FileInfo file_info = new FileInfo(file_name);
            if (file_info.Exists && file_info.Length > max_size)
            {
                // Remove the oldest version if it exists.
                if (File.Exists(file_name + "." + num_backups.ToString()))
                {
                    File.Delete(file_name + "." + num_backups.ToString());
                    richTextBox1.Text += "delete\t" + file_name + "\n";
                }

                // Bump down earlier backups.
                //richTextBox1.Text += "\n一個一個改名\n";
                for (int i = num_backups - 1; i > 0; i--)
                {
                    if (File.Exists(file_name + "." + i.ToString("D4")))
                    {
                        // Move file i to file i + 1.
                        File.Move(file_name + "." + i.ToString("D4"), file_name + "." + (i + 1).ToString("D4"));
                        //richTextBox1.Text += "i = " + i.ToString() + " rename\told = " + file_name + "." + i.ToString() + "\tnew = " + file_name + "." + (i + 1).ToString() + "\n";
                    }
                }
                // Move the main log file.
                File.Move(file_name, file_name + ".0001");
            }

            // Write the text.
            File.AppendAllText(file_name, new_text + '\n');
        }

        int i = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            i++;
            string ttt = i.ToString() + " " + DateTime.Now.ToString();
            WriteToLog(ttt, LogFileName, 100, 300);
        }

        public static class EventLog
        {
            public static string FilePath { get; set; }
            public static void Write(string format, params object[] arg)
            {
                Write(string.Format(format, arg));
            }

            public static void Write(string message)
            {
                if (string.IsNullOrEmpty(FilePath))
                {
                    FilePath = Directory.GetCurrentDirectory();
                }

                string filename = FilePath + string.Format("\\{0:yyyy}-{0:MM}\\LOG_{0:yyyy-MM-dd}.txt", DateTime.Now);
                FileInfo finfo = new FileInfo(filename);
                if (finfo.Directory.Exists == false)
                {
                    finfo.Directory.Create();
                }
                string writeString = string.Format("{0:yyyy/MM/dd HH:mm:ss} {1}",
                    DateTime.Now, message) + Environment.NewLine;

                File.AppendAllText(filename, writeString, Encoding.Unicode);
            }
        }

        int i2 = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫log的方法2\n";
            WriteLog("寫log的方法2 " + (i2++).ToString());
        }

        private void WriteLog(string text)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory;
            path = System.IO.Path.Combine(path, "OutputStreamLogs\\" + DateTime.Now.ToString("yy-MM-dd"));

            if (!System.IO.Directory.Exists(path))
            {
                System.IO.Directory.CreateDirectory(path);
            }
            string fileFullName = System.IO.Path.Combine(path, string.Format("{0}.log", DateTime.Now.ToString("yyMMdd-HHmmss")));

            using (StreamWriter output = System.IO.File.AppendText(fileFullName))
            {
                output.WriteLine(text);
                output.Close();
            }
        }

        int i3 = 0;
        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫log的方法3\n";
            WriteLog2("寫log的方法3 " + (i3++).ToString());
        }

        public static void WriteLog2(string text)
        {
            string myPath = Application.StartupPath;
            string myName = "david_log";

            if (myPath == "" || myName == "")
                return;

            string Year = DateTime.Now.Year.ToString();
            string Month = DateTime.Now.Month.ToString().PadLeft(2, '0');
            string Day = DateTime.Now.Day.ToString().PadLeft(2, '0');

            //年月日文件夾是否存在，不存在則建立
            if (!Directory.Exists(myPath + "\\LogFiles\\" + Year + "_" + Month + "\\" + Year + "_" + Month + "_" + Day))
            {
                Directory.CreateDirectory(myPath + "\\LogFiles\\" + Year + "_" + Month + "\\" + Year + "_" + Month + "_" + Day);
            }

            //寫入日志UNDO,Exception has not been handle
            string LogFile = myPath + "\\LogFiles\\" + Year + "_" + Month + "\\" + Year + "_" + Month + "_" + Day + "\\" + myName;
            if (!File.Exists(LogFile))
            {
                System.IO.StreamWriter myFile;
                myFile = System.IO.File.AppendText(LogFile);
                myFile.Close();
            }

            while (true)
            {
                try
                {
                    StreamWriter sr = File.AppendText(LogFile);
                    sr.WriteLine(DateTime.Now.ToString("HH:mm:ss") + "  " + text);
                    sr.Close();
                    break;
                }
                catch (Exception e)
                {
                    System.Threading.Thread.Sleep(50);
                    continue;
                }
            }
        }

        /// <summary>
        /// 日志等级
        /// </summary>
        public enum FlashLogLevel
        {
            Debug,
            Info,
            Error,
            Warn,
            Fatal
        }


        /// <summary>
        /// 日志内容
        /// </summary>
        public class FlashLogMessage
        {
            public string Message { get; set; }
            public FlashLogLevel Level { get; set; }
            public Exception Exception { get; set; }

        }


        /// <summary>
        /// 记录消息Queue
        /// </summary>
        private ConcurrentQueue<FlashLogMessage> _que;

        /// <summary>
        /// 信号
        /// </summary>
        ManualResetEvent _mre;

        /// <summary>
        /// 日志
        /// </summary>
        //private readonly ILog _log;

        /// <summary>
        /// 日志
        /// </summary>
        //private static FlashLogger _flashLog = new FlashLogger();

        /*
        private FlashLogger()
        {
            var configFile = new FileInfo(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "log4net.config"));
            if (!configFile.Exists)
            {
                throw new Exception("未配置log4net配置文件！");
            }

            // 设置日志配置文件路径
            //XmlConfigurator.Configure(configFile);

            //_que = new ConcurrentQueue<FlashLogMessage>();
            //_mre = new ManualResetEvent(false);
            //_log = LogManager.GetLogger(System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);
        }
        */

        /*
        /// <summary>
        /// 实现单例
        /// </summary>
        /// <returns></returns>
        public static FlashLogger Instance()
        {
            return _flashLog;
        }
        */

        /// <summary>
        /// 另一个线程记录日志，只在程序初始化时调用一次
        /// </summary>
        public void Register()
        {
            Thread t = new Thread(new ThreadStart(WriteLog));
            t.IsBackground = false;
            t.Start();
        }

        /// <summary>
        /// 从队列中写日志至磁盘
        /// </summary>
        private void WriteLog()
        {
            while (true)
            {
                // 等待信号通知
                _mre.WaitOne();

                FlashLogMessage msg;
                // 判断是否有内容需要如磁盘 从列队中获取内容，并删除列队中的内容
                while (_que.Count > 0 && _que.TryDequeue(out msg))
                {
                    // 判断日志等级，然后写日志
                    switch (msg.Level)
                    {
                        case FlashLogLevel.Debug:
                            //_log.Debug(msg.Message, msg.Exception);
                            richTextBox1.Text += msg.Message + "\n";
                            break;
                        case FlashLogLevel.Info:
                            //_log.Info(msg.Message, msg.Exception);
                            richTextBox1.Text += msg.Message + "\n";
                            break;
                        case FlashLogLevel.Error:
                            //_log.Error(msg.Message, msg.Exception);
                            richTextBox1.Text += msg.Message + "\n";
                            break;
                        case FlashLogLevel.Warn:
                            //_log.Warn(msg.Message, msg.Exception);
                            richTextBox1.Text += msg.Message + "\n";
                            break;
                        case FlashLogLevel.Fatal:
                            //_log.Fatal(msg.Message, msg.Exception);
                            richTextBox1.Text += msg.Message + "\n";
                            break;
                    }
                }

                // 重新设置信号
                _mre.Reset();
                Thread.Sleep(1);
            }
        }


        /// <summary>
        /// 写日志
        /// </summary>
        /// <param name="message">日志文本</param>
        /// <param name="level">等级</param>
        /// <param name="ex">Exception</param>
        public void EnqueueMessage(string message, FlashLogLevel level, Exception ex = null)
        {
            _que.Enqueue(new FlashLogMessage
            {
                Message = "[" + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss,fff") + "]\r\n" + message,
                Level = level,
                Exception = ex
            });

            // 通知线程往磁盘中写日志
            _mre.Set();
        }

        public void Debug(string msg)
        {
            EnqueueMessage(msg, FlashLogLevel.Debug);
        }

        public void Error(string msg)
        {
            EnqueueMessage(msg, FlashLogLevel.Error);
        }

        public void Fatal(string msg)
        {
            EnqueueMessage(msg, FlashLogLevel.Fatal);
        }

        public void Info(string msg)
        {
            EnqueueMessage(msg, FlashLogLevel.Info);
        }

        public void Warn(string msg)
        {
            EnqueueMessage(msg, FlashLogLevel.Warn);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Debug("AAAAAAAA");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Error("BBBBBBBB");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Fatal("CCCCCCCC");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Info("DDDDDDDD");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Warn("EEEEEEEE");
        }

        int i4 = 0;
        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫log的方法4\n";
            LogConsole.Log("寫log的方法4 " + (i4++).ToString());
        }


        public List<string> Log = new List<string>();
        int iii = 0;
        private void AddLog(string logtext)
        {
            if (Log.Count < 1000)
                Log.Add(System.DateTime.Now.ToString() + "\t" + logtext);
            else if (Log.Count == 1000)
                Log.Add(System.DateTime.Now.ToString() + " 達到日志上限,不再追加");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //加入LOG
            iii++;
            AddLog("add log " + iii.ToString());
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //顯示LOG
            int len = Log.Count;
            if (len <= 0)
            {
                richTextBox1.Text += "無資料\n";
            }
            else
            {
                richTextBox1.Text += "共有 " + Log.Count.ToString() + " 筆資料, 分別是:\n";
                int i;
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += Log[i] + "\n";
                }
            }
        }

        int i5 = 0;
        private void button12_Click(object sender, EventArgs e)
        {
            LogAPI.WriteLog("寫log的方法5 " + (i5++).ToString());
        }

        int i6 = 0;
        private void button13_Click(object sender, EventArgs e)
        {
            Logger.WriteLog("寫log的方法6 " + (i6++).ToString());
        }
    }

    public class LogAPI
    {
        private static string myPath = "";
        private static string myName = "";

        /// 
        /// 初始化日志文件
        /// 

        /// 
        /// 
        public static void InitLogAPI(string logPath, string logName)
        {
            myPath = logPath;
            myName = logName;
        }

        /// 
        /// 寫入日志
        /// 

        /// 日志信息
        public static void WriteLog(string ex)
        {
            if (myPath == "" || myName == "")
                return;

            string Year = DateTime.Now.Year.ToString();
            string Month = DateTime.Now.Month.ToString().PadLeft(2, '0');
            string Day = DateTime.Now.Day.ToString().PadLeft(2, '0');

            //年月日文件夾是否存在，不存在則建立
            if (!Directory.Exists(myPath + "\\LogFiles\\" + Year + "_" + Month + "\\" + Year + "_" + Month + "_" + Day))
            {
                Directory.CreateDirectory(myPath + "\\LogFiles\\" + Year + "_" + Month + "\\" + Year + "_" + Month + "_" + Day);
            }

            //寫入日志UNDO,Exception has not been handle
            string LogFile = myPath + "\\LogFiles\\" + Year + "_" + Month + "\\" + Year + "_" + Month + "_" + Day + "\\" + myName;
            if (!File.Exists(LogFile))
            {
                System.IO.StreamWriter myFile;
                myFile = System.IO.File.AppendText(LogFile);
                myFile.Close();
            }

            while (true)
            {
                try
                {
                    StreamWriter sr = File.AppendText(LogFile);
                    sr.WriteLine(DateTime.Now.ToString("HH:mm:ss") + "  " + ex);
                    sr.Close();
                    break;
                }
                catch (Exception e)
                {
                    System.Threading.Thread.Sleep(50);
                    continue;
                }
            }
        }
    }

    public class LogConsole
    {
        static string logFileName = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "vcs_log.txt");

        public static void Log(string msg)
        {
            byte[] data = Encoding.UTF8.GetBytes(msg);

            FileStream fs = new FileStream(logFileName, FileMode.OpenOrCreate);
            fs.Position = fs.Length;
            StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);
            sw.WriteLine(string.Format("{0}-{1}", DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"), msg));
            sw.Flush();
            sw.Close();
            fs.Close();
        }
    }

    public class Logger
    {
        /// <summary>
        /// 寫入日志.
        /// </summary>
        /// <param name="strList">The STR list.</param>
        /// <remarks> </remarks>
        /// <Description></Description>
        //public static void WriteLog(string ex)
        public static void WriteLog(params object[] strList)
        {
            if (strList.Count() == 0) return;
            string strDicPath = "";
            string strPath = "";
            try
            {
                //LogFileName = Application.StartupPath + "\\log_" + DateTime.Now.ToString("yyyyMMdd") + ".txt";
                strDicPath = Application.StartupPath + "//";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日志記錄.txt";
            }
            catch (Exception e)
            {
                strDicPath = "C:/temp/log/";
                strPath = strDicPath + string.Format("{0:yyyy年-MM月-dd日}", DateTime.Now) + "日志記錄.txt";
            }

            if (!Directory.Exists(strDicPath)) Directory.CreateDirectory(strDicPath);
            if (!File.Exists(strPath)) using (FileStream fs = File.Create(strPath)) { }
            string str = File.ReadAllText(strPath);
            StringBuilder sb = new StringBuilder();
            foreach (var item in strList)
            {
                sb.Append("\r\n" + DateTime.Now.ToString() + "-----" + item + "");
            }
            File.WriteAllText(strPath, sb.ToString() + "\r\n-----z-----\r\n" + str);
        }
    }
}

