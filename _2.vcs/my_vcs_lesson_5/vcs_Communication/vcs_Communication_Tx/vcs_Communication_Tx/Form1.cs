using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

/*
這種方法的原理就是，利用FindWindow函數通過窗體標題查找出對方的進程，然後取得窗口

Handle，再通過DLL庫中的SendMessage函數發送消息給接收端，這樣就完成了程序的直接通信。
*/

namespace vcs_Communication_Tx
{
    public partial class Form1 : Form
    {
        //WM_COPYDATA消息所要求的數據結構
        public struct CopyDataStruct
        {
            public IntPtr dwData;
            public int cbData;

            [MarshalAs(UnmanagedType.LPStr)]

            public string lpData;
        }

        public const int WM_COPYDATA = 0x004A;

        //通過窗口的標題來查找窗口的句柄 
        [DllImport("User32.dll", EntryPoint = "FindWindow")]
        private static extern int FindWindow(string lpClassName, string lpWindowName);

        //在DLL庫中的發送消息函數
        [DllImport("User32.dll", EntryPoint = "SendMessage")]
        private static extern int SendMessage
            (
            int hWnd,                         // 目標窗口的句柄  
            int Msg,                          // 在這裡是WM_COPYDATA
            int wParam,                       // 第一個消息參數
            ref  CopyDataStruct lParam        // 第二個消息參數
           );

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //將文本框中的值， 發送給接收端
            string strURL = "將文本框中的值， 發送給接收端";
            CopyDataStruct cds;
            cds.dwData = (IntPtr)1; //這裡可以傳入一些自定義的數據，但只能是4字節整數      
            cds.lpData = strURL;    //消息字符串
            cds.cbData = System.Text.Encoding.Default.GetBytes(strURL).Length + 1;  //注意，這裡的長度是按字節來算的
            SendMessage(FindWindow(null, "Rx"), WM_COPYDATA, 0, ref cds);       // 這裡要修改成接收窗口的標題“接收端”
        }
    }
}
