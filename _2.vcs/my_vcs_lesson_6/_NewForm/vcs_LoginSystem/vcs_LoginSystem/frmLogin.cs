using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.Data.SqlClient;
namespace vcs_LoginSystem
{
    /// <summary>
    /// Form1 ™∫∫K≠nª°©˙°C
    /// </summary>
    public class frmLogin : System.Windows.Forms.Form
    {
        private System.Windows.Forms.Label lbluPwd;
        private System.Windows.Forms.Label lbluName;
        private System.Windows.Forms.Button btnConcel;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.TextBox txtUser;
        private System.Windows.Forms.TextBox txtPasword;
        private System.ComponentModel.IContainer components;

        public frmLogin()
        {
            //
            // Windows µ°≈È≥]≠pæπ§‰´˘©“•≤ª›™∫
            //
            InitializeComponent();

            //
            // TODO: ¶b InitializeComponent Ω’•Œ´·≤K•[•Ù¶Û∫c≥y®Áº∆•NΩX
            //
        }

        /// <summary>
        /// ≤M≤z©“¶≥•ø¶b®œ•Œ™∫∏Í∑Ω°C
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

        #region Windows µ°≈È≥]≠pæπ•Õ¶®™∫•NΩX
        /// <summary>
        /// ≥]≠pæπ§‰´˘©“ª›™∫§Ë™k - §£≠n®œ•Œ•NΩXΩsøËæπ≠◊ßÔ
        /// ¶π§Ë™k™∫§∫Æe°C
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmLogin));
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
            this.txtUser.Location = new System.Drawing.Point(107, 25);
            this.txtUser.Name = "txtUser";
            this.txtUser.Size = new System.Drawing.Size(173, 22);
            this.txtUser.TabIndex = 13;
            this.txtUser.Tag = "µnø˝¶W°G";
            // 
            // txtPasword
            // 
            this.txtPasword.Location = new System.Drawing.Point(107, 59);
            this.txtPasword.Name = "txtPasword";
            this.txtPasword.PasswordChar = '°¥';
            this.txtPasword.Size = new System.Drawing.Size(173, 22);
            this.txtPasword.TabIndex = 14;
            this.txtPasword.Tag = "±K  ΩX°G";
            // 
            // lbluPwd
            // 
            this.lbluPwd.AutoSize = true;
            this.lbluPwd.Location = new System.Drawing.Point(33, 59);
            this.lbluPwd.Name = "lbluPwd";
            this.lbluPwd.Size = new System.Drawing.Size(29, 12);
            this.lbluPwd.TabIndex = 12;
            this.lbluPwd.Text = "±KΩX";
            // 
            // lbluName
            // 
            this.lbluName.AutoSize = true;
            this.lbluName.Location = new System.Drawing.Point(33, 33);
            this.lbluName.Name = "lbluName";
            this.lbluName.Size = new System.Drawing.Size(29, 12);
            this.lbluName.TabIndex = 11;
            this.lbluName.Text = "±b∏π";
            // 
            // btnConcel
            // 
            this.btnConcel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.btnConcel.Location = new System.Drawing.Point(181, 101);
            this.btnConcel.Name = "btnConcel";
            this.btnConcel.Size = new System.Drawing.Size(80, 24);
            this.btnConcel.TabIndex = 17;
            this.btnConcel.Text = "¬˜∂} (&E)";
            this.btnConcel.Click += new System.EventHandler(this.btnConcel_Click);
            // 
            // btnOK
            // 
            this.btnOK.Location = new System.Drawing.Point(67, 101);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(80, 24);
            this.btnOK.TabIndex = 16;
            this.btnOK.Text = "µn§J (&O)";
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // frmLogin
            // 
            this.AcceptButton = this.btnOK;
            this.AutoScaleBaseSize = new System.Drawing.Size(5, 15);
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
            this.Text = "ø≈›≈÷ÓëMèe„e°º’÷øoì•Èº’t«Ô";
            this.Load += new System.EventHandler(this.frmLoginwe_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }
        #endregion

        /// <summary>
        /// ¿≥•Œµ{ß«™∫•D§J§f¬I°C
        /// </summary>

        frmMain frm = new frmMain();
        private void btnOK_Click(object sender, System.EventArgs e)//ΩT©w
        {
            if (txtUser.Text == "")
            {
                MessageBox.Show("Ω–øÈ§J±b∏π");
                return;
            }
            else if (txtPasword.Text == "")
            {
                MessageBox.Show("Ω–øÈ§J±KΩX");
                return;
            }
            else if (txtUser.Text == "Admin" && txtPasword.Text == "Admin")
            {

                frm.Show();
                frm.button1.Visible = false;
                frm.button4.Visible = false;
                frm.Text = frm.Text + "    " + "æﬁß@≠˚:" + txtUser.Text;
                this.Hide();

            }
            else if (txtUser.Text == "Mr" && txtPasword.Text == "Mrsoft")
            {
                frm.Show();
                frm.Text = frm.Text + "    " + "®t≤Œ∫ﬁ≤z≠˚:" + txtPasword.Text;
                this.Hide();

            }
            else
            {
                MessageBox.Show("±b∏π©Œ±KΩXø˘ª~");
                txtUser.Text = "";
                txtPasword.Text = "";
                txtUser.Focus();
            }

        }

        private void btnConcel_Click(object sender, System.EventArgs e)//®˙Æ¯
        {
            DialogResult bb = MessageBox.Show("¨Oß_≠n∞h•Xµnø˝°H", "∞h•Xµnø˝", MessageBoxButtons.YesNo);
            if (Convert.ToString(bb) == "Yes")
            { Application.Exit(); }
        }

        private void frmLoginwe_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }


    }

}
