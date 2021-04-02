using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace DataAbduct
{
    public partial class Form1 : Form
    {
        DataTable dt = null;
        TextBox[] txtBox;
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            showList();
        }
        private void showList()
        {
            listView1.View = View.Details;//圖示
            listView1.GridLines = true;//網格線
            using (SqlDataAdapter da = new SqlDataAdapter("select * from 帳單", con))
            {
                //產生結果集
                dt = new DataTable();
                da.Fill(dt);
                ColumnHeader ch;
                for (int i = 0; i < dt.Columns.Count; i++)//列
                {
                    ch = new ColumnHeader();
                    ch.Text = dt.Columns[i].ColumnName.ToString();
                    ch.Name = dt.Columns[i].ColumnName.ToString();
                    ch.Width = 72;
                    this.listView1.Columns.Add(ch);
                }
                //建立結構
                Method(dt);
            }
        }
        private void tbADD_Click(object sender, EventArgs e)
        {
            if (dt != null)
            {
                DataRow row;
                txtBox = new TextBox[6];
                txtBox[0] = this.textBox1;
                txtBox[1] = this.textBox2;
                txtBox[2] = this.textBox3;
                txtBox[3] = this.textBox4;
                txtBox[4] = this.textBox5;
                txtBox[5] = this.textBox6;
                row = dt.NewRow();
                for (int i = 0; i < dt.Columns.Count; i++)
                {
                    row[dt.Columns[i].ToString()] = this.txtBox[i].Text.ToString();
                }
                dt.Rows.Add(row);
                Method(dt);
            }
        }

        private void Method(DataTable dt)
        {
            listView1.Items.Clear();
            ListViewItem listItem = null;
            for (int j = 0; j < dt.Rows.Count; j++)
            {
                listItem = new ListViewItem(dt.Rows[j][0].ToString());
                for (int k = 1; k < dt.Columns.Count; k++)
                {
                    listItem.SubItems.Add(dt.Rows[j][k].ToString());
                }
                listView1.Items.Add(listItem);
            }
        }

        private void tbSave_Click(object sender, EventArgs e)
        {
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                SqlCommand command = new SqlCommand("INSERT INTO 帳單 " +
                "VALUES (@員工姓名, @基本工資,@獎金,@扣款,@午餐,@實際工資)", con);
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 10, "員工姓名");
                command.Parameters.Add("@基本工資", SqlDbType.VarChar, 10, "基本工資");
                command.Parameters.Add("@獎金", SqlDbType.VarChar, 10, "獎金");
                command.Parameters.Add("@扣款", SqlDbType.VarChar, 10, "扣款");
                command.Parameters.Add("@午餐", SqlDbType.VarChar, 10, "午餐");
                command.Parameters.Add("@實際工資", SqlDbType.VarChar, 10, "實際工資");
                da.InsertCommand = command;
                da.Update(dt);
                MessageBox.Show("以成功能將訊息解析回資料庫");
            }

        }


    }
}