﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


using System.Data.SqlClient;	//引用System.Data.SqlClient命名空間
using System.Data.Linq;    	//引用System.Data.Linq命名空間


namespace Linq_to_SQL2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                            "AttachDbFilename=|DataDirectory|ch20DB.mdf;" +
                            "Integrated Security=True";
                DataContext dc = new DataContext(cn);
                Table<Employee> emp = dc.GetTable<Employee>();
                var result = from p in emp
                             select new { p.員工編號, p.員工姓名, p.職位, p.聯絡電話, p.月薪 };
                dataGridView1.DataSource = result;
            }

        }
    }
}
