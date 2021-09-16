using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace BindingManagerBase1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 宣告BindingManagerBase物件bm
        // 使用此物件來巡覽產品資料表的記錄
        BindingManagerBase bm;

       // 定義CheckBm方法, 該方法用來顯示目前記錄的位置
        // 使 第一筆 、上一筆 、下一筆 、最未筆  鈕是否可被使用
        private void Checkbm()
        {
            if (bm.Position == 0)
            {
                btnFirst.Enabled = false;
                btnPrev.Enabled = false;
                btnNext.Enabled = true;
                btnLast.Enabled = true;
            }
            else if (bm.Position == bm.Count - 1)
            {
                btnFirst.Enabled = true;
                btnPrev.Enabled = true;
                btnNext.Enabled = false;
                btnLast.Enabled = false;
            }
            else
            {
                btnFirst.Enabled = true;
                btnPrev.Enabled = true;
                btnNext.Enabled = true;
                btnLast.Enabled = true;
            }
            lblShow.Text = "目前在第 " + (bm.Position + 1).ToString() + " 筆記錄, 共 " + bm.Count.ToString() + " 筆記錄";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch18DB.mdf;" +
                    "Integrated Security=True";
                // 建立DataSet物件ds
                // 在ds物件的DataTable內填入 [會員] 資料表的所有記錄
                DataSet ds = new DataSet();
                SqlDataAdapter daMember = new SqlDataAdapter("SELECT * FROM 會員", cn);
                daMember.Fill(ds, "會員");
                // 建立Binding物件，並繫結至對應的資料表欄位
                Binding bindId = new Binding("Text", ds, "會員.編號");
                Binding bindName = new Binding("Text", ds, "會員.姓名");
                Binding bindTel = new Binding("Text", ds, "會員.電話");
                Binding bindSex = new Binding("Text", ds, "會員.性別");
                Binding bindDate = new Binding("Text", ds, "會員.入會日期");
                Binding bindIsMarry = new Binding("Checked", ds, "會員.婚姻狀態");
                // 將控制項與Binding物件做資料繫結
                // 使控制項顯示資料表的欄位內容
                txtId.DataBindings.Add(bindId);
                txtName.DataBindings.Add(bindName);
                txtTel.DataBindings.Add(bindTel);
                cboSex.DataBindings.Add(bindSex);
                dtpDate.DataBindings.Add(bindDate);
                chkIsMarry.DataBindings.Add(bindIsMarry);

                bm = this.BindingContext[ds, "會員"];
            }
            Checkbm();
        }
        // 按 第一筆 鈕執行此事件，使移到第一筆記錄位置
        private void btnFirst_Click(object sender, EventArgs e)
        {
            bm.Position = 0;
            Checkbm();
        }
        // 按 上一筆 鈕執行此事件，使移到上一筆記錄位置
        private void btnPrev_Click(object sender, EventArgs e)
        {
            if (bm.Position > 0)
            {
                bm.Position -= 1;
            }
            Checkbm();
        }
        // 按 下一筆 鈕執行此事件，使移到下一筆記錄位置
        private void btnNext_Click(object sender, EventArgs e)
        {
            if (bm.Position < bm.Count - 1)
            {
                bm.Position += 1;
            }
            Checkbm();
        }
        // 按 最末筆 鈕執行此事件，使移到最後一筆記錄位置
        private void btnLast_Click(object sender, EventArgs e)
        {
            bm.Position = bm.Count - 1;
            Checkbm();
        }
    }
}
