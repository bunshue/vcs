using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;
using System.Management;

namespace 根據cpu序列號_磁盤序列號設計軟件註冊程序
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

        // 取得設備硬盤的卷標號
        public string GetDiskVolumeSerialNumber()
        {
            ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObject disk = new ManagementObject("win32_logicaldisk.deviceid=\"d:\"");
            disk.Get();
            return disk.GetPropertyValue("VolumeSerialNumber").ToString();
        }

        //獲得CPU的序列號
        public string getCpu()
        {
            string strCpu = null;
            ManagementClass myCpu = new ManagementClass("win32_Processor");
            ManagementObjectCollection myCpuConnection = myCpu.GetInstances();
            foreach (ManagementObject myObject in myCpuConnection)
            {
                strCpu = myObject.Properties["Processorid"].Value.ToString();
                break;
            }
            return strCpu;
        }

        //產生機器碼
        private void button1_Click(object sender, EventArgs e)
        {
            label2.Text = getCpu() + GetDiskVolumeSerialNumber();//獲得24位Cpu和硬盤序列號

            richTextBox1.Text += "CPU : " + getCpu() + "\n";
            richTextBox1.Text += "HDD : " + GetDiskVolumeSerialNumber() + "\n";


            string[] strid = new string[24];//
            for (int i = 0; i < 24; i++)//把字符賦給數組
            {
                strid[i] = label2.Text.Substring(i, 1);
            }

            label2.Text = "";
            Random rdid = new Random();
            for (int i = 0; i < 24; i++)//從數組隨機抽取24個字符組成新的字符產生機器三
            {
                label2.Text += strid[rdid.Next(0, 24)];
            }

            richTextBox1.Text += "strid : " + label2.Text + "\n";
        }

        public int[] intCode = new int[127];//用於存密鑰
        public void setIntCode()//給數組賦值個小於10的隨機數
        {
            Random ra = new Random();
            for (int i = 1; i < intCode.Length; i++)
            {
                intCode[i] = ra.Next(0, 9);
            }
        }
        public int[] intNumber = new int[25];//用於存機器碼的Ascii值
        public char[] Charcode = new char[25];//儲存機器碼字

        //產生註冊碼
        private void button2_Click(object sender, EventArgs e)
        {
            if (label2.Text != "")
            {
                //把機器碼存入數組中
                setIntCode();//初始化127位數組
                for (int i = 1; i < Charcode.Length; i++)//把機器碼存入數組中
                {
                    Charcode[i] = Convert.ToChar(label2.Text.Substring(i - 1, 1));
                }//
                for (int j = 1; j < intNumber.Length; j++)//把字符的ASCII值存入一個整數組中。
                {
                    intNumber[j] = intCode[Convert.ToInt32(Charcode[j])] + Convert.ToInt32(Charcode[j]);

                }
                string strAsciiName = null;//用於儲存機器碼
                for (int j = 1; j < intNumber.Length; j++)
                {
                    //MessageBox.Show((Convert.ToChar(intNumber[j])).ToString());
                    if (intNumber[j] >= 48 && intNumber[j] <= 57)//判斷字符ASCII值是否0－9之間
                    {
                        strAsciiName += Convert.ToChar(intNumber[j]).ToString();
                    }
                    else if (intNumber[j] >= 65 && intNumber[j] <= 90)//判斷字符ASCII值是否A－Z之間
                    {
                        strAsciiName += Convert.ToChar(intNumber[j]).ToString();
                    }
                    else if (intNumber[j] >= 97 && intNumber[j] <= 122)//判斷字符ASCII值是否a－z之間
                    {
                        strAsciiName += Convert.ToChar(intNumber[j]).ToString();
                    }
                    else//判斷字符ASCII值不在以上範圍內
                    {
                        if (intNumber[j] > 122)//判斷字符ASCII值是否大於z
                        { strAsciiName += Convert.ToChar(intNumber[j] - 10).ToString(); }
                        else
                        {
                            strAsciiName += Convert.ToChar(intNumber[j] - 9).ToString();
                        }

                    }
                    label3.Text = strAsciiName;//得到註冊碼
                    richTextBox1.Text += "得到註冊碼 : " + strAsciiName + "\n";

                }
            }
            else
            {
                MessageBox.Show("請選產生機器碼", "註冊提示");
            }
        }

        //註冊
        private void button3_Click(object sender, EventArgs e)
        {
            if (label3.Text != "")
            {
                if (textBox1.Text.TrimEnd().Equals(label3.Text.TrimEnd()))
                {
                    /*
                    Microsoft.Win32.RegistryKey retkey = Microsoft.Win32.Registry.CurrentUser.OpenSubKey("software", true).CreateSubKey("ZHY").CreateSubKey("ZHY.INI").CreateSubKey(textBox1.Text.TrimEnd());
                    retkey.SetValue("UserName", "明日科技");
                    */

                    richTextBox1.Text += "偽執行\n";

                    MessageBox.Show("註冊成功");
                }
                else
                {
                    MessageBox.Show("註冊碼輸入錯誤");

                }

            }
            else { MessageBox.Show("請產生註冊碼", "註冊提示"); }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}

