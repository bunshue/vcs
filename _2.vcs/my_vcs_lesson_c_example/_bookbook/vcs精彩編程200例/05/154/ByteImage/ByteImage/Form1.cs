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

namespace ByteImage
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files1\_vcs200_db\db_09_Data.MDF";
        //string filename = @"C:\______test_files1\_vcs200_db\db_09_Log.LDF";   another

        public Form1()
        {
            InitializeComponent();
        }

        #region 定义公共的类对象及变量
        SqlConnection sqlcon;       //声明数据库连接对象
        SqlDataAdapter sqlda;       //声明数据桥接器对象
        DataSet myds;               //声明数据集对象
        //定义数据库连接字符串
        string strCon = "Data Source=XIAOKE;Database=db_09;uid=sa;pwd=;";
        #endregion

        private void Form1_Load(object sender, EventArgs e)
        {
            ShowInfo();             //显示用户信息
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //定义可选择的头像类型
            openFileDialog1.Filter = "*.jpg,*jpeg,*.bmp,*.ico,*.png,*.tif,*.wmf|*.jpg;*jpeg;*.bmp;*.ico;*.png;*.tif;*.wmf";
            openFileDialog1.Title = "选择头像";
            //判断是否选择了头像
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //显示选择的用户头像
                pictureBox1.Image = Image.FromFile(openFileDialog1.FileName);
            }
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            //记录选择的用户名
            string strName = dataGridView1.Rows[e.RowIndex].Cells[0].Value.ToString();
            if (strName != "")
            {
                sqlcon = new SqlConnection(strCon);     //实例化数据库连接对象
                //实例化数据桥接器对象
                sqlda = new SqlDataAdapter("select * from tb_Image where name='" + strName + "'", sqlcon);
                myds = new DataSet();                   //实例化数据集对象
                sqlda.Fill(myds);                       //填充数据集
                //显示用户名称
                textBox1.Text = myds.Tables[0].Rows[0][1].ToString();
                //使用数据库中存储的二进制头像实例化内存数据流
                MemoryStream MStream = new MemoryStream((byte[])myds.Tables[0].Rows[0][2]);
                pictureBox1.Image = Image.FromStream(MStream);  //显示用户头像
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                if (openFileDialog1.FileName != "" && textBox1.Text != "")
                {
                    //添加用户信息
                    if (AddInfo(textBox1.Text, openFileDialog1.FileName))
                    {
                        MessageBox.Show("用户信息添加成功");
                    }
                    else
                    {
                        MessageBox.Show("已经存在该用户");
                    }
                }
                ShowInfo();
            }
        }

        #region 添加用户信息
        /// <summary>
        /// 添加用户信息
        /// </summary>
        /// <param name="strName">用户名称</param>
        /// <param name="strImage">选择的头像名称</param>
        /// <returns>执行成功，返回true</returns>
        private bool AddInfo(string strName, string strImage)
        {
            sqlcon = new SqlConnection(strCon);
            //实例化数据桥接器对象
            sqlda = new SqlDataAdapter("select * from tb_Image where name='" + strName + "'", sqlcon);
            myds = new DataSet();                   //实例化数据集对象
            sqlda.Fill(myds);                       //填充数据集
            if (myds.Tables[0].Rows.Count <= 0)
            {
                FileStream FStream = new FileStream(strImage, FileMode.Open, FileAccess.Read);
                BinaryReader BReader = new BinaryReader(FStream);
                byte[] byteImage = BReader.ReadBytes((int)FStream.Length);
                SqlCommand sqlcmd = new SqlCommand("insert into tb_Image(name,photo) values(@name,@photo)", sqlcon);
                sqlcmd.Parameters.Add("@name", SqlDbType.VarChar, 50).Value = strName;
                sqlcmd.Parameters.Add("@photo", SqlDbType.Image).Value = byteImage;
                sqlcon.Open();
                sqlcmd.ExecuteNonQuery();
                sqlcon.Close();
                return true;
            }
            else
            {
                return false;
            }
        }
        #endregion

        #region 在DataGridView中显示用户名称
        /// <summary>
        /// 在DataGridView中显示用户名称
        /// </summary>
        private void ShowInfo()
        {
            sqlcon = new SqlConnection(strCon);
            sqlda = new SqlDataAdapter("select name as 用户名称 from tb_Image", sqlcon);
            myds = new DataSet();
            sqlda.Fill(myds);
            dataGridView1.DataSource = myds.Tables[0];
        }
        #endregion

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
