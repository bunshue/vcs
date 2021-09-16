using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;

namespace SearchXml
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 按 [搜尋] 鈕時執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            txtResult.Text = "";
            DataSet ds = new DataSet();
            ds.ReadXml("person.xml");  //將person.xml讀入至ds
            //建立學號為學生DataTable的主鍵
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);
            //DataRowCollection的Find方法搜尋txtSearchId主鍵資料
            DataRow dr = ds.Tables["學生"].Rows.Find(txtStuId.Text);
            //判斷dr是否為null
            if (dr == null)
            {
                // 找不到學生記錄執行此處
                txtResult.Text = "沒有學號 " + txtStuId.Text + " 的學生";
                return;
            }
            else
            {
                // 找到學生記錄執行此處
                txtResult.Text += "學號：" + dr["學號"] + Environment.NewLine;
                txtResult.Text += "姓名：" + dr["姓名"] + Environment.NewLine;
                txtResult.Text += "電話：" + dr["電話"] + Environment.NewLine;
                txtResult.Text += "信箱：" + dr["信箱"] ;
            }
        }


    }
}
