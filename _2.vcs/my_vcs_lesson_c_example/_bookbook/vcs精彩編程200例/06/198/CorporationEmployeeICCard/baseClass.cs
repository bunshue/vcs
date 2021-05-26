using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Data.OleDb;
using System.IO;
using System.Drawing;

namespace CorporationEmployeeICCard
{

    #region 使用动态链接库，声明方法
    [StructLayout(LayoutKind.Sequential)]
    public unsafe class IC
    {
        //对设备进行初始化
        [DllImport("Mwic_32.dll", EntryPoint = "auto_init", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern int auto_init(int port, int baud);
        //设备密码格式
        [DllImport("Mwic_32.dll", EntryPoint = "setsc_md", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern int setsc_md(int icdev, int mode);
        //获取设备当前状态
        [DllImport("Mwic_32.dll", EntryPoint = "get_status", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 get_status(int icdev, Int16* state);
        //关闭设备通讯接口
        [DllImport("Mwic_32.dll", EntryPoint = "ic_exit", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern int ic_exit(int icdev);
        //使设备发出蜂鸣声
        [DllImport("Mwic_32.dll", EntryPoint = "dv_beep", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern int dv_beep(int icdev, int time);
        //向IC卡中写数据
        [DllImport("Mwic_32.dll", EntryPoint = "swr_4442", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern int swr_4442(int icdev, int offset, int len, char* w_string);
        //读取IC卡中数据
        [DllImport("Mwic_32.dll", EntryPoint = "srd_4442", SetLastError = true, CharSet = CharSet.Ansi, ExactSpelling = true, CallingConvention = CallingConvention.StdCall)]
        public static extern int srd_4442(int icdev, int offset, int len, char* r_string);
        //核对卡密码  
        [DllImport("Mwic_32.dll", EntryPoint = "csc_4442", SetLastError = true, CharSet = CharSet.Auto, ExactSpelling = true, CallingConvention = CallingConvention.Winapi)]
        public static extern Int16 Csc_4442(int icdev, int len, [MarshalAs(UnmanagedType.LPArray)] byte[] p_string);
    }
    #endregion

    class baseClass
    {
        public static int WriteIC(string id)//写入IC卡的方法
        {
            int flag = -1;
            //初始化
            int icdev = IC.auto_init(0, 9600);
            if (icdev < 0)
                MessageBox.Show("端口初始化失败,请检查接口线是否连接正确。", "错误提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            int md = IC.setsc_md(icdev, 1); //设备密码格式
            unsafe
            {
                Int16 status = 0;
                Int16 result = 0;
                result = IC.get_status(icdev, &status);
                if (result != 0)
                {
                    MessageBox.Show("设备当前状态错误！");
                    int d1 = IC.ic_exit(icdev);   //关闭设备
                }
                if (status != 1)
                {
                    MessageBox.Show("请插入ＩＣ卡");
                    int d2 = IC.ic_exit(icdev);   //关闭设备
                }
            }
            unsafe
            {
                //卡的密码默认为6个F（密码为：ffffff），1个F的16进制是15,2个F的16进制是255。
                byte[] pwd = new byte[3] { 0xff, 0xff, 0xff };
                Int16 checkIC_pwd = IC.Csc_4442(icdev, 3, pwd);
                if (checkIC_pwd < 0)
                {
                    MessageBox.Show("ＩＣ卡密码错误！");
                }
                char str = 'a';
                int write = -1;
                for (int j = 0; j < id.Length; j++)
                {
                    str = Convert.ToChar(id.Substring(j, 1));
                    write = IC.swr_4442(icdev, 33 + j, id.Length, &str);
                }
                if (write == 0)
                {
                    flag = write;
                    int beep = IC.dv_beep(icdev, 20);  //发出蜂鸣声
                }
                else
                    MessageBox.Show("数据写入ＩＣ卡失败！");
            }
            int d = IC.ic_exit(icdev);  //关闭设备
            return flag;
        }

        public static int ff = -1;
        public static int ReadIC(TextBox tb)//读取IC卡
        {
            int flag = -1;
            //初始化
            int icdev = IC.auto_init(0, 9600);
            if (icdev < 0)
                MessageBox.Show("端口初始化失败,请检查接口线是否连接正确。", "错误提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            int md = IC.setsc_md(icdev, 1); //设备密码格式
            unsafe
            {
                Int16 status = 0;
                Int16 result = 0;
                result = IC.get_status(icdev, &status);
                if (result != 0)
                {
                    MessageBox.Show("设备当前状态错误！");
                    int d1 = IC.ic_exit(icdev);   //关闭设备
                }

                if (status != 1)
                {
                    ff = -1;
                    int d2 = IC.ic_exit(icdev);   //关闭设备
                }
            }
            unsafe
            {
                char str;
                int read = -1;
                string ic = "";
                for (int j = 0; j < 6; j++)
                {
                    read = IC.srd_4442(icdev, 33 + j, 1, &str);
                    ic = ic + Convert.ToString(str);
                }
                tb.Text = ic;
                if (ff == -1)
                {
                    int i = IC.dv_beep(icdev, 10);  //发出蜂鸣声
                }
                if (read == 0)
                {
                    ff = 0;
                    flag = read;
                }
            }
            int d = IC.ic_exit(icdev);  //关闭设备
            return flag;
        }

        public static bool ExecuteSQL(string sql)//执行SQL语句
        {
            bool flag = false;
            string strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\db1.mdb";
            OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
            conn.Open();
            OleDbCommand cmd = new OleDbCommand(sql, conn);
            int i = cmd.ExecuteNonQuery();
            if (i > 0)
            {
                flag = true;
                conn.Close();
            }
            return flag;
        }

        public static bool CheckID(string id)//判断输入的IC卡号是否已经存在
        {
            bool flag = false;
            string strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\db1.mdb";
            OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
            conn.Open();
            OleDbCommand cmd = new OleDbCommand("select Count(*) from Employee where CardID='"+id+"'", conn);
            int i = Convert.ToInt32(cmd.ExecuteScalar());
            conn.Close();
            if (i > 0)
            {
                flag = true;
            }
            return flag;
        }

        public static void GetInfo(string id,TextBox name,TextBox sex,TextBox job,TextBox folk,TextBox dept,GroupBox gb)//根据IC卡号获取相应的信息
        {
            if (CheckID(id))
            {
                string strg = Application.StartupPath.ToString();
                strg = strg.Substring(0, strg.LastIndexOf("\\"));
                strg = strg.Substring(0, strg.LastIndexOf("\\"));
                strg += @"\db1.mdb";
                OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
                conn.Open();
                OleDbCommand cmd = new OleDbCommand("select * from Employee where CardID='" + id + "'", conn);
                OleDbDataReader sdr = cmd.ExecuteReader();
                sdr.Read();
                name.Text = sdr["E_Name"].ToString();
                sex.Text = sdr["E_Sex"].ToString();
                job.Text = sdr["E_Job"].ToString();
                folk.Text = sdr["E_Folk"].ToString();
                dept.Text = sdr["E_Dept"].ToString();
                gb.Text = "考勤进行中（考勤成功）";
                sdr.Close();
                conn.Close();
            }
            else
            {
                gb.Text = "考勤进行中（此IC卡未被注册！）";
            }
        }

        public static void ExportData(DataGridView srcDgv, string fileName)//导出数据,传入一个datagridview和一个文件路径
        {

            string type = fileName.Substring(fileName.IndexOf(".") + 1);//获得数据类型
            if (type.Equals("xls", StringComparison.CurrentCultureIgnoreCase))//Excel文档
            {
                Excel.Application excel = new Excel.Application();
                try
                {
                    excel.DisplayAlerts = false;
                    excel.Workbooks.Add(true);
                    excel.Visible = false;

                    for (int i = 0; i < srcDgv.Columns.Count; i++)//设置标题
                    {
                        excel.Cells[2, i + 1] = srcDgv.Columns[i].HeaderText;
                    }

                    for (int i = 0; i < srcDgv.Rows.Count; i++)//填充数据
                    {
                        for (int j = 0; j < srcDgv.Columns.Count; j++)
                        {
                            if (srcDgv[j, i].ValueType.ToString() == "System.Byte[]")
                            {
                                excel.Cells[i + 3, j + 1] = "System.Byte[]";
                            }
                            else
                            {
                                excel.Cells[i + 3, j + 1] = srcDgv[j, i].Value;
                            }
                        }
                    }

                    excel.Workbooks[1].SaveCopyAs(fileName);//保存
                }
                finally
                {
                    excel.Quit();
                }
                return;
            }
            //保存Word文件
            if (type.Equals("doc", StringComparison.CurrentCultureIgnoreCase))
            {

                object path = fileName;
                Object none = System.Reflection.Missing.Value;
                Word.Application wordApp = new Word.Application();
                Word.Document document = wordApp.Documents.Add(ref none, ref none, ref none, ref none);
                //建立表格
                Word.Table table = document.Tables.Add(document.Paragraphs.Last.Range, srcDgv.Rows.Count + 1, srcDgv.Columns.Count, ref none, ref none);
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
                            string a = srcDgv[j, i].ValueType.ToString();
                            if (a == "System.Byte[]")
                            {
                                PictureBox pp = new PictureBox();
                                byte[] pic = (byte[])(srcDgv[j, i].Value); //将数据库中的图片转换成二进制流
                                MemoryStream ms = new MemoryStream(pic);	//将字节数组存入到二进制流中
                                pp.Image = Image.FromStream(ms);           //二进制流Image控件中显示
                                pp.Image.Save(@"C:\22.bmp");               //将图片存入到指定的路径
                                object aaa = table.Cell(i + 2, j + 1).Range;
                                wordApp.Selection.ParagraphFormat.Alignment = Word.WdParagraphAlignment.wdAlignParagraphCenter;
                                wordApp.Selection.InlineShapes.AddPicture(@"C:\22.bmp", ref none, ref none, ref aaa);
                                pp.Dispose();
                            }
                            else
                            {
                                table.Cell(i + 2, j + 1).Range.Text = srcDgv[j, i].Value.ToString();
                            }
                        }
                    }
                    document.SaveAs(ref path, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none);
                    document.Close(ref none, ref none, ref none);
                    if (File.Exists(@"C:\22.bmp"))
                    {
                        File.Delete(@"C:\22.bmp");
                    }
                }
                finally
                {
                    wordApp.Quit(ref none, ref none, ref none);
                }
            }
        }

        public static void BinddataGridView(DataGridView dg, string datetime)
        {
            string strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\db1.mdb";
            OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
            conn.Open();
            string str = "select C_CardID as IC卡编号,C_Name as 员工姓名,C_Sex as 性别,C_Job as 职位,C_Folk as 民族,C_Dept as 员工部门,C_Time as 考勤日期 from CheckNote where C_Time='" + datetime + "'";
            OleDbDataAdapter da = new OleDbDataAdapter(str, conn);
            System.Data.DataTable dt = new System.Data.DataTable();
            da.Fill(dt);
            dg.DataSource = dt;
            dg.Columns[0].Width = 80;
            dg.Columns[1].Width = 80;
            dg.Columns[2].Width = 60;
            dg.Columns[3].Width = 60;
            dg.Columns[4].Width = 60;
            dg.Columns[5].Width = 80;
            dg.Columns[6].Width = 80;
            conn.Close();
        }

        public static bool isCheck(string id)//检查是否已经参加过考勤
        {
            bool flag = false;
            string strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\db1.mdb";
            OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
            conn.Open();
            OleDbCommand cmd = new OleDbCommand("select Count(*) from CheckNote where C_CardID='" + id + "'", conn);
            int i = Convert.ToInt32(cmd.ExecuteScalar());
            conn.Close();
            if (i > 0)
            {
                flag = true;
            }
            return flag;
        }

        public static int GetNum(string datetime)//获取所有参加考勤的人数
        {
            string strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\db1.mdb";
            OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
            conn.Open();
            OleDbCommand cmd = new OleDbCommand("select Count(*) from CheckNote where C_Time='" + datetime + "'", conn);
            int i = Convert.ToInt32(cmd.ExecuteScalar());
            conn.Close();
            return i;
        }
    }
}
