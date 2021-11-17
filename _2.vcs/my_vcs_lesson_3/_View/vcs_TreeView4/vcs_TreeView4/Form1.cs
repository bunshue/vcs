using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_TreeView4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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

    }
}
