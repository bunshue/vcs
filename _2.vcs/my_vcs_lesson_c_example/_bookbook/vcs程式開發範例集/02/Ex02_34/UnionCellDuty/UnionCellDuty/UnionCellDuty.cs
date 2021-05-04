using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace UnionCellDuty
{
    public partial class UnionCellDuty : Form
    {
        public UnionCellDuty()
        {
            InitializeComponent();
        }

        #region 声明的变量
        static string connectionString = "Data Source=.;DataBase=pubs;integrated security=sspi";
        SqlConnection conn = new SqlConnection(connectionString);
        SqlDataAdapter Adapter;
        DataSet dataSet = new DataSet();
        #endregion

        private void UnionCellDuty_Load(object sender,EventArgs e)
        {
            try
            {
                if(conn.State == ConnectionState.Closed)
                {
                    conn.Open();
                }
                dataSet.Clear();
                string selectString = "select job_id as 工作编号,job_desc as 工作次序,min_lvl as 最低水平,max_lvl as 最高水平 from jobs";
                Adapter = new SqlDataAdapter(selectString,conn);
                Adapter.Fill(dataSet,"UserInfo");
                DataTable dataTable = dataSet.Tables["UserInfo"];
                dataGridView1.DataSource = dataTable.DefaultView;
            }
            catch(SqlException ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                conn.Close();
            }
        }

        #region 合并列相同的内容
        private void dataGridView1_CellPainting(object sender,DataGridViewCellPaintingEventArgs e)//绘制单元格事件
        {
            // 对第1列相同单元格进行合并     
            if(e.ColumnIndex == 2 && e.RowIndex != -1 || e.ColumnIndex == 3 && e.RowIndex != -1)
            {
                Brush datagridBrush = new SolidBrush(dataGridView1.GridColor);
                SolidBrush groupLineBrush = new SolidBrush(e.CellStyle.BackColor);
                using(Pen datagridLinePen = new Pen(datagridBrush))
                {
                    // 清除单元格
                    e.Graphics.FillRectangle(groupLineBrush,e.CellBounds);
                    if(e.RowIndex < dataGridView1.Rows.Count - 1 && dataGridView1.Rows[e.RowIndex + 1].Cells[e.ColumnIndex].Value != null && dataGridView1.Rows[e.RowIndex + 1].Cells[e.ColumnIndex].Value.ToString() != e.Value.ToString())
                    {
                        //绘制底边线
                        e.Graphics.DrawLine(datagridLinePen,e.CellBounds.Left,e.CellBounds.Bottom - 1,e.CellBounds.Right,e.CellBounds.Bottom - 1);
                        // 画右边线
                        e.Graphics.DrawLine(datagridLinePen,e.CellBounds.Right - 1,e.CellBounds.Top,e.CellBounds.Right - 1,e.CellBounds.Bottom);
                    }
                    else
                    {
                        // 画右边线
                        e.Graphics.DrawLine(datagridLinePen,e.CellBounds.Right - 1,e.CellBounds.Top,e.CellBounds.Right - 1,e.CellBounds.Bottom);
                    }
                    //对最后一条记录只画底边线
                    if(e.RowIndex == dataGridView1.Rows.Count - 1)
                    {
                        //绘制底边线
                        e.Graphics.DrawLine(datagridLinePen,e.CellBounds.Left,e.CellBounds.Bottom - 1,e.CellBounds.Right,e.CellBounds.Bottom - 1);
                    }
                    // 填写单元格内容，相同的内容的单元格只填写第一个                        
                    if(e.Value != null)
                    {
                        if(e.RowIndex > 0 && dataGridView1.Rows[e.RowIndex - 1].Cells[e.ColumnIndex].Value.ToString() == e.Value.ToString())
                        {
                        }
                        else
                        {
                            //绘制单元格内容
                            e.Graphics.DrawString(e.Value.ToString(),e.CellStyle.Font,Brushes.Black,e.CellBounds.X + 2,e.CellBounds.Y + 5,StringFormat.GenericDefault);
                        }
                    }
                    e.Handled = true;
                }
            }
        }
        #endregion
    }
}
