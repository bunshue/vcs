using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Text.RegularExpressions;

namespace vcs_ListView6_DragDrop
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.AllowDrop = true;
            listView1.AllowDrop = true;
            listView1.View = View.Details;
            listView1.DragEnter += Files_DragEnter;//物件拖拽事件
            listView1.DragDrop += Files_DragDrop;//拖拽操作完成事件

            listView1.Columns.Add("檔案", 400, HorizontalAlignment.Center);



        }

        //檔案拖拽進入
        private void Files_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.Link;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }


        //拖拽操作完成事件
        private void Files_DragDrop(object sender, DragEventArgs e)
        {
            try
            {
                string fileName, fileExtension, fileSize, temp;
                FileInfo fi = null;
                ListViewItem lvi = null;
                Array array = (Array)e.Data.GetData(DataFormats.FileDrop);
                Regex regex = new Regex("(\\.mp3|\\.wav|\\.wma)");
                string filePath;
                for (int i = 0; i < array.Length; i++)
                {
                    filePath = array.GetValue(i).ToString();
                    richTextBox1.Text += "get file : " + filePath + "\n";
                    listView1.Items.Add(filePath);

                    /*
                    //屬於音樂檔案 且列表中不存在
                    if (regex.IsMatch(filePath) &&
                        !dic.ContainsKey(filePath))
                    {

                        InsertPlayList(out fileName, out fileExtension, out fileSize, out temp, out fi, out lvi, filePath);
                    }
                    */
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
