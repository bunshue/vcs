using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using log4net;
//1. 參考/加入參考/log4net.dll
//2. 要使用.Net Framework 4

namespace vcs_Log4net
{
    public partial class Form1 : Form
    {
        //private ILog log = LogManager.GetLogger(typeof(Form1));   //也可
        private ILog log = LogManager.GetLogger("MyLogger");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取log4net的設定, 也可把設定寫在app.config裏
            string log4netPath = "log4net.config";
            log4net.Config.XmlConfigurator.ConfigureAndWatch(new System.IO.FileInfo(log4netPath));
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫一些log.....\n";
            log.Debug("Debug訊息 AAAA");
            log.Info("Info 訊息 BBBB");
            log.Warn("Warn 訊息 CCCC");
            log.Error("Error訊息 DDDD");
            log.Fatal("Fatal訊息 EEEE");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "用另一個Logger寫一些log.....\n";
            ILog log = LogManager.GetLogger("另一個Logger");
            log.Debug("Debug訊息 aaaa");
            log.Info("Info 訊息 bbbb");
            log.Warn("Warn 訊息 cccc");
            log.Error("Error訊息 dddd");
            log.Fatal("Fatal訊息 eeee");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "aaaa " + log.Logger.Name + "\n";
            richTextBox1.Text += "aaaa " + log.Logger.Name + "\n";
            richTextBox1.Text += "aaaa " + log.Logger.Name + "\n";


        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}
