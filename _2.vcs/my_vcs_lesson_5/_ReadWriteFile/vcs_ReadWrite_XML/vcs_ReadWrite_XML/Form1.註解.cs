using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Xml;

namespace vcs_ReadWrite_XML
{
    public partial class Form1 : Form
    {
        string filename = "C:\\______test_files\\_xml\\books.xml";
        string filename_add = "C:\\______test_files\\_xml\\books_add.xml";
        string filename_delete = "C:\\______test_files\\_xml\\books_delete.xml";

        public Form1()
        {
            InitializeComponent();
        }

        /// <summary>
        /// 得到XML內容按鈕事件方法
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnGet_Click(object sender, EventArgs e)
        {
            lbXmlValue.Items.Clear();

            if (File.Exists(filename))
            {
                //加載XML文件
                XmlDocument xdDocument = new XmlDocument();
                richTextBox1.Text += "開啟XML文件 : " + filename + "\n";
                xdDocument.Load(filename);

                //得到主節點
                XmlElement xeRoot = xdDocument.DocumentElement;
                if (xeRoot != null)
                {
                    XmlNode xnNodeRoot = (XmlNode)xeRoot;
                    RecurseXmlDocument(xnNodeRoot, 0);
                    richTextBox1.Text += "\n讀取XML文件 : " + filename + " 完成\n";
                }
            }
            else
                richTextBox1.Text += "XML文件 : " + filename + " 不存在\n";
        }

