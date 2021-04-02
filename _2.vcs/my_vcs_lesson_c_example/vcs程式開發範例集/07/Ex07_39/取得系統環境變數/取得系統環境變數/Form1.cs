using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Collections;

namespace 取得系統環境變數
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.Details;
            listView1.GridLines = true;
            listView1.Columns.Add("環境變數", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("變數值", 150, HorizontalAlignment.Left);
            ListViewItem myItem;
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                myItem = new ListViewItem(DEntry.Key.ToString(), 0);
                myItem.SubItems.Add(DEntry.Value.ToString());
                listView1.Items.Add(myItem);
            }
        }
    }
}