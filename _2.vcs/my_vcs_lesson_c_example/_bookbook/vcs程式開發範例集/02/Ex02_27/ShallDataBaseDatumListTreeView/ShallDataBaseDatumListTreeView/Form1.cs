using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace ShallDataBaseDatumListTreeView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }



        private void Form1_Load(object sender, EventArgs e)
        {

            treeView1.ShowLines = true;
            treeView1.ImageList = imageList1;
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_07", con);
            SqlDataReader dr = com.ExecuteReader();
            TreeNode newNode1 = treeView1.Nodes.Add("A", "商品信息", 1, 2);//一級節點
            while (dr.Read())
            {
                TreeNode newNode12 = new TreeNode("商品編號" + dr[1].ToString(), 3, 4);// 二級節點
                // 3表示沒有單擊節點時顯示的圖標索引值，
                newNode12.Nodes.Add("A", "商品名稱：" + dr[0].ToString(), 5, 6);
                newNode12.Nodes.Add("A", "商品數量：" + dr[3].ToString(), 7, 8);
                newNode12.Nodes.Add("A", "商品價格：" + dr[2].ToString(), 9, 10);
                newNode1.Nodes.Add(newNode12);

            }
            dr.Close();
            con.Close();
            treeView1.ExpandAll();
        }
    }
}