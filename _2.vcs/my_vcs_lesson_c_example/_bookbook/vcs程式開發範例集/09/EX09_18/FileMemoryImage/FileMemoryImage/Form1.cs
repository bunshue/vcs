using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.IO;
using System.Data.SqlClient;

namespace FileMemoryImage
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        string strPath = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] strSex = { "男", "女" };
            this.comboBox1.DataSource = strSex;
            string[] strCall = { "員工", "主幹人員", "部門經理", "經理" };
            this.comboBox2.DataSource = strCall;
            string[] strHunYin = { "以婚", "未婚", "離異" };
            this.comboBox3.DataSource = strHunYin;
            string[] strJianKang = { "很好", "良好", "一般" };
            this.comboBox4.DataSource = strJianKang;
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            this.openFileImage.ShowDialog();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (TextInfo())
            {
                if (insertInfo())
                {
                    MessageBox.Show("新增成功");
                    clearText();
                }
            }
            else
            {
                MessageBox.Show("請輸入正確訊息");
            }
        }

        private void clearText()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    c.Text = "";
                }
            }
            pictureBox1.Image = null;
        }

        private Boolean TextInfo()
        {
            foreach (Control c in groupBox1.Controls)
            {
                if (c is TextBox)
                {
                    if (c.Text == "")
                    {
                        return false;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
            return true;
        }

        private void openFileImage_FileOk(object sender, CancelEventArgs e)
        {
            strPath = this.openFileImage.FileName;
            this.pictureBox1.Image = Image.FromFile(strPath);
        }

        private bool insertInfo()
        {
            try
            {
                con.Open();
                StringBuilder strSql = new StringBuilder();
                strSql.Append("insert into 檔案訊息 values(@檔案編號,@工號,");
                strSql.Append("@姓名,@照片,@性別,@出生日期,@籍貫,@工齡,@電話,");
                strSql.Append("@部門名稱,@技術職稱,@婚姻狀態,@健康狀態)");
                SqlCommand cmd = new SqlCommand(strSql.ToString(), con);
                cmd.Parameters.Add("@檔案編號", SqlDbType.Text).Value = this.textBox1.Text.Trim().ToString();
                cmd.Parameters.Add("@工號", SqlDbType.Text).Value = this.textBox2.Text.Trim().ToString();
                cmd.Parameters.Add("@姓名", SqlDbType.Text).Value = this.textBox3.Text.Trim().ToString();
                cmd.Parameters.Add("@照片", SqlDbType.Text).Value = strPath;
                cmd.Parameters.Add("@性別", SqlDbType.Text).Value = this.comboBox1.Text.Trim().ToString();
                cmd.Parameters.Add("@出生日期", SqlDbType.Text).Value = this.textBox4.Text.Trim().ToString();
                cmd.Parameters.Add("@籍貫", SqlDbType.Text).Value = this.textBox5.Text.Trim().ToString();
                cmd.Parameters.Add("@工齡", SqlDbType.Int).Value = Convert.ToInt16(this.textBox6.Text.Trim().ToString());
                cmd.Parameters.Add("@電話", SqlDbType.Text).Value = this.textBox6.Text.Trim().ToString();
                cmd.Parameters.Add("@部門名稱", SqlDbType.Text).Value = this.textBox7.Text.Trim().ToString();
                cmd.Parameters.Add("@技術職稱", SqlDbType.Text).Value = this.comboBox2.Text.Trim().ToString();
                cmd.Parameters.Add("@婚姻狀態", SqlDbType.Text).Value = this.comboBox3.Text.Trim().ToString();
                cmd.Parameters.Add("@健康狀態", SqlDbType.Text).Value = this.comboBox4.Text.Trim().ToString();
                cmd.ExecuteNonQuery();
                con.Close();
                return true;
            }
            catch (Exception ey)
            {
                return false;
            }

        }

        #region//存取器
        private string 檔案編號;
        private string 工號;
        private string 姓名;
        private string 照片;
        private string 性別;
        private string 出生日期;
        private string 籍貫;
        private int 工齡;
        private string 電話;
        private string 部門名稱;
        private string 技術職稱;
        private string 婚姻狀態;
        private string 健康狀態;

        private string ID
        {
            get { return 檔案編號; }
            set { 檔案編號 = value; }
        }
        private string NumID
        {
            get { return 工號; }
            set { 工號 = value; }
        }
        private string name
        {
            get { return 姓名; }
            set { 姓名 = value; }
        }
        private string pic
        {
            get { return 照片; }
            set { 照片 = value; }
        }
        private string sex
        {
            get { return 性別; }
            set { 性別 = value; }
        }
        private string birthday
        {
            get { return 出生日期; }
            set { 出生日期 = value; }
        }
        private string city
        {
            get { return 籍貫; }
            set { 籍貫 = value; }
        }
        private int years
        {
            get { return 工齡; }
            set { 工齡 = value; }
        }
        private string phone
        {
            get { return 電話; }
            set { 電話 = value; }
        }
        private string part
        {
            get { return 部門名稱; }
            set { 部門名稱 = value; }
        }
        private string state
        {
            get { return 技術職稱; }
            set { 技術職稱 = value; }
        }
        private string marriage
        {
            get { return 婚姻狀態; }
            set { 婚姻狀態 = value; }
        }
        private string health
        {
            get { return 健康狀態; }
            set { 健康狀態 = value; }
        }

        #endregion

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
