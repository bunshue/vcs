using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DirectoryInfo, 對文件進行操作

//參考 / 加入參考 / .NET  System.Management
using System.Management;

//加入一個ImageList/屬性/Images/打開(集合)/影像集合編輯器/加入影像
//treeView4/屬性/ImageList/加入imageList1

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

namespace vcs_TreeView1
{
    public partial class Form1 : Form
    {
        //string foldername = Path.Combine(Environment.CurrentDirectory, "..\\..");
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\";

        public static string tempstr = "";
        string Tem_Dir = "";
        public static TreeNode TN_Docu = new TreeNode();//單個文件的節點

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            treeView0.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView1.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView2.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView3.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView4.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView5.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView6.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);
            treeView7.AfterSelect += new TreeViewEventHandler(treeView_AfterSelect);

            setup_treeView0();
            setup_treeView1();
            setup_treeView2();
            setup_treeView3();
            setup_treeView4();
            setup_treeView5();
            setup_treeView6();
            setup_treeView7();

            button1_Click(sender, e);
        }

        void show_item_location()
        {
            int W = 300;
            int H = 350;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            int dd = 30;

            treeView0.Size = new Size(W, H);
            treeView1.Size = new Size(W, H);
            treeView2.Size = new Size(W, H);
            treeView3.Size = new Size(W, H);
            treeView4.Size = new Size(W, H);
            treeView5.Size = new Size(W, H);
            treeView6.Size = new Size(W, H);
            treeView7.Size = new Size(W, H);

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd);
            label4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd);
            label6.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            label7.Location = new Point(x_st + dx * 3, y_st + dy * 1 + dd);

            treeView0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            treeView1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd + dd);
            treeView2.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            treeView3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd + dd);
            treeView4.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd);
            treeView5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd + dd);
            treeView6.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            treeView7.Location = new Point(x_st + dx * 3, y_st + dy * 1 + dd + dd);

            dy = 60 + 5;
            button0.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 4 + 150, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1580, 840);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //TreeView全摺疊
            treeView0.CollapseAll();
            treeView1.CollapseAll();
            treeView2.CollapseAll();
            treeView3.CollapseAll();
            treeView4.CollapseAll();
            treeView5.CollapseAll();
            treeView6.CollapseAll();
            treeView7.CollapseAll();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //TreeView全展開
            treeView0.ExpandAll();
            treeView1.ExpandAll();
            treeView2.ExpandAll();
            treeView3.ExpandAll();
            treeView4.ExpandAll();
            treeView5.ExpandAll();
            treeView6.ExpandAll();
            treeView7.ExpandAll();
        }

        void setup_treeView0()
        {
            label0.Text = "treeView0";
        }

        void setup_treeView1()
        {
            //讀取文件資料TreeView
            label1.Text = "從txt讀資料到TreeView";
            string file_name = Application.StartupPath + "\\test.txt";
            LoadTreeViewFromFile(file_name, treeView1);
        }

        // Load a TreeView control from a file that uses tabs
        // to show indentation.
        private void LoadTreeViewFromFile(string file_name, TreeView trv)
        {
            // Get the file's contents.
            string file_contents = File.ReadAllText(file_name);

            // Break the file into lines.
            string[] lines = file_contents.Split(
                new char[] { '\r', '\n' },
                StringSplitOptions.RemoveEmptyEntries);

            // Process the lines.
            trv.Nodes.Clear();
            Dictionary<int, TreeNode> parents =
                new Dictionary<int, TreeNode>();
            foreach (string text_line in lines)
            {
                // See how many tabs are at the start of the line.
                int level = text_line.Length -
                    text_line.TrimStart('\t').Length;

                // Add the new node.
                if (level == 0)
                    parents[level] = trv.Nodes.Add(text_line.Trim());
                else
                    parents[level] = parents[level - 1].Nodes.Add(text_line.Trim());
                parents[level].EnsureVisible();
            }

            if (trv.Nodes.Count > 0) trv.Nodes[0].EnsureVisible();
        }

        void setup_treeView2()
        {
            label2.Text = "在TreeView屬性中的Nodes加入項目";
        }

        void setup_treeView3()
        {
            label3.Text = "本機硬碟資訊TreeView";

            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject info in searcher.Get())
            {
                TreeNode node = treeView3.Nodes.Add(info["DeviceID"].ToString());
                node.Nodes.Add("Model: " + info["Model"].ToString());
                node.Nodes.Add("Interface: " + info["InterfaceType"].ToString());
                node.Nodes.Add("Serial#: " + info["SerialNumber"].ToString());
            }
            treeView3.ExpandAll();
        }

        void setup_treeView4()
        {
            label4.Text = "本機檔案資料TreeView";

            //treeView4/屬性/ImageList/加入imageList1
            treeView4.ImageList = imageList1;

            DirectoryInfo dir_info = new DirectoryInfo(foldername);

            treeView4.LoadFromDirectory(dir_info.FullName, 0, 1);
            treeView4.ExpandAll();
            treeView4.SelectedNode = treeView4.Nodes[0];
        }

        void setup_treeView5()
        {
            label5.Text = "由程式中加入Node";

            treeView5.Nodes.Clear();
            SearchDir(treeView5.Nodes, foldername);
            treeView5.ExpandAll();  //展開所有項目
        }

        void setup_treeView6()
        {
            label6.Text = "treeView6 + AfterSelect";

            TreeNode TopNode = treeView6.Nodes.Add("博主"); //建立第一个顶级节点
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

        private void treeView_AfterSelect(object sender, TreeViewEventArgs e)
        {
            richTextBox1.Text += "單擊 :" + e.Node.Text + "\n";
        }

        void setup_treeView7()
        {
            //資料夾內容TreeView
            //取得文件夾下的所有文件夾及文件的名稱

            label7.Text = "treeView7 + TreeNodeMouseClick";
            treeView7.NodeMouseDoubleClick += new TreeNodeMouseClickEventHandler(treeView7_NodeMouseDoubleClick);

            //textBox1.Text = foldername;

            tempstr = foldername;

            TreeNode TNode = new TreeNode();//實例化一個線程
            Files_Copy(treeView7, tempstr, TNode, 0);
        }

        // 傳回上一級目錄
        /// <summary>
        /// 傳回上一級目錄
        /// </summary>
        /// <param dir="string">目錄</param>
        /// <returns>傳回String對像</returns>
        public string UpAndDown_Dir(string dir)
        {
            string Change_dir = "";
            Change_dir = Directory.GetParent(dir).FullName;
            return Change_dir;
        }

        // 顯示文件夾下所有子文件夾及文件的名稱
        /// <summary>
        /// 顯示文件夾下所有子文件夾及文件的名稱
        /// </summary>
        /// <param Sdir="string">文件夾的目錄</param>
        /// <param TNode="TreeNode">節點</param>
        /// <param n="int">標識，判斷目前是文件夾，還是文件</param>
        private void Files_Copy(TreeView TV, string Sdir, TreeNode TNode, int n)
        {
            DirectoryInfo dir = new DirectoryInfo(Sdir);
            try
            {
                if (!dir.Exists)//判斷所指的文件或文件夾是否存在
                {
                    return;
                }
                DirectoryInfo dirD = dir as DirectoryInfo;//如果給定參數不是文件夾則退出
                if (dirD == null)//判斷文件夾是否為空
                {
                    return;
                }
                else
                {
                    if (n == 0)
                    {
                        TNode = TV.Nodes.Add(dirD.Name);//新增文件夾的名稱
                        TNode.Tag = 1;
                    }
                    else
                    {
                        TNode = TNode.Nodes.Add(dirD.Name);//新增文件夾裡面各文件夾的名稱
                        TNode.Tag = 1;
                    }
                }
                FileSystemInfo[] files = dirD.GetFileSystemInfos();//取得文件夾中所有文件和文件夾
                //對單個FileSystemInfo進行判斷,如果是文件夾則進行遞歸操作
                foreach (FileSystemInfo FSys in files)
                {
                    FileInfo file = FSys as FileInfo;
                    if (file != null)//如果是文件的話，進行文件的複製操作
                    {
                        FileInfo SFInfo = new FileInfo(file.DirectoryName + "\\" + file.Name);//取得文件所在的原始路徑
                        TNode.Nodes.Add(file.Name);//新增文件
                        TNode.Tag = 1;
                    }
                    else
                    {
                        string pp = FSys.Name;//取得目前搜索到的文件夾名稱
                        Files_Copy(TV, Sdir + "\\" + FSys.ToString(), TNode, 1);//如果是文件夾，則進行遞歸呼叫
                    }
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                return;
            }
        }

        private void treeView7_NodeMouseDoubleClick(object sender, TreeNodeMouseClickEventArgs e)
        {
            richTextBox1.Text += "雙擊 :" + e.Node.Text + "\n";

            if (e.Node.Tag == null)
                Tem_Dir = "";
            else
                Tem_Dir = e.Node.Tag.ToString();
            if (Tem_Dir == "")
            {
                Tem_Dir = UpAndDown_Dir(tempstr) + "\\" + e.Node.FullPath;
                richTextBox1.Text += "你點選了 " + Tem_Dir + "\n";
                //System.Diagnostics.Process.Start(Tem_Dir);
            }
        }

        // List the files and subdirectories of this directory.
        private void SearchDir(TreeNodeCollection nodes, string foldername)
        {
            TreeNode dir_node = nodes.Add(foldername);
            foreach (string filename in Directory.GetFiles(foldername))
            {
                dir_node.Nodes.Add(filename);
            }
            foreach (string subdir in Directory.GetDirectories(foldername))
            {
                SearchDir(dir_node.Nodes, subdir);
            }
        }
    }
}
