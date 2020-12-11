using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DirectoryInfo

//加入一個ImageList/屬性/images/打開(集合)/影像集合編輯器/加入影像
//treeView1/屬性/ImageList/加入imageList1

namespace vcs_TreeView2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Go up two directories and build a TreeView from there.
        private void Form1_Load(object sender, EventArgs e)
        {
            //string dir = Path.Combine(Environment.CurrentDirectory, "..\\..");
            string dir = "C:\\______test_files\\";

            DirectoryInfo dir_info = new DirectoryInfo(dir);

            treeView1.LoadFromDirectory(dir_info.FullName, 0, 1);
            treeView1.ExpandAll();
            treeView1.SelectedNode = treeView1.Nodes[0];

        }
    }
}
