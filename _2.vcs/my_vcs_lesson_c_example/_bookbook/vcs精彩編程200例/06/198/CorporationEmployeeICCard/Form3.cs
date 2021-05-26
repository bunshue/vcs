using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace CorporationEmployeeICCard
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)//查询
        {
            //BinddataGridView方法根据选择的日期查询相应的考勤信息
            baseClass.BinddataGridView(dataGridView1, dateTimePicker1.Text);
        }

        private void button2_Click(object sender, EventArgs e)//导出
        {
            string savePath = "";
            if (radioButton1.Checked == true)//如果导出EXCEL
            {
                saveFileDialog1.Filter = "EXCEL(*.xls)|*.xls";
                if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    savePath = saveFileDialog1.FileName;
                    //调用ExportData方法将数据导出到指定的文件中
                    baseClass.ExportData(dataGridView1, savePath);
                }
            }
            if (radioButton2.Checked == true)//如果导出WORD
            {
                saveFileDialog1.Filter = "WORD(*.doc)|*.doc";
                if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    savePath = saveFileDialog1.FileName;
                    //调用ExportData方法将数据导出到指定的文件中
                    baseClass.ExportData(dataGridView1, savePath);
                }
            }     
        }

        private void Form3_Load(object sender, EventArgs e)
        {

        }
    }
}
