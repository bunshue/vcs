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
    /// Frm_Login��ժҪ˵����
	/// </summary>
	public class Frm_Login : System.Windows.Forms.Form
    {
        private System.Windows.Forms.Label lbluPwd;
        private System.Windows.Forms.Label lbluName;
		private System.Windows.Forms.Button btnConcel;
		private System.Windows.Forms.Button btnOK;
		private System.Windows.Forms.TextBox txtUser;
		private System.Windows.Forms.TextBox txtPasword;
        private System.ComponentModel.IContainer components = null;

		public Frm_Login()
		{
			//
			// Windows ���������֧���������
			//
			InitializeComponent();

			//
			// TODO: �� InitializeComponent ���ú�����κι��캯������
			//
		}

		/// <summary>
		/// ������������ʹ�õ���Դ��
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows ������������ɵĴ���
		/// <summary>
		/// �����֧������ķ��� - ��Ҫʹ�ô���༭���޸�
		/// �˷��������ݡ�
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
            this.SuspendLayout();
            // 
            // txtUser
            // 
            this.txtUser.Location = new System.Drawing.Point(128, 23);
            this.txtUser.Name = "txtUser";
            this.txtUser.Size = new System.Drawing.Size(208, 21);
            this.txtUser.TabIndex = 13;
            this.txtUser.Tag = "��¼����";
            // 
            // txtPasword
            // 
            this.txtPasword.Location = new System.Drawing.Point(128, 55);
            this.txtPasword.Name = "txtPasword";
            this.txtPasword.PasswordChar = '��';
            this.txtPasword.Size = new System.Drawing.Size(208, 21);
            this.txtPasword.TabIndex = 14;
            this.txtPasword.Tag = "��  �룺";
            // 
            // lbluPwd
            // 
            this.lbluPwd.AutoSize = true;
            this.lbluPwd.Location = new System.Drawing.Point(40, 55);
            this.lbluPwd.Name = "lbluPwd";
            this.lbluPwd.Size = new System.Drawing.Size(53, 12);
            this.lbluPwd.TabIndex = 12;
            this.lbluPwd.Text = "��  �룺";
            // 
            // lbluName
            // 
            this.lbluName.AutoSize = true;
            this.lbluName.Location = new System.Drawing.Point(40, 31);
            this.lbluName.Name = "lbluName";
            this.lbluName.Size = new System.Drawing.Size(53, 12);
            this.lbluName.TabIndex = 11;
            this.lbluName.Text = "��¼����";
            // 
            // btnConcel
            // 
            this.btnConcel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnConcel.Location = new System.Drawing.Point(188, 93);
            this.btnConcel.Name = "btnConcel";
            this.btnConcel.Size = new System.Drawing.Size(96, 23);
            this.btnConcel.TabIndex = 17;
            this.btnConcel.Text = "�˳�(&E)";
            this.btnConcel.Click += new System.EventHandler(this.btnConcel_Click);
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(52, 93);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(96, 23);
            this.btnOK.TabIndex = 16;
            this.btnOK.Text = "ȷ��(&O)";
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // frmLogin
            // 
            this.AcceptButton = this.btnOK;
            this.AutoScaleBaseSize = new System.Drawing.Size(6, 14);
            this.ClientSize = new System.Drawing.Size(376, 137);
            this.Controls.Add(this.lbluName);
            this.Controls.Add(this.btnConcel);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.txtUser);
            this.Controls.Add(this.txtPasword);
            this.Controls.Add(this.lbluPwd);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "frmLogin";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "��������ʱ���������ؼ�";
            this.ResumeLayout(false);
            this.PerformLayout();

		}
		#endregion

		/// <summary>
		/// Ӧ�ó��������ڵ㡣
		/// </summary>

        Frm_Main frm = new Frm_Main();//�����������
		private void btnOK_Click(object sender, System.EventArgs e)//ȷ��
		{
            if (txtUser.Text == "")//����û���Ϊ��
            {
                MessageBox.Show("�������û���");//������Ϣ�Ի���
                return;//�˳�����
            } else if (txtPasword.Text=="")//�������Ϊ��
            {
                MessageBox.Show("�������û�����");//������Ϣ�Ի���
                return;//�˳�����
            }
            else if (txtUser.Text == "Admin" &&//���������û�����������ȷ
                txtPasword.Text == "Admin")
            {
                frm.Show();//��ʾ����
                frm.button1.Visible = false;//����Button��ť
                frm.button4.Visible = false;//����Button��ť
                frm.Text = frm.Text + "    " + //��ʾ�������
                    "����Ա:" + txtUser.Text;
                this.Hide();//���ص�½����
            }
            else if (txtUser.Text == "Mr" &&//���������û�����������ȷ
                txtPasword.Text == "Mrsoft")
            {
                frm.Show();//��ʾ����
                frm.Text = frm.Text + "    " +//��ʾ�������
                    "ϵͳ����Ա:" + txtPasword.Text;
                this.Hide();//���ص�½����
            }
            else
            {
                MessageBox.Show("�û������������");//������Ϣ�Ի���
                txtUser.Text = "";//����û���
                txtPasword.Text = "";//�������
                txtUser.Focus();//�ؼ��õ�����
            }

		}

		private void btnConcel_Click(object sender, System.EventArgs e)//���ȡ����ť
		{
			DialogResult bb =MessageBox.Show(//������Ϣ�Ի���
                "�Ƿ�Ҫ�˳���¼��","�˳���¼",MessageBoxButtons.YesNo);
			if(Convert.ToString(bb)=="Yes")//������ȷ����ť
			{Application .Exit();}//�˳�Ӧ�ó���
		}
	}
}
