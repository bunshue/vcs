namespace PingHost
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
          this.txtIP = new System.Windows.Forms.TextBox();
          this.label1 = new System.Windows.Forms.Label();
          this.btnPing = new System.Windows.Forms.Button();
          this.tabControl1 = new System.Windows.Forms.TabControl();
          this.tabPage1 = new System.Windows.Forms.TabPage();
          this.txtResult = new System.Windows.Forms.TextBox();
          this.tabPage2 = new System.Windows.Forms.TabPage();
          this.txtError = new System.Windows.Forms.TextBox();
          this.tabControl1.SuspendLayout();
          this.tabPage1.SuspendLayout();
          this.tabPage2.SuspendLayout();
          this.SuspendLayout();
          // 
          // txtIP
          // 
          this.txtIP.Location = new System.Drawing.Point(99, 10);
          this.txtIP.Name = "txtIP";
          this.txtIP.Size = new System.Drawing.Size(227, 22);
          this.txtIP.TabIndex = 0;
          // 
          // label1
          // 
          this.label1.AutoSize = true;
          this.label1.Location = new System.Drawing.Point(8, 13);
          this.label1.Name = "label1";
          this.label1.Size = new System.Drawing.Size(85, 12);
          this.label1.TabIndex = 5;
          this.label1.Text = "Host Name or IP:";
          // 
          // btnPing
          // 
          this.btnPing.Location = new System.Drawing.Point(124, 226);
          this.btnPing.Name = "btnPing";
          this.btnPing.Size = new System.Drawing.Size(86, 28);
          this.btnPing.TabIndex = 2;
          this.btnPing.Text = "Ping";
          this.btnPing.UseVisualStyleBackColor = true;
          this.btnPing.Click += new System.EventHandler(this.btnPing_Click);
          // 
          // tabControl1
          // 
          this.tabControl1.Controls.Add(this.tabPage1);
          this.tabControl1.Controls.Add(this.tabPage2);
          this.tabControl1.Location = new System.Drawing.Point(9, 47);
          this.tabControl1.Name = "tabControl1";
          this.tabControl1.SelectedIndex = 0;
          this.tabControl1.Size = new System.Drawing.Size(317, 164);
          this.tabControl1.TabIndex = 2;
          // 
          // tabPage1
          // 
          this.tabPage1.Controls.Add(this.txtResult);
          this.tabPage1.Location = new System.Drawing.Point(4, 21);
          this.tabPage1.Name = "tabPage1";
          this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
          this.tabPage1.Size = new System.Drawing.Size(309, 139);
          this.tabPage1.TabIndex = 0;
          this.tabPage1.Text = "Reply";
          this.tabPage1.UseVisualStyleBackColor = true;
          // 
          // txtResult
          // 
          this.txtResult.Dock = System.Windows.Forms.DockStyle.Fill;
          this.txtResult.Location = new System.Drawing.Point(3, 3);
          this.txtResult.Multiline = true;
          this.txtResult.Name = "txtResult";
          this.txtResult.ScrollBars = System.Windows.Forms.ScrollBars.Both;
          this.txtResult.Size = new System.Drawing.Size(303, 133);
          this.txtResult.TabIndex = 3;
          // 
          // tabPage2
          // 
          this.tabPage2.Controls.Add(this.txtError);
          this.tabPage2.Location = new System.Drawing.Point(4, 21);
          this.tabPage2.Name = "tabPage2";
          this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
          this.tabPage2.Size = new System.Drawing.Size(309, 139);
          this.tabPage2.TabIndex = 1;
          this.tabPage2.Text = "Error";
          this.tabPage2.UseVisualStyleBackColor = true;
          // 
          // txtError
          // 
          this.txtError.Dock = System.Windows.Forms.DockStyle.Fill;
          this.txtError.Location = new System.Drawing.Point(3, 3);
          this.txtError.Multiline = true;
          this.txtError.Name = "txtError";
          this.txtError.ScrollBars = System.Windows.Forms.ScrollBars.Both;
          this.txtError.Size = new System.Drawing.Size(303, 133);
          this.txtError.TabIndex = 4;
          // 
          // Form1
          // 
          this.AcceptButton = this.btnPing;
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(337, 268);
          this.Controls.Add(this.tabControl1);
          this.Controls.Add(this.btnPing);
          this.Controls.Add(this.txtIP);
          this.Controls.Add(this.label1);
          this.MaximizeBox = false;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "Ping";
          this.tabControl1.ResumeLayout(false);
          this.tabPage1.ResumeLayout(false);
          this.tabPage1.PerformLayout();
          this.tabPage2.ResumeLayout(false);
          this.tabPage2.PerformLayout();
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtIP;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnPing;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TextBox txtResult;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.TextBox txtError;
    }
}

