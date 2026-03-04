namespace vcs_TextBox2
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.tb_auto_complete2 = new System.Windows.Forms.TextBox();
            this.tb_auto_complete1 = new System.Windows.Forms.TextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox0.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.tb_auto_complete2);
            this.groupBox0.Controls.Add(this.tb_auto_complete1);
            this.groupBox0.Location = new System.Drawing.Point(12, 26);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(286, 136);
            this.groupBox0.TabIndex = 0;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "自動完成";
            // 
            // tb_auto_complete2
            // 
            this.tb_auto_complete2.Location = new System.Drawing.Point(19, 88);
            this.tb_auto_complete2.Name = "tb_auto_complete2";
            this.tb_auto_complete2.Size = new System.Drawing.Size(244, 22);
            this.tb_auto_complete2.TabIndex = 12;
            // 
            // tb_auto_complete1
            // 
            this.tb_auto_complete1.Location = new System.Drawing.Point(19, 34);
            this.tb_auto_complete1.Name = "tb_auto_complete1";
            this.tb_auto_complete1.Size = new System.Drawing.Size(244, 22);
            this.tb_auto_complete1.TabIndex = 11;
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(850, 42);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 39;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(823, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 38;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(935, 591);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.TextBox tb_auto_complete2;
        private System.Windows.Forms.TextBox tb_auto_complete1;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

