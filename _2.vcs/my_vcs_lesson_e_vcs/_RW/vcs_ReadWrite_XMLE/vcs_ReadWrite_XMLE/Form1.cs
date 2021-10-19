using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;

namespace vcs_ReadWrite_XMLE
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

        }

        class TreeExXMLCls
        {
            private TreeView thetreeview;
            private string xmlfilepath;
            XmlTextWriter textWriter;
            XmlNode Xmlroot;
            XmlDocument textdoc;

            public TreeExXMLCls()
            {
                //----构造函数
                textdoc = new XmlDocument();

            }

            ~TreeExXMLCls()
            {
                //----析构函数

            }

            #region　遍历treeview并实现向XML的转化
            ///　<summary>　　　
            ///　遍历treeview并实现向XML的转化
            ///　</summary>　　　
            ///　<param　name="TheTreeView">树控件对象</param>　　　
            ///　<param　name="XMLFilePath">XML输出路径</param>　　　
            ///　<returns>0表示函数顺利执行</returns>　　　

            public int TreeToXML(TreeView TheTreeView, string XMLFilePath)
            {
                //-------初始化转换环境变量
                thetreeview = TheTreeView;
                xmlfilepath = XMLFilePath;
                textWriter = new XmlTextWriter(xmlfilepath, null);

                //-------创建XML写操作对象
                textWriter.Formatting = Formatting.Indented;

                //-------开始写过程，调用WriteStartDocument方法
                textWriter.WriteStartDocument();

                //-------写入说明
                textWriter.WriteComment("this　XML　is　created　from　a　tree");
                textWriter.WriteComment("By　思月行云");

                //-------添加第一个根节点
                textWriter.WriteStartElement("TreeExXMLCls");
                textWriter.WriteEndElement();

                //------　写文档结束，调用WriteEndDocument方法
                textWriter.WriteEndDocument();

                //-----关闭输入流
                textWriter.Close();

                //-------创建XMLDocument对象
                textdoc.Load(xmlfilepath);

                //------选中根节点
                XmlElement Xmlnode = textdoc.CreateElement(thetreeview.Nodes[0].Text);
                Xmlroot = textdoc.SelectSingleNode("TreeExXMLCls");

                //------遍历原treeview控件，并生成相应的XML
                TransTreeSav(thetreeview.Nodes, (XmlElement)Xmlroot);
                textdoc.Save(xmlfilepath);//正确的位置保存一次

                return 0;


            }

            private int TransTreeSav(TreeNodeCollection nodes, XmlElement ParXmlnode)
            {

                //-------遍历树的各个故障节点，同时添加节点至XML
                XmlElement xmlnode;
                Xmlroot = textdoc.SelectSingleNode("TreeExXMLCls");

                foreach (TreeNode node in nodes)
                {
                    xmlnode = textdoc.CreateElement(node.Text);
                    ParXmlnode.AppendChild(xmlnode);

                    if (node.Nodes.Count > 0)
                    {
                        TransTreeSav(node.Nodes, xmlnode);
                    }
                }
                //　　textdoc.Save(xmlfilepath);//原创的人才不注意保存一次大量数据会卡死

                return 0;
            }

            #endregion

            #region　遍历XML并实现向tree的转化
            ///　<summary>　　　
            ///　遍历treeview并实现向XML的转化
            ///　</summary>　　　
            ///　<param　name="XMLFilePath">XML输出路径</param>　　　
            ///　<param　name="TheTreeView">树控件对象</param>　　　
            ///　<returns>0表示函数顺利执行</returns>　　　

            public int XMLToTree(string XMLFilePath, TreeView TheTreeView)
            {
                //-------重新初始化转换环境变量
                thetreeview = TheTreeView;
                xmlfilepath = XMLFilePath;

                //-------重新对XMLDocument对象赋值
                textdoc.Load(xmlfilepath);

                XmlNode root = textdoc.SelectSingleNode("TreeExXMLCls");

                foreach (XmlNode subXmlnod in root.ChildNodes)
                {
                    TreeNode trerotnod = new TreeNode();
                    trerotnod.Text = subXmlnod.Name;
                    thetreeview.Nodes.Add(trerotnod);
                    TransXML(subXmlnod.ChildNodes, trerotnod);

                }

                return 0;
            }

            private int TransXML(XmlNodeList Xmlnodes, TreeNode partrenod)
            {
                //------遍历XML中的所有节点，仿照treeview节点遍历函数
                foreach (XmlNode xmlnod in Xmlnodes)
                {
                    TreeNode subtrnod = new TreeNode();
                    subtrnod.Text = xmlnod.Name;
                    partrenod.Nodes.Add(subtrnod);

                    if (xmlnod.ChildNodes.Count > 0)
                    {
                        TransXML(xmlnod.ChildNodes, subtrnod);
                    }
                }

                return 0;

            }

            #endregion

        }
    }
}
