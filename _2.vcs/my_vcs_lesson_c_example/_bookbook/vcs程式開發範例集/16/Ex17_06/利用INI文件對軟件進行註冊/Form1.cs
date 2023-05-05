using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;
namespace 利用INI文件對軟件進行註冊
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            FileStream c = new FileStream(@"C:\_git\vcs\_1.data\______test_files1\desck.ini", FileMode.OpenOrCreate, FileAccess.Write);
            
        }
        //*********************
        //C＃申明INI文件的寫操作函數WritePrivateProfileString（）： 
        [ DllImport ( "kernel32" ) ]
        private static extern long WritePrivateProfileString ( string section ,string key , string val , string filePath ) ;
        //參數說明：section：INI文件中的段落；key：INI文件中的關鍵字；val：INI文件中關鍵字的數值；filePath：INI文件的完整的路徑和名稱。
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);
       // //參數說明：section：INI文件中的段落名稱；key：INI文件中的關鍵字；def：無法讀取時候時候的缺省數值；retVal：讀取數值；size：數值的大小；filePath：INI文件的完整路徑和名稱。
        private void button1_Click(object sender, EventArgs e)
        {
            StringBuilder temp = new StringBuilder(200);
            string FileName = "C:\\desck.ini";//NI文件的完整的路徑和名稱。
            foreach (object ct in Controls)
            {
                if (ct.GetType().ToString() == "System.Windows.Forms.TextBox")
                {
                    TextBox tx = (TextBox)ct;
                    if (tx.Text == "")
                    {
                        MessageBox.Show(tx.Tag.ToString()+"不能為空");
                    }//
                }//
            }//
            string section = textBox3.Text;//INI文件中的段落
            string key = textBox1.Text;//INI文件中的關鍵字
            string keyValue = textBox2.Text;//INI文件中的關鍵字
            int i = GetPrivateProfileString(section, key, "無法讀取對應數值！", temp, 200, FileName);//判斷是否註冊過
            if (temp.ToString() == "無法讀取對應數值！")
            {
                WritePrivateProfileString(section, key, keyValue, FileName);
                MessageBox.Show("註冊成功寫入INI文件！", "訊息");
            }
            else
            {
                MessageBox.Show("此訊息已註冊過了");
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
       


    }
}
