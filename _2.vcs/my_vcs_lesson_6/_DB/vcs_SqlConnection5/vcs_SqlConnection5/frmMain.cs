using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;//使用SqlConnection, SqlCommand, SqlDataAdapter必須引用

namespace vcs_SqlConnection5
{
    public partial class frmMain : Form
    {
        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

        public frmMain()
        {
            InitializeComponent();
        }

        private void frmMain_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //產品類別管理

            //透過MyDBClass類別的GetCategory()方法取得產品類別
            //並顯示dataGridView1上
            dataGridView1.DataSource = db.GetCategory();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //產品資料管理

            //將產品類別顯示在清單中   
            cboCategoryId.DataSource = db.GetCategory();
            cboCategoryId.DisplayMember = "類別名稱";//指定Text屬性繫結的是類別名稱
            cboCategoryId.ValueMember = "類別編號";  //指定Value屬性繫結的是類別名稱
            //取得目前清單中的Value值，即目前選取項目的類別編號
            int CategoryId = int.Parse(cboCategoryId.SelectedValue.ToString());
            //呼叫GetProduct()方法並傳入類別編號
            //依類別編號取得指定的產品資料並顯示於dataGridView1上
            dataGridView1.DataSource = db.GetProduct(CategoryId);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //產品關聯查詢

            dgvCategory.DataSource = db.GetCategory();
            //dgvCategory.Dock = DockStyle.Top;
            //dgvProduct.Dock = DockStyle.Fill;
            //取得目前產品類別dgvCategory所選取記錄的第一欄資料，即類別編號
            //並指定給CategoryId整數變數
            int CategoryId = int.Parse(dgvCategory.CurrentRow.Cells[0].Value.ToString());
            //呼叫GetProduct()方法並傳入類別編號CategoryId來取得該類別相對應的產品資料
            //接著將產品資料顯示在dgvProduct上
            dgvProduct.DataSource = db.GetProduct(CategoryId);
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            //新增
            //呼叫Edit()方法並傳入INSERT陳述式新增產品類別記錄
            db.Edit("INSERT INTO 產品類別(類別名稱)VALUES(N'" + txtName.Text.Replace("'", "''") + "')");
            dataGridView1.DataSource = db.GetCategory();
            txtName.Text = "";

            //3030

            //修改
            //呼叫Edit()方法並傳入UPDATE陳述式修改產品類別記錄
            //dataGridView1.CurrentRow.Cells[0].Value.ToString()
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            db.Edit("UPDATE 產品類別 SET 類別名稱=N'" + txtName.Text.Replace("'", "''") + "' WHERE 類別編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());
            dataGridView1.DataSource = db.GetCategory();
            txtName.Text = "";

            //3030

            //刪除
            //呼叫Edit()方法並傳入DELETE陳述式刪除指定的產品類別記錄
            db.Edit("DELETE FROM 產品類別 WHERE 類別編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());
            //刪除與產品類別相關聯的產品資料
            db.Edit("DELETE FROM 產品資料 WHERE 類別編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());
            dataGridView1.DataSource = db.GetCategory();
            txtName.Text = "";


        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
        }

        private void btnDel_Click(object sender, EventArgs e)
        {
        }

        private void dgvCategory_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "aaaa\n";
            //產品類別dgvCategory上按一下執行
            try
            {
                int CategoryId = int.Parse(dgvCategory.CurrentRow.Cells[0].Value.ToString());
                dgvProduct.DataSource = db.GetProduct(CategoryId);
            }
            catch (Exception ex)
            { }
        }

        void TextBoxClear()  //清除文字方塊欄位
        {
            txtName2.Text = txtPrice.Text = txtMsg.Text = "";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //新增
            db.Edit("INSERT INTO 產品資料(類別編號,品名,單價,說明)VALUES(" +
                cboCategoryId.SelectedValue.ToString() + ",N'" +
                txtName.Text.Replace("'", "''") + "'," +
                txtPrice.Text + ",N'" +
                txtMsg.Text.Replace("'", "''") + "')");
            int CategoryId1 = int.Parse(cboCategoryId.SelectedValue.ToString());
            dataGridView1.DataSource = db.GetProduct(CategoryId1);
            TextBoxClear();

            //3030

            //修改
            db.Edit("UPDATE 產品資料 SET 品名=N'" +
                txtName.Text.Replace("'", "''") + "', 單價=" +
                txtPrice.Text + ", 說明=N'" +
                txtMsg.Text.Replace("'", "''") + "' WHERE 產品編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());
            int CategoryId2 = int.Parse(cboCategoryId.SelectedValue.ToString());
            dataGridView1.DataSource = db.GetProduct(CategoryId2);
            TextBoxClear();

            //3030

            //刪除
            db.Edit("DELETE FROM 產品資料 WHERE 產品編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());
            int CategoryId3 = int.Parse(cboCategoryId.SelectedValue.ToString());
            dataGridView1.DataSource = db.GetProduct(CategoryId3);
            TextBoxClear();
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        //選取類別編號下拉式清單時執行
        private void cboCategoryId_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                int CategoryId = int.Parse(cboCategoryId.SelectedValue.ToString());
                dataGridView1.DataSource = db.GetProduct(CategoryId);
            }
            catch (Exception ex)
            {
            }
        }
    }

    class MyDBClass
    {
        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //GetCategory()方法可傳回產品類別的DataTable
        public DataTable GetCategory()
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            return ds.Tables[0];
        }

        //GetProduct()方法可依傳入的類別編號來傳回指定的產品資料的DataTable
        public DataTable GetProduct(int CategoryId)
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId, cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            return ds.Tables[0];
        }

        //Edit()方法可依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除
        public void Edit(string SqlCmd)
        {
            try
            {
                SqlConnection cn = new SqlConnection(cnStr);
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = SqlCmd;
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                cn.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
