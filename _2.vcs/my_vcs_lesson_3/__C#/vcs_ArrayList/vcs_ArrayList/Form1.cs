using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Collections;  // for ArrayList

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
        ArrayList myArrayList1 = new ArrayList();
        ArrayList myArrayList2 = new ArrayList();

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

            //------------------------------------------------------------  # 60個

            label1.Text = "共有 " + myArrayList1.Count.ToString() + " 個項目";

            richTextBox1.Text += "讀出系統變數至ArrayList\n";
            myArrayList2 = Properties.Settings.Default.pdf_filenames;
            //show_pdf_filename_ArrayListData(); NG
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            groupBox1.Size = new Size(410, 460);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox2.Size = new Size(410, 580);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //groupbox 裡面
            x_st = 10;
            y_st = 20;
            dx = 190 + 10;
            dy = 60 + 10;
            bt_arrayList00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_arrayList01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_arrayList02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_arrayList03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_arrayList04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_arrayList05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_arrayList06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_arrayList07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_arrayList08.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_arrayList09.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_arrayList10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_arrayList11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_arrayList12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_arrayList13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_arrayList14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            bt_arrayList15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            this.Size = new Size(1180, 750);
            this.Text = "vcs_ArrayList";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            myArrayList1.Add(textBox1.Text);
            label1.Text = "共有 " + myArrayList1.Count.ToString() + " 個項目";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            /*
            for (i = 0; i < myArrayList1.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + myArrayList1[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in myArrayList1)
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
            myArrayList1.Remove(textBox1.Text);
            label1.Text = "共有 " + myArrayList1.Count.ToString() + " 個項目";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int item = int.Parse(textBox2.Text);
            if ((item > 0) && (item <= myArrayList1.Count))
            {
                myArrayList1.RemoveAt(item - 1);      //刪除特定項目
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            myArrayList1.Sort();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            myArrayList1.Reverse();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Object tmp;
            if (textBox3.Text == "")
                return;
            tmp = textBox3.Text;  //取得所輸入的資料
            if (myArrayList1.IndexOf(tmp) < 0)
            {
                //若超過陣列索引值則表示找不到符合的資料
                richTextBox1.Text += "找不到您所輸入的資料\n";
            }
            else
            {
                richTextBox1.Text += "您所尋找的資料在第 " + (myArrayList1.IndexOf(tmp) + 1).ToString() + " 筆\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            myArrayList1.Insert(3, "David"); //插入一個元素
        }

        void show_pdf_filename_ArrayListData()
        {
            richTextBox1.Text += "顯示ArrayList資料\n";
            richTextBox1.Text += "共有 " + myArrayList2.Count.ToString() + " 個項目\n";

            int i = 0;
            /*
            for (i = 0; i < myArrayList2.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + myArrayList2[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in myArrayList2)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }
        }

        void update_pdf_filename_ArrayListData(string new_data)
        {
            new_data = "2024/1/27 上午 03:41:01";

            bool flag_file_exists = false;
            foreach (string str_name in myArrayList2)
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

                myArrayList2.Remove(new_data);

                myArrayList2.Insert(0, new_data); //插入一個元素
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
            //myArrayList2.Add(DateTime.Now.ToString());
            myArrayList2.Insert(0, DateTime.Now.ToString()); //插入一個元素
            richTextBox1.Text += "目前ArrayList內共有 " + myArrayList2.Count.ToString() + " 個項目\n";
        }

        private void bt_arrayList03_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將ArrayList寫入系統變數\n";
            Properties.Settings.Default.pdf_filenames = myArrayList2;
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

            myArrayList2 = Properties.Settings.Default.pdf_filenames;

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
                myArrayList2.Insert(0, pdf_filename); //插入一個元素
                richTextBox1.Text += "目前ArrayList內共有 " + myArrayList2.Count.ToString() + " 個項目\n";
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
            //ArrayList 1
            ArrayList myArrayList = new ArrayList();   // 非泛型

            //SortedList<string, Member> myArrayList = new SortedList<string, Member>();

            myArrayList.Add(new Member() { Name = "David", Select = true, Score = 70 });
            myArrayList.Add(new Member() { Name = "Mary", Select = false, Score = 65 });
            myArrayList.Add(new Member() { Name = "Tom", Select = true, Score = 85 });
            myArrayList.Add(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 非泛型陣列操作需強制轉換 .... \n");
            foreach (var item in myArrayList)
            {
                if (item is Member)
                {
                    Console.WriteLine("{0} ", item.ToString());
                }
                else
                {
                    Console.WriteLine("{0} ", (string)item);
                }
            }
            Console.Read();
        }

        //------------------------------------------------------------  # 60個

        // "走訪串列所有元素
        public static void PrintOut(IEnumerable tAryLst)
        { // 公開能逐一查看非泛型集合內容的一次的列舉直
            int i = 0;
            Console.WriteLine("  目前 AryLst串列內所有元素 : ");
            foreach (Object obj in tAryLst)
            {
                Console.WriteLine("    第{0}個元素 : {1} ", ++i, obj);
            }
        }

        private void bt_arrayList09_Click(object sender, EventArgs e)
        {
            //ArrayList 2

            ArrayList myArrayList = new ArrayList { "Jack", 20, true }; // 元素為不同資料型別  
            Console.WriteLine("1.設定 AryLst串列內初值 :");
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            //插入串列的最後面
            Console.WriteLine("2.插入 \"大學\" 到串列的最後面 :");
            myArrayList.Add("大學");
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            //多筆資料採陣列方式插入到串列最後面
            Console.WriteLine("3.插入\"台北\" , \"101\" 兩個元素到串列的最後面 :");
            myArrayList.AddRange(new string[] { "台北", "101" });
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            //插入到串列的第2個元素後面
            Console.WriteLine("4.插入\"Wu\" 到串列的第2個元素後面");
            myArrayList.Insert(1, "Wu");
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            //刪除串列中 "Wu" 佇個元素
            Console.WriteLine("5.移除串列中元素為 Wu");
            myArrayList.Remove("Wu");
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            //移除串列中第3個元素
            Console.WriteLine("6.移除串列中第3個元素");
            myArrayList.RemoveAt(2);
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            // 移除串列中從第3個元素開始共兩個元素
            Console.WriteLine("7.移除串列中從第3個元素開始共兩個元素");
            myArrayList.RemoveRange(2, 2);
            PrintOut(myArrayList);
            Console.WriteLine("---------------------------------------");

            // 移除串列中所有元素
            Console.WriteLine("8.移除串列中所有元素");
            myArrayList.Clear();
            Console.WriteLine("  目前 AryList 串列元素總個數 : ", myArrayList.Count);
            Console.WriteLine("---------------------------------------");
        }

        public static void PrintOut2(IEnumerable myArrayList)
        {
            int i = 0;
            foreach (Object obj in myArrayList)
            {
                Console.WriteLine("\t第{0}個元素 : {1} ", ++i, obj);
            }
        }

        private void bt_arrayList10_Click(object sender, EventArgs e)
        {
            //ArrayList 3
            ArrayList myArrayList = new ArrayList { "Jack", "Ford", "Bob", "David" };

            // 顯示ArrayList串列的初值內容(排序前）：
            Console.WriteLine(" 1. 顯示串列初值設定內容(排序前）:");
            PrintOut2(myArrayList);
            Console.WriteLine(" ---------------------------------");

            // 顯示ArrayList串列排序後內容
            myArrayList.Sort();

            Console.WriteLine(" 2.  myArrayList.Sort()由小而大做遞增排序 :");
            PrintOut2(myArrayList);
            Console.WriteLine(" ----------------------------------");

            // 顯示ArrayList串列排序後內容
            myArrayList.Reverse();
            Console.WriteLine(" 3. myArrayList.Reverse()由大而小做遞減排序 :");
            PrintOut2(myArrayList);
            Console.WriteLine(" ----------------------------------");
        }

        //------------------------------------------------------------  # 60個

        private void bt_arrayList11_Click(object sender, EventArgs e)
        {
            //ArrayList 4
            richTextBox1.Text += "建立一個ArrayList\n";

            ArrayList myArrayList = new ArrayList();

            myArrayList.Add("alive");
            myArrayList.Add("silver");
            myArrayList.Add("dog");
            myArrayList.Add("Ftp");

            //顯示在 listBox 上
            listBox1.DataSource = myArrayList;
        }

        private void bt_arrayList12_Click(object sender, EventArgs e)
        {
            //ArrayList 5
            richTextBox1.Text += "建立一個ArrayList\n";

            ArrayList myArrayList = new ArrayList();

            myArrayList.Add("Hello");
            myArrayList.Add("World");
            myArrayList.Add("!");

            richTextBox1.Text += "顯示ArrayList的內容:\n";
            richTextBox1.Text += "myArrayList\n";
            richTextBox1.Text += "    Count:    " + myArrayList.Count.ToString() + "\n";
            richTextBox1.Text += "    Capacity: " + myArrayList.Capacity.ToString() + "\n";

            richTextBox1.Text += "內容 :\n";
            foreach (Object obj in myArrayList)
            {
                richTextBox1.Text += obj.ToString() + "\n";
            }
        }

        private void bt_arrayList13_Click(object sender, EventArgs e)
        {
            //ArrayList 6
            //ArrayList 測試
            ArrayList myArrayList = new ArrayList();
            myArrayList.Add("mouse");
            myArrayList.Add("ox");
            myArrayList.Add("tiger");
            myArrayList.Add("rabbit");

            foreach (string temp in myArrayList)
            {
                richTextBox1.Text += temp + "\n";
            }
        }

        private void bt_arrayList14_Click(object sender, EventArgs e)
        {

        }

        private void bt_arrayList15_Click(object sender, EventArgs e)
        {

        }
    }

    class Member
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


