using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_Thread5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int a = 0;

        thread1 obj;
        Thread t;
        private void button1_Click(object sender, EventArgs e)
        {
            a++;
            obj = new thread1("花旗銀行 " + a.ToString());
            t = new Thread(obj.runMe);
            t.Start();
        }


        class thread1
        {
            private String title;
            public thread1(String title)
            {
                this.title = title;
            }
            public void runMe()
            {
                while (true)
                {
                    Console.Write(title + "\r\n");
                    System.Threading.Thread.Sleep(1000);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            t.Abort();

        }

    }
}
