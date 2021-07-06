using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;

using System.Data.SqlClient;

namespace AddAndRemoveControl
{
    /// <summary>
    /// Frm_Login的摘要说明。
    /// </summary>
    public class Frm_Login : System.Windows.Forms.Form
    {
        private System.Windows.Forms.Label lbluPwd;
        private System.Windows.Forms.Label lbluName;
        private System.Windows.Forms.Button btnConcel;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.TextBox txtUser;
        private System.Windows.Forms.TextBox txtPasword;
        private Label label1;
        private System.ComponentModel.IContainer components = null;

        public Frm_Login()
        {
            //
            // Windows 窗体设计器支持所必需的
            //
            InitializeComponent();

            //
            // TODO: 在 InitializeComponent 调用后添加任何构造函数代码
            //
        }

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                if (components != null)
                {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码
        /// <summary>
        /// 设计器支持所需的方法 - 不要使用代码编辑器修改
        /// 此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Frm_Login));
            this.txtUser = new System.Windows.Forms.TextBox();
            this.txtPasword = new System.Windows.Forms.TextBox();
            this.lbluPwd = new System.Windows.Forms.Label();
            this.lbluName = new System.Windows.Forms.Label();
            this.btnConcel = new System.Windows.Forms.Button();
            this.btnOK = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtUser
            // 
            this.txtUser.Location = new System.Drawing.Point(107, 25);
            this.txtUser.Name = "txtUser";
            this.txtUser.Size = new System.Drawing.Size(173, 22);
            this.txtUser.TabIndex = 13;
            this.txtUser.Tag = "登录名：";
            // 
            // txtPasword
            // 
            this.txtPasword.Location = new System.Drawing.Point(107, 59);
            this.txtPasword.Name = "txtPasword";
            this.txtPasword.PasswordChar = '●';
            this.txtPasword.Size = new System.Drawing.Size(173, 22);
            this.txtPasword.TabIndex = 14;
            this.txtPasword.Tag = "密  码：";
            // 
            // lbluPwd
            // 
            this.lbluPwd.AutoSize = true;
            this.lbluPwd.Location = new System.Drawing.Point(33, 59);
            this.lbluPwd.Name = "lbluPwd";
            this.lbluPwd.Size = new System.Drawing.Size(47, 12);
            this.lbluPwd.TabIndex = 12;
            this.lbluPwd.Text = "密  码：";
            // 
            // lbluName
            // 
            this.lbluName.AutoSize = true;
            this.lbluName.Location = new System.Drawing.Point(33, 33);
            this.lbluName.Name = "lbluName";
            this.lbluName.Size = new System.Drawing.Size(53, 12);
            this.lbluName.TabIndex = 11;
            this.lbluName.Text = "登录名：";
            // 
            // btnConcel
            // 
            this.btnConcel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnConcel.Location = new System.Drawing.Point(157, 100);
            this.btnConcel.Name = "btnConcel";
            this.btnConcel.Size = new System.Drawing.Size(80, 24);
            this.btnConcel.TabIndex = 17;
            this.btnConcel.Text = "退出(&E)";
            this.btnConcel.Click += new System.EventHandler(this.btnConcel_Click);
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(43, 100);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(80, 24);
            this.btnOK.TabIndex = 16;
            this.btnOK.Text = "确定(&O)";
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(64, 168);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 24);
            this.label1.TabIndex = 18;
            this.label1.Text = "label1";
            // 
            // Frm_Login
            // 
            this.AcceptButton = this.btnOK;
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
            this.ClientSize = new System.Drawing.Size(473, 390);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lbluName);
            this.Controls.Add(this.btnConcel);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.txtUser);
            this.Controls.Add(this.txtPasword);
            this.Controls.Add(this.lbluPwd);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Frm_Login";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "程序运行时智能增减控件";
            this.Load += new System.EventHandler(this.Frm_Login_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }
        #endregion

        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>

        private void Frm_Login_Load(object sender, EventArgs e)
        {
            label1.Text = "操作員 : Admin / Admin\n系統管理員 : Mr / Mrsoft";
        }

        Frm_Main frm = new Frm_Main();//创建窗体对象
        private void btnOK_Click(object sender, System.EventArgs e)//确定
        {
            if (txtUser.Text == "")//如果用户名为空
            {
                MessageBox.Show("请输入用户名");//弹出消息对话框
                return;//退出方法
            }
            else if (txtPasword.Text == "")//如果密码为空
            {
                MessageBox.Show("请输入用户密码");//弹出消息对话框
                return;//退出方法
            }
            else if (txtUser.Text == "Admin" && txtPasword.Text == "Admin")//如果输入的用户名和密码正确
            {
                frm.Show();//显示窗体
                frm.button1.Visible = false;//隐藏Button按钮
                frm.button4.Visible = false;//隐藏Button按钮
                frm.Text = frm.Text + "    " + "操作员:" + txtUser.Text;//显示窗体标题
                this.Hide();//隐藏登陆窗体
            }
            else if (txtUser.Text == "Mr" && txtPasword.Text == "Mrsoft")//如果输入的用户名和密码正确
            {
                frm.Show();//显示窗体
                frm.Text = frm.Text + "    " + "系统管理员:" + txtPasword.Text;//显示窗体标题
                this.Hide();//隐藏登陆窗体
            }
            else
            {
                MessageBox.Show("用户名或密码错误");//弹出消息对话框
                txtUser.Text = "";//清空用户名
                txtPasword.Text = "";//清空密码
                txtUser.Focus();//控件得到焦点
            }
        }

        private void btnConcel_Click(object sender, System.EventArgs e)//点击取消按钮
        {
            DialogResult bb = MessageBox.Show("是否要退出登录？", "退出登录", MessageBoxButtons.YesNo);   //弹出消息对话框
            if (Convert.ToString(bb) == "Yes")//如果点击确定按钮
            {
                Application.Exit(); //退出应用程序
            }
        }
    }
}

