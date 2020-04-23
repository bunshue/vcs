using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Office.Interop.Word;
using System.Reflection;    //for Missing

namespace vcs_translate2
{
    public partial class Form1 : Form
    {
        /*
        1. (Win7, Kilo)方案總管->參考->右鍵->加入參考->COM->選Microsoft Word 11.0 Object Library->確定
           (Win10, Sugar)方案總管->參考->右鍵->加入參考->COM->選Microsoft Word 12.0 Object Library->確定
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

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str_tc = "她來聽我　的演唱會　在十七歲的初戀　第一次約會";
            string str_sc = "她来听我　的演唱会　在十七岁的初恋　第一次约会";

            richTextBox1.Text += "TC字串: " + str_tc + ", 轉SC: " + ConvertUsingWord(str_tc, true) + "\n";
            richTextBox1.Text += "SC字串: " + str_sc + ", 轉TC: " + ConvertUsingWord(str_sc, false) + "\n";
        }

    }
}
