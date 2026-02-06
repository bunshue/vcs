using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace CommandDemo3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 建立cnstr連接字串用來連接ch17DB.mdf資料庫
        //string cnstr = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

        // 定義ShowData()方法將員工資料表所有記錄顯示於dataGridView1上
        void ShowData()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工 ORDER BY 編號 DESC", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }
        // 表單載入時執行此事件
        private void Form1_Load(object sender, EventArgs e)
        {
            ShowData();
        }
        // 按下 [新增] 鈕時執行此事件
        private void btnAdd_Click(object sender, EventArgs e)
        {
            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr;
                    cn.Open();
                    string sqlStr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資)" + "VALUES(@name, @position, @tel, @salary)";
                    SqlCommand cmd = new SqlCommand(sqlStr, cn);
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar ));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters["@name"].Value = txtName.Text;
                    cmd.Parameters["@position"].Value = txtPosition.Text;
                    cmd.Parameters["@tel"].Value = txtTel.Text;
                    cmd.Parameters["@salary"].Value = int.Parse(txtSalary.Text);
                    cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + " 新增資料發生錯誤");
            }
        }
        // 按下 [更新] 鈕執行此事件 
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr;
                    cn.Open();
                    string sqlStr = "UPDATE 員工 SET 職稱=@position," + "電話=@tel, 薪資=@salary WHERE 姓名=@name";
                    SqlCommand cmd = new SqlCommand(sqlStr, cn);
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters["@name"].Value = txtName.Text;
                    cmd.Parameters["@position"].Value = txtPosition.Text;
                    cmd.Parameters["@tel"].Value = txtTel.Text;
                    cmd.Parameters["@salary"].Value = int.Parse(txtSalary.Text);
                    cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + " 修改資料發生錯誤");
            }
        }
        // 按下 [刪除] 鈕執行此事件
        private void btnDel_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                cn.Open();
                string sqlStr = "DELETE FROM 員工 WHERE 姓名 = @name";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar ));
                cmd.Parameters["@name"].Value = txtName.Text;
                cmd.ExecuteNonQuery();
            }
            ShowData();
        }
    }
}