using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

//Windows API是對Windows操作系統的API函數，在C#中調用Windows API的實質是托管代碼對非托管代碼的調用。

namespace vcs_WinAPI
{
    public partial class Form1 : Form
    {

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern bool GetCursorPos(ref Point point);

        [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
        public static extern IntPtr GetCursor();


        [DllImport("kernel32", CharSet = CharSet.Ansi)]
        public static extern bool Beep(int frequery, int duration);

        [DllImport("user32.dll")]
        private static extern bool SetCursorPos(int X, int Y);

        public struct Point
        {
            int x;
            int y;
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
            Beep(500, 300);
        }




        private void button2_Click(object sender, EventArgs e)
        {
            //以下是用WinAPI 模擬鼠標定位和單機左鍵的操作：

            Point point = new Point();
            bool getResult = GetCursorPos(ref point);
            bool setRight = SetCursorPos(1920 / 2, 1080 / 2);
            //MouseClick("left");


        }
    }
}
