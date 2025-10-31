using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//TreeView組件搜尋磁碟目錄

namespace vcs_TreeView2_ListView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            TreeNode CountNode = new TreeNode("我的電腦");//初始化TreeView控件添加總結點
            treeView1.Nodes.Add(CountNode);
            ListViewShow(CountNode);	//初始化ListView控件

            setup_treeView1();
            setup_listView1();
        }

        void show_item_location()
        {
            int W = 400;
            int H = 500;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            int dd = 30;

            treeView1.Size = new Size(W, H);
            listView1.Size = new Size(W, H);
            richTextBox1.Size = new Size(W, H);

            treeView1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1580, 840);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        private void ListViewShow(TreeNode NodeDir)//初始化ListView控件，把TrreView控件中的數據添加進來
        {
            listView1.Clear();

            try
            {
                if (NodeDir.Parent == null)// 如果當前TreeView的父結點為空，就把我的電腦下的分區名稱添加進來
                {
                    foreach (string DrvName in Directory.GetLogicalDrives())//獲得硬盤分區名
                    {
                        ListViewItem ItemList = new ListViewItem(DrvName);
                        listView1.Items.Add(ItemList);//添加進來
                    }
                }
                else//如果當前TreeView的父結點不為空，把點擊的結點，做為一個目錄文件的總結點
                {
                    foreach (string DirName in Directory.GetDirectories((string)NodeDir.Tag))//編歷當前分區或文件夾所有目錄
                    {
                        ListViewItem ItemList = new ListViewItem(DirName);
                        listView1.Items.Add(ItemList);
                    }
                    foreach (string FileName in Directory.GetFiles((string)NodeDir.Tag))//編歷當前分區或文件夾所有目錄的文件
                    {
                        ListViewItem ItemList = new ListViewItem(FileName);
                        listView1.Items.Add(ItemList);
                    }
                }
            }
            catch { }
        }

        private void ListViewShow(string DirFileName)//獲取當有文件夾內的文件和目錄
        {
            listView1.Clear();
            try
            {
                foreach (string DirName in Directory.GetDirectories(DirFileName))
                {
                    ListViewItem ItemList = new ListViewItem(DirName);
                    listView1.Items.Add(ItemList);
                }
                foreach (string FileName in Directory.GetFiles(DirFileName))
                {
                    ListViewItem ItemList = new ListViewItem(FileName);
                    listView1.Items.Add(ItemList);
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

        void setup_treeView1()
        {
            treeView1.AfterSelect += new TreeViewEventHandler(treeView1_AfterSelect);

        }

        void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            ListViewShow(e.Node);
            TreeViewShow(e.Node);
        }

        void setup_listView1()
        {
            listView1.View = View.List;
            listView1.DoubleClick += new EventHandler(listView1_DoubleClick);
            listView1.SelectedIndexChanged += new EventHandler(listView1_SelectedIndexChanged);
        }

        void listView1_DoubleClick(object sender, EventArgs e)
        {
            foreach (int ListIndex in listView1.SelectedIndices)
            {
                ListViewShow(listView1.Items[ListIndex].Text);
                //richTextBox1.Text += listView1.Items[ListIndex].Text + "\n";
            }
        }

        void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "listView1_SelectedIndexChanged\n";
        }
    }
}
