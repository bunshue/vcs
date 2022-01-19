using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//C#中調用命令行cmd開啟wifi熱點的實例代碼

/*
要點1：cmd命令行的輸入命令
netsh wlan set hostednetwork mode=allow ssid=用戶名  key=密碼
netsh wlan start hostednetwork
netsh waln stop hostednetwork
netsh interface ip set address name="本地連接" source=dhcp

要點2：在C#中調用cmd.exe命令行

    */

namespace WindowsFormsApplication0119a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //“創建wifi熱點”按鈕
        private void button1_Click(object sender, EventArgs e)
        {
            string str;
            string userName = textBox1.Text;
            string password = textBox2.Text;
            if (password.Length >= 8 && userName != null)
            {
                // 命令行輸入命令，用來新建wifi
                str = "netsh wlan set hostednetwork mode=allow ssid=" + userName + " key=" + password;
                create(str);
                MessageBox.Show("新建了wifi熱點",
                    "新建成功",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Information);
                label4.Text = "新建了wifi熱點";
            }
            else
            {
                MessageBox.Show("你的賬號為空或你的密碼長度小於8",
                    "登陸失敗",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation);
            }
        }
        //"開啟wifi"按鈕
        private void button2_Click(object sender, EventArgs e)
        {
            // 命令行輸入命令，
            string str = "netsh wlan start hostednetwork";
            create(str);
            label4.Text = "已啟動wifi熱點";
        }
        //“關閉wifi”按鈕
        private void button3_Click(object sender, EventArgs e)
        {
            // 命令行輸入命令，
            string str = "netsh wlan stop hostednetwork";
            create(str);
            label4.Text = "已關閉wifi熱點";
        }
        //在cmd控制台輸入命令，
        private void create(string str)
        {
            //process用於調用外部程序
            System.Diagnostics.Process p = new System.Diagnostics.Process();
            //調用cmd.exe
            p.StartInfo.FileName = "cmd.exe";
            //是否指定操作系統外殼進程啟動程序
            p.StartInfo.UseShellExecute = false;
            //可能接受來自調用程序的輸入信息
            //重定向標准輸入
            p.StartInfo.RedirectStandardInput = true;
            //重定向標准輸出
            p.StartInfo.RedirectStandardOutput = true;
            //重定向錯誤輸出
            p.StartInfo.RedirectStandardError = true;
            //不顯示程序窗口
            p.StartInfo.CreateNoWindow = true;
            //啟動程序
            p.Start();
            //睡眠1s。
            System.Threading.Thread.Sleep(1000);
            //輸入命令
            p.StandardInput.WriteLine(str);
            //一定要關閉。
            p.StandardInput.WriteLine("exit");
        }
        //自動IP連接 按鈕
        private void button4_Click(object sender, EventArgs e)
        {
            // 命令行輸入命令，用來自動連接wifi：netsh interface ip set address name="本地連接" source=dhcp
            string str = "netsh interface ip set address name=\"本地連接\" source=dhcp";
            string str1 = "銳捷是否提示你設置自動獲取IP\n" + "或你想自動獲取IP，請按確定";
            DialogResult result = MessageBox.Show(str1, "自動連接IP",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Information);
            if (result == DialogResult.OK)
            {
                create(str);
                label4.Text = "銳捷自動獲取IP";
            }
        }
    }
}


