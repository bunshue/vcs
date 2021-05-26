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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lblTime.Text = DateTime.Now.ToString();//当进行考勤的时候在窗体中显示当前时间
            tsslTime.Text = DateTime.Now.ToString();//在任务栏中显示当前时间
        }

        private void 添加员工ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 frm2 = new Form2();
            frm2.ShowDialog();
        }

        private void 系统信息ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("MSINFO32.EXE");
        }

        private void 开始考勤ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            timer1.Start();//开始考勤
            panel1.Visible = true;//显示考勤界面
            timer2.Start();//开始显示当前时间
            开始考勤ToolStripMenuItem.Enabled = false;//禁用开始考勤菜单
        }

        int flag = -1;//设置的一个变量，用于控制一张IC卡只读取一次以及向数据库中只添加一次内容
        int flag2 = -1;//设置的一个变量，用于控制当某个IC卡已经参加考勤后，弹出一次错误提示
        private void timer1_Tick(object sender, EventArgs e)
        {
            int i = baseClass.ReadIC(txtICCard);//调用公共类中的ReadIC方法开始循环读取IC卡
            if (i == -1)//如果返回值是-1说明没有IC卡
            {
                //清空显示员工信息的文本框
                txtDept.Text = "";
                txtFolk.Text = "";
                txtICCard.Text = "";
                txtJob.Text = "";
                txtName.Text = "";
                txtSex.Text = "";
                groupBox1.Text = "考勤进行中";
                flag = -1;//初始化标记
                flag2 = -1;//初始化标记
            }
            else//如果有IC卡进行考勤
            {
                if (flag ==-1)//只有当flag为-1的时候执行
                {
                    string icID = txtICCard.Text.Trim();//获取读取的IC卡编号
                    if (baseClass.isCheck(icID))//isCheck方法判断是否参加过考勤
                    {
                        if (flag2 == -1)//只有当flag2为-1的时候执行
                        {
                            flag2 = 0;//改变标记的值从而实现只弹出一次警告对话框
                            MessageBox.Show("已经参加过考勤！", "警告", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            //清空文本框
                            txtDept.Text = "";
                            txtFolk.Text = "";
                            txtICCard.Text = "";
                            txtJob.Text = "";
                            txtName.Text = "";
                            txtSex.Text = "";
                            txtICCard.Text = "";
                            groupBox1.Text = "考勤进行中";
                        }
                    }
                    else//如果没有参加过考勤
                    {
                        //调用GetInfo方法获取IC卡对应的员工信息
                        baseClass.GetInfo(txtICCard.Text.Trim(), txtName, txtSex, txtJob, txtFolk, txtDept, groupBox1);
                        string name = txtName.Text.Trim();//员工姓名
                        string sex = txtSex.Text.Trim();//员工性别
                        string job = txtJob.Text.Trim();//员工职位
                        string folk = this.txtFolk.Text.Trim();//员工民族
                        string dept = txtDept.Text.Trim();//员工部门
                        //声明一个字符串，用于存储一条插入语句，实现将考勤信息插入到数据表中
                        string str = "insert into CheckNote(C_CardID,C_Name,C_Sex,C_Job,C_Folk,C_Dept,C_Time) values('" + icID + "','" + name + "','" + sex + "','" + job + "','" + folk + "','" + dept + "','" + DateTime.Now.ToShortDateString() + "')";
                        baseClass.ExecuteSQL(str);//ExecuteSQL方法执行SQL语句
                        tsslEinfo.Text = "已经有"+baseClass.GetNum(DateTime.Now.ToShortDateString())+"人参加考勤";
                    }
                }
                flag = 0;//改变flag的值实现一张IC卡只存储一次信息

            }
        }

        private void 退出系统ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            lblTime.Text = DateTime.Now.ToString();
        }

        private void 考勤结束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            开始考勤ToolStripMenuItem.Enabled = true;
            panel1.Visible = false;
            timer1.Stop();
            timer2.Stop();
            tsslEinfo.Text = "";
        }

        private void 考勤记录ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form3 frm3 = new Form3();
            frm3.ShowDialog();
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            tsslTime.Text = DateTime.Now.ToString();
        }

        private void 关于ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            AboutBox1 ab = new AboutBox1();
            ab.ShowDialog();
        }
    }
}
