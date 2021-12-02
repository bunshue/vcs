using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewL_AddFiles
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            listView1.GridLines = true;

            listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("檔名1", 400, HorizontalAlignment.Left);

            
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);


        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.Items.Add("aaaaaaaa1");
            listView1.Items.Add("aaaaaaaa2");
            listView1.Items.Add("aaaaaaaa3");
            listView1.Items.Add("aaaaaaaa4");
            listView1.Items.Add("aaaaaaaa5");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.CheckFileExists = true;
            openFileDialog1.ValidateNames = true;   //只接收有效的文件名
            openFileDialog1.Multiselect = true;     //允許一次選擇多個文件
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                int len = openFileDialog1.FileNames.Length;
                if (len > 0)
                {
                    int i;
                    for (i = 0; i < len; i++)
                    {
                        listView1.Items.Add(openFileDialog1.FileNames[i]);
                    }

                }


                //listView1.Items.AddRange(new ListViewItem[] { item1, item2, item3, item4 });
                //listView1.Items.AddRange((ListViewItem[])(openFileDialog1.FileNames));
                //listView1.Items.AddRange(openFileDialog1.FileNames);
                //listView1.Items.AddRange(openFileDialog1.FileNames);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int len = listView1.Items.Count;
            //show
            if (len > 0)
            {
                for (int i = 0; i < len; i++)
                {
                    richTextBox1.Text += listView1.Items[i].ToString() + "\n";
                }

            }
            else
            {
                richTextBox1.Text += "無項目\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();
        }
    }
}
