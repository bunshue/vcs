using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_TreeView3
{
    public partial class Form1 : Form
    {
        string dir_name = @"D:\_git\vcs\_1.data\______test_files1\_case1";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            treeView1.Nodes.Clear();
            SearchDir(treeView1.Nodes, dir_name);
            treeView1.ExpandAll();  //展開所有項目
        }

        // List the files and subdirectories of this directory.
        private void SearchDir(TreeNodeCollection nodes, string dir_name)
        {
            TreeNode dir_node = nodes.Add(dir_name);
            foreach (string filename in Directory.GetFiles(dir_name))
            {
                dir_node.Nodes.Add(filename);
            }
            foreach (string subdir in Directory.GetDirectories(dir_name))
            {
                SearchDir(dir_node.Nodes, subdir);
            }
        }


    }
}
