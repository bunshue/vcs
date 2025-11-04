using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DirectoryInfo, 對文件進行操作

//加入一個ImageList/屬性/Images/打開(集合)/影像集合編輯器/加入影像
//treeView/屬性/ImageList/加入imageList1

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

            setup_treeView0(treeView0);
            setup_treeView1(treeView1);
            setup_treeView2(treeView2);
            setup_treeView3(treeView3);

            button1_Click(sender, e);
        }

        void show_item_location()
        {
            int W = 350;
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

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd);
            label4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd);

            treeView0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            treeView1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd + dd);
            treeView2.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            treeView3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd + dd);
            treeView4.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd);
            treeView5.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd + dd);

            dy = 60 + 5;
            button0.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 3 + 105, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 3 + 210, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 1);

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
        }

        private void button2_Click(object sender, EventArgs e)
        {
            my_SearchDir(treeView0.Nodes, foldername);
        }

        // List the files and subdirectories of this directory.
        private void my_SearchDir(TreeNodeCollection nodes, string foldername)
        {
            richTextBox1.Text += "foldername = " + foldername + "\n";
            TreeNode dir_node = nodes.Add(foldername);
            foreach (string filename in Directory.GetFiles(foldername))
            {
                richTextBox1.Text += "filename = " + filename + "\n";
                dir_node.Nodes.Add(filename);
            }
            foreach (string subdir in Directory.GetDirectories(foldername))
            {
                richTextBox1.Text += "subdir = " + subdir + "\n";
                SearchDir(dir_node.Nodes, subdir);
            }
        }

        void setup_treeView0(TreeView tv)
        {
            label0.Text = "三國";
            tv.Nodes.Clear();//清除TreeView

            tv.Font = new Font("新細明體", 18F);

            //------------------------------------------------------------  # 60個

            //建立父節點, 魏
            TreeNode TopNode1 = tv.Nodes.Add("魏");

            //魏之曹操家, 第一代
            TreeNode ParentNode1a = new TreeNode("曹操");//基礎節點
            TopNode1.Nodes.Add(ParentNode1a);//基礎節點加入到父節點中

            //魏之曹操家, 第二代, 3人
            TreeNode ChildNode1a1 = new TreeNode("曹昂");
            TreeNode ChildNode1a2 = new TreeNode("曹丕");
            TreeNode ChildNode1a3 = new TreeNode("曹植");
            //加入到曹操的節點
            ParentNode1a.Nodes.Add(ChildNode1a1);
            ParentNode1a.Nodes.Add(ChildNode1a2);
            ParentNode1a.Nodes.Add(ChildNode1a3);

            TreeNode ChildNode1a2a = new TreeNode("曹叡");
            ChildNode1a2.Nodes.Add(ChildNode1a2a);

            //魏之司馬懿家, 第一代
            TreeNode ParentNode1b = new TreeNode("司馬懿");//基礎節點
            TopNode1.Nodes.Add(ParentNode1b);//基礎節點加入到父節點中

            //魏之司馬懿家, 第二代, 3人
            TreeNode ChildNode1b1 = new TreeNode("司馬師");
            TreeNode ChildNode1b2 = new TreeNode("司馬昭");
            TreeNode ChildNode1b3 = new TreeNode("司馬倫");
            ParentNode1b.Nodes.Add(ChildNode1b1);
            ParentNode1b.Nodes.Add(ChildNode1b2);
            ParentNode1b.Nodes.Add(ChildNode1b3);

            //魏之司馬懿家, 第三代, 1人
            TreeNode ChildNode1b2a = new TreeNode("司馬炎");
            ChildNode1b2.Nodes.Add(ChildNode1b2a);

            //------------------------------------------------------------  # 60個

            //建立父節點, 蜀
            TreeNode TopNode2 = tv.Nodes.Add("蜀");

            //蜀之劉備家, 第一代
            TreeNode ParentNode2 = new TreeNode("劉備");//基礎節點
            TopNode2.Nodes.Add(ParentNode2);//基礎節點加入到父節點中

            //蜀之劉備家, 第二代, 3人
            TreeNode ChildNode2a = new TreeNode("劉禪");
            TreeNode ChildNode2b = new TreeNode("劉永");
            TreeNode ChildNode2c = new TreeNode("劉理");
            ParentNode2.Nodes.Add(ChildNode2a);
            ParentNode2.Nodes.Add(ChildNode2b);
            ParentNode2.Nodes.Add(ChildNode2c);

            //------------------------------------------------------------  # 60個

            //建立父節點, 吳
            TreeNode TopNode3 = tv.Nodes.Add("吳");

            //吳之孫堅家, 第一代
            TreeNode ParentNode3 = new TreeNode("孫堅");//基礎節點
            TopNode3.Nodes.Add(ParentNode3);//基礎節點加入到父節點中

            //吳之孫堅家, 第二代, 2人
            TreeNode ChildNode3a = new TreeNode("孫策");
            TreeNode ChildNode3b = new TreeNode("孫權");
            ParentNode3.Nodes.Add(ChildNode3a);
            ParentNode3.Nodes.Add(ChildNode3b);

            //吳之孫堅家, 第三代, 4人
            TreeNode ChildNode3b1 = new TreeNode("孫登");
            TreeNode ChildNode3b2 = new TreeNode("孫和");
            TreeNode ChildNode3b3 = new TreeNode("孫休");
            TreeNode ChildNode3b4 = new TreeNode("孫亮");
            ChildNode3b.Nodes.Add(ChildNode3b1);
            ChildNode3b.Nodes.Add(ChildNode3b2);
            ChildNode3b.Nodes.Add(ChildNode3b3);
            ChildNode3b.Nodes.Add(ChildNode3b4);

            //------------------------------------------------------------  # 60個

            for (int i = 0; i < 3; i++)
            {
                //一個父節點加上3個子節點
                TreeNode node = tv.Nodes.Add("AAAA");
                node.Nodes.Add("BBBB");
                node.Nodes.Add("CCCC");
                node.Nodes.Add("DDDD");
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "父節點個數 tv.Nodes.Count = " + tv.Nodes.Count.ToString() + "\n";
            if (tv.Nodes.Count > 0)
            {
                tv.Nodes[0].EnsureVisible();
            }
        }

        void setup_treeView1(TreeView tv)
        {
            label1.Text = "本機檔案資料TreeView";

            //treeView/屬性/ImageList/加入imageList1
            tv.ImageList = imageList1;

            DirectoryInfo dir_info = new DirectoryInfo(foldername);

            tv.LoadFromDirectory(dir_info.FullName, 0, 1);
            tv.ExpandAll();
            tv.SelectedNode = tv.Nodes[0];
        }

        void setup_treeView2(TreeView tv)
        {
            label2.Text = "由程式中加入Node";

            tv.Nodes.Clear();//清除TreeView

            SearchDir(tv.Nodes, foldername);

            tv.ExpandAll();  //展開所有項目
        }

        private void treeView_AfterSelect(object sender, TreeViewEventArgs e)
        {
            richTextBox1.Text += "單擊 :" + e.Node.Text + "\n";
        }

        void setup_treeView3(TreeView tv)
        {
            //資料夾內容TreeView
            //取得文件夾下的所有文件夾及文件的名稱

            label3.Text = "treeView + TreeNodeMouseClick";
            tv.NodeMouseDoubleClick += new TreeNodeMouseClickEventHandler(treeView_NodeMouseDoubleClick);

            tempstr = foldername;

            TreeNode TNode = new TreeNode();//實例化一個線程
            Files_Copy(tv, tempstr, TNode, 0);
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

        private void treeView_NodeMouseDoubleClick(object sender, TreeNodeMouseClickEventArgs e)
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


//6060
//------------------------------------------------------------  # 60個

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個


