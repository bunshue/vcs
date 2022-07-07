using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//for Interaction,          //參考/加入參考/.NET/Microsoft.VisualBasic
using Microsoft.VisualBasic.Devices;    //for Computer

namespace vcs_VisualBasic
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

        private void button1_Click(object sender, EventArgs e)
        {
            //VisualBasic 使用範例

            string i;   //記錄使用者輸入的資料
            double num; //使用者輸入資料轉成double的值
            i = Microsoft.VisualBasic.Interaction.InputBox
                ("請輸入數值：", "求平方");
            num = Convert.ToDouble(i); //將使用者輸入的資料轉成double
            MessageBox.Show(i + "的平方等於" + (num * num).ToString() + "\n", "平方");

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //參考/加入參考/.Net/Microsoft.VisualBasic
            Computer myComputer = new Computer();
            label0.Text = "物理內存總量（M）：" + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024);
            label1.Text = "可用物理內存（M）：" + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024);
            label2.Text = "虛擬內存總量（M）：" + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024);
            label3.Text = "可用虛擬內存（M）：" + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024);
            label4.Text = "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + " 秒";

        }
    }
}


