using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh9_2_3_11
{
    public partial class Form1 : Form
    {
        DataSet studentsDataSet;
        DataView view;

        public Form1()
        {
            InitializeComponent();
        }

        private void MakeDataTable()
        {
            // 建構DataSet及其組成分子
            studentsDataSet = new DataSet("StudentsDataSet");
            DataTable studentTable = new DataTable("StudentTable");

            // 這個資料表的資料列中的初始開始大小。預設值為 50。
            studentTable.MinimumCapacity = 50;

            // 建構資料欄
            DataColumn idColumn = new DataColumn("編號", 
                Type.GetType("System.Int32"));
            // 設定「編號」資料欄為自動增加數值
            idColumn.AutoIncrement = true;
            DataColumn nameColumn = new DataColumn("姓名");
            DataColumn schoolColumn = new DataColumn("學歷");

            studentTable.Columns.Add(idColumn);
            studentTable.Columns.Add(nameColumn);
            studentTable.Columns.Add(schoolColumn);

            studentsDataSet.Tables.Add(studentTable);

            // 加入記錄
            DataRow newRow;
            newRow = studentTable.NewRow();
            newRow["姓名"] = "唐三藏";
            newRow["學歷"] = "碩士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "孫悟空";
            newRow["學歷"] = "學士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "豬八戒";
            newRow["學歷"] = "高中";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "牛魔王";
            newRow["學歷"] = "學士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "如來佛";
            newRow["學歷"] = "博士";
            studentTable.Rows.Add(newRow);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MakeDataTable();
            comboBox1.Items.AddRange(new object[] { "博士", "碩士", "學士", "高中" });
            comboBox2.Items.AddRange(new object[] { "博士", "碩士", "學士", "高中" });
        }

        private void button1_Click(object sender, EventArgs e)
        {
            view = new DataView();
            view.Table = studentsDataSet.Tables["StudentTable"];
            view.AllowDelete = true;
            view.AllowEdit = true;
            view.AllowNew = true;
            view.RowFilter = "學歷 = '博士'";
            view.Sort = "編號 DESC";

            // 繫結至可繫結元件
            textBox1.DataBindings.Add("Text", view, "姓名");
            dataGridView1.DataSource = view;

            button1.Enabled = false;
            label3.Text = "資料筆數：" + view.Count.ToString();
            ShowAllows();
        }

        private void ShowAllows()
        {
            label4.Text = "是否可用 AddNew ()->" + (view.AllowNew ? "是" : "否");
            label5.Text = "是否允許編輯->" + (view.AllowEdit ? "是" : "否");
            label6.Text = "是否允許刪除->" + (view.AllowDelete ? "是" : "否");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 清除RowFilter的屬性，並重新顯示應有的記錄筆數
            view.RowFilter = "";
            label3.Text = "資料筆數：" + view.Count.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            DataRowView rowView = view.AddNew();

            // 新增DataRow.
            rowView["姓名"] = textBox2.Text;
            // 亦可使用DataRowView的Row屬性來替代
            // rowView["學歷"]  = comboBox2.Text;
            rowView.Row[2] = comboBox2.Text;

            MessageBox.Show("DataRowView.IsNew:->" + rowView.IsNew.ToString(),"新增資料");
            rowView.EndEdit();
            MessageBox.Show("DataRowView.IsNew:->" + rowView.IsNew.ToString(),"新增資料");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 將排序的鍵值指定為「姓名」，方便利用使用者在TextBox中輸入的姓名
            // 找出其所在的列。
            view.Sort = "姓名";
            int i = view.Find(textBox1.Text);

            // 還原排序的鍵值
            RestoreKey();

            view[i].BeginEdit();
            view[i]["姓名"] = textBox2.Text;
            view[i]["學歷"] = comboBox2.Text;
            if (MessageBox.Show("是否要修改 " + textBox1.Text + " 這筆資料？", "小心",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Exclamation) == DialogResult.OK)
            {
                view[i].EndEdit();
            }
            else
            {
                view[i].CancelEdit();
            }
            dataGridView1.Refresh();
        }

        private void RestoreKey()
        {
            if (checkBox1.Checked)
                view.Sort = "編號 ASC";
            else
                view.Sort = "編號 DESC";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show(
                "是否刪除 " + textBox1.Text + " 這筆資料？", 
                "小心",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Exclamation) == DialogResult.OK)
            {

                DataRowView row;
                DataView view = (DataView)dataGridView1.DataSource;
                row = view[dataGridView1.CurrentCell.RowIndex];
                row.Delete();
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            view.RowFilter = "學歷 = '" + comboBox1.Text + "'";
            label3.Text = "資料筆數：" + view.Count.ToString();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
             if (checkBox1.Checked)
                view.Sort = "編號 ASC";
            else
                view.Sort = "編號 DESC";
        }
    }
}
