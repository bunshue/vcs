using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_translate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string Big5toGB2312(string strBig5)
        {
            StringBuilder sb = new StringBuilder();
            byte[] unknow = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
            return Encoding.GetEncoding("gb2312").GetString(unknow); // 簡體中文 (GB2312) 
        }

        //使用系統 kernel32.dll LCMapString進行轉換
        internal const int LOCALE_SYSTEM_DEFAULT = 0x0800;
        internal const int LCMAP_SIMPLIFIED_CHINESE = 0x02000000;
        internal const int LCMAP_TRADITIONAL_CHINESE = 0x04000000;
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        internal static extern int LCMapString(int Locale, int dwMapFlags, string lpSrcStr, int cchSrc, [Out] string lpDestStr, int cchDest);

        /// <summary>
        /// 將簡體中文字元轉換成繁體中文
        /// </summary>
        /// <param name="strGB2312"></param>
        /// <returns></returns>
        private string GB2312translateBig5(string strGB2312)
        {
            String tTarget = new String(' ', strGB2312.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_TRADITIONAL_CHINESE, strGB2312, strGB2312.Length, tTarget, strGB2312.Length);
            return tTarget;
        }

        /// <summary>
        /// 將繁體中文字元轉換成簡體中文
        /// </summary>
        /// <param name="strBig5"></param>
        /// <returns></returns>
        private string Big5translateGB2312(string strBig5)
        {
            String tTarget = new String(' ', strBig5.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_SIMPLIFIED_CHINESE, strBig5, strBig5.Length, tTarget, strBig5.Length);
            return tTarget;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox5.Text = Big5toGB2312(this.richTextBox1.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox6.Text = GB2312translateBig5(this.richTextBox2.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox4.Clear();
            richTextBox5.Clear();
            richTextBox6.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox5.Text = Big5translateGB2312(this.richTextBox3.Text);
        }
    }
}
