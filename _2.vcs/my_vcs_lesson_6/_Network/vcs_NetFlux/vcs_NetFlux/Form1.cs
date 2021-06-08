using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NetFlux
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private static int intX = 0;
        private static int intY = 0;
        private NetStruct[] myNetStruct;
        private NetInfo myNetInfo;

        Int64 total_receive = 0;
        Int64 total_send = 0;

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;
            int Swidth = Screen.PrimaryScreen.WorkingArea.Width;        //获取屏幕宽度
            int SHeight = Screen.PrimaryScreen.WorkingArea.Height;      //获取屏幕高度
            this.DesktopLocation = new Point(Swidth - this.Width, SHeight - this.Height);//设置窗体加载时位置
            myNetInfo = new NetInfo();
            myNetStruct = myNetInfo.myNetStructs;
            myNetInfo.GetInfo(myNetStruct[0]);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label2.Text = DateTime.Now.ToLongDateString() + " " + getWeek() + " " + DateTime.Now.ToLongTimeString();
            NetStruct NStruct = myNetStruct[0];
            total_receive += NStruct.Receive;
            total_send += NStruct.Send;

            //label3.Text = "網路[接收:" + ByteConversionGBMBKB(Convert.ToInt64(NStruct.Receive)) + " 發送:" + ByteConversionGBMBKB(Convert.ToInt64(NStruct.Send)) + "]";
            label3.Text = "網路[接收:" + ByteConversionGBMBKB(Convert.ToInt64(total_receive)) + " 發送:" + ByteConversionGBMBKB(Convert.ToInt64(total_send)) + "]";



            //ByteConversionGBMBKB(Convert.ToInt64(NStruct.Receive)) + "\n";
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            intX = -e.X;
            intY = -e.Y;
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                Point myPosition = Control.MousePosition;  //获取当前鼠标的屏幕坐标
                myPosition.Offset(intX, intY);             //重载当前鼠标的位置
                this.DesktopLocation = myPosition;         //设置当前窗体在屏幕上的位置
            }
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        #region  判断星期几
        /// <summary>
        /// 判断星期几
        /// </summary>
        /// <returns></returns>
        public string getWeek()
        {
            string str = DateTime.Now.DayOfWeek.ToString();
            string strWeek = "";
            switch (str)
            {
                case "Monday":
                    strWeek = "星期一";
                    break;
                case "Tuesday":
                    strWeek = "星期二";
                    break;
                case "Wednesday":
                    strWeek = "星期三";
                    break;
                case "Thursday":
                    strWeek = "星期四";
                    break;
                case "Friday":
                    strWeek = "星期五";
                    break;
                case "Saturday":
                    strWeek = "星期六";
                    break;
                case "Sunday":
                    strWeek = "星期日";
                    break;
            }
            return strWeek;
        }
        #endregion



        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

    }
}
