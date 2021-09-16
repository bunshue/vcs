using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;

namespace HideVoiceDevice
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

        private void hide_Click(object sender, EventArgs e)
        {
            RegistryKey VoiceKey = Registry.CurrentUser;//實例化一個表示Windows項級節點的對象
            VoiceKey = VoiceKey.CreateSubKey("Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer");//建立一個新的子項
            VoiceKey.SetValue("Disallowcpl", 1);//設定指定的名稱/值對
            VoiceKey = VoiceKey.CreateSubKey("Disallowcpl");//打開一個現有子項進行存取
            VoiceKey.SetValue("2", "mmsys.cpl");//設定指定的名稱/值對
            VoiceKey.Close();//關閉該項
            MessageBox.Show("隱藏控制面板中的聲音設備成功，請重啟計算機檢視結果", "訊息提示", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出訊息提示
        }

        private void exit_Click(object sender, EventArgs e)
        {
            Application.Exit();//退出運用程序
        }
    }
}
