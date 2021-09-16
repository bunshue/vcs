using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_6_21
{
    public partial class Form1 : Form
    {
        static System.Windows.Forms.Timer myTimer = new System.Windows.Forms.Timer();
        static int alarmCounter = 1;

        // Timer元件的Tick事件處理程序
        private static void TimerEventProcessor(Object myObject,
                                                EventArgs myEventArgs)
        {
            // 每隔Interval間隔時，詢問是否離開
            if (MessageBox.Show("確定要離開", "第  " + alarmCounter + " 次詢問",
               MessageBoxButtons.YesNo) == DialogResult.No)
            {
                // 如果使用者回答不離開，就記錄詢問了的次數
                alarmCounter += 1;
            }
            else
            {
                // Stops the timer.
                myTimer.Stop();
                Application.Exit();
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
 
        }

        private void button1_Click(object sender, EventArgs e)
        {
             // 委派Tick事件的事件處理程序為TimerEventProcessor()方法
            myTimer.Tick += new EventHandler(TimerEventProcessor);

            // 每5秒驅動一次Tick事件
            myTimer.Interval = 5000;
            myTimer.Start();
        }
    }
}
