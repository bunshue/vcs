using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Runtime.InteropServices;

namespace vcs_KeyboardSendKeys
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
            //模擬鍵盤 SendKeys

            SendKeys.SendWait("{Tab}");
            SendKeys.SendWait("{Tab}");
            SendKeys.SendWait("{Tab}");
            SendKeys.SendWait("{Tab}");
            SendKeys.SendWait("{Tab}");

            SendKeys.SendWait("{Enter}");
            SendKeys.SendWait("123456789");

            SendKeys.SendWait("{Enter}");
            SendKeys.SendWait("123456789");

            SendKeys.SendWait("{Enter}");
            string name = "this is a lion-mouse";

            SendKeys.SendWait("{Enter}");
            foreach (char ArrayValue in name.ToCharArray())
            {
                SendKeys.SendWait(ArrayValue.ToString());
                Thread.Sleep(10);
            }

            SendKeys.SendWait("{Enter}");


            //SendKeys.SendWait("{Tab}");
            SendKeys.SendWait("{Enter}");
        }

        int cnt = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            //C# 模擬鍵盤操作--SendKey(),SendKeys()
            //https://www.cnblogs.com/wolfocme110/p/13444309.html

            //光标移至richTextBox1
            richTextBox1.Focus();

            //模拟按下"ABCDEFG"
            SendKeys.SendWait("(ABCDEFG)");
            SendKeys.SendWait("{left 5}");
            SendKeys.SendWait("{h 10}");

            /*
            更多举例:
            SendKeys.SendWait("^C");  //Ctrl+C 组合键
            SendKeys.SendWait("+C");  //Shift+C 组合键
            SendKeys.SendWait("%C");  //Alt+C 组合键
            SendKeys.SendWait("+(AX)");  //Shift+A+X 组合键
            SendKeys.SendWait("+AX");  //Shift+A 组合键,之后按X键
            SendKeys.SendWait("{left 5}");  //按←键 5次
            SendKeys.SendWait("{h 10}");   //按h键 10次
            SendKeys.Send("汉字");  //模拟输入"汉字"2个字
            */

            richTextBox1.Text += "到richTextBox裡面添加一些文字\n";
            richTextBox1.Focus();
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");
            SendKeys.Send("{TAB}"); //按了Tab
            SendKeys.Send("123456");
            SendKeys.Send("{ENTER}");   //添加Enter
            SendKeys.Send("{ENTER}");
            SendKeys.Send("{ENTER}");
            SendKeys.Send("到richTextBox裡面添加一些文字  " + (cnt++).ToString() + "\n");



        }

        private void button3_Click(object sender, EventArgs e)
        {
            //C# 模擬鍵盤操作--SendKey(),SendKeys()
            //模擬鍵盤輸入就是使用以下2個語法實現的.
            //SendKeys.Send(string keys);  //模擬漢字(文本)輸入
            //SendKeys.SendWait(string keys); //模擬按鍵輸入

            //光标移至richTextBox1
            richTextBox1.Focus();

            //模拟按下"ABCDEFG"
            SendKeys.SendWait("(ABCDEFG)");
            SendKeys.SendWait("{left 5}");
            SendKeys.SendWait("{h 10}");

            /*
            更多举例:
            SendKeys.SendWait("^C");  //Ctrl+C 组合键
            SendKeys.SendWait("+C");  //Shift+C 组合键
            SendKeys.SendWait("%C");  //Alt+C 组合键
            SendKeys.SendWait("+(AX)");  //Shift+A+X 组合键
            SendKeys.SendWait("+AX");  //Shift+A 组合键,之后按X键
            SendKeys.SendWait("{left 5}");  //按←键 5次
            SendKeys.SendWait("{h 10}");   //按h键 10次
            SendKeys.Send("汉字");  //模拟输入"汉字"2个字
            */

        }

        [DllImport("user32.dll")]
        static extern void keybd_event
        (
            byte bVk,// 虛擬鍵值  
            byte bScan,// 硬件掃描碼  
            uint dwFlags,// 動作標識  
            IntPtr dwExtraInfo// 與鍵盤動作關聯的輔加信息  
        );

        private void button4_Click(object sender, EventArgs e)
        {
            //模擬按下PrintScreen
            keybd_event((byte)0x2c, 0, 0x0, IntPtr.Zero);//down
            Application.DoEvents();
            keybd_event((byte)0x2c, 0, 0x2, IntPtr.Zero);//up
            Application.DoEvents();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //模擬按下Alt + PrintScreen

            keybd_event((byte)Keys.Menu, 0, 0x0, IntPtr.Zero);
            keybd_event((byte)0x2c, 0, 0x0, IntPtr.Zero);//down
            Application.DoEvents();
            Application.DoEvents();
            keybd_event((byte)0x2c, 0, 0x2, IntPtr.Zero);//up
            keybd_event((byte)Keys.Menu, 0, 0x2, IntPtr.Zero);
            Application.DoEvents();
            Application.DoEvents();

        }
    }
}
