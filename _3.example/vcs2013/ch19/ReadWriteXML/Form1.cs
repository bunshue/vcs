using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;

namespace ReadWriteXML
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        DataSet ds = new DataSet();
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            // 讀取XML文件並放入DataSet
            ds.ReadXml("person.xml");
            dataGridView1.DataSource = ds.Tables["學生"];
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            // 在學生DataTable建立學號欄位為主鍵，主鍵名稱為「PK_學號」
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);
        }
        // 按 [新增] 鈕執行此事件
        private void btnAdd_Click(object sender, EventArgs e)
        {
            DataRow dr;
            // 尋找指定的DataRow，若找不到會傳回null
            dr = ds.Tables["學生"].Rows.Find(txtId.Text);
            // 若DataRow為null，表示DataTable內沒有該筆記錄
            if (dr == null)
            {
                // 新增DataRow，即新增一筆記錄
                DataRow myRow = ds.Tables["學生"].NewRow();
                myRow["學號"] = txtId.Text;
                myRow["姓名"] = txtName.Text;
                myRow["電話"] = txtTel.Text;
                myRow["信箱"] = txtMail.Text;
                ds.Tables["學生"].Rows.Add(myRow);
                MessageBox.Show("學號" + txtId.Text + "這筆記錄已經在記憶體新增完成!!");
            }
            else
            {
                MessageBox.Show(txtId.Text + "學號重複，已經有此筆記錄!!", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
        // 按 [更新] 鈕執行此事件 
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            DataRow dr;
            dr = ds.Tables["學生"].Rows.Find(txtId.Text);
            if (dr == null)
            {
                MessageBox.Show("找不到學號 " + txtId.Text + "的資料!!所以無法進行修改作業", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                //修改記錄
                dr["姓名"] = txtName.Text;
                dr["電話"] = txtTel.Text;
                dr["信箱"] = txtMail.Text;
                MessageBox.Show("學號" + txtId.Text + "這筆記錄已經在記憶體更新完成!!");
            }
        }
        // 按 [刪除] 鈕執行此事件 
        private void btnDel_Click(object sender, EventArgs e)
        {
            DataRow dr;
            dr = ds.Tables["學生"].Rows.Find(txtId.Text);
            if (dr == null)
            {
                MessageBox.Show("找不到學號 " + txtId.Text + "的資料!!所以無法進行刪除作業", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                // 刪除記錄
                ds.Tables["學生"].Rows.Remove(dr);
                MessageBox.Show("學號" + txtId.Text + "這筆記錄已經在記憶體刪除完成!!");
            }
        }
        // 按 [整批更新] 鈕執行此事件 
        private void btnAllUpdate_Click(object sender, EventArgs e)
        {
            // 將DataSet的資料一次寫回XML文件
            ds.WriteXml("person.xml");
            MessageBox.Show("成功的將資料更新到XML檔");
        }
    }
}
