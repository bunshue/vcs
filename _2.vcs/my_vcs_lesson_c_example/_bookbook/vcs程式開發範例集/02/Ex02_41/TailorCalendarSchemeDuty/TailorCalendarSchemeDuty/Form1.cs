using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Text.RegularExpressions;

namespace TailorCalendarSchemeDuty
{
    public partial class Form1 : Form
    {
        public int Falg;//0１表示添加//2表示修改
        public string strFalg;//表示要修改的日期

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            monthCalendar1.TitleBackColor = System.Drawing.Color.Blue;
            monthCalendar1.TrailingForeColor = System.Drawing.Color.Red;
            monthCalendar1.TitleForeColor = System.Drawing.Color.Yellow;

            getDateTime("four");// 修改數據
            getDateTime("one");//查找今天是否有任務在執行
            if (strName != null)
            {
                textBox2.Text = "今天有任務" + ":" + "任務說明：" + strName + "任務日期:" + strDate;
                textBox2.BackColor = Color.Beige;
                textBox2.ForeColor = Color.Red;
            }
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            monthCalendar1.ShowToday = !monthCalendar1.ShowToday;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            getDateTime("two");//查找所有末完成的任務內容
            if (listBox1.Items.Count == 0)
            {
                MessageBox.Show("現在還沒有設定任務", "信息提示");
            }
        }

