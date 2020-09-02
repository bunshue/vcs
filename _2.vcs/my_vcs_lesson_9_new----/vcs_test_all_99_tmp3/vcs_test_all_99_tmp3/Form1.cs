using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Timers;    //for ElapsedEventHandler

namespace vcs_test_all_99_tmp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
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
            string Username;
            string Password;
            Username = textBox1.Text;	//取得textBox1的內容為名字
            Password = textBox2.Text;	//取得textBox2的內容為密碼
            if (Username == "root" && Password == "123456")
                MessageBox.Show("您是合法的使用者！！");
            else
                MessageBox.Show("滾蛋！！！！");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            textBox2.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.AcceptButton = button5;            //在表單按enter就執行button1按鈕的動作
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            int i = 0;
            while (i < 1000)
            {
                textBox3.Text = i.ToString();
                Application.DoEvents();         //執行某一事件，以達到延遲效果。
                for (int j = 0; j < 200; j++)
                    System.Threading.Thread.Sleep(1);
                i++;
            }
        }

        //開啟關閉thread    ST
        System.Timers.Timer t = new System.Timers.Timer(1234);
        int number = 0;

        private void button_start_thread_Click(object sender, EventArgs e)
        {
            t.Elapsed += new ElapsedEventHandler(run);
            t.Enabled = true;
        }

        private void button_stop_thread_Click(object sender, EventArgs e)
        {
            t.Enabled = false;
            number = 0;
        }
        public void run(object source, System.Timers.ElapsedEventArgs e)
        {
            number++;
            MessageBox.Show("number = " + number);
        }
        //開啟關閉thread    SP

        private void button14_Click(object sender, EventArgs e)
        {
            for(int i=0;i<=100;i++)
            {
                label13.Text = "讀取進度： " + i + "%";
                progressBar1.Value = i;
                Application.DoEvents();         //執行某一事件，以達到延遲效果。
                for (int j = 0; j < 100; j++)
                    System.Threading.Thread.Sleep(1);
            }
            label13.Text += "   讀取完成";
        }

        int progress = 0;

        private void button15_Click(object sender, EventArgs e)
        {
            timer3.Enabled = true;
            progress = 0;
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            progress++;
            label13.Text = "讀取進度： " + progress + "%";
            progressBar1.Value = progress;
            if (progress >= 100)
            {
                timer3.Enabled = false;
                label13.Text += "   讀取完成";
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            progress = 0;
            timer3.Enabled = false;
            progressBar1.Value = progress;
            label13.Text = "讀取進度： ";
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {

        }
    
    }
}
