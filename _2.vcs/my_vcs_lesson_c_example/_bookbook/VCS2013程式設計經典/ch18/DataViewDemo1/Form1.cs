using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data .SqlClient ;

namespace DataViewDemo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        DataView dvScore;  // 宣告DataView物件dvScore
        // 表單載入時執行此事件
        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch18DB.mdf;" +
                    "Integrated Security=True";
                SqlDataAdapter daScore = new SqlDataAdapter("SELECT * FROM 成績單 ORDER BY 國文 DESC", cn);
                DataSet ds = new DataSet();
                daScore.Fill(ds, "成績單");
                dvScore = ds.Tables["成績單"].DefaultView;
            }
            dataGridView1.DataSource = dvScore;
            rdbChi.Checked = true;  // 國文選項按鈕預設選取
            rdbDesc.Checked = true;  // 遞增選項按鈕預設選取
        }
        // 按下 [確定] 鈕執行此事件 
        private void btnOk_Click(object sender, EventArgs e)
        {
            string sortStr = "";
            if (rdbChi.Checked) sortStr += rdbChi.Text;
            if (rdbEng.Checked) sortStr += rdbEng.Text;
            if (rdbMath.Checked) sortStr += rdbMath.Text;
            if (rdbDesc.Checked) sortStr += " DESC";
            if (rdbAsc.Checked) sortStr += " ASC";
            dvScore.RowFilter = txtFilter.Text;
            dvScore.Sort = sortStr;
            dataGridView1.DataSource = dvScore;
        }
    }
}