        public string strDate;//存儲今天任務信息
        public string strName;//存儲今天任務時間
        //任務和時間查詢
        public int aasdf = 0;
        public void getDateTime(string strFalg)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_10", con);
            SqlDataReader dr = com.ExecuteReader();
            while (dr.Read())
            {
                switch (strFalg)//任務操作標記
                {
                    case "one"://查找末完成的任務的時間
                        // string a = dr.GetValue(3).ToString();
                        if (dr.GetValue(3).ToString() != "True")
                        {
                            DateTime dt = Convert.ToDateTime(dr[1].ToString());

                            if (dt.ToShortDateString().Equals(DateTime.Now.ToShortDateString()))
                            {
                                strDate = dt.ToShortDateString();//查找今天是否有任務時間
                                strName = dr[2].ToString();//任務內容
                                listBox1.Items.Add(strDate);
                            }
                            else
                            {
                                listBox1.Items.Add(dt.ToShortDateString());//末完成的任務的時間
                            }

                        }
                        break;
                    case "two"://查找末完成的任務
                        if (dr.GetValue(3).ToString() != "True")
                        {

                            listBox1.Items.Add(dr[2].ToString());
                        }

                        break;
                    case "three"://查找已完成的任務
                        if (dr.GetValue(3).ToString() == "True")
                        {
                            DateTime dt = Convert.ToDateTime(dr[1].ToString());
                            listBox1.Items.Add(dt.ToShortDateString());
                        }
                        break;
                    case "four"://修改
                        //任務t時間小於現在時間，並且是末完成的任務取消
                        string str1 = Convert.ToDateTime(dr[1].ToString()).ToString();
                        string str2 = DateTime.Now.ToShortDateString();
                        int intt = DateTime.Compare(Convert.ToDateTime(dr[1].ToString()), Convert.ToDateTime(DateTime.Now.ToShortDateString()));
                        if ((intt < 0) && (dr.GetValue(3).ToString() != "True"))
                        {
                            string strg = strDatDelteUpdate(Convert.ToDateTime(dr[1].ToString()), "", 1, 1);

                        }
                        break;
                }

            }
            dr.Close();
        }

        //查找判斷今天是否有任務，有顯示任務
        public string getStrName(string strName)
        {
            string strDataName = null;
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_10 where strdate='" + Convert.ToDateTime(strName) + "'", con);
            SqlDataReader dr = com.ExecuteReader();
            while (dr.Read())
            {

                strDataName = dr[2].ToString();
            }
            dr.Close();
            return strDataName;
        }

        //添加任務時間
        private void monthCalendar1_MouseUp(object sender, MouseEventArgs e)
        {
            if (monthCalendar1.SelectionStart >= DateTime.Now)
            {
                if (MessageBox.Show("是否要把今天設為任務日期", "提示", MessageBoxButtons.OKCancel) == DialogResult.OK)
                {

                    monthCalendar1.AddBoldedDate(monthCalendar1.SelectionStart);
                    monthCalendar1.UpdateBoldedDates();
                    SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
                    con.Open();
                    SqlCommand com = new SqlCommand("select * from tb_10 where strdate='" + monthCalendar1.SelectionStart.ToShortDateString() + "'", con);
                    int intstr = Convert.ToInt32(com.ExecuteScalar());
                    if (intstr == 0)
                    {
                        listBox1.Items.Add(monthCalendar1.SelectionStart.ToShortDateString());

                        MessageBox.Show("任務日期已添加到任務列表\n" + "請補充添加任務說明否則\n" + "此次操作不會保存到數據庫中", "請添加任務說明");
                        textBox1.Focus();
                        Falg = 1;

                    }
                    else
                    {
                        MessageBox.Show("此日期已有任務請選擇其它日期", "信息提示");
                    }
                    con.Close();
                }//'
            }//
        }

        //任務取消提示
        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
            {
                if (MessageBox.Show("請選擇取消的任務時間", "任務取消提示", MessageBoxButtons.OK) == DialogResult.OK) ;
                {
                    listBox1.Items.Clear();
                    getDateTime("one");
                    if (listBox1.Items.Count == 0)
                    { MessageBox.Show("當前沒有任務", "信息提示"); }
                }
            }
            else
            {
                if (ValidateDate2(listBox1.SelectedItem.ToString()))
                {
                    if (MessageBox.Show("是否真的取消任務", "任務取消提示", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {
                        if (strDatDelteUpdate(Convert.ToDateTime(listBox1.SelectedItem.ToString()), textBox1.Text, 0, 2) == "DeleteFalg")
                        {
                            MessageBox.Show("取消成功", "取消提示 ");

                        }
                        listBox1.Items.Remove(listBox1.SelectedItem.ToString());
                    }// end 
                }// end block if 
                else
                {
                    listBox1.Items.Clear();
                    getDateTime("one");
                }//
            }//
        }// end bl

        //讓列表顯示任務日期
        private void button4_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            getDateTime("one");//查找任務時間
            if (listBox1.Items.Count == 0)
            { MessageBox.Show("現在還沒有設定任務", "信息提示"); }
        }

        //修改任務內容
        private void button1_Click(object sender, EventArgs e)
        {

            if (listBox1.SelectedItem == null)
            {
                if (MessageBox.Show("請選擇要修改的任務時間", "任務修改提示", MessageBoxButtons.OK) == DialogResult.OK)
                {
                    listBox1.Items.Clear();
                    getDateTime("one");
                    if (listBox1.Items.Count == 0)
                    { MessageBox.Show("現在還沒有設定任務", "信息提示"); }
                }
            }
            else
            {
                if (ValidateDate2(listBox1.SelectedItem.ToString()))
                {
                    if (MessageBox.Show("是否真的要修改任務", "任務修改提示", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {
                        textBox1.Text = getStrName(listBox1.SelectedItem.ToString());
                        strFalg = listBox1.SelectedItem.ToString();
                        textBox1.Focus();
                        textBox1.BackColor = Color.Beige;
                        Falg = 2;
                        MessageBox.Show("修改完畢以後請單擊[確定]按鈕，保存到數據庫", "修改提示");
                    }// end block if 
                }
                else
                {
                    listBox1.Items.Clear();
                    getDateTime("one");
                }// end block if 

            }// end block else
        }// end

        //添加任務
        private void button5_Click(object sender, EventArgs e)
        {
            if (Falg == 1)//添加
            {
                if (textBox1.Text != "")//
                {
                    if (MessageBox.Show("任務日期是否為\n" + listBox1.Items[listBox1.Items.Count - 1].ToString(), "任務日期提示", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    {
                        if (strDatInsert(Convert.ToDateTime(listBox1.Items[listBox1.Items.Count - 1].ToString()), textBox1.Text, 0) == "YAdd")
                        {
                            MessageBox.Show("任務日期已有任務，請選擇別的日期", "添加提示");
                        }//
                        else
                        {
                            MessageBox.Show("任務日期，添加成功", "添加提示");
                            textBox1.Text = "";
                            Falg = 0;
                            return;
                        }//
                    }//判斷ListBox最後是項是否為添加日期，不是請重新選擇
                    else
                    {

                        if (MessageBox.Show("請選擇添加作任務日期否則\n" + "此次操作將不會保存到數據庫中", "重要提示", MessageBoxButtons.YesNo) == DialogResult.Yes)
                        {
                            if (strDatInsert(Convert.ToDateTime(listBox1.SelectedItem.ToString()), textBox1.Text, 0) == "YAdd")
                            {
                                MessageBox.Show("任務日期已有任務，請選擇別的日期", "添加提示");
                            }//
                            else
                            {
                                MessageBox.Show("任務日期，添加成功", "添加提示");
                                textBox1.Text = "";
                                Falg = 0;
                                return;
                            }//
                        }// end 
                        else
                        {
                            MessageBox.Show("你已取消了修改", "修改提示");
                            textBox1.Text = "";
                            Falg = 0;
                        }// end block 
                    }//
                }//end block if 
                else
                {
                    MessageBox.Show("請填寫任務說明否則\n" + "此次操作不會成功", "重要提示");
                    textBox1.Focus();
                    return;
                }// end 
            }//添加
            if (Falg == 2)//修改
            {   //修改內容確定
                if (MessageBox.Show("任務日期為：" + strFalg + "\n" + "修改任務說明為：\n" + textBox1.Text.ToString(), "修改提示", MessageBoxButtons.YesNo) == DialogResult.Yes)
                {
                    if (strDatDelteUpdate(Convert.ToDateTime(strFalg), textBox1.Text, 0, 0) == "Update")
                    {
                        MessageBox.Show("修改成功", "修改提示 ");
                        textBox1.Text = "";
                        Falg = 0;
                    }
                }//
                else
                {
                    MessageBox.Show("你已取消了修改", "修改提示");
                    textBox1.Text = "";
                    Falg = 0;
                }
            }
        }

        // 添加任務的方法
        public string strDatInsert(DateTime strDate, string strName, int intFalg)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand();
            com.CommandText = "insertDate";
            com.CommandType = CommandType.StoredProcedure;
            com.Connection = con;
            com.Parameters.Add("@strDate", SqlDbType.DateTime, 8);
            com.Parameters["@strDate"].Value = strDate;
            com.Parameters.Add("@strName", SqlDbType.VarChar, 100);
            com.Parameters["@strName"].Value = strName;
            com.Parameters.Add("@strFalg", SqlDbType.Bit, 1);
            com.Parameters["@strFalg"].Value = intFalg;
            SqlParameter sqlpar = com.Parameters.Add("@strResult", SqlDbType.VarChar, 20);

            sqlpar.Direction = ParameterDirection.Output;
            com.ExecuteNonQuery();
            return com.Parameters["@strResult"].Value.ToString();
        }

        //已完成的任務
        private void button6_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            getDateTime("three");
        }

        //修改冊除任務 
        public string strDatDelteUpdate(DateTime strDate, string strName, int intFalg, int Falg)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand();
            com.CommandText = "StrDateUpDelect";
            com.CommandType = CommandType.StoredProcedure;
            com.Connection = con;
            com.Parameters.Add("@strDate", SqlDbType.DateTime, 8);
            com.Parameters["@strDate"].Value = strDate;
            com.Parameters.Add("@strName", SqlDbType.VarChar, 100);
            com.Parameters["@strName"].Value = strName;

            com.Parameters.Add("@strFalg", SqlDbType.Bit, 1);
            com.Parameters["@strFalg"].Value = intFalg;

            com.Parameters.Add("@Falg", SqlDbType.Int);
            com.Parameters["@Falg"].Value = Falg;
            SqlParameter sqlpar = com.Parameters.Add("@strResult", SqlDbType.VarChar, 20);
            sqlpar.Direction = ParameterDirection.Output;
            com.ExecuteNonQuery();
            return com.Parameters["@strResult"].Value.ToString();
        }

        //驗證日期類型
        public bool ValidateDate2(string input)
        {
            return Regex.IsMatch(input, "\\b(?<year>\\d{2,4})-(?<month>\\d{1,2})-(?<day>\\d{1,2})\\b");
        }

        // 用任務時間查找了
        public void getSelect(string strName, string strFalg)
        {
            string strSelect = null;
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            switch (strFalg)
            {
                case "one":
                    strSelect = "select * from tb_10 where strdate='" + Convert.ToDateTime(strName) + "'";
                    break;
                case "two":
                    strSelect = "select * from tb_10 where strName='" + strName + "'";
                    break;
            }
            SqlCommand com = new SqlCommand(strSelect, con);
            SqlDataReader dr = com.ExecuteReader();
            while (dr.Read())
            {
                switch (strFalg)
                {
                    case "one":

                        textBox1.Text = dr[2].ToString();
                        break;
                    case "two":
                        textBox1.Text = dr[1].ToString();
                        break;
                }
            }//dr
            dr.Close();
            con.Close();
            DateTime.Now.ToShortDateString();
            DateTime.Now.ToShortTimeString();
            DateTime.Now.ToLongDateString();
            DateTime.Now.ToLongTimeString();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem != null)
            {
                if (ValidateDate2(listBox1.SelectedItem.ToString()))
                {
                    getSelect(listBox1.SelectedItem.ToString(), "one");
                }
                else
                {
                    getSelect(listBox1.SelectedItem.ToString(), "two");
                }
            }
        }
    }
}

