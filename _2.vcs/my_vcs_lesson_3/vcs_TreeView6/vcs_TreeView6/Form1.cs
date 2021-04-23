using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;//新增的命名空間，對文件進行操作
using System.Threading;//線程序的命名空間

namespace vcs_TreeView6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string foldername = @"C:\______test_files\";

        public static string tempstr = "";
        string Tem_Dir = "";
        private System.Threading.Thread thdAddFile; //建立一個線程
        //private System.Threading.Thread thdOddDocument; //建立一個線程
        public static TreeNode TN_Docu = new TreeNode();//單個文件的節點
        private static TreeView Tem_TView;

        public delegate void AddFile();//定義托管線程
        /// <summary>
        /// 設定托管線程
        /// </summary>
        public void SetAddFile()
        {
            this.Invoke(new AddFile(RunAddFile));//對指定的線程進行托管
        }

        /// <summary>
        /// 設定線程
        /// </summary>
        public void RunAddFile()
        {
            TreeNode TNode = new TreeNode();//實例化一個線程
            Files_Copy(treeView1, tempstr, TNode, 0);
            Thread.Sleep(0);//持起主線程
            thdAddFile.Abort();//執行線程      
        }

        #region  傳回上一級目錄
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
        #endregion

        #region  顯示文件夾下所有子文件夾及文件的名稱
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
        #endregion

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Text = foldername;
            tempstr = foldername;
            thdAddFile = new Thread(new ThreadStart(SetAddFile));   //建立一個線程
            thdAddFile.Start(); //執行目前線程
        }

        private void treeView1_NodeMouseDoubleClick(object sender, TreeNodeMouseClickEventArgs e)
        {
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

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = foldername;
            tempstr = foldername;

            Tem_TView = new TreeView();
            Tem_TView = treeView1;
        }
    }
}
