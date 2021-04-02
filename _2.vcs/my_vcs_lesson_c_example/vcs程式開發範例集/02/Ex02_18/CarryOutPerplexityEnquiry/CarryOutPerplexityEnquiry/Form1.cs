using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace CarryOutPerplexityEnquiry
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
        public void GetScoure(string strSql)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand(strSql, con);
            dataGridView1.Rows.Clear();
            SqlDataReader dr = com.ExecuteReader();
            while (dr.Read())
            {
                dataGridView1.Rows.Add(dr[0].ToString(), dr[1].ToString(), dr[2].ToString(), dr[3].ToString(), dr[4].ToString(), dr[5].ToString());
            }
            dr.Close();
            con.Close();
        }

        private void bntEsce_Click(object sender, EventArgs e)
        {
            ckClass.Checked = false;
            ckName.Checked = false;
            ckId.Checked = false;
            rdbMan.Checked = false;
            rdbWoMan.Checked = false;
        }

        private void ckId_CheckedChanged(object sender, EventArgs e)
        {
            if (ckId.Checked == true)
            {
                txtstuId.Enabled = true;
                txtstuId.Focus();
            }
            else
            {
                txtstuId.Text = "";
                txtstuId.Enabled = false;
            }
        }

        private void ckClass_CheckedChanged(object sender, EventArgs e)
        {
            if (ckClass.Checked == true)
            {
                txtClass.Enabled = true;
                txtClass.Focus();
            }
            else
            {
                txtClass.Text = "";
                txtClass.Enabled = false;
            }
        }

        private void ckName_CheckedChanged(object sender, EventArgs e)
        {
            if (ckName.Checked == true)
            {
                txtName.Enabled = true;
                txtName.Focus();
            }
            else
            {
                txtName.Text = "";
                txtName.Enabled = false;
            }
        }
        //
        public string strSql;//用於存儲SQL語句
        public string strId;//用於存學生編號
        public string strName;//用於存儲學生姓名
        public string strClass;//用於存儲學生班級
        public string strSex;//用於存儲學生姓別
        public static int intCount = 0;//控制數據組索引
        public string[] strScoure = new string[4];
        public int intAdd;//用來判斷SQL語句數組
        private void bntSearch_Click(object sender, EventArgs e)
        {
            intCount = 0;
            if (txtstuId.Text != "")
            {
                strId = "學生編號  like '%" + txtstuId.Text + "%'";

                strScoure[intCount] = strId;
                intCount++;

            }
            if (txtName.Text != "")
            {
                strName = "學生姓名 like '%" + txtName.Text + "%' ";
                strScoure[intCount] = strName;
                intCount++;
            }
            if (txtClass.Text != "")
            {
                strClass = "所在年級 like '%" + txtClass.Text + "%'";
                strScoure[intCount] = strClass;
                intCount++;
            }
            if (rdbMan.Checked == true)
            {
                strSex = "學生性別 like '%" + rdbMan.Text + "%'";
                strScoure[intCount] = strSex;
                intCount++;
            }
            if (rdbWoMan.Checked == true)
            {
                strSex = "學生性別 like '%" + rdbWoMan.Text + "%'";
                strScoure[intCount] = strSex;
                intCount++;
            }
            for (int i = 0; i < strScoure.Length; i++)
            {
                if (strScoure[i] != null)
                {
                    strSql += strScoure[i];
                    intAdd++;
                }
            }// end 
            switch (intAdd)
            {

                case 0:
                    strSql = "select * from tb_01";
                    break;
                case 1:
                    strSql = "select * from tb_01 where " + strScoure[0];

                    break;
                case 2:
                    strSql = "select * from tb_01 where " + strScoure[0] + " and " + strScoure[1];

                    break;
                case 3:
                    strSql = "select * from tb_01 where " + strScoure[0] + " and " + strScoure[1] + " and " + strScoure[2];
                    break;
                case 4:
                    strSql = "select * from tb_01 where " + strScoure[0] + " and " + strScoure[1] + " and " + strScoure[2] + " and " + strScoure[3];
                    break;
            }
            GetScoure(strSql);
            //MessageBox.Show(strSql);
            intAdd = 0;
            intCount = 0;
            strSql = "";
            for (int i = 0; i < strScoure.Length; i++)
            {
                if (strScoure[i] != null)
                {
                    strScoure[i] = null;
                }
            }// end
        }

        public void getScoure(string str_name)
        {
            string txtId, txtstuName, txtEmpty, txtSex, txtAge, txtKnowledge, txtTeching;
            //連接數據庫
            SqlConnection con = new SqlConnection("server=.;integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_04 where 人員姓名= '" + str_name + "'", con);
            SqlDataReader dr = com.ExecuteReader();//
            while (dr.Read())
            {
                txtId = dr[0].ToString();
                txtstuName = dr[1].ToString();
                txtEmpty = dr[2].ToString();
                txtSex = dr[3].ToString();
                txtAge = dr[4].ToString();
                txtKnowledge = dr[5].ToString();
                txtTeching = dr[6].ToString();
            }
            dr.Close();
            con.Close();
        }
    }
}