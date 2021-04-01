namespace Host
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
          this.button1 = new System.Windows.Forms.Button();
          this.txtIP = new System.Windows.Forms.TextBox();
          this.Label2 = new System.Windows.Forms.Label();
          this.txtHost = new System.Windows.Forms.TextBox();
          this.Label1 = new System.Windows.Forms.Label();
          this.SuspendLayout();
          // 
          // button1
          // 
          this.button1.Location = new System.Drawing.Point(65, 80);
          this.button1.Name = "button1";
          this.button1.Size = new System.Drawing.Size(92, 28);
          this.button1.TabIndex = 25;
          this.button1.Text = "OK";
          this.button1.Click += new System.EventHandler(this.button1_Click);
          // 
          // txtIP
          // 
          this.txtIP.Location = new System.Drawing.Point(78, 12);
          this.txtIP.Name = "txtIP";
          this.txtIP.Size = new System.Drawing.Size(132, 22);
          this.txtIP.TabIndex = 26;
          // 
          // Label2
          // 
          this.Label2.Location = new System.Drawing.Point(10, 16);
          this.Label2.Name = "Label2";
          this.Label2.Size = new System.Drawing.Size(64, 20);
          this.Label2.TabIndex = 29;
          this.Label2.Text = "IP Address:";
          // 
          // txtHost
          // 
          this.txtHost.Location = new System.Drawing.Point(78, 40);
          this.txtHost.Name = "txtHost";
          this.txtHost.Size = new System.Drawing.Size(132, 22);
          this.txtHost.TabIndex = 27;
          // 
          // Label1
          // 
          this.Label1.Location = new System.Drawing.Point(10, 44);
          this.Label1.Name = "Label1";
          this.Label1.Size = new System.Drawing.Size(64, 20);
          this.Label1.TabIndex = 28;
          this.Label1.Text = "Host Name:";
          // 
          // Form1
          // 
          this.AcceptButton = this.button1;
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(222, 122);
          this.Controls.Add(this.txtIP);
          this.Controls.Add(this.Label2);
          this.Controls.Add(this.txtHost);
          this.Controls.Add(this.Label1);
          this.Controls.Add(this.button1);
          this.MaximizeBox = false;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "DNS";
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox txtIP;
        private System.Windows.Forms.Label Label2;
        private System.Windows.Forms.TextBox txtHost;
        private System.Windows.Forms.Label Label1;
    }
}

