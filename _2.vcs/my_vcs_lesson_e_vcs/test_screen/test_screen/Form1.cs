using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Text.RegularExpressions;

using Microsoft.Win32;  //for Registry


namespace test_screen
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
            //生成大量隨機碼
            StreamWriter swriter = new StreamWriter("1.txt", true);
            for (int i = 0; i < 100; i++)
            {
                swriter.Write(generateRandomString(20));
                swriter.WriteLine();
                Console.WriteLine("Number: {0}", i);
            }
            swriter.Flush();
            swriter.Close();

        }

        static Random random = new Random();
        static string generateRandomString(int length)
        {
            var chars = "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789";
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < length; i++)
            {
                int index = random.Next(chars.Length);
                result.Append(chars[index]);
            }
            return result.ToString();
        }


        //C#過濾html標簽 
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");

            //htmlStr = htmlStr.Replace(""", ""); //去除異常的引號" " "
            //htmlStr = htmlStr.Replace(""", "");//去除异常的引号" " "
            //htmlStr = htmlStr.Replace("'", ""); //去除異常的引號" " "
            //htmlStr = htmlStr.Replace(""", "");
            return htmlStr.Trim();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

    }
}
