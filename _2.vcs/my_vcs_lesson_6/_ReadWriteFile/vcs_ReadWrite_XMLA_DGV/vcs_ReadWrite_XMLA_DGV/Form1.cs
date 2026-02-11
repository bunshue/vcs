using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_XMLA_DGV
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

        private void button0_Click(object sender, EventArgs e)
        {
            DataSet ds = new DataSet();	//建立ds屬於DataSet物件
            ds.ReadXml("../../person.xml");		//讀入person.xml文件檔
            //在dataGridView1控制項上顯示person.xml文件檔的所有資料
            dataGridView1.DataSource = ds.Tables["學生"];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DataSet ds = new DataSet();

            // 讀取XML文件並放入DataSet
            ds.ReadXml("../../person.xml");
            dataGridView1.DataSource = ds.Tables["學生"];
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            // 在學生DataTable建立學號欄位為主鍵，主鍵名稱為「PK_學號」
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);

            //3030
            //新增
            DataRow dr;
            // 尋找指定的DataRow，若找不到會傳回null

            string student_id = "123456";
            string name = "david";
            string telephone = "0912345678";
            string email = "david@lion.mouse.cat.dog";

            dr = ds.Tables["學生"].Rows.Find(student_id);
            // 若DataRow為null，表示DataTable內沒有該筆記錄
            if (dr == null)
            {
                // 新增DataRow，即新增一筆記錄
                DataRow myRow = ds.Tables["學生"].NewRow();
                myRow["學號"] = student_id;
                myRow["姓名"] = name;
                myRow["電話"] = telephone;
                myRow["信箱"] = email;
                ds.Tables["學生"].Rows.Add(myRow);
                MessageBox.Show("學號" + student_id + "這筆記錄已經在記憶體新增完成!!");
            }
            else
            {
                MessageBox.Show(student_id + "學號重複，已經有此筆記錄!!", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }

            //3030
            //修改

            student_id = "123456";
            name = "mary";
            telephone = "0912876543";
            email = "mary@lion.mouse.cat.dog";


            //DataRow dr;
            dr = ds.Tables["學生"].Rows.Find(student_id);
            if (dr == null)
            {
                MessageBox.Show("找不到學號 " + student_id + "的資料!!所以無法進行修改作業", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                //修改記錄
                dr["姓名"] = name;
                dr["電話"] = telephone;
                dr["信箱"] = email;
                MessageBox.Show("學號" + student_id + "這筆記錄已經在記憶體更新完成!!");
            }

            //3030
            //刪除
            //DataRow dr;
            dr = ds.Tables["學生"].Rows.Find(student_id);
            if (dr == null)
            {
                MessageBox.Show("找不到學號 " + student_id + "的資料!!所以無法進行刪除作業", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                // 刪除記錄
                ds.Tables["學生"].Rows.Remove(dr);
                MessageBox.Show("學號" + student_id + "這筆記錄已經在記憶體刪除完成!!");
            }

            //3030
            //儲存

            // 將DataSet的資料一次寫回XML文件
            ds.WriteXml("tmp_person_new.xml");
            MessageBox.Show("成功的將資料更新到XML檔");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DataSet ds = new DataSet();
            ds.ReadXml("../../person.xml");  //將person.xml讀入至ds
            //建立學號為學生DataTable的主鍵
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);
            //DataRowCollection的Find方法搜尋txtSearchId主鍵資料
            string student_id = "9096003";
            DataRow dr = ds.Tables["學生"].Rows.Find(student_id);
            //判斷dr是否為null
            if (dr == null)
            {
                // 找不到學生記錄執行此處
                richTextBox1.Text = "沒有學號 " + student_id + " 的學生";
                return;
            }
            else
            {
                // 找到學生記錄執行此處
                richTextBox1.Text += "學號：" + dr["學號"] + Environment.NewLine;
                richTextBox1.Text += "姓名：" + dr["姓名"] + Environment.NewLine;
                richTextBox1.Text += "電話：" + dr["電話"] + Environment.NewLine;
                richTextBox1.Text += "信箱：" + dr["信箱"];
            }
        }
    }
}

