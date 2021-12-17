using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
树视图TreeView 属性及方法

属性	说明
Nodes	获取分配给树视图控件的树节点集合
PathSeparator	获取或设置树节点路径所使用的分隔符串
SelesctedNode	获取或设置当树节点选定时所使用的图像列表索引值
ShowNodeToolTips	获取或设置一个值,用以指示树图中的树节点是否经过排序
VisibleCount	获取树视图控件黄总完全可见的树节点数目
CollapseAll	折叠所有的树节点
ExpandAll 	展开所有的树节点
GetNodeAt	检索位于指定位置的 树节点
GetNodeCount	检索分配给树视图控件的树节点数


事件	说明
AfterCheck	在选中树节点复选框后 发生
AfterCollapse	在选中树节点复选框后发生
AfterExpand	在展开树节点后发生
AfterSelect	在选定树节点后发生
NodeMouseClick	当用户使用鼠标单击TreeView 时发生
NodeMouseDoubleClick	当用户使用鼠标双击TreeNode 时发生
*/

namespace vcs_TreeView8
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
            TreeNode TopNode = treeView1.Nodes.Add("博主"); //建立第一个顶级节点
            //建立4个基础节点 ,分别表示 4个大的分支
            TreeNode ParentNode1 = new TreeNode("家人");
            TreeNode ParentNode2 = new TreeNode("朋友");
            TreeNode ParentNode3 = new TreeNode("老师");
            TreeNode ParentNode4 = new TreeNode("同学");
            //将四个基础节点添加到顶级节点中
            TopNode.Nodes.Add(ParentNode1);
            TopNode.Nodes.Add(ParentNode2);
            TopNode.Nodes.Add(ParentNode3);
            TopNode.Nodes.Add(ParentNode4);
            //建立6个子节点,分别表示6个小的分支
            TreeNode ChildNode1 = new TreeNode("ShinePans");
            TreeNode ChildNode2 = new TreeNode("爸爸");
            TreeNode ChildNode3 = new TreeNode("妈妈");
            TreeNode ChildNode4 = new TreeNode("xuzhengmao");
            TreeNode ChildNode5 = new TreeNode("秦明");
            TreeNode ChildNode6 = new TreeNode("zhangyihui");
            TreeNode ChildNode7 = new TreeNode("xuzhengmao");
            TreeNode ChildNode8 = new TreeNode("zhangyihui");
            ParentNode1.Nodes.Add(ChildNode1);
            ParentNode1.Nodes.Add(ChildNode2);
            ParentNode1.Nodes.Add(ChildNode3);
            ParentNode4.Nodes.Add(ChildNode4);
            ParentNode3.Nodes.Add(ChildNode5);
            ParentNode4.Nodes.Add(ChildNode6);
            ParentNode2.Nodes.Add(ChildNode7);
            ParentNode2.Nodes.Add(ChildNode8);

        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            richTextBox1.Text += "AfterSelect:\t" + "选择的部门:\t" + e.Node.Text + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //TreeView全展開
            treeView1.ExpandAll();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //TreeView全摺疊
            treeView1.CollapseAll();
        }
    }
}
