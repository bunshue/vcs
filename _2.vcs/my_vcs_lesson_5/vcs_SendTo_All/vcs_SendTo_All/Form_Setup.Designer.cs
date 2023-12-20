namespace vcs_SendTo_All
{
    partial class Form_Setup
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
            this.tb_filesize_mb = new System.Windows.Forms.TextBox();
            this.cb_search_big_files = new System.Windows.Forms.CheckBox();
            this.lb_main_mesg2 = new System.Windows.Forms.Label();
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.bt_save = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.lb_filesize = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // tb_filesize_mb
            // 
            this.tb_filesize_mb.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_filesize_mb.Location = new System.Drawing.Point(194, 58);
            this.tb_filesize_mb.Name = "tb_filesize_mb";
            this.tb_filesize_mb.Size = new System.Drawing.Size(100, 30);
            this.tb_filesize_mb.TabIndex = 27;
            this.tb_filesize_mb.Text = "5";
            this.tb_filesize_mb.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cb_search_big_files
            // 
            this.cb_search_big_files.AutoSize = true;
            this.cb_search_big_files.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_search_big_files.Location = new System.Drawing.Point(194, 24);
            this.cb_search_big_files.Name = "cb_search_big_files";
            this.cb_search_big_files.Size = new System.Drawing.Size(149, 28);
            this.cb_search_big_files.TabIndex = 26;
            this.cb_search_big_files.Text = "只搜尋大檔";
            this.cb_search_big_files.UseVisualStyleBackColor = true;
            // 
            // lb_main_mesg2
            // 
            this.lb_main_mesg2.AutoSize = true;
            this.lb_main_mesg2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg2.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2.Location = new System.Drawing.Point(12, 58);
            this.lb_main_mesg2.Name = "lb_main_mesg2";
            this.lb_main_mesg2.Size = new System.Drawing.Size(135, 24);
            this.lb_main_mesg2.TabIndex = 25;
            this.lb_main_mesg2.Text = "main_mesg2";
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(12, 24);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(135, 24);
            this.lb_main_mesg1.TabIndex = 24;
            this.lb_main_mesg1.Text = "main_mesg1";
            // 
            // bt_save
            // 
            this.bt_save.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.Location = new System.Drawing.Point(194, 127);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(94, 32);
            this.bt_save.TabIndex = 23;
            this.bt_save.Text = "儲存";
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Right;
            this.richTextBox1.Location = new System.Drawing.Point(349, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(191, 453);
            this.richTextBox1.TabIndex = 28;
            this.richTextBox1.Text = "";
            // 
            // lb_filesize
            // 
            this.lb_filesize.AutoSize = true;
            this.lb_filesize.Font = new System.Drawing.Font("標楷體", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_filesize.Location = new System.Drawing.Point(23, 127);
            this.lb_filesize.Name = "lb_filesize";
            this.lb_filesize.Size = new System.Drawing.Size(40, 27);
            this.lb_filesize.TabIndex = 29;
            this.lb_filesize.Text = "MB";
            // 
            // Form_Setup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(540, 453);
            this.Controls.Add(this.lb_filesize);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.tb_filesize_mb);
            this.Controls.Add(this.cb_search_big_files);
            this.Controls.Add(this.lb_main_mesg2);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.bt_save);
            this.Name = "Form_Setup";
            this.Text = "Form_Setup";
            this.Load += new System.EventHandler(this.Form_Setup_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tb_filesize_mb;
        private System.Windows.Forms.CheckBox cb_search_big_files;
        private System.Windows.Forms.Label lb_main_mesg2;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label lb_filesize;
    }
}