using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//方案總管/右鍵/加入/新增項目/類別/預設Class1.cs改成Person.cs

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Person p1 = new Person();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //在Form1_Load時把資料讀出來
            txtDirectory.Text = Properties.Settings.Default.Directory;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Default firstname = " + p1.FirstName + "\n";
            //讀FirstName
            p1.FirstName = "FN"; //寫firstname
            richTextBox1.Text += "set new firstname = " + p1.FirstName + "\n";
            //p1.LastName ="LN";
            //由於LastName不可寫，因此此行會顯示readonly無法編譯
            richTextBox1.Text += "Default lastname = " + p1.LastName + "\n";
            p1.Age = 5;
            richTextBox1.Text += "condition change Age = " + p1.Age + "\n";
            p1.Age = 20;
            richTextBox1.Text += "condition change Age =" + p1.Age + "\n";
            richTextBox1.Text += "Default sex =" + p1.Sex + "\n";
            p1.Sex = "male";
            richTextBox1.Text += "set new sex =" + p1.Sex + "\n";
            //p1.ADDR = "123"; ADDR不可寫，因此此行會顯示readonly無法編譯



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Person p1 = new Person();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (txtDirectory.Text == "")
            {
                folderBrowserDialog1.SelectedPath = "c:\\______test_files";  //預設開啟的路徑
            }
            else
            {
                folderBrowserDialog1.SelectedPath = txtDirectory.Text;  //預設開啟的路徑
            }

            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                txtDirectory.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "dir = " + Properties.Settings.Default.Directory + "\n";
        }

        //在Form1_FormClosing時把資料存起來
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Directory = txtDirectory.Text;
            Properties.Settings.Default.Save();
        }

    }
}
