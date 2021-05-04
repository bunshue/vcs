using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Movie
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtQtyF.Text = "0";  //預設全票文字方塊文字為0
            txtQtyF.Focus();     //預設全票文字方塊取得駐停焦點
        }
        // 全票文字方塊取得駐停焦點時執行
        private void txtQtyF_Enter(object sender, EventArgs e)
        {
            txtQtyF.Text = "";
        }
        // 全票與半票文字方塊的Text屬性改變時執行
        private void txtQtyF_TextChanged(object sender, EventArgs e)
        {
            try
            {
                int sumF;
                //計算全票總金額
                sumF = Convert.ToInt32(lblPriceF.Text) * Convert.ToInt32(txtQtyF.Text);
                lblSumF.Text = Convert.ToString(sumF);   //顯示全票總金額
            }
            catch
            {
                lblSumF.Text = "0";
            }
        }

    }
}
