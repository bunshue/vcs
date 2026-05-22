using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for FileStream
using System.Collections;  // for ArrayList

namespace vcs_DataSet_DataTable
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            dataGridView1.Size = new Size(410, 340);
            dataGridView1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            dataGridView2.Size = new Size(410, 340);
            dataGridView2.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1280, 750);
            this.Text = "vcs_DataSet_DataTable";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //建立DataTable 1
            //1.創建表實例
            DataTable dt = new DataTable();

            // 建立資料表結構, 預設格式為字串
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            // 創建新行, 並為新行賦值 並 添加到DataTable
            DataRow dr1 = dt.NewRow();
            dr1[0] = "1";
            dr1[1] = "david";
            dr1[2] = "100";
            dt.Rows.Add(dr1);

            DataRow dr2 = dt.NewRow();
            dr2[0] = "5";
            dr2[1] = "john";
            dr2[2] = "80";
            dt.Rows.Add(dr2);

            DataRow dr3 = dt.NewRow();
            dr3[0] = "12";
            dr3[1] = "mary";
            dr3[2] = "92";
            dt.Rows.Add(dr3);

            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //創建一個 DataTable 來存放資料庫

            DataTable dt = new DataTable();

            //加入所需要欄位

            // 建立資料表結構, 格式為字串
            dt.Columns.Add("學號", typeof(string));  // 加入欄位名稱為學號，是字串型別
            dt.Columns.Add("姓名", typeof(string));  // 加入欄位名稱為姓名，是字串型別
            dt.Columns.Add("座號", typeof(string));  // 加入欄位名稱為座號，是字串型別

            //欄位新增完成，加入內容

            DataRow datarow1 = dt.NewRow();
            datarow1["學號"] = "001";   //指定加入學號為001
            datarow1["姓名"] = "大熊";  //指定加入姓名為大熊
            datarow1["座號"] = "01";   //指定加入座號為01
            dt.Rows.Add(datarow1);       //將 datarow1 的內容加入到 dt.Rows 裡

            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //動態處理DataTable

            //1.創建表實例
            DataTable dt = new DataTable();

            // 建立資料表結構, 預設格式為字串
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.創建新行
            DataRow dr = dt.NewRow();

            //4.為新行賦值
            dr[0] = "1";
            dr[1] = "林林";

            //5.將新行添加到表
            dt.Rows.Add(dr);

            /*
            //1.創建表實例
            DataTable dt = new DataTable();

            // 建立資料表結構, 預設格式為字串
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.添加新行
            dt.Rows.Add("1", "Name");
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            DataTable dt = new DataTable();
            // 建立資料表結構, 格式為布林
            dt.Columns.Add("A", typeof(bool));
            dt.Columns.Add("B", typeof(bool));
            dt.Columns.Add("C", typeof(bool));

            dt.Rows.Add(true, false, true);
            //dt.Rows.Add(true, true, false);
            //dt.Rows.Add(false, true, false);
            //dt.Rows.Add(false, false, true);

            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();

            // 建立資料表結構, 預設格式為字串
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.添加新行
            dt.Rows.Add("1", "david", "100");
            dt.Rows.Add("5", "john", "80");
            dt.Rows.Add("12", "mary", "92");

            richTextBox1.Text += "原DataTable :\n";
            show_DataTable(dt);  // 顯示 DataTable 的內容

            richTextBox1.Text += "由 姓名 項列出資料\n";
            int R = dt.Rows.Count;
            for (int i = 0; i < R; i++)
            {
                richTextBox1.Text += "找到\t" + dt.Rows[i]["姓名"].ToString() + "\n";
            }

            richTextBox1.Text += "刪除第1項後DataTable :\n";
            dt.Rows.RemoveAt(1);
            show_DataTable(dt);  // 顯示 DataTable 的內容

            richTextBox1.Text += "由 姓名 項列出資料\n";
            R = dt.Rows.Count;
            for (int i = 0; i < R; i++)
            {
                richTextBox1.Text += "找到\t" + dt.Rows[i]["姓名"].ToString() + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "構建DataTable，給列名添加公式\n";

            //計算公式
            string expression1 = "a+b*(c-d)";
            string expression2 = "a+b-c-d";

            //構建 DataTable
            DataTable dt = new DataTable();
            // 建立資料表結構, 格式為整數
            dt.Columns.Add("a", typeof(int));
            dt.Columns.Add("b", typeof(int));
            dt.Columns.Add("c", typeof(int));
            dt.Columns.Add("d", typeof(int));
            dt.Columns.Add("e1", typeof(int));//公式列
            dt.Columns.Add("e2", typeof(int));//公式列

            //添加公式
            dt.Columns["e1"].Expression = expression1;
            dt.Columns["e2"].Expression = expression2;

            //添加一行並賦值
            DataRow row = dt.Rows.Add();
            row["a"] = 1;
            row["b"] = 2;
            row["c"] = 4;
            row["d"] = 3;

            dt.BeginLoadData();
            dt.EndLoadData();

            int C = dt.Columns.Count;
            for (int i = 0; i < C; i++)
            {
                //Console.Write(dt.Columns[i].ColumnName + "\t");
                richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
            }

            //Console.WriteLine();
            richTextBox1.Text += "\n";

            C = dt.Columns.Count;
            for (int i = 0; i < C; i++)
            {
                Console.Write(row[i].ToString() + "\t");
                richTextBox1.Text += row[i].ToString() + "\t";
            }

            richTextBox1.Text += "\n";

            /*
            //使用DataTable的Compute()方法

            DataTable dt = new DataTable();
            string value = dt.Compute("1+2*(4-3)", "").ToString();
            Console.WriteLine(value);
            */

            //可以把 DataTable 直接轉給 DataGridView 顯示
            //dataGridView1.DataSource = dt.DefaultView;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //DataTable用法

            //初始化一個DataTable, 並給定名稱
            DataTable dt = new DataTable("第一資料表");

            //添加資料1
            // 建立資料表結構, 格式為字串
            dt.Columns.Add("column0", Type.GetType("System.String"));
            //添加資料2
            // 建立資料表結構, 格式為布林
            DataColumn dc = new DataColumn("column1", Type.GetType("System.Boolean"));
            dt.Columns.Add(dc);

            DataRow dr = dt.NewRow();
            dr["column0"] = "AX";
            dr["column1"] = true;
            dt.Rows.Add(dr);
            //Doesn't initialize the row
            DataRow dr1 = dt.NewRow();
            dt.Rows.Add(dr1);

            //Search the second row 如果沒有賦值,則用is null來select
            DataRow[] drs = dt.Select("column1 is null");
            DataRow[] drss = dt.Select("column0 = 'AX'");

            //複製DataTable, 全部
            DataTable dtNew = dt.Copy();

            //複製DataTable, 僅Scheme
            DataTable dtOnlyScheme = dt.Clone();

            //對dt的操作
            //Method 1
            DataRow drOperate = dt.Rows[0];
            drOperate["column0"] = "AXzhz";
            drOperate["column1"] = false;
            //Method 2
            drOperate[0] = "AXzhz";
            drOperate[1] = false;
            //Method 3
            dt.Rows[0]["column0"] = "AXzhz";
            dt.Rows[0]["column1"] = false;
            //Method 4
            dt.Rows[0][0] = "AXzhz";
            dt.Rows[0][1] = false;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            DataTable dt = new DataTable();
            // 建立資料表結構
            dt.Columns.Add("id", typeof(string));
            dt.Columns.Add("value", typeof(int));

            for (int i = 1; i <= 5; i++)
            {
                DataRow dRow = dt.NewRow();
                dRow["id"] = "id" + i.ToString();
                dRow["value"] = i;
                dt.Rows.Add(dRow);
            }

            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //DataTable用法

            DataTable dt = new DataTable();
            // 建立資料表結構, 預設格式為字串
            dt.Columns.Add("第一欄");
            string data = string.Empty;
            for (int i = 0; i < 5; i++)
            {
                data = "DT資料 " + i.ToString();
                dt.Rows.Add(data);
                richTextBox1.Text += "加入資料 : " + data + "\n";
            }

            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //DataTable用法
            DataTable dt = new DataTable();

            // 建立資料表結構, 3欄
            DataColumn column1 = new DataColumn();//创建数据列对象
            column1.DataType = Type.GetType("System.String");   //设置数据类型
            column1.ColumnName = "姓名"; //设置列名称
            dt.Columns.Add(column1);//添加数据列

            DataColumn column2 = new DataColumn();//创建数据列对象
            column2.DataType = Type.GetType("System.String");   //设置数据类型
            column2.ColumnName = "英文"; //设置列名称
            dt.Columns.Add(column2);//添加数据列

            DataColumn column3 = new DataColumn();//创建数据列对象
            column3.DataType = Type.GetType("System.String");   //设置数据类型
            column3.ColumnName = "數學"; //设置列名称
            dt.Columns.Add(column3);//添加数据列

            Random r = new Random();

            for (int i = 0; i < 10; i++)
            {
                DataRow dr;//创建数据行变量
                dr = dt.NewRow();//得到数据行对象
                dr["姓名"] = "姓名" + i.ToString();  //设置内容
                dr["英文"] = r.Next(90, 100).ToString();  //设置内容
                dr["數學"] = r.Next(70, 100).ToString();  //设置内容
                dt.Rows.Add(dr);//添回数据行
                //Method(dt);//显示数据表中内容
            }

            int C = dt.Columns.Count;
            int R = dt.Rows.Count;
            richTextBox1.Text += "C = " + C.ToString() + "\n";
            richTextBox1.Text += "R = " + R.ToString() + "\n";

            for (int i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            for (int j = 0; j < R; j++)
            {
                for (int i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "判斷DataTable中是否包含某值\n";

            string columnName = "英文";
            string fieldData = "90";

            Boolean result = IsColumnIncludeData(dt, columnName, fieldData);

            richTextBox1.Text += "科目 : " + columnName + "\t成績 : " + fieldData + "\t\t";

            if (result == true)
            {
                richTextBox1.Text += "存在\n";
            }
            else
            {
                richTextBox1.Text += "不存在\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "向DataTable中添加數據\n";
            DataRow dr2;
            for (int i = 0; i < 5; i++)
            {
                //if (IsColumnIncludeData(dt, "SystemCode", code[i]) == false)
                {
                    dr2 = dt.NewRow();
                    dr2[0] = "NNNN";
                    dr2[1] = "EEEE";
                    dr2[2] = "MMMM";
                    dt.Rows.Add(dr2);
                }
            }

            C = dt.Columns.Count;
            R = dt.Rows.Count;
            richTextBox1.Text += "C = " + C.ToString() + "\n";
            richTextBox1.Text += "R = " + R.ToString() + "\n";

            for (int i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            for (int j = 0; j < R; j++)
            {
                for (int i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        /// <summary>
        /// 判斷DataTable中是否包含某值
        /// </summary>
        /// <param name="dt">DataTable</param>
        /// <param name="columnName">列名</param>
        /// <param name="fieldData">值</param>
        /// <returns></returns>
        public Boolean IsColumnIncludeData(DataTable dt, String columnName, string fieldData)
        {
            if (dt == null)
            {
                return false;
            }
            else
            {
                DataRow[] dataRows = dt.Select(columnName + "='" + fieldData + "'");
                if (dataRows.Length.Equals(1))
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //DataTable用法

            DataTable dt = new DataTable("第一資料表");
            // 建立資料表結構, 格式為字串
            dt.Columns.Add("第一欄", Type.GetType("System.String"));
            dt.Columns.Add("第二欄", Type.GetType("System.String"));
            dt.Columns.Add("第三欄", Type.GetType("System.String"));

            DataRow dr;

            dr = dt.NewRow();
            dr["第一欄"] = "aaaa1";
            dr["第二欄"] = "bbbb1";
            dr["第三欄"] = "cccc1";
            dt.Rows.Add(dr);

            dr = dt.NewRow();
            dr["第一欄"] = "aaaa2";
            dr["第二欄"] = "bbbb2";
            dr["第三欄"] = "cccc2";
            dt.Rows.Add(dr);

            dr = dt.NewRow();
            dr["第一欄"] = "aaaa3";
            dr["第二欄"] = "bbbb3";
            dr["第三欄"] = "cccc3";
            dt.Rows.Add(dr);

            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //DataTable用法 11

            DataTable dt = new DataTable("第一資料表");

            // 建立資料表結構, 預設格式為字串
            DataColumn column = new DataColumn("第一欄");
            dt.Columns.Add(column);

            DataRow row;

            for (int i = 0; i < 5; i++)
            {
                row = dt.NewRow();
                row["第一欄"] = "紀錄- " + i;
                dt.Rows.Add(row);
            }
            dt.AcceptChanges();

            show_DataTable(dt);//顯示 DataTable 的內容

            richTextBox1.Text += "------------------------------\n";  // 30個

            dt.Rows[1]["第一欄"] = "物件導向";

            row = dt.NewRow();
            row["第一欄"] = "程式設計";
            dt.Rows.Add(row);

            show_DataTable(dt);//顯示 DataTable 的內容

            dt.Rows[1].Delete();
            dt.Rows[2].Delete();
            dt.Rows[3].Delete();

            //NG show_DataTable(dt);//顯示 DataTable 的內容
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //DataTable中使用Order By排序與Where過濾

            richTextBox1.Text += "DataTable\n";

            //這裡構造一個數據源
            DataTable dt = new DataTable();

            // 建立資料表結構, 格式為字串
            dt.Columns.Add("ID", typeof(String));
            dt.Columns.Add("uName", typeof(String));
            dt.Columns.Add("uDate", typeof(DateTime));
            for (int i = 0; i < 10; i++)
            {
                DataRow dr = dt.NewRow();
                dr["ID"] = i.ToString();
                dr["uName"] = "name" + i;
                dt.Rows.Add(dr);
            }
            dt.DefaultView.Sort = "ID asc";//相當於Order By
            dt.DefaultView.RowFilter = "ID>5";//相當於Where

            //GridView1.DataSource = dt;
            //GridView1.DataBind();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //去除DataTable中的重複項

            //建立DataTable 1
            //1.創建表實例
            DataTable dt = new DataTable();

            // 建立資料表結構, 預設格式為字串
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            // 創建新行, 並為新行賦值 並 添加到DataTable
            DataRow dr1 = dt.NewRow();
            dr1[0] = "1";
            dr1[1] = "david";
            dr1[2] = "100";
            dt.Rows.Add(dr1);

            DataRow dr2 = dt.NewRow();
            dr2[0] = "5";
            dr2[1] = "john";
            dr2[2] = "80";
            dt.Rows.Add(dr2);

            DataRow dr3 = dt.NewRow();
            dr3[0] = "12";
            dr3[1] = "mary";
            dr3[2] = "92";
            dt.Rows.Add(dr3);

            //加一筆重複資料

            //3.創建新行
            DataRow dr4 = dt.NewRow();

            //4.為新行賦值 並 添加到DataTable
            dr4[0] = "5";
            dr4[1] = "john";
            dr4[2] = "80";
            dt.Rows.Add(dr4);

            richTextBox1.Text += "原資料:\n";
            show_DataTable(dt);  // 顯示 DataTable 的內容

            richTextBox1.Text += "\n去除DataTable中的重複項\n\n";

            DeleteSameRow(dt, "座號");    //後面是比較項目, Columns資料, "座號", "姓名", "分數"

            richTextBox1.Text += "新資料:\n";
            show_DataTable(dt);  // 顯示 DataTable 的內容
        }

        ///
        /// 删除DataTable重复列，类似distinct   
        ///
        ///DataTable
        ///字段名
        ///
        public static DataTable DeleteSameRow(DataTable dt, string Field)
        {
            ArrayList indexList = new ArrayList();
            // 找出待删除的行索引   
            int R = dt.Rows.Count;
            for (int i = 0; i < R - 1; i++)
            {
                if (!IsContain(indexList, i))
                {
                    for (int j = i + 1; j < R; j++)
                    {
                        if (dt.Rows[i][Field].ToString() == dt.Rows[j][Field].ToString())
                        {
                            indexList.Add(j);
                        }
                    }
                }
            }
            indexList.Sort();
            // 排序
            for (int i = indexList.Count - 1; i >= 0; i--)// 根据待删除索引列表删除行  
            {
                int index = Convert.ToInt32(indexList[i]);
                dt.Rows.RemoveAt(index);
            }
            return dt;
        }

        /// <summary>   
        /// 判断数组中是否存在   
        /// </summary>   
        /// <param name="indexList">数组</param>   
        /// <param name="index">索引</param>   
        /// <returns></returns>   
        public static bool IsContain(ArrayList indexList, int index)
        {
            for (int i = 0; i < indexList.Count; i++)
            {
                int tempIndex = Convert.ToInt32(indexList[i]);
                if (tempIndex == index)
                {
                    return true;
                }
            }
            return false;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //DataTable常用方法
            richTextBox1.Text += "DataTable常用方法\n";

            DataTable dt = new DataTable("第一資料表");

            // 建立資料表結構, 3欄
            DataColumn column1 = new DataColumn();
            column1.DataType = Type.GetType("System.Int32");
            column1.ColumnName = "id";
            column1.ReadOnly = true;
            dt.Columns.Add(column1);

            DataColumn column2 = new DataColumn();
            column2.DataType = Type.GetType("System.String");
            column2.ColumnName = "Name";
            dt.Columns.Add(column2);

            DataColumn column3 = new DataColumn();
            column3.DataType = Type.GetType("System.DateTime");
            column3.ColumnName = "Timer";
            dt.Columns.Add(column3);

            //// 主键的创建
            //DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            //PrimaryKeyColumns[0] = dt.Columns["id"];
            //dt.PrimaryKey = PrimaryKeyColumns;

            dt.PrimaryKey = new DataColumn[] { column1 };

            DataRow dr;

            dr = dt.NewRow();
            dr["id"] = 1;
            dr["Name"] = "Name";
            dr["Timer"] = DateTime.Now.AddSeconds(10);
            dt.Rows.Add(dr);

            dr = dt.NewRow();
            dr["id"] = 11;
            dr["Name"] = "Name11";
            dr["Timer"] = DateTime.Now.AddSeconds(8);
            dt.Rows.Add(dr);

            dr = dt.NewRow();
            dr["id"] = 111;
            dr["Name"] = "Name111";
            dr["Timer"] = DateTime.Now.AddSeconds(5);
            dt.Rows.Add(dr);

            dr = dt.NewRow();
            dr["id"] = 2;
            dr["Name"] = "Name2";
            dr["Timer"] = DateTime.Now.AddSeconds(3);
            dt.Rows.Add(dr);

            StringBuilder sb = new StringBuilder();

            string sortOrder = "Timer asc";

            //foreach (DataColumn dc in dt.Columns)
            //{
            //    //sb.Append(dc.ColumnName+"<br/>");    
            //}

            //foreach (DataRow dr in dt.Rows)
            //{
            //    foreach (DataColumn dc in dt.Columns)
            //    {
            //        sb.Append(dr[dc] + "|");
            //    }
            //    sb.Append("<br/>");
            //}

            dt = DeleteRows("11", dt);

            string expression;
            expression = "id>0";
            DataRow[] foundRows;

            foundRows = dt.Select(expression, sortOrder);

            for (int i = 0; i < foundRows.Length; i++)
            {
                sb.Append(foundRows[i]["Name"] + "=" + foundRows[i]["Timer"] + "<br/>");
            }

            //if (UpdataNews("1", dt, "xiaohu"))
            //{
            //    sb.Append("update true");
            //}
            //else
            //{
            //    sb.Append("update False");
            //}

            sb.Append("====================================<br/>");

            dt = DeleteRows("1", dt);
            expression = "id>0";
            foundRows = dt.Select(expression, sortOrder);
            for (int i = 0; i < foundRows.Length; i++)
            {
                sb.Append(foundRows[i]["Name"] + "=" + foundRows[i]["Timer"] + "<br/>");
            }

            // 用户判断当前的ID是不是存在
            if (CheckIDBool("1", dt))
            {
                sb.Append("Bool true");
            }
            else
            {
                sb.Append("Bool false");
            }
            richTextBox1.Text += sb.ToString() + "\n";
        }

        /// <summary>
        /// 判断是不是存在
        /// </summary>
        /// <param name="key"></param>
        /// <param name="dt"></param>
        /// <returns></returns>
        private bool CheckIDBool(string key, DataTable dt)
        {
            bool rs = false;
            //string strKey ="";
            //strKey = "id=" + key;
            //if (dt.Select(strKey).Length > 0)
            //{
            //    rs = true;
            //}

            // 方法二:
            //northwindDataSet1.Customers.FindByCustomerID("ALFKI");

            DataRow foundRow = dt.Rows.Find(key);

            if (foundRow != null)
            {
                rs = true;
            }
            return rs;
        }

        /// <summary>
        /// 根据主键查找DataTable中的值,返回DataRow
        /// </summary>
        /// <param name="key"></param>
        /// <param name="dt"></param>
        /// <returns></returns>
        private DataRow[] DtSelect(string key, DataTable dt)
        {
            string strKey = "";
            strKey = "id=" + key;
            DataRow[] foundRows;
            foundRows = dt.Select(strKey);
            return foundRows;
        }

        private DataRow[] DtSelect(string key, DataTable dt, string sortOrder)
        {
            string strKey = "";
            strKey = "id=" + key;
            DataRow[] foundRows;
            foundRows = dt.Select(strKey, sortOrder);
            return foundRows;
        }

        private bool UpdataNews(string key, DataTable dt, string name)
        {
            bool rs = false;
            string strKey = "";
            strKey = "id='" + key + "'";

            if (CheckIDBool(key, dt))
            {
                DataRow[] customerRow =
                dt.Select(strKey);
                customerRow[0]["Name"] = name;
                customerRow[0]["Timer"] = DateTime.Now.AddYears(-1);
                rs = true;
            }
            return rs;
        }

        private DataTable DeleteRows(string key, DataTable dt)
        {
            DataRow[] foundRows;
            foundRows = DtSelect(key, dt);
            if (foundRows.Length > 0)
            {
                dt.Rows.Remove(foundRows[0]);
            }
            return dt;
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
            // 建構DataSet及其組成的資料表1
            DataSet ds = new DataSet("學生資料集");

            DataTable dt = new DataTable("學生資料表");

            // 這個資料表的資料列中的初始開始大小。預設值為 50。
            dt.MinimumCapacity = 50;

            // 建構資料欄
            DataColumn column1 = new DataColumn("編號");
            DataColumn column2 = new DataColumn("姓名");
            DataColumn column3 = new DataColumn("學歷");

            // 設定「編號」資料欄為自動增加數值
            column1.DataType = Type.GetType("System.Int32");
            column1.AutoIncrement = true;

            // 建立資料表結構, 3欄
            dt.Columns.Add(column1);
            dt.Columns.Add(column2);
            dt.Columns.Add(column3);

            // 將資料表加入DataSet
            ds.Tables.Add(dt);

            // 加入記錄
            DataRow newRow;
            newRow = dt.NewRow();
            newRow["姓名"] = "唐三藏";
            newRow["學歷"] = "博士";
            dt.Rows.Add(newRow);

            newRow = dt.NewRow();
            newRow["姓名"] = "孫悟空";
            newRow["學歷"] = "碩士";
            dt.Rows.Add(newRow);

            newRow = dt.NewRow();
            newRow["姓名"] = "豬八戒";
            newRow["學歷"] = "學士";
            dt.Rows.Add(newRow);

            newRow = dt.NewRow();
            newRow["姓名"] = "牛魔王";
            newRow["學歷"] = "學士";
            dt.Rows.Add(newRow);

            newRow = dt.NewRow();
            newRow["姓名"] = "如來佛";
            newRow["學歷"] = "博士";
            dt.Rows.Add(newRow);

            ds.AcceptChanges();

            // 秀出剛動態建構出來的DataSet

            dataGridView1.DataSource = ds.Tables["學生資料表"];

            richTextBox1.Text += "------------------------------\n";  // 30個

            //寫成XML文件

            string xml_filename = string.Empty;
            try
            {
                // 將ds寫成XML文件
                //string xml_filename = @"C:\\XmlDocument-" + DateTime.Now.Millisecond.ToString() + ".xml";
                xml_filename = @"tmp_xml_" + DateTime.Now.Millisecond.ToString() + ".xml";
                FileStream streamWrite = new FileStream(xml_filename, FileMode.Create);
                ds.WriteXml(streamWrite);
                streamWrite.Dispose();

                MessageBox.Show("已建構完成XML文件：" + xml_filename);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //另法
            xml_filename = @"tmp_xml222_" + DateTime.Now.Millisecond.ToString() + ".xml";
            FileStream fs = new FileStream(xml_filename, FileMode.OpenOrCreate, FileAccess.Write);
            // Apply the WriteXml method to write an XML document
            ds.WriteXml(fs);
            fs.Close();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //讀入XML文件

            // 建構DataSet物件
            ds = new DataSet("學生資料集");

            // 讀入XML文件 
            xml_filename = "../../XmlDocument-432.xml";
            FileStream streamRead = new FileStream(xml_filename, FileMode.Open);
            ds.ReadXml(streamRead);
            streamRead.Dispose();

            // 秀出讀入的XML文件
            dataGridView2.DataSource = ds.Tables["學生資料表"];
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
            //DT轉DS轉DGV

            // 建立兩個 DataTable dt1 dt2

            DataTable dt1 = new DataTable("第一資料表");

            // 建立資料表結構, 2欄
            DataColumn column1a = new DataColumn();
            column1a.DataType = Type.GetType("System.Int32");
            column1a.ColumnName = "第一欄";
            column1a.ReadOnly = true;
            column1a.Unique = true;
            dt1.Columns.Add(column1a);

            DataColumn column1b = new DataColumn();
            column1b.DataType = Type.GetType("System.String");
            column1b.ColumnName = "第二欄";
            column1b.AutoIncrement = false;
            column1b.Caption = "第二欄";
            column1b.ReadOnly = false;
            column1b.Unique = false;
            dt1.Columns.Add(column1b);

            // 設定 第一欄 為primary key
            DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            PrimaryKeyColumns[0] = dt1.Columns["第一欄"];
            dt1.PrimaryKey = PrimaryKeyColumns;

            DataRow dr11 = dt1.NewRow();
            dr11["第一欄"] = 11;
            dr11["第二欄"] = "alpha";
            dt1.Rows.Add(dr11);
            DataRow dr12 = dt1.NewRow();
            dr12[0] = 22;
            dr12[1] = "bravo";
            dt1.Rows.Add(dr12);
            DataRow dr13 = dt1.NewRow();
            dr13[0] = 33;
            dr13[1] = "charlie";
            dt1.Rows.Add(dr13);

            richTextBox1.Text += "------------------------------\n";  // 30個

            DataTable dt2 = new DataTable("第二資料表");
            DataRow datarow2;

            // 建立資料表結構, 3欄
            DataColumn column2a = new DataColumn();
            column2a.DataType = Type.GetType("System.Int32");
            column2a.ColumnName = "第一欄";
            column2a.AutoIncrement = true;
            column2a.Caption = "第一欄";
            column2a.ReadOnly = true;
            column2a.Unique = true;
            dt2.Columns.Add(column2a);

            DataColumn column2b = new DataColumn();
            column2b.DataType = Type.GetType("System.String");
            column2b.ColumnName = "第二欄";
            column2b.AutoIncrement = false;
            column2b.Caption = "第二欄";
            column2b.ReadOnly = false;
            column2b.Unique = false;
            dt2.Columns.Add(column2b);

            DataColumn column2c = new DataColumn();
            column2c.DataType = Type.GetType("System.Int32");
            column2c.ColumnName = "第三欄";
            column2c.AutoIncrement = false;
            column2c.Caption = "第三欄";
            column2c.ReadOnly = false;
            column2c.Unique = false;
            dt2.Columns.Add(column2c);

            DataRow dr21 = dt2.NewRow();
            dr21["第一欄"] = 11;
            dr21["第二欄"] = "alpha";
            dr21["第三欄"] = 111;
            dt2.Rows.Add(dr21);
            DataRow dr22 = dt2.NewRow();
            dr22[0] = 22;
            dr22[1] = "bravo";
            dr22[2] = 222;
            dt2.Rows.Add(dr22);
            DataRow dr23 = dt2.NewRow();
            dr23[0] = 33;
            dr23[1] = "charlie";
            dr23[2] = 333;
            dt2.Rows.Add(dr23);

            for (int i = 0; i <= 2; i++)
            {
                datarow2 = dt2.NewRow();
                datarow2["第一欄"] = i;
                datarow2["第二欄"] = "AAAAAA" + i.ToString();
                datarow2["第三欄"] = 123 * i;
                dt2.Rows.Add(datarow2);
            }

            // 建立一個 DataSet ds, 裏面有兩個 DataTable dt1 dt2
            DataSet ds = new DataSet();
            ds.Tables.Add(dt1);
            ds.Tables.Add(dt2);

            dataGridView1.DataSource = ds;
            dataGridView1.DataMember = "第一資料表";

            dataGridView2.DataSource = ds;
            dataGridView2.DataMember = "第二資料表";

            show_DataTable(dt1);//顯示 DataTable 的內容
            richTextBox1.Text += "------------------------------\n";  // 30個
            show_DataTable(dt2);//顯示 DataTable 的內容

            richTextBox1.Text += "------------------------------\n";  // 30個

            show_DataSet(ds);

            richTextBox1.Text += "------------------------------\n";  // 30個


        }

        //------------------------------------------------------------  # 60個

        void show_DataSet(DataSet ds)
        {
            // 巡覽每一資料表
            foreach (DataTable dt in ds.Tables)
            {
                show_DataTable(dt);  // 顯示 DataTable 的內容
            }
        }

        void show_DataTable(DataTable dt)
        {
            int C = dt.Columns.Count;
            int R = dt.Rows.Count;
            richTextBox1.Text += "顯示 DataTable 的內容, 表單名稱 : " + dt.TableName + "\n";
            richTextBox1.Text += "共有資料欄位 : " + C.ToString() + " 欄, 資料 : " + R.ToString() + " 筆\n";
            richTextBox1.Text += "欄位名稱 : ";
            for (int i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
            }
            richTextBox1.Text += "\n內容\n";
            for (int j = 0; j < R; j++)
            {
                for (int i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


/*

//關於c#在DataTable中根據條件刪除某一行，

我們經常會將數據源放在DataTable裡面,但是有時候也需要移除不想要的行,下面的代碼告訴你們

　　　　　　DataTable dts；
                DataRow[] foundRow;
                foundRow = dts.Select("ID=99", "");
                foreach (DataRow row in foundRow)
                {
                    dts.Rows.Remove(row);
                }

其實就是用DataTable的Select方法

上面就是如何Datatable中某一行的id為99，就移除這一行,id為字段名

//------------------------------------------------------------  # 60個

// DataTable 相關操作

///判斷DataTable中某列是否包含某值
/// <summary>
    /// 判斷DataTable中是否包含某值
    /// </summary>
    /// <param name="dt">DataTable</param>
    /// <param name="columnName">列名</param>
    /// <param name="fieldData">值</param>
    /// <returns></returns>
    public Boolean IsColumnIncludeData(DataTable dt, String columnName, string fieldData)
    {
        if (dt == null)
        {
            return false;
        }
        else
        {
            DataRow[] dataRows = dt.Select(columnName + "='" + fieldData + "'");
            if (dataRows.Length.Equals(1))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
 

向DataTable中添加數據

DataTable dt = null;

        dt = handle.ExecuteDataTable(sql, true);

        #region

        DataRow dr;

        for (int i = 0; i < code.Length; i++)
        {
            if (IsColumnIncludeData(dt, "SystemCode", code[i]) == false)
            {
                dr = dt.NewRow();
                dr[0] = name[i];
                dr[1] = code[i];
                dr[2] = 0;
                dt.Rows.Add(dr);
            }
        }
        
        #endregion



List比較像陣列
DataTable可以加標題 比較像EXCEL表單

//如何將List轉換為DataTable

public static DataTable ToDataTable(List<NetworkAdapterInformation> list)
{
	DataTable dt = new DataTable();
	if (list.Count > 0)
	{
		PropertyInfo[] propertys = list[0].GetType().GetProperties();
		foreach (PropertyInfo pi in propertys)
		{
			dt.Columns.Add(pi.Name, pi.PropertyType);
		}
		for (int i = 0; i < list.Count; i++)
		{
			ArrayList tempList = new ArrayList();
			foreach (PropertyInfo pi in propertys)
			{
				object obj = pi.GetValue(list[i], null);
				tempList.Add(obj);
			}
			object[] array = tempList.ToArray();
			dt.LoadDataRow(array, true);
		}
	}
	return dt;
}

//------------------------------------------------------------  # 60個

C#_把dataTable數據導出到CSV,XLS文件
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190579.html
https://blog.csdn.net/happmaoo/article/details/83814604
        				
//------------------------------------------------------------  # 60個
*/

