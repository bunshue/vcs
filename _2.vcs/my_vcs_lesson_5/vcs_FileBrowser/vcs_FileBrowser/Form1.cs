using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//文件瀏覽器
//使用TreeView 和 ListView

namespace vcs_FileBrowser
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //獲取邏輯驅動器
            string[] LogicDrives = System.IO.Directory.GetLogicalDrives();

            TreeNode[] cRoot = new TreeNode[LogicDrives.Length];

            for (int i = 0; i < LogicDrives.Length; i++)
            {
                TreeNode drivesNode = new TreeNode(LogicDrives[i]);

                treeView1.Nodes.Add(drivesNode);

                if (LogicDrives[i] != "A:\\" && LogicDrives[i] != "B:\\")
                {
                    getSubNode(drivesNode, true);
                }
            }
        }

        private void getSubNode(TreeNode PathName, bool isEnd)
        {
            if (!isEnd)
            {
                return; //exit this
            }

            TreeNode curNode;
            DirectoryInfo[] subDir;
            DirectoryInfo curDir = new DirectoryInfo(PathName.FullPath);

            try
            {
                subDir = curDir.GetDirectories();
                foreach (DirectoryInfo d in subDir)
                {
                    curNode = new TreeNode(d.Name);
                    PathName.Nodes.Add(curNode);
                    getSubNode(curNode, false);
                }
            }
            catch
            {
            }
        }

        //當鼠標單擊目錄節點左邊的+號時，節點將展開，此時，應在AfterExpand事件中加入以下代碼，以獲取此目錄下的子目錄節點
        private void treeView1_AfterExpand(object sender, TreeViewEventArgs e)
        {
            try
            {
                foreach (TreeNode tn in e.Node.Nodes)
                {
                    if (!tn.IsExpanded)
                    {
                        getSubNode(tn, true);
                    }
                }
            }
            catch
            {
            }
        }

        //當鼠標單擊選中目錄節點時，右邊的listView控件應顯示此目錄下的文件和目錄
        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            listView1.Items.Clear();
            DirectoryInfo selDir = new DirectoryInfo(e.Node.FullPath);
            DirectoryInfo[] listDir;
            FileInfo[] listFile;

            try
            {
                listDir = selDir.GetDirectories();
                listFile = selDir.GetFiles();
                foreach (DirectoryInfo d in listDir)
                {
                    listView1.Items.Add(d.Name, 6);
                }

                foreach (FileInfo d in listFile)
                {
                    listView1.Items.Add(d.Name);
                }
            }
            catch
            {
            }
        }
    }
}
