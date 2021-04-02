using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;//引用與輸入輸出文件流有關的命名空間
using System.Xml;//引用與XML有關的命名空間

namespace BindingXMLToTreeView
{
    public partial class BindingXMLToTreeView : Form
    {
        public BindingXMLToTreeView()
        {
            InitializeComponent();
        }

        private XmlDocument NexusDocument = new XmlDataDocument();//定義一個XML文檔對像
        private void BindingXMLToTreeView_Load(object sender, EventArgs e)
        {
            string filePath = "NexusPoint.xml";//定義一個變量保存XML文件的路徑
            if (File.Exists(filePath))//當在指定路徑下存在該文件時
            {
                NexusDocument.Load(filePath);//加載該路徑下的XML文件
                RecursionTreeControl(NexusDocument.DocumentElement, treeView1.Nodes);//將加載完成的XML文件顯示在TreeView控件中
                treeView1.ExpandAll();//展開TreeView控件中的所有項
                switchOn.Enabled = false;//設置打開按鈕為不可用狀態
            }
            else
            {
                switchOn.Enabled = true;//設置打開按鈕為可用狀態
            }
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

        private void switchOn_Click(object sender, EventArgs e)
        {
            OpenFileDialog NexusDialog = new OpenFileDialog();//定義一個提示用戶打開文件的對話框對像
            NexusDialog.Filter = "XML文件(*.XML)|*.XML";//設置打開文件的過濾參數
            if (NexusDialog.ShowDialog() == DialogResult.OK)//當單擊「打開」按鈕時
            {
                NexusDocument.Load(NexusDialog.FileName);//加載XML文件
                RecursionTreeControl(NexusDocument.DocumentElement, treeView1.Nodes);//在TreeView控件中顯示內容
                treeView1.ExpandAll();//展開TreeView控件中的所有項
                switchOn.Enabled = false;//設置打開按鈕為不可用狀態
            }
            else
            {
                switchOn.Enabled = true;//設置打開按鈕為可用狀態
            }
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {

        }
    }
}
