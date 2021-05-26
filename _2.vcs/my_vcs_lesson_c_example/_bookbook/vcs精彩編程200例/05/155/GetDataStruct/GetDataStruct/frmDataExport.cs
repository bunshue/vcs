using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.IO;

namespace GetDataStruct
{
    public partial class frmDataExport : Form
    {
        public frmDataExport()
        {
            InitializeComponent();
        }
        public string OutData ="";
        public string OutTable = "";
        public string strserver = "";
        public string struser = "";
        public string strpwd = "";

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void frmDataExport_Load(object sender, EventArgs e)
        {
            groupBox1.Text = "数据表名称：" + OutTable ;
            try
            {
                using (SqlConnection con = new SqlConnection("Server=" + strserver + ";database=" + OutData + ";Uid=" + struser + ";Pwd=" + strpwd))
                {
                    string strSql = "select  name 字段名, xusertype 类型编号, length 长度 into hy_Linshibiao from  syscolumns  where id=object_id('" + OutTable + "') ";
                    strSql += "select name 类型,xusertype 类型编号 into angel_Linshibiao from systypes where xusertype in (select xusertype from syscolumns where id=object_id('" + OutTable + "'))";
                    con.Open();
                    SqlCommand cmd = new SqlCommand(strSql, con);
                    cmd.ExecuteNonQuery();
                    SqlDataAdapter da = new SqlDataAdapter("select 字段名,类型,长度 from hy_Linshibiao t,angel_Linshibiao b where t.类型编号=b.类型编号", con);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    this.dataGridView1.DataSource = dt.DefaultView;
                    SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
                    cmdnew.ExecuteNonQuery();
                    con.Close();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "警告", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        private void SaveAs() //导出成Excel
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Execl files (*.xls)|*.xls";
            saveFileDialog.FilterIndex = 0;
            saveFileDialog.RestoreDirectory = true;
            saveFileDialog.CreatePrompt = true;
            saveFileDialog.Title = "Export Excel File To";
            saveFileDialog.ShowDialog();
            Stream myStream;
            myStream = saveFileDialog.OpenFile();
            StreamWriter sw = new StreamWriter(myStream, System.Text.Encoding.GetEncoding(-0));
            string str = "";
            try
            {
                //写标题
                for (int i = 0; i < dataGridView1.ColumnCount; i++)
                {
                   if (i > 0)
                    {
                        str += "\t";
                    }
                    str += dataGridView1.Columns[i].HeaderText;
                }
                sw.WriteLine(str);
                //写内容
                for (int j = 0; j < dataGridView1.Rows.Count; j++)
                {
                    string tempStr = "";
                    for (int k = 0; k < dataGridView1.Columns.Count; k++)
                    {
                        if (k > 0)
                        {
                            tempStr += "\t";
                        }
                        tempStr += dataGridView1.Rows[j].Cells[k].Value.ToString();
                    }
                    sw.WriteLine(tempStr);
                }
                sw.Close();
                myStream.Close();
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString());
            }
            finally
            {
                sw.Close();
                myStream.Close();
            }
        }

        public void ExportData(DataGridView srcDgv, string fileName)//导出数据,传入一个datagridview和一个文件路径
        {
            string type = fileName.Substring(fileName.IndexOf(".") + 1);//获得数据类型
            if (type.Equals("xls", StringComparison.CurrentCultureIgnoreCase))//Excel文档
            {
                SaveAs();
            }
            //保存Word文件
            if (type.Equals("doc", StringComparison.CurrentCultureIgnoreCase))
            {

                object path = fileName;
                Object none = System.Reflection.Missing.Value;
                Microsoft.Office.Interop.Word.Application wordApp = new Microsoft.Office.Interop.Word.Application();
                Microsoft.Office.Interop.Word.Document document = wordApp.Documents.Add(ref none, ref none, ref none, ref none);
                //建立表格
                Microsoft.Office.Interop.Word.Table table = document.Tables.Add(document.Paragraphs.Last.Range, srcDgv.Rows.Count + 1, srcDgv.Columns.Count, ref none, ref none);
                try
                {
                    for (int i = 0; i < srcDgv.Columns.Count; i++)//设置标题
                    {
                        table.Cell(1, i + 1).Range.Text = srcDgv.Columns[i].HeaderText;
                    }
                    for (int i = 0; i < srcDgv.Rows.Count; i++)//填充数据
                    {
                        for (int j = 0; j < srcDgv.Columns.Count; j++)
                        {

                            table.Cell(i + 2, j + 1).Range.Text = srcDgv[j, i].Value.ToString();
                        }
                    }
                    document.SaveAs(ref path, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none);
                }
                finally
                {
                    wordApp.Quit(ref none, ref none, ref none);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string savePath = "";
            if (radioButton1.Checked == true)
            {
                saveFileDialog1.Filter = "WORD(*.doc)|*.doc";
                if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    savePath = saveFileDialog1.FileName;
                    ExportData(dataGridView1, savePath);
                }
            }
            if (radioButton2.Checked == true)
            {
                SaveAs();
            }  
        }
    }
}