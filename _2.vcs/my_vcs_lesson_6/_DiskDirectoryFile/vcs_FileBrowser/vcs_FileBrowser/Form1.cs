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
            show_item_location();

            //------------------------------------------------------------  # 60個

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

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1280, 750);
            this.Text = "vcs_LINQ1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/
