using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 設定系統時間
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        [DllImport("kernel32.dll", CharSet = CharSet.Ansi)]
        public extern static bool SetSystemTime(ref SYSTEMTIME time);
        [StructLayout(LayoutKind.Sequential)]
        public struct SYSTEMTIME
        {
            public short Year;
            public short Month;
            public short DayOfWeek;
            public short Day;
            public short Hour;
            public short Minute;
            public short Second;
            public short Miliseconds;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            Microsoft.Win32.SystemEvents.TimeChanged += new EventHandler(SystemEvents_TimeChanged);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SYSTEMTIME t = new SYSTEMTIME();
            t.Year = (short)DateTime.Now.Year;
            t.Month = (short)DateTime.Now.Month;
            t.Day = (short)DateTime.Now.Day;
            t.Hour = (short)(dateTimePicker1.Value.Hour - 8);//這個函數使用的是0時區的時間,例如，要設12點，則為12-8   
            t.Minute = (short)dateTimePicker1.Value.Minute;
            t.Second = (short)dateTimePicker1.Value.Second;
            bool v = SetSystemTime(ref t); 
        }
        private void SystemEvents_TimeChanged(object sender, EventArgs e)
        {
            MessageBox.Show("系統日期修改成功！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