        /// <summary>
        /// 讀取ＸＭＬ
        /// </summary>
        /// <param name="aXnNode">節點</param>
        /// <param name="aIndent">縮進大小</param>
        private void RecurseXmlDocument(XmlNode aXnNode, int aIndent)
        {
            richTextBox1.Text += "\nRecurseXmlDocument ST aIndent = " + aIndent.ToString();
            //判斷結點中是否有內容
            if (aXnNode == null)
            {
                richTextBox1.Text += "RecurseXmlDocument SP XXXXXXXXXXXX\n";
                return;
            }

            //節點是元素時
            if (aXnNode is XmlElement)
            {
                richTextBox1.Text += "\t取得 XmlElement";
                //顯示根元素的名稱
                richTextBox1.Text += "\n根元素 : " + "\"" + aXnNode.Name.PadLeft(aXnNode.Name.Length + aIndent) + "\"" + "\t";
                lbXmlValue.Items.Add(aXnNode.Name.PadLeft(aXnNode.Name.Length + aIndent));
                if (aXnNode.Attributes != null)
                {
                    richTextBox1.Text += "有 aXnNode.Attributes 共有 " + aXnNode.Attributes.Count.ToString() + " 項屬性";
                    //得到屬性
                    int i = 0;
                    foreach (XmlAttribute xaAttribute in aXnNode.Attributes)
                    {
                        i++;
                        string sText = "";
                        sText = xaAttribute.Name;
                        richTextBox1.Text += "\n第 " + i.ToString() + " 項屬性, 屬性名 sText1 = " + "\"" + sText + "\"";
                        lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent + 2));
                        sText = xaAttribute.Value;
                        lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent + 4));
                        richTextBox1.Text += ", 屬性值 sText2 = " + "\"" + sText + "\"";
                    }
                }
                else
                    richTextBox1.Text += "無 aXnNode.Attributes\n";

                richTextBox1.Text += "\n111 aXnNode.HasChildNodes = " + aXnNode.HasChildNodes.ToString() + "\n";
                //根元素中是否有子元素
                if (aXnNode.HasChildNodes)
                {
                    richTextBox1.Text += "\n111 aXnNode.HasChildNodes = " + aXnNode.HasChildNodes.ToString() + ", ChildNodes個數 : " + aXnNode.ChildNodes.Count.ToString() + "\n";
                    richTextBox1.Text += "\n1111 aaa 有子元素 call recure with index = " + (aIndent + 2).ToString() + "\n";
                    //有子節點，遍歷子節點
                    RecurseXmlDocument(aXnNode.FirstChild, aIndent + 2);
                }
                else
                    richTextBox1.Text += "\n1111 aaa XXXXXXX 無子元素\n";

                //判斷下個節點是為空
                if (aXnNode.NextSibling != null)
                {
                    richTextBox1.Text += "\n111 aXnNode.NextSibling = " + aXnNode.NextSibling.ToString() + "\n";
                }
                else
                    richTextBox1.Text += "\n111 aXnNode.NextSibling = null \n";

                if (aXnNode.NextSibling != null)
                {
                    richTextBox1.Text += "\n1111 bbb call recurse 有下一個節點 with index = " + (aIndent + 2).ToString() + "\n";
                    RecurseXmlDocument(aXnNode.NextSibling, aIndent);
                }
                else
                    richTextBox1.Text += "\n1111 bbb XXXXXXX 無下一個節點\n";
            }
            else if (aXnNode is XmlText)
            {
                richTextBox1.Text += "\t取得 XmlText";
                //顯示節點中的內容
                string sText = ((XmlText)aXnNode).Value;
                lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent));
                richTextBox1.Text += "\t文本 sText3 = " + "\"" + sText + "\"" + "\n";
            }
            else if (aXnNode is XmlComment)
            {
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                richTextBox1.Text += "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";


                richTextBox1.Text += "\t取得 XmlComment";
                string sText = aXnNode.Value;
                lbXmlValue.Items.Add(sText.PadLeft(sText.Length + aIndent));
                richTextBox1.Text += "\n註釋 sText4 = " + "\"" + sText + "\"";
                //如果不加下邊的遍歷，資料只會得出備註中的內容，不會得出子節點內容

                if (aXnNode.NextSibling != null)
                    richTextBox1.Text += "\n222 aXnNode.NextSibling = " + aXnNode.NextSibling.ToString() + "\n";
                else
                    richTextBox1.Text += "\n222 aXnNode.NextSibling = null \n";

                if (aXnNode.HasChildNodes)
                {
                    //有子節點，遍歷子節點
                    RecurseXmlDocument(aXnNode.FirstChild, aIndent + 2);
                }
                else
                    richTextBox1.Text += "\n2222 aaa XXXXXXX\n";
                richTextBox1.Text += "\n222 aXnNode.NextSibling = " + aXnNode.NextSibling.ToString() + "\n";
                if (aXnNode.NextSibling != null)
                {
                    RecurseXmlDocument(aXnNode.NextSibling, aIndent);
                }
                else
                    richTextBox1.Text += "\n2222 bbb XXXXXXX\n";
            }
            else
            {
                richTextBox1.Text += "\t取得 其他 XXXXXXX";
            }
            richTextBox1.Text += "RecurseXmlDocument SP aIndent = " + aIndent.ToString() + "\n";
        }

        /// <summary>
        /// 創建Node按鈕事件方法
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnCreateNode_Click(object sender, EventArgs e)
        {
            //加載XML文件
            XmlDocument xdDocument = new XmlDocument();
            xdDocument.Load(filename);
            richTextBox1.Text += "載入XML文件 : " + filename + "\n";

            //得到主節點
            XmlElement xeRoot = xdDocument.DocumentElement;

            //創建節點
            XmlElement newBook = xdDocument.CreateElement("book");
            XmlElement newTitle = xdDocument.CreateElement("title");
            XmlElement newAuthor = xdDocument.CreateElement("author");
            XmlElement newCode = xdDocument.CreateElement("code");

            //創建屬性
            XmlAttribute xaNewAttribute = xdDocument.CreateAttribute("Pages");
            xaNewAttribute.Value = "1000";
            XmlText title = xdDocument.CreateTextNode("Beginning Visual C# 3rd Edition");
            XmlText author = xdDocument.CreateTextNode("Karli Watson et al");
            XmlText code = xdDocument.CreateTextNode("123456789");
            //創建備註
            XmlComment comment = xdDocument.CreateComment("This book is the book you are reading");

            //元素插入ＸＭＬ樹中
            newBook.AppendChild(comment);
            newBook.Attributes.Append(xaNewAttribute);
            newBook.AppendChild(newTitle);
            newBook.AppendChild(newAuthor);
            newBook.AppendChild(newCode);
            newTitle.AppendChild(title);
            newAuthor.AppendChild(author);
            newCode.AppendChild(code);

            //插入某節點後邊
            xeRoot.InsertAfter(newBook, xeRoot.FirstChild);

            //插入某節點前邊
            //xeRoot.InsertBefore(newBook, xeRoot.FirstChild);

            //保存結果
            xdDocument.Save(filename_add);
            richTextBox1.Text += "寫入XML文件 : " + filename_add + "\n";
        }

        /// <summary>
        /// 刪除節點按鈕事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void btnDeleteNode_Click(object sender, EventArgs e)
        {
            //加載XML文件
            XmlDocument xdDocument = new XmlDocument();
            xdDocument.Load(filename);
            richTextBox1.Text += "載入XML文件 : " + filename + "\n";

            //得到主節點
            XmlElement xeRoot = xdDocument.DocumentElement;

            if (xeRoot.HasChildNodes)
            {
                //得到最後一個節點
                XmlNode xnBook = xeRoot.LastChild;
                //刪除最後一個結點
                xeRoot.RemoveChild(xnBook);
                //保存結果
                xdDocument.Save(filename_delete);
                richTextBox1.Text += "寫入XML文件 : " + filename_delete + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


    }
}
