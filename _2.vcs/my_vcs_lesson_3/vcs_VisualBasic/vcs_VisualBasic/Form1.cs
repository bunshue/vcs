using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//for Interaction,          //參考/加入參考/.NET/Microsoft.VisualBasic
using Microsoft.VisualBasic;    //for DateAndTime
using Microsoft.VisualBasic.Devices;    //for Computer
using System.Runtime.InteropServices;   //for DllImport, StructLayout
using System.Threading;

namespace vcs_VisualBasic
{
    public partial class Form1 : Form
    {
        //目標時間
        DateTime dt_target = Convert.ToDateTime(Convert.ToDateTime("2028-7-26 00:00:00"));

        Thread td;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            CheckForIllegalCrossThreadCalls = false;

            //for Interaction,          //參考/加入參考/.NET/Microsoft.VisualBasic
            string uName = Microsoft.VisualBasic.Interaction.InputBox("請輸入姓名", "程式啟動時，輸入資料");
            DialogResult dr = MessageBox.Show(uName + "歡迎您！", "歡迎", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            this.Text = uName;	//表單標題顯示姓名
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (td != null)
            {
                td.Abort();
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            richTextBox1.Size = new Size(400, 300);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(900, 750);
            this.Text = "vcs_VisualBasic";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }

        [DllImport("kernel32.dll")]
        private static extern int SetComputerName(string ipComputerName);//重寫API函數

        private void button0_Click(object sender, EventArgs e)
        {
            //取得並修改電腦名(偽執行)
            Computer computer = new Computer();//創建計算機對象
            richTextBox1.Text += "取得原計算機名 : " + computer.Name + "\n";

            richTextBox1.Text += "偽執行 計算機名稱修改, 須重啟計算機使之生效\n";
            //SetComputerName("lion-mouse");//修改計算機名稱

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

        private void button2_Click(object sender, EventArgs e)
        {

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

        //變量用于存儲年、月、日、時、分、秒
        public long LogYear, logMonth, logDay, logHour, logMinte, logSencon;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //參考/加入參考/.Net/Microsoft.VisualBasic
            Computer myComputer = new Computer();
            label0.Text = "物理內存總量（M）：" + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024);
            label1.Text = "可用物理內存（M）：" + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024);
            label2.Text = "虛擬內存總量（M）：" + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024);
            label3.Text = "可用虛擬內存（M）：" + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024);
            label4.Text = "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + " 秒";

            //6060

            //得到當前系統時間
            DateTime dt = DateTime.Now;
            string mesg = "目標時間距今 :\n";

            //計算相隔年數
            mesg += "相隔年數 : " + DateAndTime.DateDiff("yyyy", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + "\n";

            //計算相隔月數
            mesg += "相隔月數 : " + DateAndTime.DateDiff("m", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + "\n";

            //計算相隔天數
            mesg += "相隔天數 : " + DateAndTime.DateDiff("d", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + "\n";

            //計算相隔小時數
            mesg += "相隔小時數 : " + DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + "\n";

            //計算相隔分鐘數
            mesg += "相隔分鐘數 : " + DateAndTime.DateDiff("n", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + "\n";

            //計算相隔秒數
            mesg += "相隔秒數 : " + DateAndTime.DateDiff("s", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + "\n";

            //richTextBox1.Text = mesg;
            label_time.Text = mesg;
        }

        private void GetMemoryInfo()
        {
            Memory();
        }

        private void Memory()
        {
            Microsoft.VisualBasic.Devices.Computer myInfo = new Microsoft.VisualBasic.Devices.Computer();
            //获取物理内存总量
            pbMemorySum.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemorySum.Value = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            lblSum.Text = (myInfo.Info.TotalPhysicalMemory / 1024).ToString();
            //获取可用物理内存总量
            pbMemoryUse.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemoryUse.Value = Convert.ToInt32(myInfo.Info.AvailablePhysicalMemory / 1024 / 1024);
            lblMuse.Text = (myInfo.Info.AvailablePhysicalMemory / 1024).ToString();
            //获取虚拟内存总量
            pbVmemorysum.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemorysum.Value = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            lblVinfo.Text = (myInfo.Info.TotalVirtualMemory / 1024).ToString();
            //获取可用虚拟内存总量
            pbVmemoryuse.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemoryuse.Value = Convert.ToInt32(myInfo.Info.AvailableVirtualMemory / 1024 / 1024);
            lblVuse.Text = (myInfo.Info.AvailableVirtualMemory / 1024).ToString();
        }

        private void timer_memory_Tick(object sender, EventArgs e)
        {
            //使用Computer()讀得記憶體狀態

            //1. 參考 -> 加入參考 -> .NET/Microsoft.VisualBasic
            //2. using Microsoft.VisualBasic.Devices;

            Computer myComputer = new Computer();
            /*
            //Bytes
            label1.Text = "物理內存總量(B)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory);
            label2.Text = "可用物理內存(B)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory);
            label3.Text = "虛擬內存總量(B)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory);
            label4.Text = "可用虛擬內存(B)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory);

            //MB
            label1.Text = "物理內存總量(MB)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024) + " MB";
            label2.Text = "可用物理內存(MB)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024) + " MB";
            label3.Text = "虛擬內存總量(MB)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024) + " MB";
            label4.Text = "可用虛擬內存(MB)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024) + " MB";
            */
            //------------------------------------------------------------  # 60個

            //GetMemoryInfo();
            td = new Thread(new ThreadStart(GetMemoryInfo));
            td.Start();

        }
    }
}
