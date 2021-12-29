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

                            using System.Xml.Linq;  //for XElement
                            // XElement物件預設是以序列的方式處理xml資料，可以直接根據xml資料的階層結構，透過XElement物件建立資料

namespace vcs_ReadWrite_XML7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        //開啟XML檔案到TreeView ST
        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML6.xml";
            LoadTreeViewFromXmlFile(filename, treeView1);
        }

        // Load a TreeView control from an XML file.
        private void LoadTreeViewFromXmlFile(string filename, TreeView trv)
        {
            // Load the XML document.
            XmlDocument xml_doc = new XmlDocument();
            xml_doc.Load(filename);

            // Add the root node's children to the TreeView.
            trv.Nodes.Clear();
            AddTreeViewChildNodes(trv.Nodes, xml_doc.DocumentElement);
        }

        // Add the children of this XML node 
        // to this child nodes collection.
        private void AddTreeViewChildNodes(TreeNodeCollection parent_nodes, XmlNode xml_node)
        {
            foreach (XmlNode child_node in xml_node.ChildNodes)
            {
                // Make the new TreeView node.
                TreeNode new_node = parent_nodes.Add(child_node.Name);

                // Recursively make this node's descendants.
                AddTreeViewChildNodes(new_node.Nodes, child_node);

                // If this is a leaf node, make sure it's visible.
                if (new_node.Nodes.Count == 0) new_node.EnsureVisible();
            }
        }
        //開啟XML檔案到TreeView SP


        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //開啟XML檔案到TreeView ST
        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_xml\NexusPoint.xml";
            //string filename = @"C:\______test_files\__RW\_xml\vcs_ReadWrite_XML6.xml";

            XmlDocument NexusDocument = new XmlDataDocument();//定義一個XML文檔對像
            NexusDocument.Load(filename);//加載XML文件
            RecursionTreeControl(NexusDocument.DocumentElement, treeView1.Nodes);//將加載完成的XML文件顯示在TreeView控件中
            treeView1.ExpandAll();//展開TreeView控件中的所有項
        }

        /// <summary>
        /// RecursionTreeControl:表示將XML文件的內容顯示在TreeView控件中
        /// </summary>
        /// <param name="xmlNode">將要加載的XML文件中的節點元素</param>
        /// <param name="nodes">將要加載的XML文件中的節點集合</param>
        private void RecursionTreeControl(XmlNode xmlNode, TreeNodeCollection nodes)
        {
            foreach (XmlNode node in xmlNode.ChildNodes)//循環遍歷當前元素的子元素集合
            {
                string temp = (node.Value != null ? node.Value : (node.Attributes != null && node.Attributes.Count > 0) ? node.Attributes[0].Value : node.Name);//表示TreeNode節點的文本內容
                TreeNode new_child = new TreeNode(temp);//定義一個TreeNode節點對像
                nodes.Add(new_child);//向當前TreeNodeCollection集合中添加當前節點
                RecursionTreeControl(node, new_child.Nodes);//調用本方法進行遞歸
            }
        }




    }
}
