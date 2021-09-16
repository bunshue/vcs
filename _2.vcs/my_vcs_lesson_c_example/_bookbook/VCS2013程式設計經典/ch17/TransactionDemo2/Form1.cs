using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace TransactionDemo2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 建立cnstr連接字串用來連接ch17DB.mdf資料庫
        string cnstr = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch17DB.mdf;" +
                    "Integrated Security=True";

        // 定義ShowData()方法將銀行帳戶資料表所有記錄顯示於dataGridView1上
        void ShowData()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 銀行帳戶", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "銀行帳戶");
                dataGridView1.DataSource = ds.Tables["銀行帳戶"];
            }
        }
        // 表單載入時執行此事件
        private void Form1_Load(object sender, EventArgs e)
        {
            ShowData();
        }
        // 按下 [轉帳] 鈕執行此事件
        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                cn.Open();
                // 建立SqlCommand物件selectCmd1，用來查詢使用者帳號是否存在
                SqlCommand selectCmd1 = new SqlCommand("SELECT * FROM 銀行帳戶 WHERE 帳號='" + txtMyId.Text.Replace("'", "''") + "'", cn);
                // 建立SqlCommand物件selectCmd1，用來查詢轉入帳號是否存在
                SqlCommand selectCmd2 = new SqlCommand("SELECT * FROM 銀行帳戶 WHERE 帳號='" + txtIncomeId.Text.Replace("'", "''") + "'", cn);
                // 宣告SqlDataReader物件dr1與dr2
                SqlDataReader dr1, dr2;
                // 傳回SqlDataReader物件dr1，用來查詢使用者帳號是否存在
                dr1 = selectCmd1.ExecuteReader();
                if (!dr1.Read())   // 使用者帳號不存在執行下列敘述
                {
                    MessageBox.Show("你的帳號" + txtMyId.Text + "錯誤");
                    return;  
                }
                // 取得使用者的餘額並定給myMoney
                int myMoney = int.Parse(dr1["餘額"].ToString());
                dr1.Close();  // 關閉SqlDataRader物件dr1
                // 傳回SqlDataReader物件dr2，用來查詢轉入帳號是否存在
                dr2 = selectCmd2.ExecuteReader();
                if (!dr2.Read())   // 轉入帳號不存在執行下列敘述
                {
                    MessageBox.Show("轉入帳號" + txtIncomeId.Text + "錯誤");
                    return;
                }
                dr2.Close();  // 關閉SqlDataRader物件dr2
                try
                {
                    // 若使用者餘額小於轉入金額，則執行下列敘述
                    if (myMoney < int.Parse(txtIncomeMoney.Text))
                    {
                        MessageBox.Show(txtMyId.Text + "帳號沒這麼多存款");
                        return;
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("金額請輸入數值");
                    return;
                }
                // 建立SqlTransaction交易物件tran
                SqlTransaction tran = cn.BeginTransaction();
                try
                {
                    // 使用者帳號扣款的SQL語法
                    SqlCommand updateCmd1 = new SqlCommand("UPDATE 銀行帳戶 SET 餘額=餘額-" + txtIncomeMoney.Text + " WHERE 帳號='" + txtMyId.Text.Replace("'", "''") + "'", cn, tran);
                    // 設定轉入帳號匯款的SQL語法
                    SqlCommand updateCmd2 = new SqlCommand("UPDATE 銀行帳戶 SET 餘額=餘額+" + txtIncomeMoney.Text + " WHERE 帳號='" + txtIncomeId.Text.Replace("'", "''") + "'", cn, tran);
                    updateCmd1.ExecuteNonQuery();
                    throw new Exception("電腦當機");
                    updateCmd2.ExecuteNonQuery();
                    tran.Commit(); // 認可交易
                    MessageBox.Show("轉帳成功", "交易成功");
                    txtIncomeId.Text = "";
                    txtIncomeMoney.Text = "";
                    txtMyId.Text = "";
                }
                catch (Exception ex)
                {
                    tran.Rollback();// 回復交易
                    MessageBox.Show("轉帳失敗\n" + ex.Message, "交易失敗");
                }
                ShowData();
            }
        }
    }
}
    

