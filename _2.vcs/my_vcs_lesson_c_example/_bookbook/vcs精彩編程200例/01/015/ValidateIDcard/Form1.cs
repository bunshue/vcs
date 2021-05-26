using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.OleDb;
namespace ValidateIDcard
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string strg;//数据库路径
        OleDbConnection conn;//数据连接对象
        OleDbCommand cmd;//OleDbCommand对象
        OleDbDataReader sdr;//OleDbDataReader对象

        private bool CheckCard(string cardId)//创建一个CheckCard方法用于检查身份证号码是否合法
        {
            if (cardId.Length == 18)        //如果身份证号为18位
            {
               return  CheckCard18(cardId);//调用CheckCard18方法验证
            }
            else if (cardId.Length == 15)   //如果身份证号为15位
            {
                return CheckCard15(cardId);//调用CheckCard15方法验证
            }
            else
            {
                return false;
            }
        }

        private bool CheckCard18(string CardId)//CheckCard18方法用于检查18位身份证号码的合法性
        {
            long n = 0;
            bool flag = false;
            if (long.TryParse(CardId.Remove(17), out n) == false || n < Math.Pow(10, 16) || long.TryParse(CardId.Replace('x', '0').Replace('X', '0'), out n) == false)
                return false;//数字验证
            string[] Myaddress =new string[]{ "11","22","35","44","53","12",
                "23","36","45","54","13","31","37","46","61","14","32","41",
                "50","62","15","33","42","51","63","21","34","43","52","64",
                "65","71","81","82","91"};
            for (int kk = 0; kk < Myaddress.Length;kk++ )
            {
                if (Myaddress[kk].ToString() == CardId.Remove(2))
                {
                    flag = true;
                }
            }
            if (flag)
            {
                return flag;
            }
            string Mybirth = CardId.Substring(6, 8).Insert(6, "-").Insert(4, "-");
             DateTime Mytime = new DateTime();
            if (DateTime.TryParse(Mybirth, out Mytime) == false)
                return false;//生日验证
            string[] MyVarifyCode = ("1,0,x,9,8,7,6,5,4,3,2").Split(',');
            string[] wi = ("7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2").Split(',');
            char[] ai = CardId.Remove(17).ToCharArray();
            int sum = 0;
            for (int i = 0; i < 17; i++)
                sum += int.Parse(wi[i]) * int.Parse(ai[i].ToString());
            int y = -1;
            Math.DivRem(sum, 11, out y);
            if (MyVarifyCode[y] != CardId.Substring(17, 1).ToLower())
            {
                return false;//校验码验证
            }
            return true;//符合GB11643-1999标准
        }

        private bool CheckCard15(string CardId)
        {
            long n = 0;
            bool flag = false;
            if (long.TryParse(CardId, out n) == false || n < Math.Pow(10, 14))
                return false;//数字验证
            string[] Myaddress = new string[]{ "11","22","35","44","53","12",
                "23","36","45","54","13","31","37","46","61","14","32","41",
                "50","62","15","33","42","51","63","21","34","43","52","64",
                "65","71","81","82","91"};
            for (int kk = 0; kk < Myaddress.Length; kk++)
            {
                if (Myaddress[kk].ToString() == CardId.Remove(2))
                {
                    flag = true;
                }
            }
            if (flag)
            {
                return flag;
            }
            string Mybirth = CardId.Substring(6, 6).Insert(4, "-").Insert(2, "-");
            DateTime Mytime = new DateTime();
            if (DateTime.TryParse(Mybirth, out Mytime) == false)
            {
                return false;//生日验证
            }
            return true;//符合15位身份证标准
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtCardID.Text == "")//如果没有输入身份证号码
            {
                return;              //不执行操作
            }
            else
            {
                if (CheckCard(txtCardID.Text.Trim()))//如果通过CheckCard方法验证成功
                {
                    this.Height = 237;               //设置窗体高度
                    string card=txtCardID.Text.Trim();//获取输入的身份证号码
                    if (card.Length == 15)          //如果输入的是15位的身份证号码，需要将其转换成18位
                    {
                        int[] w = new int[] { 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1 };
                        char[] a = new char[] { '1', '0', 'x', '9', '8', '7', '6', '5', '4', '3', '2' };
                        string newID = "";
                        int s = 0;
                        newID =this.txtCardID.Text.Trim().Insert(6, "19");
                        for (int i = 0; i < 17; i++)
                        {
                             int k = Convert.ToInt32(newID[i]) * w[i];
                             s = s + k;
                        }
                        int h = 0;
                        Math.DivRem(s, 11, out h);
                        newID = newID + a[h];
                        card = newID;               //最后将转换成18位的身份证号码赋值给card
                    }
                    int addnum =Convert.ToInt32(card.Remove(6));//获取身份证号码中的地址码
                    //连接数据库
                    conn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + strg);
                    conn.Open();//打开数据库
                    //查找数据库中是否存在输入的身份证号码中的地址码
                    cmd = new OleDbCommand("select count(*) from address where AddNum="+addnum, conn);
                    int KK = Convert.ToInt32(cmd.ExecuteScalar());
                    if (KK > 0)//如果存在
                    {
                        //检索数据库
                        cmd = new OleDbCommand("select * from address where AddNum=" + addnum, conn);
                        //实例化OleDbDataReader对象
                        sdr = cmd.ExecuteReader();
                        sdr.Read();//读取该对象
                        string address = sdr["AddName"].ToString();//获取地址码对应的归属地
                        string birthday = card.Substring(6, 8);//从身份证号码中截取出公民的生日
                        string byear = birthday.Substring(0,4);//获取出生年份
                        string bmonth = birthday.Substring(4,2);//获取出生月份
                        if (bmonth.Substring(0, 1) == "0")//如果月份是以0开头
                        {
                            bmonth = bmonth.Substring(1,1);//去掉0
                        }
                        string bday = birthday.Substring(6,2);//获取出生“日”
                        if (bday.Substring(0, 1) == "0")//如果“日”以0开头
                        {
                            bday = bday.Substring(1, 1);//去掉0
                        }
                        string sex = "";//性别
                        if (txtCardID.Text.Trim().Length == 15)//如果输入的身份证号码是15位
                        {
                            int PP=Convert.ToInt32(txtCardID.Text.Trim().Substring(14,1))%2;//判断最后一位是奇数还是偶数
                            if (PP == 0)//如果是偶数
                            {
                                sex = "女";//说明身份证号码的持有者是女性
                            }
                            else
                            {
                                sex = "男";//如果是奇数则身份证号码的持有者是男性
                            }
                        }
                        if (txtCardID.Text.Trim().Length == 18)//如果输入的身份证号码是18位
                        {
                            int PP = Convert.ToInt32(txtCardID.Text.Trim().Substring(16, 1)) % 2;//判断倒数第二位是奇数还是偶数
                            if (PP == 0)//如果是偶数
                            {
                                sex = "女";//说明身份证号码的持有者是女性
                            }
                            else
                            {
                                sex = "男";//如果是奇数则身份证号码的持有者是男性
                            }
                        }
                        sdr.Close();//关闭OleDbDataReader连接
                        conn.Close();//关闭数据库连接
                        lblAddress.Text = address;//显示身份证持有者的归属地
                        lblbirthday.Text = byear + "年" + bmonth + "月" + bday + "日";//显示身份证持有者的生日
                        lblsex.Text = sex;//显示身份证持有者的性别
                        lblresult.Text = "合法的公民身份证号！";//显示验证结果
                    }
                    else
                    {
                        MessageBox.Show("公民身份证号输入有误！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                else
                {
                    MessageBox.Show("非法公民身份证号！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            txtCardID.Text = "";//清空输入框
            this.Height = 78;   //设置窗体高度位78
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Height = 78;//设置窗体高度
            //获取数据库路径
            strg = Application.StartupPath.ToString();
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg = strg.Substring(0, strg.LastIndexOf("\\"));
            strg += @"\db.mdb";
        }
    }
}
