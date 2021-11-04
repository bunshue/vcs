using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;

//WMI是Windows Management Instrumentation的簡稱，即：視窗管理規范。

namespace system_test3_wmi
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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲取主板序列號
            string sn = GetBIOSNumber();
            richTextBox1.Text += "主板序列號:\t" + sn + "\n";
        }

        private static string GetBIOSNumber()
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select SerialNumber From Win32_BIOS");
            string biosNumber = string.Empty;
            foreach (ManagementObject mgt in searcher.Get())
            {
                biosNumber += mgt["SerialNumber"].ToString();
            }
            return biosNumber;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //獲得CPU的編號
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += mo["processorid"].ToString() + "\n";   //取得CPU編號
                richTextBox1.Text += "cpu info:\t" + mo.Properties["ProcessorId"].Value.ToString() + "\n";
            }

            ManagementObjectSearcher mos = new ManagementObjectSearcher("Select * From Win32_Processor"); //查詢CPU訊息
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += mo["Manufacturer"].ToString() + "\n";//取得CPU製造商名稱
                richTextBox1.Text += mo["Version"].ToString() + "\n";     //取得CPU版本號 
                richTextBox1.Text += mo["Name"].ToString() + "\n";        //取得CPU產品名稱
            }

            richTextBox1.Text += "\ncall Processor() ST\n";
            Processor();
            richTextBox1.Text += "call Processor() SP\n";

            richTextBox1.Text +="\n獲取CPU的序列號\n";
            string result = GetCpuID();
            richTextBox1.Text += result + "\n";


        }

        //C# 獲得處理器參數程序代碼
        //public void Processor(out string[] Manufacturer, out string[] ID, out string[] ProcessorId)
        public void Processor()
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            string[] Manufacturer = new string[searcher.Get().Count];
            string[] ID = new string[searcher.Get().Count];
            string[] ProcessorId = new string[searcher.Get().Count];
            richTextBox1.Text += "count = " + searcher.Get().Count.ToString() + "\n";
            int i = 0;
            foreach (ManagementObject share in searcher.Get())
            {
                try
                {
                    Manufacturer[i] = share.GetPropertyValue("Manufacturer").ToString();
                    //ID[i] = share.GetPropertyValue("Id").ToString(); not known
                    ProcessorId[i] = share.GetPropertyValue("ProcessorId").ToString();

                    richTextBox1.Text += "i = " + i.ToString() + "\n";
                    richTextBox1.Text += "Manufacturer : " + Manufacturer[i] + "\n";
                    richTextBox1.Text += "ProcessorId : " + ProcessorId[i] + "\n";
                    
                }
                catch (System.Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }

        //獲取CPU的序列號
        private string GetCpuID()
        {
            try
            {
                //獲取CPU序列號代碼
                string cpuInfo = "";//cpu序列號
                ManagementClass mc = new ManagementClass("Win32_Processor");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                }
                moc = null;
                mc = null;
                return cpuInfo;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //C#讀取計算機CPU信息
        public string getCpuInfo() //讀取CPU信息
        {
            //獲得CPU訊息
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                return mo.Properties["ProcessorId"].Value.ToString();   //取得CPU編號
                //return mo["ProcessorId"].ToString();   //取得CPU編號  same
            }
            return "";
        }

        //C#讀取計算機HDD信息
        public string getHddInfo() //讀取硬盤信息
        {
            ManagementClass mc = new ManagementClass("Win32_PhysicalMedia");
            ManagementObjectCollection moc = mc.GetInstances();
            foreach (ManagementObject mo in moc)
            {
                return mo.Properties["SerialNumber"].Value.ToString();
            }
            return "";
        }


        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "CPU信息: \t" + getCpuInfo() + "\n";
            richTextBox1.Text += "HDD信息: \t" + getHddInfo() + "\n";
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
    }
}
