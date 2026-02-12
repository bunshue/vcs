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

/*
方案右鍵/屬性/設定
名稱 : pdf_filenames
型別 : System.Collections.ArrayList 在 mscorlib/System.Collections之下
範圍 : User
*/

namespace vcs_ArrayList
{
    public partial class Form1 : Form
    {
        ArrayList ArrayListData = new ArrayList();
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

            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";

            richTextBox1.Text += "讀出系統變數至ArrayList\n";
            pdf_filename_ArrayListData = Properties.Settings.Default.pdf_filenames;
            //show_pdf_filename_ArrayListData(); NG
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

            /*
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            */

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ArrayListData.Add(textBox1.Text);
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            /*
            for (i = 0; i < ArrayListData.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + ArrayListData[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in ArrayListData)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            ArrayListData.Remove(textBox1.Text);
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int item = int.Parse(textBox2.Text);
            if ((item > 0) && (item <= ArrayListData.Count))
            {
                ArrayListData.RemoveAt(item - 1);      //刪除特定項目
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            ArrayListData.Sort();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            ArrayListData.Reverse();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Object tmp;
            if (textBox3.Text == "")
                return;
            tmp = textBox3.Text;  //取得所輸入的資料
            if (ArrayListData.IndexOf(tmp) < 0)
            {
                //若超過陣列索引值則表示找不到符合的資料
                richTextBox1.Text += "找不到您所輸入的資料\n";
            }
            else
            {
                richTextBox1.Text += "您所尋找的資料在第 " + (ArrayListData.IndexOf(tmp) + 1).ToString() + " 筆\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            ArrayListData.Insert(3, "David"); //插入一個元素
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //建立一個ArrayList

            ArrayList list = new ArrayList();

            list.Add("alive");
            list.Add("silver");
            list.Add("dog");
            list.Add("Ftp");

            //d.SetData("para", list);

            //將制定的值賦值給應用程序域的屬性

            //foreach (string s in (ArrayList)d.GetData("para"))
            {// 獲取存在當前應用程序域中的值

                //Console.WriteLine("you will see" + s);
            }

            //顯示在 listBox 上
            listBox1.DataSource = list;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //建立和初始化 ArrayList ，以及顯示其值

            // Creates and initializes a new ArrayList.
            ArrayList myAL = new ArrayList();
            myAL.Add("Hello");
            myAL.Add("World");
            myAL.Add("!");

            // Displays the properties and values of the ArrayList.
            Console.WriteLine("myAL");
            Console.WriteLine("    Count:    {0}", myAL.Count);
            Console.WriteLine("    Capacity: {0}", myAL.Capacity);
            Console.Write("    Values:");
            PrintValues(myAL);

            richTextBox1.Text += "顯示ArrayList的內容:\n";
            richTextBox1.Text += "myAL\n";
            richTextBox1.Text += "    Count:    " + myAL.Count.ToString() + "\n";
            richTextBox1.Text += "    Capacity: " + myAL.Capacity.ToString() + "\n";
            richTextBox1.Text += "    Values: ";

            foreach (Object obj in myAL)
            {
                richTextBox1.Text += "   " + obj.ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        public static void PrintValues(IEnumerable myList)
        {
            foreach (Object obj in myList)
            {
                Console.Write("   {0}", obj);
            }
            Console.WriteLine();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //ArrayList 測試
            ArrayList animal = new ArrayList();
            string name_of_animal = string.Empty;
            name_of_animal = "mouse";
            animal.Add(name_of_animal);
            name_of_animal = "ox";
            animal.Add(name_of_animal);
            name_of_animal = "tiger";
            animal.Add(name_of_animal);
            name_of_animal = "rabbit";
            animal.Add(name_of_animal);

            foreach (string temp in animal)
            {
                richTextBox1.Text += temp + "\n";
            }
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

        private void bt_arrayList00_Click(object sender, EventArgs e)
        {
            //清除ArrayList
        }

        private void bt_arrayList01_Click(object sender, EventArgs e)
        {
            show_pdf_filename_ArrayListData();
        }

        private void bt_arrayList02_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入一筆資料至ArrayList\n";
            //pdf_filename_ArrayListData.Add(DateTime.Now.ToString());
            pdf_filename_ArrayListData.Insert(0, DateTime.Now.ToString()); //插入一個元素
            richTextBox1.Text += "目前ArrayList內共有 " + pdf_filename_ArrayListData.Count.ToString() + " 個項目\n";
        }

        private void bt_arrayList03_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將ArrayList寫入系統變數\n";
            Properties.Settings.Default.pdf_filenames = pdf_filename_ArrayListData;
            Properties.Settings.Default.Save();
        }

        private void bt_arrayList04_Click(object sender, EventArgs e)
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

        private void bt_arrayList05_Click(object sender, EventArgs e)
        {
            //檢查ArrayList
            string new_data = "2024/1/27 上午 03:41:01";
            update_pdf_filename_ArrayListData(new_data);
        }

        private void bt_arrayList06_Click(object sender, EventArgs e)
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

        private void bt_arrayList07_Click(object sender, EventArgs e)
        {

        }

        private void bt_arrayList08_Click(object sender, EventArgs e)
        {

        }

        private void bt_arrayList09_Click(object sender, EventArgs e)
        {

        }
    }
}
