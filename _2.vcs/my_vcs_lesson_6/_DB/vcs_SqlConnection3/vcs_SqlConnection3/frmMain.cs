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

namespace vcs_SqlConnection3
{
    public partial class frmMain : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

        public frmMain()
        {
            InitializeComponent();
        }

        private void frmMain_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            int W = 550;
            int H = 380;
            dataGridView1.Size = new Size(W, H);
            dataGridView2.Size = new Size(W, H);
            dataGridView3.Size = new Size(W, H);
            dataGridView4.Size = new Size(W, H);
            richTextBox1.Size = new Size(300, H + 100);
            dx = W + 10;
            dy = H + 30;
            int dd = 25;
            lb_dgv1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_dgv2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_dgv3.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_dgv4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            dataGridView1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);
            dataGridView2.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);
            dataGridView3.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd);
            dataGridView4.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1 + dd - 100);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            dy = 30;
            button1.Location = new Point(x_st + dx * 2 + 110 * 0, y_st + dy * 0 + dd);
            button2.Location = new Point(x_st + dx * 2 + 110 * 1, y_st + dy * 0 + dd);
            button3.Location = new Point(x_st + dx * 2 + 110 * 2, y_st + dy * 0 + dd);

            button4.Location = new Point(x_st + dx * 2 + 110 * 0, y_st + dy * 4 + dd);
            button5.Location = new Point(x_st + dx * 2 + 110 * 1, y_st + dy * 4 + dd);
            button6.Location = new Point(x_st + dx * 2 + 110 * 2, y_st + dy * 4 + dd);

            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";

            this.Size = new Size(1500, 900);
            this.Text = "vcs_SqlConnection3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            dataGridView1.DataSource = null;//設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;//設定DGV的資料來源為無, 即清除
            dataGridView3.DataSource = null;//設定DGV的資料來源為無, 即清除
            dataGridView4.DataSource = null;//設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";
        }

        void show_product_data(DataGridView dgv, string mesg)
        {
            //取得產品類別, 並顯示dataGridView1上
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet
                dgv.DataSource = ds.Tables[0];
                lb_dgv1.Text = mesg;
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

            show_product_data(dataGridView1, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品資料管理

            //將產品類別顯示在清單中   
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
                DataSet ds = new DataSet();  // 建立DataSet來儲存Table
                da.Fill(ds);  // 將DataAdapter查詢之後的結果填充至DataSet
                dataGridView2.DataSource = ds.Tables[0];
                lb_dgv2.Text = "產品類別";
            }

            //查詢 類別編號 = 1 的資料
            int CategoryId1 = 1;
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView3.DataSource = ds.Tables[0];
                lb_dgv3.Text = "產品資料管理";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品關聯查詢

            show_product_data(dataGridView1, "產品類別");

            //查詢 類別編號 = 1 的資料
            //int CategoryId1 = 1;

            //取得目前產品類別dataGridView4所選取記錄的第一欄資料，即類別編號
            //並指定給CategoryId整數變數
            int CategoryId2 = 1;
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            //傳入類別編號CategoryId來取得該類別相對應的產品資料
            //接著將產品資料顯示在dataGridView4上
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView4.DataSource = ds.Tables[0];
                lb_dgv4.Text = "產品關聯查詢";
            }
        }

        private void dataGridView1_Click(object sender, EventArgs e)
        {
        }

        private void dgvCategory_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增類別名稱\n";

            string new_item = "麥當勞";

            //呼叫Edit()方法並傳入INSERT陳述式新增產品類別記錄
            db.Edit("INSERT INTO 產品類別(類別名稱)VALUES(N'" + new_item + "')");

            show_product_data(dataGridView1, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改, 修改 類別編號4 的 產品類別\n";

            int old_id = 4;

            string new_item2 = "肯德雞";

            //呼叫Edit()方法並傳入UPDATE陳述式修改產品類別記錄
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            db.Edit("UPDATE 產品類別 SET 類別名稱=N'" + new_item2 + "' WHERE 類別編號=" + old_id.ToString());

            show_product_data(dataGridView2, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除\n";

            int delete_id = 5;

            //呼叫Edit()方法並傳入DELETE陳述式刪除指定的產品類別記錄
            db.Edit("DELETE FROM 產品類別 WHERE 類別編號=" + delete_id.ToString());

            delete_id = 6;
            //刪除與產品類別相關聯的產品資料
            db.Edit("DELETE FROM 產品資料 WHERE 類別編號=" + delete_id.ToString());

            show_product_data(dataGridView3, "產品類別");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "新增\n";

            string new_item = "必勝客";
            int price = 12345;//單價
            string mesg = "電話訂購";//說明

            db.Edit("INSERT INTO 產品資料(類別編號,品名,單價,說明)VALUES(" +
                "1" + ",N'" +
                new_item + "'," +
                price.ToString() + ",N'" +
                mesg + "')");

            int CategoryId1 = 1;//類別編號
            richTextBox1.Text += "CategoryId1 = " + CategoryId1.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
                lb_dgv1.Text = "新增 產品資料";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改\n";

            new_item = "達美樂";
            price = 123;//單價
            mesg = "網路訂購";//說明

            db.Edit("UPDATE 產品資料 SET 品名=N'" +
                new_item + "', 單價=" +
                price.ToString() + ", 說明=N'" +
                mesg + "' WHERE 產品編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId2 = 1;//類別編號
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
                lb_dgv1.Text = "修改 產品資料";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除\n";

            db.Edit("DELETE FROM 產品資料 WHERE 產品編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId3 = 1;//類別編號
            richTextBox1.Text += "CategoryId3 = " + CategoryId3.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))
            {
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId3, cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                dataGridView1.DataSource = ds.Tables[0];
                lb_dgv1.Text = "刪除 產品資料";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
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


//combobox 類別編號
//cboCategoryId.DisplayMember = "類別名稱";//指定Text屬性繫結的是類別名稱
//cboCategoryId.ValueMember = "類別編號";  //指定Value屬性繫結的是類別編號
//int CategoryId1 = int.Parse(cboCategoryId.SelectedValue.ToString());
//int CategoryId2 = int.Parse(cboCategoryId.SelectedValue.ToString());
//int CategoryId3 = int.Parse(cboCategoryId.SelectedValue.ToString());

//dataGridView1.CurrentRow.Cells[0].Value
//dataGridView1.CurrentRow.Cells[0].Value


/*
                Bitmap bitM = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);  // 创建画布
                Graphics g = Graphics.FromImage(bitM);  // 创建Graphics对象
                Pen p = new Pen(new SolidBrush(Color.SlateGray), 1.0f);  // 创建Pen对象
                p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;  // 设置虚线
                g.Clear(Color.White);  // 设置画布颜色

                        int x, y, w, h;  // 声明变量存储坐标和大小
                        g.DrawString(dr[0].ToString(), new Font("宋体", 9, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.pictureBox1.Height - 16);  // 绘制商品名称
                        x = 78 + 40 * j;  // X坐标

                        //richTextBox1.Text += "bbbb : " + Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100))) + "\n";
                        y = this.pictureBox1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));  // Y坐标

                        w = 24;  // 宽度

                        richTextBox1.Text += "cccc : " + dr[1].ToString() + "\n";
                        //richTextBox1.Text += "cccc : " + Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100) + "\n";
                        h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);  // 高度

                        g.FillRectangle(new SolidBrush(Color.SlateGray), x, y, w, h);  // 绘制柱形图
                        g.DrawString((h * 100 / 20).ToString(), new Font("宋体", 8, FontStyle.Bold), new SolidBrush(Color.Tomato), new Point(x + 4, y - 10));  // 在柱形图指定的位置绘制文字
                this.pictureBox1.BackgroundImage = bitM;  // 显示绘制的图形

*/
