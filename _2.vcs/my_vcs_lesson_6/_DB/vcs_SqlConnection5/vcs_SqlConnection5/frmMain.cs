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
        //string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\{0};Integrated Security=True;Connect Timeout=30";
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

        public frmMain()
        {
            InitializeComponent();
        }

        private void frmMain_Load(object sender, EventArgs e)
        {

        }

        void show_product_data()
        {
            //取得產品類別, 並顯示dataGridView1上
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet
                dataGridView1.DataSource = ds.Tables[0];
                lb_dgv1.Text = "產品類別";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //兩個表單

            //產品類別 => dataGridView1
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet
                dataGridView1.DataSource = ds.Tables[0];
                lb_dgv1.Text = "產品類別";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品資料 => dataGridView2
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品資料", cn);
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet
                dataGridView2.DataSource = ds.Tables[0];
                lb_dgv2.Text = "產品資料";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //產品類別管理

            show_product_data();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品資料管理

            //將產品類別顯示在清單中   
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet
                cboCategoryId.DataSource = ds.Tables[0];
                dataGridView3.DataSource = ds.Tables[0];
            }

            //查詢 類別編號 = 1 的資料
            int CategoryId1 = 1;
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView2.DataSource = ds.Tables[0];
                lb_dgv2.Text = "產品資料管理";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品關聯查詢

            show_product_data();

            //查詢 類別編號 = 1 的資料
            //int CategoryId1 = 1;

            //取得目前產品類別dataGridView4所選取記錄的第一欄資料，即類別編號
            //並指定給CategoryId整數變數
            int CategoryId2 = 1;
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            //傳入類別編號CategoryId來取得該類別相對應的產品資料
            //接著將產品資料顯示在dataGridView5上
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView5.DataSource = ds.Tables[0];
                lb_dgv3.Text = "產品關聯查詢";
            }
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            //新增類別名稱
            string new_item = "aaaaaaaaaaa";
            txtName.Text = new_item;

            //呼叫Edit()方法並傳入INSERT陳述式新增產品類別記錄
            db.Edit("INSERT INTO 產品類別(類別名稱)VALUES(N'" + txtName.Text.Replace("'", "''") + "')");

            show_product_data();

            txtName.Text = "";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //修改, 修改 類別編號4 的 產品類別

            int old_id = 4;

            string new_name = "bbbbb";
            txtName.Text = new_name;

            //呼叫Edit()方法並傳入UPDATE陳述式修改產品類別記錄
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            db.Edit("UPDATE 產品類別 SET 類別名稱=N'" + txtName.Text.Replace("'", "''") + "' WHERE 類別編號=" + old_id.ToString());

            show_product_data();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除

            int delete_id = 5;

            //呼叫Edit()方法並傳入DELETE陳述式刪除指定的產品類別記錄
            db.Edit("DELETE FROM 產品類別 WHERE 類別編號=" + delete_id.ToString());

            delete_id = 6;
            //刪除與產品類別相關聯的產品資料
            db.Edit("DELETE FROM 產品資料 WHERE 類別編號=" + delete_id.ToString());

            show_product_data();
        }

        private void dataGridView1_Click(object sender, EventArgs e)
        {
        }

        private void dgvCategory_Click(object sender, EventArgs e)
        {
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
            richTextBox1.Text += "CategoryId1 = " + CategoryId1.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
            }

            TextBoxClear();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //修改
            db.Edit("UPDATE 產品資料 SET 品名=N'" +
                txtName.Text.Replace("'", "''") + "', 單價=" +
                txtPrice.Text + ", 說明=N'" +
                txtMsg.Text.Replace("'", "''") + "' WHERE 產品編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId2 = int.Parse(cboCategoryId.SelectedValue.ToString());
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
            }

            TextBoxClear();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除
            db.Edit("DELETE FROM 產品資料 WHERE 產品編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId3 = int.Parse(cboCategoryId.SelectedValue.ToString());
            richTextBox1.Text += "CategoryId3 = " + CategoryId3.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId3, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
            }
            TextBoxClear();
        }

        private void cboCategoryId_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

    }

    class MyDBClass
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //Edit()方法可依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除
        public void Edit(string SqlCmd)
        {
            try
            {
                SqlConnection cn = new SqlConnection(db_cnstr);
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


//cboCategoryId.DisplayMember = "類別名稱";//指定Text屬性繫結的是類別名稱
//cboCategoryId.ValueMember = "類別編號";  //指定Value屬性繫結的是類別編號

//dataGridView1.CurrentRow.Cells[0].Value
//dataGridView1.CurrentRow.Cells[0].Value

