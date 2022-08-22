using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for Process

namespace vcs_Process_Start
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
            y_st = 22;
            dx = 170;
            dy = 62;

            groupBox1.Location = new Point(10, 10);
            groupBox2.Location = new Point(10 + dx * 3+40, 10);
            groupBox3.Location = new Point(10 + dx * 4+100, 10);
            richTextBox1.Location = new Point(10 + dx * 5 + 160, 10);


            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 0, y_st + dy * 9);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //開啟小算盤應用程式
            //Process.Start(@"C:\WINDOWS\system32\calc.exe");   same
            Process.Start("calc");  //打開計算機
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟記事本程式
            //Process.Start("notepad.exe"); //same
            Process.Start("notepad");   //打開記事本
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Process.Start("EXCEL.exe");  //啟動Excel
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Process.Start("Firefox.exe");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Process.Start("dvdplay.exe");	//啟動Windows Media Player
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //打開Windows版本信息
            Process.Start("winver.exe ");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //開啟imsLink
            Process.Start(@"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //打開D槽
            Process.Start("d:");
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //開啟特定程式 1
            Process.Start(@"C:\___small\imagesweeper5.1影像清潔工.exe");
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Process.Start("cmd.exe");
        }

        private void button12_Click(object sender, EventArgs e)
        {
            Process.Start("regedit.exe");
        }

        private void button13_Click(object sender, EventArgs e)
        {
            Process.Start("mspaint.exe");
        }

        private void button14_Click(object sender, EventArgs e)
        {
            Process.Start("write.exe");
        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //開啟IE, 指名網址
            //Process.Start("IExplore.exe", "www.google.com.tw");   //same
            Process.Start("iexplore.exe", "www.google.com.tw");
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //開啟FireFox, 指名網址
            Process.Start("Firefox.exe", "www.google.com.tw");
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //用Adobe開啟pdf檔案
            string filename = "C:\\______test_files\\__RW\\_pdf\\note_Linux_workstation.pdf";
            Process process;
            process = Process.Start(filename);

            process.WaitForExit();  //需等開啟的程式結束後才可以回到表單
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //開啟記事本, 指名檔案

            //啟動一個外部程序

            ////////////聲明一個程序信息類，指定啟動進程是的參數信息     
            ProcessStartInfo Info = new ProcessStartInfo();

            //設置外部程序名
            Info.FileName = "notepad.exe";
            //設置外部程序的啟動參數（命令行參數）為test.txt
            Info.Arguments = "file_to_save.txt";
            //設置外部程序工作目錄為  C:\
            Info.WorkingDirectory = @"C:\______test_files";
            ///////////聲明一個程序類,也就是創建一個進程
            Process Proc;
            try
            {
                //     //啟動外部程序
                Proc = Process.Start(Info);
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。\r{0}", ex);
                return;
            }
            //打印出外部程序的開始執行時間
            Console.WriteLine("外部程序的開始執行時間：{0}", Proc.StartTime);
            //等待3秒鐘
            Proc.WaitForExit(3000);

            //如果這個外部程序沒有結束運行則對其強行終止
            if (Proc.HasExited == false)
            {
                Console.WriteLine("由主程序強行終止外部程序的運行！");
                Proc.Kill();
            }
            else
            {
                Console.WriteLine("由外部程序正常退出！");
            }
            Console.WriteLine("外部程序的結束運行時間：{0}", Proc.ExitTime);
            Console.WriteLine("外部程序在結束運行時的返回值：{0}", Proc.ExitCode);
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //檔案總管 C槽
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //資源管理器
            processStartInfo.Arguments = @"C:\";
            Process.Start(processStartInfo);
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //檔案總管 C槽
            //開啟檔案總管
            String pathname = "C:\\";
            Process.Start(pathname);
            /*
            if (Directory.Exists(this.FolderPath))
            {
                Process.Start(this.FolderPath);
                return true;
            }
            else
                return false;
             */
        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void button40_Click(object sender, EventArgs e)
        {
            //開啟Notepad程序
            process1.StartInfo.FileName = "notepad.exe";
            process1.Start();


        }

        private void button41_Click(object sender, EventArgs e)
        {
            //關閉Notepad程序
            Process[] myProcesses;
            myProcesses = Process.GetProcessesByName("Notepad");
            foreach (Process instance in myProcesses)
            {
                instance.CloseMainWindow();
                instance.WaitForExit(3000);
                instance.Close();
            }

        }
    }
}

