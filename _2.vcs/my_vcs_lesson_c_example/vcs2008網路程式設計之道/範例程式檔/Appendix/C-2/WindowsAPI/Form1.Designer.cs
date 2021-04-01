namespace WindowsAPI
{
    partial class Form1
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
            this.txtCaption = new System.Windows.Forms.TextBox();
            this.Label2 = new System.Windows.Forms.Label();
            this.btnShow = new System.Windows.Forms.Button();
            this.txtMsg = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtCaption
            // 
            this.txtCaption.Location = new System.Drawing.Point(66, 40);
            this.txtCaption.Name = "txtCaption";
            this.txtCaption.Size = new System.Drawing.Size(156, 22);
            this.txtCaption.TabIndex = 1;
            this.txtCaption.Text = "Windows API Test";
            // 
            // Label2
            // 
            this.Label2.Location = new System.Drawing.Point(10, 44);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(60, 16);
            this.Label2.TabIndex = 31;
            this.Label2.Text = "Caption:";
            // 
            // btnShow
            // 
            this.btnShow.Location = new System.Drawing.Point(78, 76);
            this.btnShow.Name = "btnShow";
            this.btnShow.Size = new System.Drawing.Size(76, 24);
            this.btnShow.TabIndex = 2;
            this.btnShow.Text = "Show";
            this.btnShow.Click += new System.EventHandler(this.btnShow_Click);
            // 
            // txtMsg
            // 
            this.txtMsg.Location = new System.Drawing.Point(66, 12);
            this.txtMsg.Name = "txtMsg";
            this.txtMsg.Size = new System.Drawing.Size(156, 22);
            this.txtMsg.TabIndex = 0;
            this.txtMsg.Text = "Hello World";
            // 
            // Label1
            // 
            this.Label1.Location = new System.Drawing.Point(10, 16);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(60, 16);
            this.Label1.TabIndex = 30;
            this.Label1.Text = "Message:";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnShow;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(232, 113);
            this.Controls.Add(this.txtCaption);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.btnShow);
            this.Controls.Add(this.txtMsg);
            this.Controls.Add(this.Label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Windows API";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtCaption;
        private System.Windows.Forms.Label Label2;
        private System.Windows.Forms.Button btnShow;
        private System.Windows.Forms.TextBox txtMsg;
        private System.Windows.Forms.Label Label1;
    }
}

