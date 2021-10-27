using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace test_listview
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //listView1.IteMactivate += new EventHandler(listView1_IteMactivate);
            listView1.ItemActivate += new EventHandler(listView1_ItemActivate);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            createHeadersAndFillListVIEw();

            string foldername = @"C:\______test_files";

            PaintListView(foldername);
        }

        void createHeadersAndFillListVIEw()
        {
            ColumnHeader colHead;
            colHead = new ColumnHeader();
            colHead.Text = "Filename";
            listView1.Columns.Add(colHead);

            colHead = new ColumnHeader();
            colHead.Text = "Size";
            listView1.Columns.Add(colHead);

            colHead = new ColumnHeader();
            colHead.Text = "Last Accessed";
            listView1.Columns.Add(colHead);
        }

        void PaintListView(string root)
        {
            try
            {
                ListViewItem lvi;
                ListViewItem.ListViewSubItem lvsi;

                if (root.CompareTo("") == 0)
                    return;
                DirectoryInfo dir = new DirectoryInfo(root);
                DirectoryInfo[] dirs = dir.GetDirectories();
                FileInfo[] files = dir.GetFiles();


                //顯示本機文件夾及文件


                listView1.Items.Clear();


                //labPathName.Text = root;
                listView1.BeginUpdate();

                foreach (DirectoryInfo di in dirs)
                {
                    lvi = new ListViewItem();
                    lvi.Text = di.Name;
                    lvi.ImageIndex = 0;
                    lvi.Tag = di.FullName;

                    lvsi = new ListViewItem.ListViewSubItem();
                    lvsi.Text = "";

                    lvi.SubItems.Add(lvsi);

                    lvsi = new ListViewItem.ListViewSubItem();
                    lvsi.Text = di.LastAccessTime.ToString();
                    lvi.SubItems.Add(lvsi);

                    listView1.Items.Add(lvi);
                }

                foreach (FileInfo fi in files)
                {
                    lvi = new ListViewItem();
                    lvi.Text = fi.Name;
                    lvi.ImageIndex = 1;
                    lvi.Tag = fi.FullName;

                    lvsi = new ListViewItem.ListViewSubItem();
                    lvsi.Text = fi.Length.ToString();
                    lvi.SubItems.Add(lvsi);

                    listView1.Items.Add(lvi);
                }
                listView1.EndUpdate();
            }
            catch (Exception err)
            {
                MessageBox.Show("Error:" + err.Message);
            }
        }

        void listView1_ItemActivate(object sender, EventArgs e)
        {
            ListView lw = (ListView)sender; //將觸發此事件的對象轉換為該ListView對象

            string filename = lw.SelectedItems[0].Tag.ToString();
            if (lw.SelectedItems[0].ImageIndex != 0)
            {
                try
                {
                    System.Diagnostics.Process.Start(filename);
                }
                catch
                {
                    return;
                }
            }
            else
            {
                //PaintListVIEw(filename);
                //foldCol.Add(filename);
            }


        }
        

    }
}

