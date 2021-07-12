using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;  //for RegistryKey

using System.Reflection;    //for Assembly

using System.IO;    //for StreamReader

namespace 真的只是一個測試1
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 165;
            dy = 65;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //計算二維陣列所有元素總和
            int[,] array = new int[,] { { 0, 11, 3, 45, 17 }, { 23, 41, 5, 8, 10 }, { 9, 21, 16, 84, 51 } };

            int Total = 0;
            foreach (int element in array)
            {
                Total += element;
            }
            richTextBox1.Text += "此二維陣列的各個元素總和為: " + Total.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string strpath = Environment.SystemDirectory + "\\music";
            richTextBox1.Text += "strpath = " + strpath + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string sText = this.Text;
            string sFullName = string.Format("{0} %1", Application.ExecutablePath);
            // Application.ExecutablePath 是程式執行檔的完整路徑檔案名稱
            // %1 表示傳入的檔案
            //if (this.rbFile.Checked)
            {
                // 加入檔案右鍵選單
                RegFile(sText, sFullName);
            }
            //else
            {
                // 加入目錄右鍵選單
                //RegDirectory(sText, sFullName);
            }
            MessageBox.Show("作業成功");

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得專案內所有表單名稱

            Assembly a = Assembly.GetExecutingAssembly();       //取得目前組件

            richTextBox1.Text += "目前組件 : " + a.ToString() + "\n";
            richTextBox1.Text += "CodeBase : " + a.CodeBase.ToString() + "\n";
            richTextBox1.Text += "FullName : " + a.FullName.ToString() + "\n";
            richTextBox1.Text += "Location : " + a.Location.ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetType().ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetName() + "\n";
            richTextBox1.Text += "GetType : " + a.ImageRuntimeVersion + "\n";

            foreach (Type t in a.GetTypes())                    //找尋組件內所有類別型態
            {
                richTextBox1.Text += t.ToString() + "\n";

                if (t.IsSubclassOf(typeof(Form)))           //如果父類別是繼承自Form的話
                {
                    //richTextBox1.Text += t.ToString() + "\n"; //列出該類別資訊

                }
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //從檔案完整路徑分離出資料夾,檔案名稱,副檔名
            string full_filename = @"C:\______test_files\_case1\_case1a\_case1aa\eula.3081a.txt";
            //取得資料夾路徑
            string foldername = full_filename.Substring(0, full_filename.LastIndexOf("\\") + 1);
            //取得檔案名稱
            string short_filename =
                full_filename.Substring(full_filename.LastIndexOf("\\") + 1,
                full_filename.LastIndexOf(".") -
                (full_filename.LastIndexOf("\\") + 1));
            //取得副檔名
            string ext_filename =
                full_filename.Substring(full_filename.LastIndexOf(".") + 1,
                full_filename.Length - full_filename.LastIndexOf(".") - 1);

            richTextBox1.Text += "檔案完整路徑:\t" + full_filename + "\n";
            richTextBox1.Text += "資料夾路徑:\t" + foldername + "\n";
            richTextBox1.Text += "檔案名稱:\t" + short_filename + "\n";
            richTextBox1.Text += "副檔名:\t" + ext_filename + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //char可以存放中文字
            char[] gender = new char[5];
            gender[0] = '男';
            gender[1] = '女';
            gender[2] = '男';
            gender[3] = '男';
            gender[4] = '女';
            for (int i = 0; i < 5; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + gender[i] + "\n";

            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //一行一行讀取文字檔
            string filename = @"C:\______test_files\_case1\_case1a\_case1aa\eula.3081a.txt";

            StreamReader SReader = new StreamReader(filename, Encoding.Default);
            string strLine = string.Empty;
            while ((strLine = SReader.ReadLine()) != null)
            {
                richTextBox1.Text += strLine + "\n";
            }


        }

        private void RegFile(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"*\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue(string.Empty, sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }
        private void RegDirectory(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"directory\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue("", sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            browse_all_controls(this.Controls);
        }

        public void browse_all_controls(Control.ControlCollection cc)
        {
            foreach (Control c in cc)  //撈出所有控件
            {
                richTextBox1.Text += c.GetType().Name;

                if (c.GetType().Name == "Button")   //判斷是否為 Button 控件
                {
                    richTextBox1.Text += "\t" + ((Button)c).Text + " " + ((Button)c).Size.Width.ToString() + " X " + ((Button)c).Size.Height.ToString();

                    if (((Button)c).Tag != null)
                    {
                        richTextBox1.Text += "\t" + ((Button)c).Tag.ToString().ToString();
                    }
                }
                richTextBox1.Text += "\n";
            }
        }
    }
}
