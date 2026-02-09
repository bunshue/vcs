using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Linq_to_SQL4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.Text = "請選擇查詢項目";
            comboBox1.Items.Add("產品資料統計");
            comboBox1.Items.Add("類別分組統計");
            comboBox1.Items.Add("所有產品資料");
            comboBox1.Items.Add("單價大於等於20元的產品");
        }

        // 按下 [確定] 鈕執行此事件處理函式 
        private void btnOk_Click(object sender, EventArgs e)
        {
            NorthwindDataContext dc = new NorthwindDataContext();
            dc.Log = Console.Out;
            txtResult.Text = "";
            if (comboBox1.Text == "產品資料統計")
            {
                var result = from p in dc.產品資料
                             select p.單價;
                txtResult.Text += Environment.NewLine + "產品最高價："
                   + result.Max().ToString();
                txtResult.Text += Environment.NewLine + "產品最低價："
                   + result.Min().ToString();
                txtResult.Text += Environment.NewLine + "產品平均價："
                   + result.Average().ToString();
                txtResult.Text += Environment.NewLine + "產品　總價："
                   + result.Sum().ToString();
                txtResult.Text += Environment.NewLine + "產品總筆數："
                   + result.Count().ToString();
            }
            else if (comboBox1.Text == "類別分組統計")
            {
                var result = from category in dc.產品類別
                             join product in dc.產品資料
                             on category.類別編號 equals product.類別編號
                             into num
                             select new
                             {
                                 類別名稱 = category.類別名稱,
                                 產品數量 = num.Count()
                             };
                foreach (var c in result)
                {
                    txtResult.Text += c.類別名稱 + "類別共 " + c.產品數量 +
                       " 個產品" + Environment.NewLine;
                }
            }
            else if (comboBox1.Text == "所有產品資料")
            {
                var result = from category in dc.產品類別
                             orderby category.類別編號 descending
                             select category;
                foreach (var c in result)
                {
                    txtResult.Text += "*" + c.類別名稱 + Environment.NewLine;
                    foreach (var p in c.產品資料)
                    {
                        txtResult.Text += "\t" + p.產品 +
                           Environment.NewLine;
                    }
                    txtResult.Text += "==================" +
                       Environment.NewLine + Environment.NewLine;
                }
            }
            else if (comboBox1.Text == "單價大於等於20元的產品")
            {
                var result = from product in dc.產品資料
                             orderby product.單價 ascending
                             where product.單價 >= 20
                             select product;
                foreach (var p in result)
                {
                    txtResult.Text += p.產品 + "\t" + p.單價 +
                       Environment.NewLine;
                }
            }
            else
            {
                txtResult.Text = "請選擇查詢項目";
            }
        }
    }
}
