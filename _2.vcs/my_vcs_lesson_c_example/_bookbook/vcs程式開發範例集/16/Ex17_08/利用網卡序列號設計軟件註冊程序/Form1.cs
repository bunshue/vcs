using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;
using Microsoft.Win32;
namespace 利用網卡序列號設計軟件註冊程序
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string[] strLanCode = new string[12];// 網卡訊息儲存到
        string[] strkey ={ "Q", "W", "7", "E", "D", "F", "2", "G", "R", "T", "Y", "8", "P", "N", "B", "V", "C", "X", "Z", "0", "9", "I", "8", "6", "U", "O", "P", "M", "5", "4", "3", "1", "A", "S", "H", "J", "K", "L" };
        //產生註冊碼
        public int intRand = 0;//判斷隨機產生次數
        private void button1_Click(object sender, EventArgs e)
        {
            //把網卡訊息轉換成字串
            string strCode = GetNetCardMacAddress();//呼叫函數取得網卡訊息
            strCode = strCode.Substring(0, 2) + strCode.Substring(3, 2) + strCode.Substring(6, 2) + strCode.Substring(9, 2) + strCode.Substring(12, 2) +strCode.Substring(15, 2);
            string strb = strCode.Substring(0, 4) + strCode.Substring(4, 4) + strCode.Substring(8, 4);//把網卡訊息儲存到
            for (int i = 0; i < strLanCode.Length; i++)//把網卡訊息存入數組
            {
                strLanCode[i] = strb.Substring(i, 1);
            }
            Random ra = new Random();
            switch (intRand)//隨機產生註冊碼的順序
            {
                case 0:
                    label5.Text = strCode.Substring(0, 4) + "-" + strCode.Substring(4, 4) + "-" + strCode.Substring(8, 4) + "-" + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString();
                    intRand = 1;
                    break;
                case 1:
                    label5.Text = strCode.Substring(0, 4) + "-" + strCode.Substring(4, 4) + "-" + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + "-" + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString();
                    intRand = 2;
                    break;
                case 2:
                    label5.Text = strCode.Substring(0, 4) + "-" + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + "-" + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + "-" + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString();
                    intRand = 3;
                    break;
                case 3:
                    label5.Text = strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + "-" + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + "-" + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + strLanCode[ra.Next(0, 11)] + "-" + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString() + strkey[ra.Next(0, 37)].ToString();
                    intRand = 0;
                    break;
            }//
         
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label2.Text = Environment.MachineName.ToString();//得到計算機名
            label4.Text = GetNetCardMacAddress();//得到網卡訊息

        }
        //獲得網卡訊息函數
        public string GetNetCardMacAddress()
        { 	

           ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
           ManagementObjectCollection moc = mc.GetInstances();
            string str = "";
            foreach (ManagementObject mo in moc)
            {
                if ((bool)mo["IPEnabled"] == true)
                    str = mo["MacAddress"].ToString();
            }
            return str;
        }
        //註冊
        private void button2_Click(object sender, EventArgs e)
        {
            if (label5.Text == "")
            { MessageBox.Show("請產生註冊碼"); }
            else
            {
                string strNameKey = textBox1.Text.TrimEnd() + textBox2.Text.TrimEnd() + textBox3.Text.TrimEnd() + textBox4.Text.TrimEnd();
                string strNumber = label5.Text.Substring(0, 4) + label5.Text.Substring(5, 4) + label5.Text.Substring(10, 4) + label5.Text.Substring(15, 4);
                if (strNameKey == strNumber)
                {
                   // Microsoft.Win32.RegistryKey retkey1 = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software").OpenSubKey("ZHY").OpenSubKey("ZHY.INI", true);
                    Microsoft.Win32.RegistryKey retkey1 = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software", true).CreateSubKey("ZHY").CreateSubKey("ZHY.INI");
                    foreach (string strName in retkey1.GetSubKeyNames())//判斷註冊碼是否過期
                    {
                        if (strName == strNameKey)
                        {
                            MessageBox.Show("此註冊碼已經過期");
                            return;
                        }
                    }//開始註冊訊息
                    Microsoft.Win32.RegistryKey retkey = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software",true).CreateSubKey("ZHY").CreateSubKey("ZHY.INI").CreateSubKey(strNumber.TrimEnd());
                    retkey.SetValue("UserName", "明日科技");
                    MessageBox.Show("註冊成功!", "提示");
                    Application.Exit();
                }
                else
                { MessageBox.Show("註冊碼輸入錯誤"); }
            }
   
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void textBox1_KeyUp(object sender, KeyEventArgs e)
        {
            if (textBox1.Text.Length == 4)
            { textBox2.Focus();
            textBox2.SelectAll();
            e.Handled = true;
            }
        }

        private void textBox2_KeyUp(object sender, KeyEventArgs e)
        {
            if (textBox2.Text.Length == 4)
            {
                textBox3.Focus();
                textBox3.SelectAll();
                e.Handled = true;
            }
        }

        private void textBox3_KeyUp(object sender, KeyEventArgs e)
        {
            if (textBox3.Text.Length == 4)
            {
                textBox4.Focus();
                textBox4.SelectAll();
                e.Handled = true;
            }

        }

      
    }
}