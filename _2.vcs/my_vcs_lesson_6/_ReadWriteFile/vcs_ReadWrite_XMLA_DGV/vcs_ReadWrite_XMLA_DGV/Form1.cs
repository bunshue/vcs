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

        //------------------------------------------------------------  # 60個

        DataSet studentsDataSet;
        DataTable studentTable;
        DataRow newRow;

        private void button4_Click(object sender, EventArgs e)
        {
            //讀取XML文件
            studentsDataSet = new DataSet();
            studentsDataSet.ReadXml(@"../../XmlDocument-432.xml");
            studentTable = studentsDataSet.Tables["studentTable"];

            dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];

            int id = Convert.ToInt32(dataGridView1.Rows[0].Cells[0].Value);
            textBox1.Text = id.ToString();

            string name = (string)dataGridView1.Rows[0].Cells[1].Value;
            textBox2.Text = name;

            string school = (string)dataGridView1.Rows[0].Cells[2].Value;
            textBox3.Text = school;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //寫入XML文件
            studentsDataSet.WriteXml(@"tmp_XmlDocument.xml");
            MessageBox.Show("成功寫入");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //新增
            newRow = studentsDataSet.Tables["studentTable"].NewRow();
            newRow["id"] = Convert.ToInt32(textBox1.Text);
            newRow["姓名"] = textBox2.Text;
            newRow["學歷"] = textBox3.Text;
            studentsDataSet.Tables["StudentTable"].Rows.Add(newRow);
            studentsDataSet.Tables["studentTable"].AcceptChanges();

            dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //修改
            bool isFound = false;// 是否找到要修改的記錄
            bool isModified = false;// 找到的記錄是否已被修改
            for (int i = 0; i < studentsDataSet.Tables["studentTable"].Rows.Count; i++)
            {
                string wantModified = studentsDataSet.Tables["studentTable"].Rows[i][0].ToString();
                if (textBox1.Text == wantModified)
                {
                    isFound = true;
                    if (MessageBox.Show("是否修改？", "小心", MessageBoxButtons.OKCancel) == DialogResult.OK)
                    {
                        isModified = true;
                        studentsDataSet.Tables["studentTable"].Rows[i][1] = textBox2.Text;
                        studentsDataSet.Tables["studentTable"].Rows[i][2] = textBox3.Text;
                        MessageBox.Show("編號 " + textBox1.Text + " 已修改");
                    }
                    break;
                }
            }

            if (isFound & isModified)
            {
                dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];
            }
            else
            {
                if (!isFound)
                {
                    MessageBox.Show("找不到編號 " + textBox1.Text + " 的資料 !!!");
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //刪除
            bool isFound = false;// 是否找到要修改的記錄
            bool isDeleted = false;// 找到的記錄是否已被刪除
            for (int i = 0; i < studentsDataSet.Tables["studentTable"].Rows.Count; i++)
            {
                string wantDeleted = studentsDataSet.Tables["studentTable"].Rows[i][0].ToString();
                if (textBox1.Text == wantDeleted)
                {
                    isFound = true;
                    if (MessageBox.Show("是否刪除？", "小心", MessageBoxButtons.OKCancel) == DialogResult.OK)
                    {
                        isDeleted = true;
                        string currentID = textBox1.Text;
                        studentsDataSet.Tables["studentTable"].Rows[i].Delete();
                        MessageBox.Show("編號 " + currentID + " 已刪除");
                    }
                    break;
                }
            }

            if (isFound & isDeleted)
            {
                dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];
            }
            else
            {
                if (!isFound)
                {
                    MessageBox.Show("找不到編號 " + textBox1.Text + " 的資料 !!!");
                }
            }
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            int id = Convert.ToInt32(dataGridView1.Rows[e.RowIndex].Cells[0].Value);
            textBox1.Text = id.ToString();

            string name = (string)dataGridView1.Rows[e.RowIndex].Cells[1].Value;
            textBox2.Text = name;

            string school = (string)dataGridView1.Rows[e.RowIndex].Cells[2].Value;
            textBox3.Text = school;
        }

        //------------------------------------------------------------  # 60個
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/

