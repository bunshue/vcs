using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Stream
using System.Net;
using System.Xml;
using System.Collections;   //for Hashtable

namespace vcs_ReadRSS1
{
    public partial class Form1 : Form
    {
        public class rss
        {
            public struct Channel
            {
                public string Title;
                public Hashtable Items;
            }

            public struct Item
            {
                public string Title;
                public string Description;
                public string Link;
                public string author;
                public string pubdate;
            }
        }
        //Channel下面包含Title和Item两个变量，TItle存的是该RSS源的名称，Item存放的是该RSS源中的新闻列表，Item里面的每一个变量都是Struct Item类型的。

        //先写了一个FoundChildNode（XmlNode Node, string Name）函数去查找指定Node结点下名称为Name的子节点
        private XmlNode FoundChildNode(XmlNode Node, string Name)
        {
            XmlNode childlNode = null;
            for (int i = 0; i < Node.ChildNodes.Count; i++)
            {
                if (Node.ChildNodes[i].Name == Name && Node.ChildNodes[i].ChildNodes.Count > 0)
                {
                    childlNode = Node.ChildNodes[i];
                    return childlNode;
                }
            }
            return childlNode;
        }

        //getRssItem函数是遍历所有Item结点的子节点，然后将相应的内容存入Item中，也就是将我们需要的新闻标题，时间，描述等等存入Item中。
        private rss.Item getRssItem(XmlNode Node)
        {
            rss.Item item = new rss.Item();
            for (int i = 0; i < Node.ChildNodes.Count; i++)
            {
                if (Node.ChildNodes[i].Name == "title")
                {
                    item.Title = Node.ChildNodes[i].InnerText;
                }
                else if (Node.ChildNodes[i].Name == "description")
                {
                    item.Description = Node.ChildNodes[i].InnerText;
                }
                else if (Node.ChildNodes[i].Name == "link")
                {
                    item.Link = Node.ChildNodes[i].InnerText;
                }
                else if (Node.ChildNodes[i].Name == "author")
                {
                    item.author = Node.ChildNodes[i].InnerText;
                }
                else if (Node.ChildNodes[i].Name == "pubdate")
                {
                    item.pubdate = Node.ChildNodes[i].InnerText;
                }
            }
            return item;
        }

        public rss.Channel ReadXml()
        {
            string url = @"https://www.mohw.gov.tw/rss-16-1.html";
            XmlTextReader Reader = new XmlTextReader(url);
            XmlValidatingReader Valid = new XmlValidatingReader(Reader);
            Valid.ValidationType = ValidationType.None;
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(Reader);

            XmlNode rssNode = FoundChildNode(xmlDoc, "rss");
            XmlNode channelNode = FoundChildNode(rssNode, "channel");

            //然后我们就可以遍历它的子节点，根据子节点的Name属性，读取我们需要的信息。
            rss.Channel channel = new rss.Channel();
            channel.Items = new Hashtable();
            for (int i = 0; i < channelNode.ChildNodes.Count; i++)
            {
                switch (channelNode.ChildNodes[i].Name)
                {
                    case "title":
                        {
                            channel.Title = channelNode.ChildNodes[i].InnerText;
                            break;
                        }
                    case "item":
                        {
                            rss.Item item = this.getRssItem(channelNode.ChildNodes[i]);
                            channel.Items.Add(channel.Items.Count, item);
                            break;
                        }
                }
            }
            return channel;
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            rss.Channel readChannel = new rss.Channel();
            readChannel = ReadXml();

            ViewRss(readChannel);

            /*
            Console.WriteLine(readChannel.Title);
            for (int i = 0; i < readChannel.Items.Count; i++)
            {
                rss.Item item = (rss.Item)readChannel.Items[i];
                Console.WriteLine(item.Title);
                Console.WriteLine(item.Link);
                Console.WriteLine(item.Description);
                Console.WriteLine(item.author);
                Console.WriteLine(item.pubdate);
            }
            */
        }

        private void ViewRss(rss.Channel channel)
        {
            treeView1.BeginUpdate();
            treeView1.Nodes.Clear();
            TreeNode channelNode = treeView1.Nodes.Add(channel.Title);
            channelNode.Tag = "";
            for (int i = 0; i < channel.Items.Count; i++)
            {
                rss.Item item = (rss.Item)channel.Items[i];
                TreeNode itemNode = channelNode.Nodes.Add(item.Title);
                itemNode.Tag = item.Link;
            }
            treeView1.ExpandAll();
            treeView1.EndUpdate();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            TreeNode itemNode = e.Node;
            string URL = itemNode.Tag.ToString();
            if (URL.Length != 0)
            {
                System.Diagnostics.Process.Start(URL);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string url1 = @"https://www.mohw.gov.tw/rss-16-1.html";
            ProcessRSSItem(url1);

            string url2 = "http://www.codeguru.com/icom_includes/feeds/codeguru/rss-all.xml";
            //ProcessRSSItem(url2);

            string url3 = "http://www.developer.com/icom_includes/feeds/special/dev-5.xml";
            //ProcessRSSItem(url3);

        }

        public void ProcessRSSItem(string rssURL)
        {
            WebRequest myRequest = WebRequest.Create(rssURL);
            WebResponse myResponse = myRequest.GetResponse();

            Stream rssStream = myResponse.GetResponseStream();
            XmlDocument rssDoc = new XmlDocument();
            rssDoc.Load(rssStream);

            XmlNodeList rssItems = rssDoc.SelectNodes("rss/channel/item");

            int i;
            int len = rssItems.Count;
            string title = "";
            string link = "";
            string description = "";

            richTextBox1.Text += "RSS內容 : " + len.ToString() + " 則\n";
            XmlNode rssDetail;

            for (i = 0; i < len; i++)
            {
                rssDetail = rssItems.Item(i).SelectSingleNode("title");
                if (rssDetail != null)
                {
                    title = rssDetail.InnerText;
                }
                else
                {
                    title = "XXX1";
                }

                rssDetail = rssItems.Item(i).SelectSingleNode("link");
                if (rssDetail != null)
                {
                    link = rssDetail.InnerText;
                }
                else
                {
                    link = "XXX2";
                }

                rssDetail = rssItems.Item(i).SelectSingleNode("description");
                if (rssDetail != null)
                {
                    description = rssDetail.InnerText;
                }
                else
                {
                    description = "XXX3";
                }

                richTextBox1.Text += "第 " + i.ToString() + " 則\n";
                richTextBox1.Text += "標題 : \n" + link + "\n";
                richTextBox1.Text += "網址 : \n" + link + "\n";
                richTextBox1.Text += "內容 : \n" + description + "\n";

            }
        }
    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}


