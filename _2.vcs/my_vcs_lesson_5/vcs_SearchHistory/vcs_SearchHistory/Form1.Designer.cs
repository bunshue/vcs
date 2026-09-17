namespace vcs_SearchHistory
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
            this.bt_clear_pattern = new System.Windows.Forms.Button();
            this.bt_remove_pattern = new System.Windows.Forms.Button();
            this.bt_add_pattern = new System.Windows.Forms.Button();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.tb_search = new System.Windows.Forms.TextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // bt_clear_pattern
            // 
            this.bt_clear_pattern.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_clear_pattern.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_pattern.Location = new System.Drawing.Point(234, 104);
            this.bt_clear_pattern.Name = "bt_clear_pattern";
            this.bt_clear_pattern.Size = new System.Drawing.Size(40, 40);
            this.bt_clear_pattern.TabIndex = 38;
            this.bt_clear_pattern.Text = "C";
            this.bt_clear_pattern.UseVisualStyleBackColor = true;
            this.bt_clear_pattern.Click += new System.EventHandler(this.bt_clear_pattern_Click);
            // 
            // bt_remove_pattern
            // 
            this.bt_remove_pattern.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_remove_pattern.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_remove_pattern.Location = new System.Drawing.Point(234, 58);
            this.bt_remove_pattern.Name = "bt_remove_pattern";
            this.bt_remove_pattern.Size = new System.Drawing.Size(40, 40);
            this.bt_remove_pattern.TabIndex = 37;
            this.bt_remove_pattern.Text = "-";
            this.bt_remove_pattern.UseVisualStyleBackColor = true;
            this.bt_remove_pattern.Click += new System.EventHandler(this.bt_remove_pattern_Click);
            // 
            // bt_add_pattern
            // 
            this.bt_add_pattern.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_add_pattern.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_add_pattern.Location = new System.Drawing.Point(234, 12);
            this.bt_add_pattern.Name = "bt_add_pattern";
            this.bt_add_pattern.Size = new System.Drawing.Size(40, 40);
            this.bt_add_pattern.TabIndex = 36;
            this.bt_add_pattern.Text = "+";
            this.bt_add_pattern.UseVisualStyleBackColor = true;
            this.bt_add_pattern.Click += new System.EventHandler(this.bt_add_pattern_Click);
            // 
            // listBox1
            // 
            this.listBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 19;
            this.listBox1.Location = new System.Drawing.Point(12, 12);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(205, 251);
            this.listBox1.TabIndex = 35;
            // 
            // tb_search
            // 
            this.tb_search.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_search.Location = new System.Drawing.Point(289, 12);
            this.tb_search.Name = "tb_search";
            this.tb_search.Size = new System.Drawing.Size(225, 30);
            this.tb_search.TabIndex = 39;
            this.tb_search.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.tb_search_KeyPress);
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(28, 335);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 64;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(14, 301);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 63;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(709, 590);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.tb_search);
            this.Controls.Add(this.bt_clear_pattern);
            this.Controls.Add(this.bt_remove_pattern);
            this.Controls.Add(this.bt_add_pattern);
            this.Controls.Add(this.listBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_clear_pattern;
        private System.Windows.Forms.Button bt_remove_pattern;
        private System.Windows.Forms.Button bt_add_pattern;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.TextBox tb_search;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

