using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

namespace test_2d_array_in_system
{
    public partial class Form1 : Form
    {
        ArrayList ArrayListData = new ArrayList();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ArrayListData.Add(DateTime.Now.ToString());
            richTextBox1.Text += "共有 " + ArrayListData.Count.ToString() + " 個項目\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "共有 " + ArrayListData.Count.ToString() + " 個項目\n";

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
            //將ArrayList寫入系統變數
            Properties.Settings.Default.pdf_filenames = ArrayListData;
            Properties.Settings.Default.Save();



        }

        private void button4_Click(object sender, EventArgs e)
        {
            //將系統變數讀出
            //string[] myStringArray = Properties.Settings.Default.StringArraySetting;

            //string[] myStringArray = Properties.Settings.Default.pdf_filenames;

            //  string save_data_path = Properties.Settings.Default.save_data_path;
            //            richTextBox1.Text += Properties.Settings.Default.pdf_filenames + "\n";

            ArrayList aList = Properties.Settings.Default.pdf_filenames;

            int i;
            i = 0;
            foreach (string str_name in aList)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }



        }
    }
}
