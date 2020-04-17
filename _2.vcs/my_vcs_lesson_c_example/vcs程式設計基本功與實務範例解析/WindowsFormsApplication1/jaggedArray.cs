using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class jaggedArray : Form
    {
        string[][] trans = new string[30][];
        char[] gender = new char[30];
        string[] name = new string[30];
        int Counter = 0;

        public jaggedArray()
        {
            InitializeComponent();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void jaggedArray_Load(object sender, EventArgs e)
        {
            lblCounter.Text = "共有0個顧客";
        }

        private void btnInput_Click(object sender, EventArgs e)
        {
            if (Counter >= 30) MessageBox.Show("儲存空間已滿","錯誤");
            else { //紀錄交易的相關資訊
                name[Counter] = txtName.Text;
                if(rdbMale.Checked) gender[ Counter ] = '男';
                else gender[Counter] = '女';

                // 檢查共買了多少商品
                int ctr = 0;
                if (checkBox1.Checked) ctr++;
                if (checkBox2.Checked) ctr++;
                if (checkBox3.Checked) ctr++;
                if (checkBox4.Checked) ctr++;
                if (checkBox5.Checked) ctr++;

                // 動態配置儲存交易商品的陣列
                trans[Counter] = new string[ctr];

                // 儲存購買的商品名稱
                ctr = 0;
                if (checkBox1.Checked) trans[Counter][ctr++] = checkBox1.Text;
                if (checkBox2.Checked) trans[Counter][ctr++] = checkBox2.Text;
                if (checkBox3.Checked) trans[Counter][ctr++] = checkBox3.Text;
                if (checkBox4.Checked) trans[Counter][ctr++] = checkBox4.Text;
                if (checkBox5.Checked) trans[Counter][ctr++] = checkBox5.Text;

                // 顯示新交易資訊
                string output = "新顧客\r\n";
                output = name[Counter] + ", " + gender[Counter];
                for (int i = 0; i < ctr; i++)
                    output += ", " + trans[Counter][i];
                txtOutput.Text = output;

                // 顧客數加1
                Counter++;
                lblCounter.Text = "共有" + Counter + "個顧客";

                //清除介面上輸入的資料
                txtName.Text = "";
                rdbMale.Checked = true;
                checkBox1.Checked = false;
                checkBox2.Checked = false;
                checkBox3.Checked = false;
                checkBox4.Checked = false;
                checkBox5.Checked = false;

                txtName.Focus();  // 取得焦點
            }
        }

        private void btnListing_Click(object sender, EventArgs e)
        {
            string str = "顧客列表\r\n";

            for (int i = 0; i < Counter; i++)
            {   //建立第i位顧客的交易資訊
                str += (i + 1) + ": ";
                str += name[i] + ", " + gender[i];
                //輸出購買的所有商品
                for (int j = 0; j < trans[i].Length; j++)
                    str += ", " + trans[i][j];

                str += "\r\n";
            }

            txtOutput.Text = str;

            txtName.Focus();
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            string n = txtName.Text;

            int i;

            for (i = 0; i < Counter; i++)
            {
                if (name[i] == n) break;
            }

            if (i < Counter) //找到
            {
                string str = "!!!搜尋結果!!!\r\n";
                str += name[i] + ", " + gender[i];
                for (int j = 0; j < trans[i].Length; j++)
                     str += ", " + trans[i][j];

                txtOutput.Text = str;
            }
            else txtOutput.Text = "!!!搜尋結果!!!\r\n沒有找到" + n;

            txtName.Text = "";
            txtName.Focus();
        }
    }
}
