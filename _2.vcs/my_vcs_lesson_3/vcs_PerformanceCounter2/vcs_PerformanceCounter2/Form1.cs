using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Diagnostics;       //for Process, PerformanceCounter

//CPU 與記憶體使用率

namespace vcs_PerformanceCounter2
{
    public partial class Form1 : Form
    {
        static PerformanceCounter cpu = new PerformanceCounter("Processor", "% Processor Time", "_Total");
        static PerformanceCounter memory = new PerformanceCounter("Memory", "% Committed Bytes in Use");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //PerformanceCounter pc = new PerformanceCounter(); 若未給參數 要在使用時給參數
            //PerformanceCounter pc = new PerformanceCounter("Processor", "% Processor Time", "_Total");


            PerformanceCounter pc = new PerformanceCounter();   //若未給參數 要在使用時給參數
            //static PerformanceCounter pc = new PerformanceCounter("Processor", "% Processor Time", "_Total");

            pc = new PerformanceCounter("Processor", "% Processor Time", "_Total");



        }

        private void button1_Click(object sender, EventArgs e)
        {

            //CPU 與記憶體使用率
            //建一個 PerformanceCounter 物件，指定分類、計數器名稱、執行個體，接著用 NextValue() 取值，輕鬆搞定。
            Console.WriteLine("CPU: {0:n1}%", cpu.NextValue());
            Console.WriteLine("Memory: {0:n0}%", memory.NextValue());

            richTextBox1.Text += "CPU: " + cpu.NextValue() + "\n";
            richTextBox1.Text += "Memory: " + memory.NextValue() + "\n";



        }

        //C＃實時獲取CPU利用率
        // constants used to select the performance counter.
        private const string CategoryName = "Processor";
        private const string CounterName = "% Processor Time";
        private const string InstanceName = "_Total";

        private static void Say(string txt)
        {
            Console.WriteLine(txt);
        }

        private static void Say()
        {
            Say("");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //C＃實時獲取CPU利用率
            Say("$Id: CpuLoadInfo.cs,v 1.2 2002/08/17 17:45:48 rz65 Exp $");
            Say();

            Say("Attempt to create a PerformanceCounter instance:");
            Say("Category name = " + CategoryName);
            Say("Counter name = " + CounterName);
            Say("Instance name = " + InstanceName);
            PerformanceCounter pc
            = new PerformanceCounter(CategoryName, CounterName, InstanceName);
            Say("Performance counter was created.");
            Say("Property CounterType: " + pc.CounterType);
            Say();

            Say("Property CounterHelp: " + pc.CounterHelp);
            Say();
            Say("Entering measurement loop.");

            while (true)
            {
                Thread.Sleep(1000); // wait for 1 second
                float cpuLoad = pc.NextValue();
                Say("CPU load = " + cpuLoad + " %.");
            }

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

        private void timer1_Tick(object sender, EventArgs e)
        {
            //double cpu_usage = pc.NextValue();
            //label5.Text = "CPU使用率 " + cpu_usage.ToString() + " %";
            //richTextBox1.Text += "CPU使用率 " + cpu_usage.ToString() + " %\n";




            // CPU 與記憶體使用率
            Console.WriteLine("CPU: {0:n1}%", cpu.NextValue());
            Console.WriteLine("Memory: {0:n0}%", memory.NextValue());

            richTextBox1.Text += "CPU: " + cpu.NextValue() + " %\n";
            richTextBox1.Text += "Memory: " + memory.NextValue() + " %\n";




            //double cpu_usage = pc.NextValue();
            //label5.Text = "CPU使用率 " + cpu_usage.ToString() + " %";
            //richTextBox1.Text += "CPU使用率 " + cpu_usage.ToString() + " %\n";

            /*
            pc.CategoryName = "Processor";
            pc.CounterName = "% Processor Time";
            pc.InstanceName = "_Total";
            */





        }
    }
}
