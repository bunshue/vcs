using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_4_2_11
{
    public partial class Form1 : Form
    {
        DataSet studentsDataSet;
        DataTable studentTable;
        DataRow newRow;

        public Form1()
        {
            InitializeComponent();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            studentsDataSet = new DataSet();
            studentsDataSet.ReadXml(@"c:\XmlDocument-432.xml");
            studentTable = studentsDataSet.Tables["studentTable"];

            dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];

            int id = Convert.ToInt32(dataGridView1.Rows[0].Cells[0].Value);
            textBox1.Text = id.ToString();

            string name = (string)dataGridView1.Rows[0].Cells[1].Value;
            textBox2.Text = name;

            string school = (string)dataGridView1.Rows[0].Cells[2].Value;
            textBox3.Text = school;
        }

         private void button1_Click(object sender, EventArgs e)
         {
             newRow = studentsDataSet.Tables["studentTable"].NewRow();
             newRow["id"] = Convert.ToInt32(textBox1.Text);
             newRow["姓名"] = textBox2.Text;
             newRow["學歷"] = textBox3.Text;
             studentsDataSet.Tables["StudentTable"].Rows.Add(newRow);
             studentsDataSet.Tables["studentTable"].AcceptChanges();

             dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];
         }

         private void button2_Click(object sender, EventArgs e)
         {
             bool isFound = false;// 是否找到要修改的記錄
             bool isModified = false;// 找到的記錄是否已被修改
             for (int i = 0; i < studentsDataSet.Tables["studentTable"].Rows.Count; i++)
             {
                 string wantModified = 
                     studentsDataSet.Tables["studentTable"].Rows[i][0].ToString();
                 if (textBox1.Text == wantModified)
                 {
                     isFound = true;
                     if (MessageBox.Show("是否修改？", 
                         "小心", 
                         MessageBoxButtons.OKCancel) == DialogResult.OK)
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
                 dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];
             else
                 if (!isFound)
                     MessageBox.Show("找不到編號 " + textBox1.Text + " 的資料 !!!");
         }

         private void button3_Click(object sender, EventArgs e)
         {
             bool isFound = false;// 是否找到要修改的記錄
             bool isDeleted = false;// 找到的記錄是否已被刪除
             for (int i = 0; i < studentsDataSet.Tables["studentTable"].Rows.Count; i++)
             {
                 string wantDeleted = 
                     studentsDataSet.Tables["studentTable"].Rows[i][0].ToString();
                 if (textBox1.Text == wantDeleted)
                 {
                     isFound = true;
                     if (MessageBox.Show("是否刪除？", 
                         "小心", MessageBoxButtons.OKCancel) == DialogResult.OK)
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
                 dataGridView1.DataSource = studentsDataSet.Tables["studentTable"];
             else
                 if (!isFound)
                     MessageBox.Show("找不到編號 " + textBox1.Text + " 的資料 !!!");
         }

         private void button5_Click(object sender, EventArgs e)
         {
             studentsDataSet.WriteXml(@"c:\XmlDocument.xml");
             MessageBox.Show("成功寫入");
         }

         private void button6_Click(object sender, EventArgs e)
         {
             dataGridView1.DataSource = "";
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

    }
}
