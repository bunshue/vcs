using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;
namespace 利用註冊表設計軟件註冊程序
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //註冊
        private void button1_Click(object sender, EventArgs e)
        {
            if(textBox1.Text=="")
            {
                MessageBox.Show("公司名稱不能為空"); return;
           
            }
                if(textBox2.Text=="")
                { MessageBox.Show("使用者名稱不能為空"); return; }
                if (textBox3.Text == "")
                { MessageBox.Show("註冊碼不能為空"); return; }
                //實例RegistryKey 類對像
           // Microsoft.Win32.RegistryKey retkey1 = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software").OpenSubKey("ZHY").OpenSubKey("ZHY.INI", true);
                Microsoft.Win32.RegistryKey retkey1 = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software", true).CreateSubKey("ZHY").CreateSubKey("ZHY.INI");
            foreach (string strName in retkey1.GetSubKeyNames())//判斷註冊碼是否過期
            {
                if (strName == textBox3.Text)
                {
                    MessageBox.Show("此註冊碼已經過期");
                    return;
                }
            }//開始註冊訊息
            Microsoft.Win32.RegistryKey retkey = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software", true).CreateSubKey("ZHY").CreateSubKey("ZHY.INI").CreateSubKey(textBox3.Text.TrimEnd());
            retkey.SetValue("UserName", textBox2.Text);
            retkey.SetValue("capataz", textBox1.Text);
            retkey.SetValue("Code", textBox3.Text);
            MessageBox.Show("註冊成功，您可以使用本軟件");
            Application.Exit();
    

        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
          
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}