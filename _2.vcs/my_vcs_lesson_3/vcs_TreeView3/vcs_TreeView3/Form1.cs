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
        string dir_name = @"C:\______test_files\_case1";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            treeView1.Nodes.Clear();
            SearchDir(treeView1.Nodes, dir_name);
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
