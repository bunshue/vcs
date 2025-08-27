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

namespace vcs_ReadWrite_PDF4
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";
        string command = string.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void webBrowser1_Navigated(object sender, WebBrowserNavigatedEventArgs e)
        {
            //richTextBox1.Text += "Navigated\n";
            this.Text = webBrowser1.Url.ToString();
        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            //richTextBox1.Text += "DocumentCompleted\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            webBrowser1.Navigate(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            richTextBox1.Text += "直接顯示第幾頁, 第10頁\n";

            command = filename + "#page=10";    //顯示第幾頁
            webBrowser1.Navigate(command);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            richTextBox1.Text += "顯示比例, 30%\n";

            command = filename + "#zoom = 30 %";    //顯示比例  有無%皆可
            webBrowser1.Navigate(command);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            richTextBox1.Text += "搜尋pattern, 找 reboot\n";

            command = filename + "#search=reboot"; //搜尋pattern
            webBrowser1.Navigate(command);
        }

        int flag_toolbar = 0;
        private void button5_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            //上方工具列, 預設為開
            richTextBox1.Text += "上方工具列\t";

            if (flag_toolbar == 0)
            {
                flag_toolbar = 1;
                command = filename + "#toolbar=1";
                richTextBox1.Text += "打開\n";
            }
            else
            {
                flag_toolbar = 0;
                command = filename + "#toolbar=0";
                richTextBox1.Text += "關閉\n";
            }
            webBrowser1.Navigate(command);
        }

        int flag_navpanes = 0;
        private void button6_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            //左右方工具列, 預設為關
            richTextBox1.Text += "左右方工具列\t";
            if (flag_navpanes == 0)
            {
                flag_navpanes = 1;
                command = filename + "#navpanes=1";
                richTextBox1.Text += "打開\n";

            }
            else
            {
                flag_navpanes = 0;
                command = filename + "#navpanes=0";
                richTextBox1.Text += "關閉\n";
            }
            webBrowser1.Navigate(command);
        }

        int flag_scrollbar = 0;
        private void button7_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            //scrollbar, 預設為開
            richTextBox1.Text += "scrollbar\t";
            if (flag_scrollbar == 0)
            {
                flag_scrollbar = 1;
                command = filename + "#scrollbar=1";
                richTextBox1.Text += "打開\n";

            }
            else
            {
                flag_scrollbar = 0;
                command = filename + "#scrollbar=0";
                richTextBox1.Text += "關閉\n";
            }
            webBrowser1.Navigate(command);
        }

        int flag_statusbar = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            //fail
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            //statusbar, 預設為開
            richTextBox1.Text += "statusbar\t";
            if (flag_statusbar == 0)
            {
                flag_statusbar = 1;
                command = filename + "#statusbar=1";
                richTextBox1.Text += "打開\n";

            }
            else
            {
                flag_statusbar = 0;
                command = filename + "#statusbar=0";
                richTextBox1.Text += "關閉\n";
            }
            webBrowser1.Navigate(command);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            richTextBox1.Text += "view\t" + comboBox1.Text + "\n";

            command = filename + "#view=" + comboBox1.Text;
            webBrowser1.Navigate(command);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
            Application.DoEvents();

            richTextBox1.Text += "只看部分 viewrect\n";

            //viewrect=x_st,y_st,width,height
            command = filename + "#viewrect=100,100,100,100";
            webBrowser1.Navigate(command);

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "C#擷取pdf文檔的頁數\n";

            int pages = GetPDFofPageCount(filename);
            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "頁數 : " + pages.ToString() + "\n";
        }

        //[操作pdf文檔]之C#判斷pdf文檔的頁數：
        /// <summary>
        /// 擷取pdf文檔的頁數
        /// </summary>
        /// <param name="filePath"></param>
        /// <returns>-1表示檔案不存在</returns>
        public static int GetPDFofPageCount(string filePath)
        {
            int count = -1;//-1表示檔案不存在
            if (File.Exists(filePath))
            {
                using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read))
                {
                    StreamReader reader = new StreamReader(fs);
                    //從流的目前位置到末尾讀取流
                    string pdfText = reader.ReadToEnd();
                    //richTextBox1.Text += pdfText + "\n";
                    Regex rgx = new Regex(@"/Type\s*/Page[^s]");
                    MatchCollection matches = rgx.Matches(pdfText);
                    count = matches.Count;
                }
            }
            return count;
        }
    }
}

