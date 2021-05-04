using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;



namespace 產品管理
{
    public partial class frmCategory : Form
    {
        public frmCategory()
        {
            InitializeComponent();
        }

        //建立MyDBClass物件db
        MyDBClass db = new MyDBClass();

        //表單載入時執行
        private void frmCategory_Load(object sender, EventArgs e)
        {
            //透過MyDBClass類別的GetCategory()方法取得產品類別
            //並顯示dataGridView1上
            dataGridView1.DataSource = db.GetCategory();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            //呼叫Edit()方法並傳入INSERT陳述式新增產品類別記錄
            db.Edit("INSERT INTO 產品類別(類別名稱)VALUES(N'" +
                    txtName.Text.Replace("'", "''") + "')");
            dataGridView1.DataSource = db.GetCategory();
            txtName.Text = "";
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            //呼叫Edit()方法並傳入UPDATE陳述式修改產品類別記錄
            //dataGridView1.CurrentRow.Cells[0].Value.ToString()
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            db.Edit("UPDATE 產品類別 SET 類別名稱=N'" +
                    txtName.Text.Replace("'", "''") + "' WHERE 類別編號=" +
                    dataGridView1.CurrentRow.Cells[0].Value.ToString());
            dataGridView1.DataSource = db.GetCategory();
            txtName.Text = "";
        }

        private void btnDel_Click(object sender, EventArgs e)
        {
            //呼叫Edit()方法並傳入DELETE陳述式刪除指定的產品類別記錄
            db.Edit("DELETE FROM 產品類別 WHERE 類別編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());
            //刪除與產品類別相關聯的產品資料
            db.Edit("DELETE FROM 產品資料 WHERE 類別編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());
            dataGridView1.DataSource = db.GetCategory();
            txtName.Text = "";
        }
    }
}
