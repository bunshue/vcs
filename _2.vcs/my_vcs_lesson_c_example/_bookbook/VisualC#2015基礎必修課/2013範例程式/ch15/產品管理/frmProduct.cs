using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 產品管理
{
    public partial class frmProduct : Form
    {
        public frmProduct()
        {
            InitializeComponent();
        }
        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

        void TextBoxClear()  //清除文字方塊欄位
        {
            txtName.Text = txtPrice.Text = txtMsg.Text = "";
        }

        //表單載入時
        private void frmProduct_Load(object sender, EventArgs e)
        {
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

        //按新增鈕
        private void btnAdd_Click(object sender, EventArgs e)
        {
            db.Edit("INSERT INTO 產品資料(類別編號,品名,單價,說明)VALUES(" +
                    cboCategoryId.SelectedValue.ToString() + ",N'" +
                    txtName.Text.Replace("'", "''") + "'," +
                    txtPrice.Text + ",N'" +
                    txtMsg.Text.Replace("'", "''") + "')");
            int CategoryId = int.Parse(cboCategoryId.SelectedValue.ToString());
            dataGridView1.DataSource = db.GetProduct(CategoryId);
            TextBoxClear();
        }
        //按修改鈕
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            db.Edit("UPDATE 產品資料 SET 品名=N'" +
                    txtName.Text.Replace("'", "''") + "', 單價=" +
                    txtPrice.Text + ", 說明=N'" +
                    txtMsg.Text.Replace("'", "''") + "' WHERE 產品編號=" +
                    dataGridView1.CurrentRow.Cells[0].Value.ToString());
            int CategoryId = int.Parse(cboCategoryId.SelectedValue.ToString());
            dataGridView1.DataSource = db.GetProduct(CategoryId);
            TextBoxClear();
        }

        //按刪除鈕
        private void btnDel_Click(object sender, EventArgs e)
        {
            db.Edit("DELETE FROM 產品資料 WHERE 產品編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());
            int CategoryId = int.Parse(cboCategoryId.SelectedValue.ToString());
            dataGridView1.DataSource = db.GetProduct(CategoryId);
            TextBoxClear();
        }
    }
}
