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
        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

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

            listView1.Columns.Add("檔名", 120, HorizontalAlignment.Center);
            listView1.Columns.Add("完整檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("ext", 80, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 100, HorizontalAlignment.Center);
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
                //string fileName, fileExtension, fileSize, temp;
                
                Array array = (Array)e.Data.GetData(DataFormats.FileDrop);

                //richTextBox1.Text += "len = " + array.Length.ToString() + "\n"; //一次拖曳的檔案個數

                Regex regex = new Regex("(\\.mp3|\\.wav|\\.wma)");
                string filename;
                for (int i = 0; i < array.Length; i++)
                {
                    filename = array.GetValue(i).ToString();

                    FileInfo fi = new FileInfo(filename);

                    richTextBox1.Text += "fullname = " + filename + ",  name = " + fi.Name + ",  ext = " + fi.Extension + ",  size = " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                    ListViewItem lvi = new ListViewItem();
                    lvi.Text = fi.Name;
                    lvi.SubItems.AddRange(new string[] { filename, fi.Extension, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) });

                    listView1.Items.Add(lvi);

                    //屬於音樂檔案 且列表中不存在
                    if (regex.IsMatch(filename))
                    {
                        //InsertPlayList(out fileName, out fileExtension, out fileSize, out temp, out fi, out lvi, filename);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
