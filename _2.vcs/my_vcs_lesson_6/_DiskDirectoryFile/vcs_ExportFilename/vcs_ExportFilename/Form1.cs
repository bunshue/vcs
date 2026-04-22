using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ExportFilename
{
    public partial class Form1 : Form
    {
        string foldername = string.Empty;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.GridLines = true;
            listView1.View = View.Details;
            //listView1.Columns.Add(new ColumnHeader("aaaa"));

            //設定欄位
            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "檔案名稱";
            ch1.Width = 500;
            listView1.Columns.Add(ch1);

            listView1.SelectedIndexChanged += new EventHandler(listView1_SelectedIndexChanged);
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            listView1.Size = new Size(700, 400);
            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Size = new Size(700, 300);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 890);
            this.Text = "vcs_ExportFilename";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count != 0)
            {
                FileInfo myFile = new FileInfo(listView1.SelectedItems[0].Text);//创建FileInfo对象
                //定义一个字符串数组，用来存储文件的相关属性
                string[] strAttribute = new string[] { myFile.Name, Convert.ToDouble(myFile.Length / 1024).ToString(), myFile.Extension, myFile.CreationTime.ToString(), myFile.IsReadOnly.ToString(), myFile.LastWriteTime.ToString() };
                var values = from str in strAttribute//使用LINQ为文件属性赋值
                             select new
                             {
                                 Name = strAttribute[0].ToString(),
                                 Size = strAttribute[1].ToString(),
                                 Exten = strAttribute[2].ToString(),
                                 CTime = strAttribute[3].ToString(),
                                 ReadOnly = strAttribute[4].ToString(),
                                 WTime = strAttribute[5].ToString()
                             };
                foreach (var v in values)
                {
                    //richTextBox1.Text += "aaaa"+
                    richTextBox1.Text += "檔名 : " + v.Name.ToString() + "\n";//显示文件名
                    richTextBox1.Text += "大小 : " + v.Size.ToString() + "\n";//显示文件大小
                    richTextBox1.Text += "副檔名 : " + v.Exten.ToString() + "\n";//显示文件扩展名
                    richTextBox1.Text += "建立時間 : " + v.CTime.ToString() + "\n";//显示文件创建时间
                    richTextBox1.Text += "修改時間 : " + v.WTime.ToString() + "\n";//显示文件最后修改时间
                    richTextBox1.Text += "是否唯讀 : " + v.ReadOnly.ToString() + "\n";//显示文件是否只读
                }
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //選取資料夾
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                listView1.Items.Clear();
                foldername = folderBrowserDialog1.SelectedPath;
                List<FileInfo> myFiles = new List<FileInfo>();//创建List泛型对象
                foreach (string strFile in Directory.GetFiles(foldername))//遍历选择文件夹中的所有文件
                {
                    myFiles.Add(new FileInfo(strFile));//将遍历的所有文件添加到List对象中
                }
                var values = from strFile in myFiles//使用LINQ从List对象中查找文件
                             group strFile by strFile.Extension into FExten
                             orderby FExten.Key
                             select FExten;
                foreach (var vFiles in values)
                {
                    foreach (var f in vFiles)
                    {
                        listView1.Items.Add(f.FullName);
                    }
                }
            }
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
    }
}
