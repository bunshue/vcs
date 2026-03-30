using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

namespace vcs_DataTable1
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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            dataGridView1.Size = new Size(400, 150);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 40);
            richTextBox1.Size = new Size(500, 500);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 784);
            this.Text = "vcs_DataTable1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立DataTable 1
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table1(dt);

            show_data_table(dt);//顯示 DataTable 的內容

            int R = dt.Rows.Count;

            string a = "";

            for (int i = 0; i < R; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    a += dt.Rows[i][j];
                    a += "\t";
                }
                a += "\n";
            }
            richTextBox1.Text += a + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table2(dt);

            show_data_table(dt);//顯示 DataTable 的內容
        }

        DataTable create_data_table1(DataTable dt)
        {
            //2.建立表結構
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.創建新行
            DataRow dr1 = dt.NewRow();
            DataRow dr2 = dt.NewRow();
            DataRow dr3 = dt.NewRow();

            //4.為新行賦值 並 添加到DataTable
            dr1[0] = "1";
            dr1[1] = "david";
            dr1[2] = "100";
            dt.Rows.Add(dr1);

            dr2[0] = "5";
            dr2[1] = "john";
            dr2[2] = "80";
            dt.Rows.Add(dr2);

            dr3[0] = "12";
            dr3[1] = "mary";
            dr3[2] = "92";
            dt.Rows.Add(dr3);

            return dt;
        }

        DataTable create_data_table2(DataTable dt)
        {
            //2.建立表結構
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.添加新行
            dt.Rows.Add("1", "david", "100");
            dt.Rows.Add("5", "john", "80");
            dt.Rows.Add("12", "mary", "92");
            return dt;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table2(dt);

            show_data_table(dt);//顯示 DataTable 的內容

            StringBuilder strXml = new StringBuilder();
            int R = dt.Rows.Count;
            int C = dt.Columns.Count;
            for (int i = 0; i < R; i++)
            {
                for (int j = 0; j < C; j++)
                {
                    strXml.AppendLine("<" + dt.Columns[j].ColumnName + ">" + dt.Rows[i][j] + "</" + dt.Columns[j].ColumnName + ">");
                }
            }
            richTextBox1.Text += strXml.ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            DataTable dt = null;
            dt = new DataTable();
            dt.Columns.Add("A", typeof(bool));
            dt.Columns.Add("B", typeof(bool));
            dt.Columns.Add("C", typeof(bool));
            dt.Rows.Add(checkBox1.Checked, checkBox2.Checked, checkBox3.Checked);

            string result = string.Format("A: {0}\r\nB: {1}\r\nC: {2}", dt.Rows[0]["A"], dt.Rows[0]["B"], dt.Rows[0]["C"]);
            richTextBox1.Text += result + "\n";
            show_data_table(dt);//顯示 DataTable 的內容
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table2(dt);

            richTextBox1.Text += "原DataTable :\n";
            show_data_table(dt);//顯示 DataTable 的內容

            richTextBox1.Text += "由 姓名 項列出資料\n";
            int R = dt.Rows.Count;
            for (int i = 0; i < R; i++)
            {
                richTextBox1.Text += "找到\t" + dt.Rows[i]["姓名"].ToString() + "\n";
            }

            richTextBox1.Text += "刪除第1項後DataTable :\n";
            dt.Rows.RemoveAt(1);
            show_data_table(dt);//顯示 DataTable 的內容

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

            //構建table
            DataTable table = new DataTable();
            table.Columns.Add("a", typeof(int));
            table.Columns.Add("b", typeof(int));
            table.Columns.Add("c", typeof(int));
            table.Columns.Add("d", typeof(int));
            table.Columns.Add("e1", typeof(int));//公式列
            table.Columns.Add("e2", typeof(int));//公式列

            //添加公式
            table.Columns["e1"].Expression = expression1;
            table.Columns["e2"].Expression = expression2;

            //添加一行並賦值
            DataRow row = table.Rows.Add();
            row["a"] = 1;
            row["b"] = 2;
            row["c"] = 4;
            row["d"] = 3;

            table.BeginLoadData();
            table.EndLoadData();

            for (int i = 0; i < table.Columns.Count; i++)
            {
                //Console.Write(table.Columns[i].ColumnName + "\t");
                richTextBox1.Text += table.Columns[i].ColumnName + "\t";
            }

            //Console.WriteLine();
            richTextBox1.Text += "\n";

            for (int i = 0; i < table.Columns.Count; i++)
            {
                Console.Write(row[i].ToString() + "\t");
                richTextBox1.Text += row[i].ToString() + "\t";
            }

            richTextBox1.Text += "\n";

            /*
            //使用DataTable的Compute()方法

            DataTable table = new DataTable();
            string value = table.Compute("1+2*(4-3)", "").ToString();
            Console.WriteLine(value);
            */

            //可以把 DataTable 直接轉給 DataGridView 顯示
            //dataGridView1.DataSource = dt.DefaultView;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //DataTable用法

            //初始化一個DataTable, 並給定名稱
            DataTable dt = new DataTable("Table_AX");

            //添加資料1
            dt.Columns.Add("column0", System.Type.GetType("System.String"));
            //添加資料2
            DataColumn dc = new DataColumn("column1", System.Type.GetType("System.Boolean"));
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
            //DataTable用法
            DataTable table = new DataTable();
            //初始化datatale 
            table.Columns.Add("id", typeof(string));
            table.Columns.Add("value", typeof(int));
            for (int i = 1; i <= 10; i++)
            {
                DataRow dRow = table.NewRow();
                dRow["id"] = "id" + i.ToString();
                dRow["value"] = i;
                table.Rows.Add(dRow);
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //DataTable用法

            DataTable dt = new DataTable();

            richTextBox1.Text += "建立DataTable, 填入資料\n";

            dt = create_datatable_data();

            richTextBox1.Text += "顯示DataTable資料a\n";
            int i;
            for (i = 0; i < 10; i++)
            {
                richTextBox1.Text += dt.Rows[i][0].ToString() + "\n";
            }

            richTextBox1.Text += "顯示DataTable資料b\n";
            ShowData(dt);
        }

        public DataTable create_datatable_data()
        {
            DataTable table = new DataTable();
            table.Columns.Add("Col");
            string data = string.Empty;
            for (int i = 0; i < 10; i++)
            {
                data = "DT資料 " + i.ToString();
                table.Rows.Add(data);
                richTextBox1.Text += "加入資料 : " + data + "\n";
            }
            return table;
        }

        public List<object> GetSomeDatas()
        {
            List<object> result = new List<object>();
            DataTable dt = new DataTable();
            dt = create_datatable_data();
            foreach (DataRow row in dt.Rows)
            {
                result.Add(row[0]);
            }
            return result;
        }

        public void ShowData(DataTable dt)
        {
            List<object> datas = GetSomeDatas();

            richTextBox1.Text += "共有資料 : " + datas.Count.ToString() + " 筆\n";

            foreach (object item in datas)
            {
                richTextBox1.Text += "顯示資料 : " + item + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //DataTable用法
            int i;
            int j;
            DataTable dt = new DataTable();

            DataColumn column1 = new DataColumn();//创建数据列对象
            column1.DataType = System.Type.GetType("System.String");   //设置数据类型
            column1.ColumnName = "姓名"; //设置列名称
            dt.Columns.Add(column1);//添加数据列

            DataColumn column2 = new DataColumn();//创建数据列对象
            column2.DataType = System.Type.GetType("System.String");   //设置数据类型
            column2.ColumnName = "英文"; //设置列名称
            dt.Columns.Add(column2);//添加数据列

            DataColumn column3 = new DataColumn();//创建数据列对象
            column3.DataType = System.Type.GetType("System.String");   //设置数据类型
            column3.ColumnName = "數學"; //设置列名称
            dt.Columns.Add(column3);//添加数据列

            Random r = new Random();

            for (i = 0; i < 10; i++)
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

            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "判斷DataTable中是否包含某值\n";
            Boolean result;

            string columnName = "英文";
            string fieldData = "90";

            result = IsColumnIncludeData(dt, columnName, fieldData);

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
            for (i = 0; i < 5; i++)
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

            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
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
            richTextBox1.Text += "構建DataTable，給列名添加公式\n";

            //計算公式
            string expression1 = "a+b*(c-d)";
            string expression2 = "a+b-c-d";

            //構建DataTable
            DataTable dt = new DataTable();
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
                Console.Write(dt.Columns[i].ColumnName + "\t");
                richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
            }

            Console.WriteLine();
            richTextBox1.Text += "\n";

            C = dt.Columns.Count;
            for (int i = 0; i < C; i++)
            {
                Console.Write(row[i].ToString() + "\t");
                richTextBox1.Text += row[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            int i;
            //DataTable用法

            DataTable dt = new DataTable();

            richTextBox1.Text += "建立DataTable, 填入資料\n";

            dt.Columns.Add("Col");
            string data = string.Empty;
            for (i = 0; i < 10; i++)
            {
                data = "DT資料 " + i.ToString();
                dt.Rows.Add(data);
                richTextBox1.Text += "加入資料 : " + data + "\n";
            }

            richTextBox1.Text += "顯示DataTable資料a\n";
            for (i = 0; i < 10; i++)
            {
                richTextBox1.Text += dt.Rows[i][0].ToString() + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //創建一個 DataTable 來存放資料庫

            DataTable dt = new DataTable();

            //加入所需要欄位

            dt.Columns.Add("學號", typeof(string));    //加入欄位名稱為學號，是字串型別
            dt.Columns.Add("姓名", typeof(string)); //加入欄位名稱為姓名，是字串型別
            dt.Columns.Add("座號", typeof(string)); //加入欄位名稱為座號，是字串型別

            //欄位新增完成，加入內容

            DataRow datarow1 = dt.NewRow();

            datarow1["學號"] = "001";   //指定加入學號為001
            datarow1["姓名"] = "大熊";  //指定加入姓名為大熊
            datarow1["座號"] = "01";   //指定加入座號為01
            dt.Rows.Add(datarow1);       //將 datarow1 的內容加入到 dt.Rows 裡
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //動態處理DataTable

            //1.創建表實例
            DataTable dt = new DataTable();

            //2.建立表結構
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
            DataTable dt=new DataTable();

            //2.建立表結構
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.添加新行
            dt.Rows.Add("1", "Name");
            */
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //DataTable用法

            DataTable dt = new DataTable();
            dt.Columns.Add("A", typeof(bool));
            dt.Columns.Add("B", typeof(bool));

            dt.Rows.Add(true, true);
            dt.Rows.Add(true, false);
            dt.Rows.Add(false, true);
            dt.Rows.Add(false, false);

            richTextBox1.Text += "result : \n";
            int i;
            for (i = 0; i < 4; i++)
            {
                richTextBox1.Text += string.Format("A: {0}\tB: {1}", dt.Rows[i]["A"], dt.Rows[i]["B"]) + "\n";
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //DataTable中使用Order By排序與Where過濾

            richTextBox1.Text += "DataTable\n";

            //這裡構造一個數據源
            DataTable dt = new DataTable();
            dt.Columns.Add("ID", typeof(System.String));
            dt.Columns.Add("uName", typeof(System.String));
            dt.Columns.Add("uDate", typeof(System.DateTime));
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

        private void button16_Click(object sender, EventArgs e)
        {
            //去除DataTable中的重複項

            //建立DataTable 1
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table1(dt);

            //加一筆重複資料

            //3.創建新行
            DataRow dr2 = dt.NewRow();

            //4.為新行賦值 並 添加到DataTable
            dr2[0] = "5";
            dr2[1] = "john";
            dr2[2] = "80";
            dt.Rows.Add(dr2);

            richTextBox1.Text += "原資料:\n";
            show_data_table(dt);//顯示 DataTable 的內容

            richTextBox1.Text += "\n去除DataTable中的重複項\n\n";

            DeleteSameRow(dt, "座號");    //後面是比較項目, Columns資料, "座號", "姓名", "分數"

            richTextBox1.Text += "新資料:\n";
            show_data_table(dt);//顯示 DataTable 的內容
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

        private void button17_Click(object sender, EventArgs e)
        {
            //DataTable常用方法
            richTextBox1.Text += "DataTable常用方法\n";

            DataTable myTb = new DataTable("auto");

            DataColumn myColid;
            myColid = new DataColumn();
            myColid.DataType = System.Type.GetType("System.Int32");
            myColid.ColumnName = "id";
            myColid.ReadOnly = true;
            myTb.Columns.Add(myColid);

            DataColumn myColname = new DataColumn();
            myColname.DataType = System.Type.GetType("System.String");
            myColname.ColumnName = "Name";
            myTb.Columns.Add(myColname);

            DataColumn myColtimer = new DataColumn();
            myColtimer.DataType = System.Type.GetType("System.DateTime");
            myColtimer.ColumnName = "Timer";
            myTb.Columns.Add(myColtimer);

            //// 主键的创建
            //DataColumn[] PrimaryKeyColumns = new DataColumn[1];
            //PrimaryKeyColumns[0] = myTb.Columns["id"];
            //myTb.PrimaryKey = PrimaryKeyColumns;

            myTb.PrimaryKey = new DataColumn[] { myColid };

            DataRow myDr;

            myDr = myTb.NewRow();
            myDr["id"] = 1;
            myDr["Name"] = "Name";
            myDr["Timer"] = DateTime.Now.AddSeconds(10);
            myTb.Rows.Add(myDr);

            myDr = myTb.NewRow();
            myDr["id"] = 11;
            myDr["Name"] = "Name11";
            myDr["Timer"] = DateTime.Now.AddSeconds(8);
            myTb.Rows.Add(myDr);

            myDr = myTb.NewRow();
            myDr["id"] = 111;
            myDr["Name"] = "Name111";
            myDr["Timer"] = DateTime.Now.AddSeconds(5);
            myTb.Rows.Add(myDr);

            myDr = myTb.NewRow();
            myDr["id"] = 2;
            myDr["Name"] = "Name2";
            myDr["Timer"] = DateTime.Now.AddSeconds(3);
            myTb.Rows.Add(myDr);

            System.Text.StringBuilder sb = new System.Text.StringBuilder();

            string sortOrder = "Timer asc";

            //foreach (DataColumn dc in myTb.Columns)
            //{
            //    //sb.Append(dc.ColumnName+"<br/>");    
            //}

            //foreach (DataRow dr in myTb.Rows)
            //{
            //    foreach (DataColumn dc in myTb.Columns)
            //    {
            //        sb.Append(dr[dc] + "|");
            //    }
            //    sb.Append("<br/>");
            //}

            myTb = DeleteRows("11", myTb);

            string expression;
            expression = "id>0";
            DataRow[] foundRows;

            foundRows = myTb.Select(expression, sortOrder);

            for (int i = 0; i < foundRows.Length; i++)
            {
                sb.Append(foundRows[i]["Name"] + "=" + foundRows[i]["Timer"] + "<br/>");
            }

            //if (UpdataNews("1", myTb, "xiaohu"))
            //{
            //    sb.Append("update true");
            //}
            //else
            //{
            //    sb.Append("update False");
            //}

            sb.Append("====================================<br/>");

            myTb = DeleteRows("1", myTb);
            expression = "id>0";
            foundRows = myTb.Select(expression, sortOrder);
            for (int i = 0; i < foundRows.Length; i++)
            {
                sb.Append(foundRows[i]["Name"] + "=" + foundRows[i]["Timer"] + "<br/>");
            }

            // 用户判断当前的ID是不是存在
            if (CheckIDBool("1", myTb))
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
        /// <param name="myTb"></param>
        /// <returns></returns>
        private bool CheckIDBool(string key, DataTable myTb)
        {
            bool rs = false;
            //string strKey ="";
            //strKey = "id=" + key;
            //if (myTb.Select(strKey).Length > 0)
            //{
            //    rs = true;
            //}

            // 方法二:
            //northwindDataSet1.Customers.FindByCustomerID("ALFKI");

            DataRow foundRow = myTb.Rows.Find(key);

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
        /// <param name="myTb"></param>
        /// <returns></returns>
        private DataRow[] DtSelect(string key, DataTable myTb)
        {
            string strKey = "";
            strKey = "id=" + key;
            DataRow[] foundRows;
            foundRows = myTb.Select(strKey);
            return foundRows;
        }

        private DataRow[] DtSelect(string key, DataTable myTb, string sortOrder)
        {
            string strKey = "";
            strKey = "id=" + key;
            DataRow[] foundRows;
            foundRows = myTb.Select(strKey, sortOrder);
            return foundRows;
        }

        private bool UpdataNews(string key, DataTable myTb, string name)
        {
            bool rs = false;
            string strKey = "";
            strKey = "id='" + key + "'";

            if (CheckIDBool(key, myTb))
            {
                DataRow[] customerRow =
                myTb.Select(strKey);
                customerRow[0]["Name"] = name;
                customerRow[0]["Timer"] = DateTime.Now.AddYears(-1);
                rs = true;
            }
            return rs;
        }

        private DataTable DeleteRows(string key, DataTable myTb)
        {
            DataRow[] foundRows;
            foundRows = DtSelect(key, myTb);
            if (foundRows.Length > 0)
            {
                myTb.Rows.Remove(foundRows[0]);
            }
            return myTb;
        }

        private DataTable MakeTable()
        {
            DataTable t = new DataTable("Control");
            t.Columns.Add("BackColor", typeof(Color));
            t.Columns.Add("ForeColor", typeof(Color));
            t.Columns.Add("Text");

            DataRow r;

            r = t.NewRow();
            r["BackColor"] = Color.Blue;
            r["ForeColor"] = Color.Yellow;
            r["Text"] = "藍底黃字";
            t.Rows.Add(r);

            r = t.NewRow();
            r["BackColor"] = Color.White;
            r["ForeColor"] = Color.Green;
            r["Text"] = "白底綠字";
            t.Rows.Add(r);

            r = t.NewRow();
            r["BackColor"] = Color.Orange;
            r["ForeColor"] = Color.Black;
            r["Text"] = "橙底黑字";
            t.Rows.Add(r);

            return t;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //DataTable用法
            DataTable t = MakeTable();
            richTextBox1.Text += t.ToString() + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //DataSet轉DataTable
            //動態建構DataSet

            // 建構DataSet及其組成的資料表
            DataSet studentsDataSet = new DataSet("StudentsDataSet");
            DataTable studentTable = new DataTable("StudentTable");

            // 建構資料欄
            DataColumn idColumn = new DataColumn("編號");
            DataColumn nameColumn = new DataColumn("姓名");
            DataColumn schoolColumn = new DataColumn("學歷");

            // 設定「編號」資料欄為自動增加數值
            idColumn.DataType = Type.GetType("System.Int32");
            idColumn.AutoIncrement = true;

            // 加入資料欄
            studentTable.Columns.Add(idColumn);
            studentTable.Columns.Add(nameColumn);
            studentTable.Columns.Add(schoolColumn);

            // 將資料表加入DataSet
            studentsDataSet.Tables.Add(studentTable);

            // 加入記錄
            DataRow newRow;
            newRow = studentTable.NewRow();
            newRow["姓名"] = "唐三藏";
            newRow["學歷"] = "博士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "孫悟空";
            newRow["學歷"] = "碩士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "豬八戒";
            newRow["學歷"] = "學士";
            studentTable.Rows.Add(newRow);

            // 秀出剛動態建構出來的DataSet 
            dataGridView1.DataSource = studentsDataSet.Tables["StudentTable"];
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //動態建構DataSet

            // 建構DataSet及其組成的資料表
            DataSet studentsDataSet = new DataSet("StudentsDataSet");
            DataTable studentTable = new DataTable("StudentTable");

            // 建構資料欄
            DataColumn idColumn = new DataColumn("編號");
            DataColumn nameColumn = new DataColumn("姓名");
            DataColumn schoolColumn = new DataColumn("學歷");

            // 設定「編號」資料欄為自動增加數值
            idColumn.DataType = Type.GetType("System.Int32");
            idColumn.AutoIncrement = true;

            // 加入資料欄
            studentTable.Columns.Add(idColumn);
            studentTable.Columns.Add(nameColumn);
            studentTable.Columns.Add(schoolColumn);

            // 將資料表加入DataSet
            studentsDataSet.Tables.Add(studentTable);

            // 加入記錄
            DataRow newRow;
            newRow = studentTable.NewRow();
            newRow["姓名"] = "唐三藏";
            newRow["學歷"] = "博士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "孫悟空";
            newRow["學歷"] = "碩士";
            studentTable.Rows.Add(newRow);

            newRow = studentTable.NewRow();
            newRow["姓名"] = "豬八戒";
            newRow["學歷"] = "學士";
            studentTable.Rows.Add(newRow);

            // 秀出剛動態建構出來的DataSet 
            // 巡覽每一資料表
            foreach (DataTable thisTable in studentsDataSet.Tables)
            {
                // 巡覽每一資料列
                foreach (DataRow row in thisTable.Rows)
                {
                    // 巡覽每一資料欄
                    foreach (DataColumn column in thisTable.Columns)
                    {
                        richTextBox1.AppendText(row[column].ToString());
                        richTextBox1.AppendText("\t");
                    }
                    richTextBox1.AppendText(Environment.NewLine);
                }
            }
        }

        private void MakeDataTable()
        {
            table = new DataTable("Table");
            column = new DataColumn("Column");
            table.Columns.Add(column);

            for (int i = 0; i < 10; i++)
            {
                row = table.NewRow();
                row["Column"] = "紀錄- " + i;
                table.Rows.Add(row);
            }
            table.AcceptChanges();
        }

        private void PrintView(DataView view, string label)
        {
            richTextBox1.AppendText(Environment.NewLine);
            richTextBox1.AppendText(Environment.NewLine + label);

            string result = "";
            for (int i = 0; i < view.Count; i++)
            {
                richTextBox1.AppendText(Environment.NewLine);
                richTextBox1.AppendText(view[i]["Column"].ToString());
                result = "DataViewRow.RowVersion值：" + view[i].RowVersion;
                richTextBox1.AppendText("，" + result);
            }
        }

        private void DemonstrateRowVersion()
        {
            DataView view = new DataView(table);

            table.Rows[1]["Column"] = "物件導向";

            row = table.NewRow();
            row["Column"] = "程式設計";
            table.Rows.Add(row);

            view.RowStateFilter = DataViewRowState.Added | DataViewRowState.ModifiedCurrent;
            PrintView(view, "**ModifiedCurrent及Added");

            view.RowStateFilter = DataViewRowState.ModifiedOriginal;
            PrintView(view, "**顯示已被變更的紀錄(ModifiedOriginal)");

            table.Rows[1].Delete();
            table.Rows[2].Delete();
            table.Rows[3].Delete();

            view.RowStateFilter = DataViewRowState.Deleted;
            PrintView(view, "**顯示已被刪除的紀錄(Deleted)");

            view.RowStateFilter = DataViewRowState.CurrentRows;
            PrintView(view, "**紀錄是目前的值(Current)");

            view.RowStateFilter = DataViewRowState.Unchanged;
            PrintView(view, "**紀錄未被變更者(Unchanged)");

            view.RowStateFilter = DataViewRowState.OriginalRows;
            PrintView(view, "**紀錄含有原始值(OriginalRows)");
        }

        DataTable table;
        DataColumn column;
        DataRow row;

        private void button21_Click(object sender, EventArgs e)
        {
            //RowVersion範例
            //DataTable
            MakeDataTable();
            DemonstrateRowVersion();
        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        void show_data_table(DataTable dt)
        {
            richTextBox1.Text += "顯示 DataTable 的內容\n";

            int i;
            int j;
            int C = dt.Columns.Count;
            int R = dt.Rows.Count;

            richTextBox1.Text += "共有資料欄位 " + C.ToString() + " 欄\n";
            richTextBox1.Text += "共有資料 " + R.ToString() + " 筆\n";
            richTextBox1.Text += "TableName = " + dt.TableName + "\n\n";
            richTextBox1.Text += "欄位名稱 : ";
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "內容\n";
            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }
    }
}
