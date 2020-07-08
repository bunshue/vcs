using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization;

using System.Threading;


using System.IO;

namespace WindowsFormsApplication1
{
    //創建SetValue的委托
    public delegate void SetValueDel(string str, object obj);

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            Thread.CurrentThread.Name = "MainThread";
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
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

        //開啟一個線程
        private void button5_Click(object sender, EventArgs e)
        {

            //將委托的方法和主窗體傳過去
            NEWThreadClass threadOneClass = new NEWThreadClass(SetValue, this);

            Thread TheThreadOne = new Thread(threadOneClass.threadOne);//不需要ThreadStart()也可以

            TheThreadOne.Name = "在 " + DateTime.Now.ToString() + " 創建的線程";//給線程命名，方便調試。這行代碼可以省略。

            //讓線程變為後台線程（默認是前台的），這樣主線程結束了，這個線程也會結束。要不然，任何前台線程在運行都會保持程序存活。
            TheThreadOne.IsBackground = true;
            TheThreadOne.Start();
        }

        //給文本框賦值
        private void SetValue(string str, object obj)
        {
            //lock裡面的代碼同一個時刻，只能被一個線程使用。其它的後面排隊。這樣防止數據混亂。
            lock (obj)
            {
                richTextBox1.Text += str + " 到此一遊\n";
                //this.txtReturnValue.Text = this.txtReturnValue.Text + str;
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int c = 0; // 定義此變量主要是來判斷目錄中是否有文件
            foreach (string s1 in Directory.GetFiles("c:\\______test_files.old")) // 返回文件名稱字符串行時的枚舉類型
            {
                ++c;
                richTextBox1.Text += "find file " + s1 + "\n";
            }

            /*
            if (c > 0) //判斷是否存在文件如果 c > 0則回收站有文件，反之則沒有
            {
                DialogResult r = MessageBox.Show("是否確定？", "垃圾處理！",
                        MessageBoxButtons.YesNo, MessageBoxIcon.Question);
                // 顯示"確定"和"取消"二個按鈕，圖標顯示是一個問號。
                int ss = (int)r;
                if (ss == 6) // 按動確定按鈕
                {
                    foreach (string s in Directory.GetFiles("c:\recycled"))
                    // 把全路徑名稱房子 s中
                    {
                        //File.Delete(s); //刪除此文件
                    }
                }
            }
            */

        }











    }


    //建一個類，模擬實際使用情況
    public class NEWThreadClass
    {
        //接收主窗體傳過來的委托方法。
        public SetValueDel setValueDel;

        //接收主窗體
        public Form form;

        //用於告訴主線程中鎖，是哪一個線程調用的。
        static object locker = new object();

        public NEWThreadClass(SetValueDel del, Form fom)
        {
            this.setValueDel = del;
            this.form = fom;
        }
        //第一個線程,給主線程創建的控件傳值。
        public void threadOne()
        {
            //這裡獲取線程的名字
            string threadName = Thread.CurrentThread.Name;
            try
            {
                while (true)
                {
                    //告訴主線程，我要更改你的控件了。
                    this.form.Invoke((EventHandler)(delegate
                    {
                        //如果在這裡使用Thread.CurrentThread.Name 獲取到的是主線程的名字。
                        setValueDel(threadName + " :Hello!", locker);//給文本框傳值，“自己的名字：Hello!”。
                    }));
                    Thread.Sleep(3 * 1000);//太累了 ，休息三秒。。。。
                }
            }
            catch (Exception ex)
            { }
        }
    }
    

}
