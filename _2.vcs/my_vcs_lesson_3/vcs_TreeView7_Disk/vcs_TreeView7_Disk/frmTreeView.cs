using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_TreeView7_Disk
{
    public partial class frmTreeView : Form
    {
        public frmTreeView()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            TreeNode CountNode = new TreeNode("我的電腦");//初始化TreeView控件添加總結點
            TreeViewFile.Nodes.Add(CountNode);
            ListViewShow(CountNode);	//初始化ListView控件
        }
        //
        private void ListViewShow(TreeNode NodeDir)//初始化ListView控件，把TrreView控件中的數據添加進來
        {
            ListViewFile.Clear();

            try
            {
                if (NodeDir.Parent == null)// 如果當前TreeView的父結點為空，就把我的電腦下的分區名稱添加進來
                {
                    foreach (string DrvName in Directory.GetLogicalDrives())//獲得硬盤分區名
                    {
                        ListViewItem ItemList = new ListViewItem(DrvName);
                        ListViewFile.Items.Add(ItemList);//添加進來
                    }
                }
                else//如果當前TreeView的父結點不為空，把點擊的結點，做為一個目錄文件的總結點
                {
                    foreach (string DirName in Directory.GetDirectories((string)NodeDir.Tag))//編歷當前分區或文件夾所有目錄
                    {
                        ListViewItem ItemList = new ListViewItem(DirName);
                        ListViewFile.Items.Add(ItemList);
                    }
                    foreach (string FileName in Directory.GetFiles((string)NodeDir.Tag))//編歷當前分區或文件夾所有目錄的文件
                    {
                        ListViewItem ItemList = new ListViewItem(FileName);
                        ListViewFile.Items.Add(ItemList);
                    }//
                }
            }
            catch { }
        }//
        private void ListViewShow(string DirFileName)//獲取當有文件夾內的文件和目錄
        {
            ListViewFile.Clear();
            try
            {
                foreach (string DirName in Directory.GetDirectories(DirFileName))
                {
                    ListViewItem ItemList = new ListViewItem(DirName);
                    ListViewFile.Items.Add(ItemList);
                }
                foreach (string FileName in Directory.GetFiles(DirFileName))
                {
                    ListViewItem ItemList = new ListViewItem(FileName);
                    ListViewFile.Items.Add(ItemList);
                }
            }
            catch { }
        }

        private void TreeViewShow(TreeNode NodeDir)//初始化TreeView控件
        {
            try
            {
                if (NodeDir.Nodes.Count == 0)
                {
                    if (NodeDir.Parent == null)//如果結點為空顯示硬盤分區
                    {
                        foreach (string DrvName in Directory.GetLogicalDrives())
                        {
                            TreeNode aNode = new TreeNode(DrvName);
                            aNode.Tag = DrvName;
                            NodeDir.Nodes.Add(aNode);
                        }
                    }// end 
                    else// 不為空，顯示分區下文件夾
                    {
                        foreach (string DirName in Directory.GetDirectories((string)NodeDir.Tag))
                        {
                            TreeNode aNode = new TreeNode(DirName);
                            aNode.Tag = DirName;
                            NodeDir.Nodes.Add(aNode);
                        }
                    }
                }
            }
            catch { }
        }


        private void TreeViewFile_AfterSelect(object sender, TreeViewEventArgs e)
        {
            ListViewShow(e.Node);
            TreeViewShow(e.Node);
        }

        private void ListViewFile_DoubleClick(object sender, EventArgs e)
        {
            foreach (int ListIndex in ListViewFile.SelectedIndices)
            {
                ListViewShow(ListViewFile.Items[ListIndex].Text);
            }
        }

        private void ListViewFile_SelectedIndexChanged(object sender, EventArgs e)
        {

        }



    }
}