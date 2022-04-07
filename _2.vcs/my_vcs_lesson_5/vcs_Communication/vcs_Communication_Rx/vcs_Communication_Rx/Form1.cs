using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_Communication_Rx
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

        private const int WM_COPYDATA = 0x004A;
        //接收消息方法
        protected override void WndProc(ref System.Windows.Forms.Message e)
        {
            if (e.Msg == WM_COPYDATA)
            {
                CopyDataStruct cds = (CopyDataStruct)e.GetLParam(typeof(CopyDataStruct));
                richTextBox1.Text += cds.lpData.ToString() + "\n";  //將文本信息顯示到文本框
                //MessageBox.Show(cds.lpData);
            }
            base.WndProc(ref e);
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
