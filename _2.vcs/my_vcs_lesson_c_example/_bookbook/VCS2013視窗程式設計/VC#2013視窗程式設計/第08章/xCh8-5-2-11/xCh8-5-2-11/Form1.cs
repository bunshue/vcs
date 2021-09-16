using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh8_5_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: 這行程式碼會將資料載入 '北風DataSet.員工' 資料表。您可以視需要進行移動或移除。
            this.員工TableAdapter.Fill(this.北風DataSet.員工);

            comboBox1.Items.AddRange( 
                       new object[] { "業務代表",
                                             "業務協調員",
                                             "業務經理",
                                             "資深工程師",
                                             "副總裁，銷售部門"}
            );

            // 顯示目前記錄所在的位置及記錄總數
            ShowPosition();
        }

        private void ShowPosition()
        {
            label3.Text = "目前位置：第 " + (員工BindingSource.Position + 1).ToString();
            label3.Text += " 筆/共 " + 員工BindingSource.Count.ToString() + " 筆";
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            員工BindingSource.Sort = "識別碼 ASC"; // ASC，即為ascending表示升冪
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            員工BindingSource.Sort = "識別碼 DESC";// DESC，即為descening表示降冪
        }

        private void button1_Click(object sender, EventArgs e)
        {
            員工BindingSource.MoveFirst();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            員工BindingSource.MovePrevious();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            員工BindingSource.MoveNext();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            員工BindingSource.MoveLast();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            員工BindingSource.Position = Convert.ToInt32(textBox1.Text)-1;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            try
            {
                員工BindingSource.EndEdit();
                員工TableAdapter.Update(this.北風DataSet.員工);
                MessageBox.Show("更新完成");
                ShowPosition();
            }
            catch (Exception ex)
            {
                MessageBox.Show("無法更新資料：" + ex.Message);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            try
            {
                員工BindingSource.AddNew();
                MessageBox.Show("請開始填入資料，填完後再點選更新");
                ShowPosition();
            }
            catch (Exception ex)
            {
                MessageBox.Show("無法新增資料：" + ex.Message);
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show
                (
                "是否刪除？", 
                "小心", 
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Question, 
                MessageBoxDefaultButton.Button2
                ) == DialogResult.Yes
               )
            {
                員工BindingSource.RemoveAt(員工BindingSource.Position);
                MessageBox.Show("完成刪除，請再點選更新");
                ShowPosition();
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            員工BindingSource.RemoveFilter();
            ShowPosition();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            string selectedPostion = (string)comboBox1.SelectedItem;
            員工BindingSource.Filter = "職稱='" + selectedPostion + "'";

            label3.Text = "符合篩選條件者，共 " + 
                員工BindingSource.Count.ToString() + 
                " 筆";
        }
    }
}
