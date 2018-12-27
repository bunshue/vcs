using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

using Microsoft.Office.Interop.Word;

//using System.Web;
using System.Reflection;    //for Missing
//using Microsoft.International.Converters.TraditionalChineseToSimplifiedConverter;
//using Microsoft.International.Converters.PinYinConverter;
//using Microsoft.VisualBasic;

//[C#] 簡體亂碼轉換

namespace vcs_test_all_18_Encoding
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

        /*
        1. 專案->參考->右鍵->加入參考->COM->選Microsoft Word 11.0 Object Library->確定
        2. using Microsoft.Office.Interop.Word;
        */
        /// <summary>
        /// 使用Microsoft.Office.Interop.Word轉換
        /// </summary>
        /// <param name="argSource"></param>
        /// <param name="argIsCht"></param>
        /// <returns></returns>
        public string ConvertUsingWord(string argSource, bool argIsCht)
        {

            var doc = new Document();
            doc.Content.Text = argSource;
            doc.Content.TCSCConverter(
                argIsCht
                    ? WdTCSCConverterDirection.wdTCSCConverterDirectionTCSC
                    : WdTCSCConverterDirection.wdTCSCConverterDirectionSCTC, true, true);

            var ret = doc.Content.Text;
            object saveChanges = false;
            object originalFormat = Missing.Value;
            object routeDocument = Missing.Value;
            doc.Close(ref saveChanges, ref originalFormat, ref routeDocument);

            return ret;

            //用法
            //ConvertUsingWord("她來聽我　的演唱會　在十七歲的初戀　第一次約會，繁轉簡", true);
            //ConvertUsingWord("她来听我　的演唱会　在十七岁的初恋　第一次约会，簡轉繁", false);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.txtGB2312.Text = Big5toGB2312(this.txtSource.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.txtSC1.Text = Big5translateGB2312(this.txtTC1.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.txtTC2.Text = GB2312translateBig5(this.txtSC2.Text);
        }

        /// <summary>
        /// 判斷是否為GB2312編碼
        /// </summary>
        /// <param name="word"></param>
        /// <returns></returns>
        public bool IsGBCode(string word)
        {
            byte[] bytes = Encoding.GetEncoding("GB2312").GetBytes(word);
            // if there is only one byte, it is ASCII code or other code
            if (bytes.Length <= 1)
            {
                return false;
            }
            else
            {
                byte byte1 = bytes[0];
                byte byte2 = bytes[1];
                //判斷是否是GB2312
                if (byte1 >= 176 && byte1 <= 247 && byte2 >= 160 && byte2 <= 254)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (IsGBCode(txtSource.Text) == true)
                richTextBox1.Text += "字串: " + txtSource.Text + "    是GB2312碼\n";
            else
                richTextBox1.Text += "字串: " + txtSource.Text + "  不是GB2312碼\n";
            if (IsGBCode(txtTC1.Text) == true)
                richTextBox1.Text += "字串: " + txtTC1.Text + "    是GB2312碼\n";
            else
                richTextBox1.Text += "字串: " + txtTC1.Text + "  不是GB2312碼\n";
            if (IsGBCode(txtSC2.Text) == true)
                richTextBox1.Text += "字串: " + txtSC2.Text + "    是GB2312碼\n";
            else
                richTextBox1.Text += "字串: " + txtSC2.Text + "  不是GB2312碼\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "字串: " + ConvertUsingWord("她來聽我　的演唱會　在十七歲的初戀　第一次約會，繁轉簡", true) + "\n";
            richTextBox1.Text += "字串: " + ConvertUsingWord("她来听我　的演唱会　在十七岁的初恋　第一次约会，簡轉繁", false) + "\n";
        }



      
    }
}
