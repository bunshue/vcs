namespace RemoteDesktop
{
    partial class frmHost
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
          this.label1 = new System.Windows.Forms.Label();
          this.txtIP = new System.Windows.Forms.TextBox();
          this.btnOK = new System.Windows.Forms.Button();
          this.btnCancel = new System.Windows.Forms.Button();
          this.label2 = new System.Windows.Forms.Label();
          this.SuspendLayout();
          // 
          // label1
          // 
          this.label1.AutoSize = true;
          this.label1.Location = new System.Drawing.Point(13, 48);
          this.label1.Name = "label1";
          this.label1.Size = new System.Drawing.Size(57, 12);
          this.label1.TabIndex = 0;
          this.label1.Text = "被控端 IP:";
          // 
          // txtIP
          // 
          this.txtIP.Location = new System.Drawing.Point(76, 45);
          this.txtIP.Name = "txtIP";
          this.txtIP.Size = new System.Drawing.Size(203, 22);
          this.txtIP.TabIndex = 0;
          // 
          // btnOK
          // 
          this.btnOK.DialogResult = System.Windows.Forms.DialogResult.OK;
          this.btnOK.Location = new System.Drawing.Point(48, 88);
          this.btnOK.Name = "btnOK";
          this.btnOK.Size = new System.Drawing.Size(86, 28);
          this.btnOK.TabIndex = 1;
          this.btnOK.Text = "OK";
          this.btnOK.UseVisualStyleBackColor = true;
          this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
          // 
          // btnCancel
          // 
          this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
          this.btnCancel.Location = new System.Drawing.Point(158, 88);
          this.btnCancel.Name = "btnCancel";
          this.btnCancel.Size = new System.Drawing.Size(86, 28);
          this.btnCancel.TabIndex = 2;
          this.btnCancel.Text = "Cancel";
          this.btnCancel.UseVisualStyleBackColor = true;
          // 
          // label2
          // 
          this.label2.AutoSize = true;
          this.label2.Location = new System.Drawing.Point(12, 19);
          this.label2.Name = "label2";
          this.label2.Size = new System.Drawing.Size(208, 12);
          this.label2.TabIndex = 3;
          this.label2.Text = "請輸入被控端之IP位址或DNS主機名稱:";
          // 
          // frmHost
          // 
          this.AcceptButton = this.btnOK;
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(294, 135);
          this.Controls.Add(this.label2);
          this.Controls.Add(this.btnCancel);
          this.Controls.Add(this.btnOK);
          this.Controls.Add(this.txtIP);
          this.Controls.Add(this.label1);
          this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
          this.MaximizeBox = false;
          this.Name = "frmHost";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
          this.Text = "Remote Host Profile";
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtIP;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.Label label2;
    }
}