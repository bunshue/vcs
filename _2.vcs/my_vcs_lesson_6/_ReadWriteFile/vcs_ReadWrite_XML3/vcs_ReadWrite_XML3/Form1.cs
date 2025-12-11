using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_XML3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\person.xml";

            DataSet ds = new DataSet();	//建立ds屬於DataSet物件
            ds.ReadXml(filename);		//讀入person.xml文件檔
            //在dataGridView1控制項上顯示person.xml文件檔的所有資料
            dataGridView1.DataSource = ds.Tables["學生"];
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\person.xml";
            DataSet ds = new DataSet();	//建立ds屬於DataSet物件
            ds.ReadXml(filename);		//讀入person.xml文件檔
            //在dataGridView1控制項上顯示person.xml文件檔的所有資料
            dataGridView1.DataSource = ds.Tables["老師"];
        }

        //以學號搜尋學生資料
        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\person.xml";
            DataSet ds = new DataSet();
            ds.ReadXml(filename);  //將person.xml讀入至ds
            //建立學號為學生DataTable的主鍵
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);
            //DataRowCollection的Find方法搜尋txtSearchId主鍵資料
            DataRow dr = ds.Tables["學生"].Rows.Find(textBox1.Text);
            //判斷dr是否為null
            if (dr == null)
            {
                // 找不到學生記錄執行此處
                richTextBox1.Text += "沒有學號 " + textBox1.Text + " 的學生\n";
                return;
            }
            else
            {
                // 找到學生記錄執行此處
                richTextBox1.Text += "學號：" + dr["學號"] + "\n";
                richTextBox1.Text += "姓名：" + dr["姓名"] + "\n";
                richTextBox1.Text += "電話：" + dr["電話"] + "\n";
                richTextBox1.Text += "信箱：" + dr["信箱"] + "\n";
            }
        }
    }
}
