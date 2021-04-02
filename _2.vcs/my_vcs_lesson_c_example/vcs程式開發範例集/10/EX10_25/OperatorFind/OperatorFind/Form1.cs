using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace OperatorFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string M_str_sqlcon = "Server=(local);DataBase=db_10;UID=sa;PWD=;";

        #region  建立DataSet對像
        /// <summary>
        /// 建立一個DataSet對像
        /// </summary>
        /// <param M_str_sqlstr="string">SQL語句</param>
        /// <param M_str_table="string">表名</param>
        /// <returns>傳回DataSet對像</returns>
        public DataSet getDataSet(string SQLstr, string tableName)
        {
            SqlConnection My_con = new SqlConnection(M_str_sqlcon);   //用SqlConnection對象與指定的數據庫相連接
            My_con.Open();  //打開數據庫連接
            SqlDataAdapter SQLda = new SqlDataAdapter(SQLstr, My_con);  //建立一個SqlDataAdapter對象，並取得指定數據表的訊息
            DataSet My_DataSet = new DataSet(); //建立DataSet對像
            if (tableName == "")
                SQLda.Fill(My_DataSet);
            else
                SQLda.Fill(My_DataSet, tableName);  //透過SqlDataAdapter對象的的Fill()方法，將數據表訊息新增到DataSet對像中
            My_con.Close();    //關閉數據庫的連接
            return My_DataSet;  //傳回DataSet對象的訊息
        }
        #endregion

        #region  取得數據表的字段名的描述訊息
        /// <summary>
        /// 取得數據表的字段名的描述訊息
        /// </summary>
        /// <param TabN="string">數據表名稱</param>
        /// <param SQLType="string">數據庫類型</param>
        public void GetFBewrite(string TabN, ComboBox combox)
        {
            combox.Items.Clear();
            string SBewrite = "";//儲存SQL語句
            //取得SQL Server 2000中數據表中的字段名
            SBewrite = "select c.name from syscolumns c,sysobjects a where a.name='" + TabN + "' and a.id=c.id";
            DataSet SqlRead = getDataSet(SBewrite, "");//將尋找的訊息存入到DataSet對像
            int nint = SqlRead.Tables[0].Rows.Count;//取得尋找數據的行數
            for (int i = 0; i < nint; i++)//將表中的字段名新增到ComboBox控制元件中
                combox.Items.Add(SqlRead.Tables[0].Rows[i][0].ToString());
        }
        #endregion

        private void Form1_Load(object sender, EventArgs e)
        {
            DataSet Dset = getDataSet("select * from 銷售表", "銷售表");
            dataGridView1.DataSource = Dset.Tables[0];
            GetFBewrite("銷售表", comboBox1);
        }

        public string BuildSQL(string TableName, string FieldName, string Condition, string FieldValue)
        {
            string StrSQL = "select * from " + TableName;//組合運算符的SQL查詢語句
            bool blur = false;//如果為True，則新增模糊查詢
            if (FieldValue.Trim().Length > 0)//如果查詢條件不為空
            {
                switch (Condition)
                {
                    case "%like%"://左右模糊查詢
                        {
                            StrSQL = StrSQL + " where " + FieldName + " like '%" + FieldValue + "%'";//組合SQL查詢語句
                            blur = true;
                            break;
                        }
                    case "%like"://左模糊查詢
                        {
                            StrSQL = StrSQL + " where " + FieldName + " like '%" + FieldValue + "'";//組合SQL查詢語句
                            blur = true;
                            break;
                        }
                    case "like%"://右模糊查詢
                        {
                            StrSQL = StrSQL + " where " + FieldName + " like '" + FieldValue + "%'";//組合SQL查詢語句
                            blur = true;
                            break;
                        }

                }
                if (!blur)//如是不是模糊查詢
                    StrSQL = StrSQL + " where " + FieldName + Condition + "'" + FieldValue + "'";//組合算數運算符查詢語句
            }
            else//查詢條件為空
                StrSQL = StrSQL + " where " + FieldName + " IS null or " + FieldName + "=''";
            return StrSQL;//傳回SQL語句
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DataSet Dset = getDataSet(BuildSQL("銷售表", comboBox1.Text, comboBox2.Text, textBox1.Text), "");//呼叫自定義方法組合SQL語句，並查詢
            dataGridView1.DataSource = Dset.Tables[0];//顯示查詢後的結果
        }
    }
}
