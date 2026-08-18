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
            show_item_location();

            //------------------------------------------------------------  # 60個

            //讀取log4net的設定, 也可把設定寫在app.config裏
            string log4netPath = "log4net.config";
            log4net.Config.XmlConfigurator.ConfigureAndWatch(new System.IO.FileInfo(log4netPath));
        }

        void show_item_location()
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

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(740, 750);
            this.Text = "vcs_Log4net";

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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

