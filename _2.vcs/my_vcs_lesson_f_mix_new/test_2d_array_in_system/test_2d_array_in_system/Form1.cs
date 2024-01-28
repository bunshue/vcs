using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Collections;   //for ArrayList

namespace test_2d_array_in_system
{
    public partial class Form1 : Form
    {
        ArrayList pdf_filename_ArrayListData = new ArrayList();

        string current_directory_pdf = Directory.GetCurrentDirectory();
        string pdf_filename = string.Empty;
        string pdf_filename_short = string.Empty;


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "讀出系統變數至ArrayList\n";

            pdf_filename_ArrayListData = Properties.Settings.Default.pdf_filenames;

            show_pdf_filename_ArrayListData();
        }


        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy; ;

            //button
            x_st = 20;
            y_st = 30;
            dx = 130;
            dy = 80;


            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button5.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 4);


            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //清除ArrayList
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_pdf_filename_ArrayListData();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入一筆資料至ArrayList\n";
            //pdf_filename_ArrayListData.Add(DateTime.Now.ToString());
            pdf_filename_ArrayListData.Insert(0, DateTime.Now.ToString()); //插入一個元素
            richTextBox1.Text += "目前ArrayList內共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將ArrayList寫入系統變數\n";
            Properties.Settings.Default.pdf_filenames = pdf_filename_ArrayListData;
            Properties.Settings.Default.Save();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀出系統變數至ArrayList\n";

            //將系統變數讀出
            //string[] myStringArray = Properties.Settings.Default.StringArraySetting;

            //string[] myStringArray = Properties.Settings.Default.pdf_filenames;

            //  string save_data_path = Properties.Settings.Default.save_data_path;
            //            richTextBox1.Text += Properties.Settings.Default.pdf_filenames + "\n";

            pdf_filename_ArrayListData = Properties.Settings.Default.pdf_filenames;

            show_pdf_filename_ArrayListData();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //檢查ArrayList
            string new_data = "2024/1/27 上午 03:41:01";
            update_pdf_filename_ArrayListData(new_data);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //開啟檔案

            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Title = "開啟pdf檔案";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.pdf";
            openFileDialog1.Filter = "pdf檔(*.pdf)|*.pdf";
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            //openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
            openFileDialog1.InitialDirectory = current_directory_pdf;
            //openFileDialog1.InitialDirectory = @"D:\______C_data1\_______doc\doc1";
            openFileDialog1.Multiselect = false;    //單選

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                /*
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                */

                show_item_location();
                pdf_filename = openFileDialog1.FileName;
                pdf_filename_short = Path.GetFileName(pdf_filename);
                current_directory_pdf = Path.GetDirectoryName(pdf_filename);

                richTextBox1.Text += "長檔案 : " + pdf_filename + "\n";
                richTextBox1.Text += "短檔名 : " + pdf_filename_short.ToString() + "\n";


                richTextBox1.Text += "加入一筆資料至ArrayList\n";
                pdf_filename_ArrayListData.Insert(0, pdf_filename); //插入一個元素
                richTextBox1.Text += "目前ArrayList內共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";
            }
            else
            {
                pdf_filename = "";
                current_directory_pdf = Directory.GetCurrentDirectory();
            }
            //this.Focus();
            this.KeyPreview = true;
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

        void show_pdf_filename_ArrayListData()
        {
            richTextBox1.Text += "顯示ArrayList資料\n";
            richTextBox1.Text += "共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";

            int i = 0;
            /*
            for (i = 0; i < pdf_filename_ArrayListData.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + pdf_filename_ArrayListData[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in pdf_filename_ArrayListData)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }
        }

        void update_pdf_filename_ArrayListData(string new_data)
        {
            new_data = "2024/1/27 上午 03:41:01";

            bool flag_file_exists = false;
            foreach (string str_name in pdf_filename_ArrayListData)
            {
                if (new_data == str_name)
                {
                    flag_file_exists = true;
                }
            }

            if (flag_file_exists == true)
            {
                richTextBox1.Text += "找到一樣的項目\n";
                richTextBox1.Text += "將此項目刪除\n";

                pdf_filename_ArrayListData.Remove(new_data);

                pdf_filename_ArrayListData.Insert(0, new_data); //插入一個元素
            }
        }
    }
}

