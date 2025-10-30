using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DirectoryInfo

//參考 / 加入參考 / .NET  System.Management
using System.Management;

//加入一個ImageList/屬性/Images/打開(集合)/影像集合編輯器/加入影像
//treeView4/屬性/ImageList/加入imageList1

namespace vcs_TreeView0
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


            setup_treeView2();
            setup_treeView3();
            setup_treeView4();
            setup_treeView5();
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
            button1.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(x_st + dx * 3 + 155, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1430, 840);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

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

            //string dir = Path.Combine(Environment.CurrentDirectory, "..\\..");
            string dir = @"D:\_git\vcs\_1.data\______test_files1\";

            DirectoryInfo dir_info = new DirectoryInfo(dir);

            treeView4.LoadFromDirectory(dir_info.FullName, 0, 1);
            treeView4.ExpandAll();
            treeView4.SelectedNode = treeView4.Nodes[0];
        }

        string dir_name = @"D:\_git\vcs\_1.data\______test_files1\_case1";

        void setup_treeView5()
        {
            label5.Text = "由程式中加入Node";

            treeView5.Nodes.Clear();
            SearchDir(treeView5.Nodes, dir_name);
            treeView5.ExpandAll();  //展開所有項目
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
