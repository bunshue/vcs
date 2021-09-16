using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace xCh4_2_1_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            // 指定位置、大小與自動依文字內容調整大小
            linkLabel1.Location = new Point(20, 20);
            linkLabel1.Size = new Size(200, 20);
            linkLabel1.AutoSize = true;

            // 設定與超連結有關的色彩
            linkLabel1.DisabledLinkColor = Color.Red;
            linkLabel1.VisitedLinkColor = Color.Blue;
            linkLabel1.LinkBehavior = LinkBehavior.HoverUnderline;
            linkLabel1.LinkColor = Color.Navy;

            // 設定超連結文字
            linkLabel1.Text = "Yahoo!奇摩  Microsoft微軟  MSDN文件庫";

            // 從超連結文字中，設定做為超連結的區域，也就是可點選的文字
            // 1.指定第7個字開始，共有4個字(二個中文字)是超連結，本例即「奇摩」
            linkLabel1.LinkArea = new LinkArea(6, 2);

            linkLabel1.Links[0].Visited = true;                // 標示第1個超連結已被點選過了
            linkLabel1.Links[0].LinkData = "tw.yahoo.com";     // 「奇摩」的網址
            
            // 2.指定另外二個超連結的區域
            // * 超連結文字中標示出「微軟」為超連結及其網址
            // * 超連結文字中標示出「文件庫」為超連結及其網址
            linkLabel1.Links.Add(19, 2, "www.microsoft.com"); 
            linkLabel1.Links.Add(27, 3, "msdn.microsoft.com");
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // 被點選的超連結，標示為「已連結」
            linkLabel1.Links[linkLabel1.Links.IndexOf(e.Link)].Visited = true;
            string target = e.Link.LinkData as string;  // 從linkData中取出該超連結的「網址」
            System.Diagnostics.Process.Start("IEXPLORE.EXE", target);   // 開啟瀏覽器連至該網址
        }

        private void button1_Click(object sender, EventArgs e)
        {
             string msg="";
            IEnumerator myLinks = linkLabel1.Links.GetEnumerator();
            while(myLinks.MoveNext())
            {
                LinkLabel.Link link = ( LinkLabel.Link)myLinks.Current;
                msg = msg + link.LinkData + "\n";
            }
            MessageBox.Show(msg, "現有的超連結內容");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 新增[MSDN]的超連結
            LinkLabel.Link aLink = new LinkLabel.Link(23, 4, "msdn.microsoft.com/zh-tw/library");
             linkLabel1.Links.Add(aLink);
             linkLabel1.Links[3].Visited = true; 
             label1.Text = "連結數：" +linkLabel1.Links.Count.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 移除[文件庫]的超連結
            linkLabel1.Links.RemoveAt(3);
            label1.Text = "連結數：" + linkLabel1.Links.Count.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //  清除所有超連結
            linkLabel1.Links.Clear();
            label1.Text = "連結數：" + linkLabel1.Links.Count.ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Text = "目前的超連結";
            button2.Text = "新增超連結";
            button3.Text = "移除現有的超連結";
            button4.Text = "清除所有的超連結";

            label1.Text = "現有的超連結數：" + linkLabel1.Links.Count.ToString();
        }
    }
}

