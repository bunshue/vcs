namespace vcs_translate_TCSC
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.richTextBox_tc = new System.Windows.Forms.RichTextBox();
            this.richTextBox_sc = new System.Windows.Forms.RichTextBox();
            this.lb_tc = new System.Windows.Forms.Label();
            this.bt_sc_tc = new System.Windows.Forms.Button();
            this.lb_sc = new System.Windows.Forms.Label();
            this.bt_tc_sc = new System.Windows.Forms.Button();
            this.bt_clear_tc = new System.Windows.Forms.Button();
            this.bt_copy_tc = new System.Windows.Forms.Button();
            this.bt_clear_sc = new System.Windows.Forms.Button();
            this.bt_copy_sc = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // richTextBox_tc
            // 
            this.richTextBox_tc.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox_tc.Location = new System.Drawing.Point(12, 42);
            this.richTextBox_tc.Name = "richTextBox_tc";
            this.richTextBox_tc.Size = new System.Drawing.Size(400, 500);
            this.richTextBox_tc.TabIndex = 0;
            this.richTextBox_tc.Text = resources.GetString("richTextBox_tc.Text");
            // 
            // richTextBox_sc
            // 
            this.richTextBox_sc.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox_sc.Location = new System.Drawing.Point(516, 42);
            this.richTextBox_sc.Name = "richTextBox_sc";
            this.richTextBox_sc.Size = new System.Drawing.Size(400, 500);
            this.richTextBox_sc.TabIndex = 1;
            this.richTextBox_sc.Text = resources.GetString("richTextBox_sc.Text");
            // 
            // lb_tc
            // 
            this.lb_tc.AutoSize = true;
            this.lb_tc.Font = new System.Drawing.Font("新細明體", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_tc.ForeColor = System.Drawing.Color.Red;
            this.lb_tc.Location = new System.Drawing.Point(12, 9);
            this.lb_tc.Name = "lb_tc";
            this.lb_tc.Size = new System.Drawing.Size(73, 29);
            this.lb_tc.TabIndex = 2;
            this.lb_tc.Text = "正中";
            // 
            // bt_sc_tc
            // 
            this.bt_sc_tc.BackgroundImage = global::vcs_translate_TCSC.Properties.Resources.left;
            this.bt_sc_tc.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_sc_tc.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_sc_tc.Location = new System.Drawing.Point(428, 233);
            this.bt_sc_tc.Name = "bt_sc_tc";
            this.bt_sc_tc.Size = new System.Drawing.Size(80, 80);
            this.bt_sc_tc.TabIndex = 4;
            this.bt_sc_tc.UseVisualStyleBackColor = true;
            this.bt_sc_tc.Click += new System.EventHandler(this.bt_sc_tc_Click);
            // 
            // lb_sc
            // 
            this.lb_sc.AutoSize = true;
            this.lb_sc.Font = new System.Drawing.Font("新細明體", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_sc.ForeColor = System.Drawing.Color.Red;
            this.lb_sc.Location = new System.Drawing.Point(76, 9);
            this.lb_sc.Name = "lb_sc";
            this.lb_sc.Size = new System.Drawing.Size(73, 29);
            this.lb_sc.TabIndex = 5;
            this.lb_sc.Text = "簡中";
            // 
            // bt_tc_sc
            // 
            this.bt_tc_sc.BackgroundImage = global::vcs_translate_TCSC.Properties.Resources.right;
            this.bt_tc_sc.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_tc_sc.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_tc_sc.Location = new System.Drawing.Point(428, 119);
            this.bt_tc_sc.Name = "bt_tc_sc";
            this.bt_tc_sc.Size = new System.Drawing.Size(80, 80);
            this.bt_tc_sc.TabIndex = 3;
            this.bt_tc_sc.UseVisualStyleBackColor = true;
            this.bt_tc_sc.Click += new System.EventHandler(this.bt_tc_sc_Click);
            // 
            // bt_clear_tc
            // 
            this.bt_clear_tc.BackgroundImage = global::vcs_translate_TCSC.Properties.Resources.x;
            this.bt_clear_tc.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_clear_tc.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_tc.Location = new System.Drawing.Point(230, 494);
            this.bt_clear_tc.Name = "bt_clear_tc";
            this.bt_clear_tc.Size = new System.Drawing.Size(48, 48);
            this.bt_clear_tc.TabIndex = 7;
            this.bt_clear_tc.UseVisualStyleBackColor = true;
            this.bt_clear_tc.Click += new System.EventHandler(this.bt_clear_tc_Click);
            // 
            // bt_copy_tc
            // 
            this.bt_copy_tc.BackgroundImage = global::vcs_translate_TCSC.Properties.Resources.clipboard;
            this.bt_copy_tc.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_copy_tc.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_copy_tc.Location = new System.Drawing.Point(155, 494);
            this.bt_copy_tc.Name = "bt_copy_tc";
            this.bt_copy_tc.Size = new System.Drawing.Size(48, 48);
            this.bt_copy_tc.TabIndex = 6;
            this.bt_copy_tc.UseVisualStyleBackColor = true;
            this.bt_copy_tc.Click += new System.EventHandler(this.bt_copy_tc_Click);
            // 
            // bt_clear_sc
            // 
            this.bt_clear_sc.BackgroundImage = global::vcs_translate_TCSC.Properties.Resources.x;
            this.bt_clear_sc.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_clear_sc.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear_sc.Location = new System.Drawing.Point(735, 494);
            this.bt_clear_sc.Name = "bt_clear_sc";
            this.bt_clear_sc.Size = new System.Drawing.Size(48, 48);
            this.bt_clear_sc.TabIndex = 9;
            this.bt_clear_sc.UseVisualStyleBackColor = true;
            this.bt_clear_sc.Click += new System.EventHandler(this.bt_clear_sc_Click);
            // 
            // bt_copy_sc
            // 
            this.bt_copy_sc.BackgroundImage = global::vcs_translate_TCSC.Properties.Resources.clipboard;
            this.bt_copy_sc.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_copy_sc.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_copy_sc.Location = new System.Drawing.Point(632, 494);
            this.bt_copy_sc.Name = "bt_copy_sc";
            this.bt_copy_sc.Size = new System.Drawing.Size(48, 48);
            this.bt_copy_sc.TabIndex = 8;
            this.bt_copy_sc.UseVisualStyleBackColor = true;
            this.bt_copy_sc.Click += new System.EventHandler(this.bt_copy_sc_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(946, 581);
            this.Controls.Add(this.bt_clear_sc);
            this.Controls.Add(this.bt_copy_sc);
            this.Controls.Add(this.bt_clear_tc);
            this.Controls.Add(this.bt_copy_tc);
            this.Controls.Add(this.lb_sc);
            this.Controls.Add(this.bt_sc_tc);
            this.Controls.Add(this.bt_tc_sc);
            this.Controls.Add(this.lb_tc);
            this.Controls.Add(this.richTextBox_sc);
            this.Controls.Add(this.richTextBox_tc);
            this.Name = "Form1";
            this.Text = "正中簡中轉換程式";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox_tc;
        private System.Windows.Forms.RichTextBox richTextBox_sc;
        private System.Windows.Forms.Label lb_tc;
        private System.Windows.Forms.Button bt_tc_sc;
        private System.Windows.Forms.Button bt_sc_tc;
        private System.Windows.Forms.Label lb_sc;
        private System.Windows.Forms.Button bt_clear_tc;
        private System.Windows.Forms.Button bt_copy_tc;
        private System.Windows.Forms.Button bt_clear_sc;
        private System.Windows.Forms.Button bt_copy_sc;
    }
}

