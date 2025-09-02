namespace vcs_DrAP
{
    partial class Form_Replace
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
            this.groupBox_replace = new System.Windows.Forms.GroupBox();
            this.lb_path = new System.Windows.Forms.Label();
            this.bt_open_dir = new System.Windows.Forms.Button();
            this.rb_file_type3 = new System.Windows.Forms.RadioButton();
            this.lb_string_new = new System.Windows.Forms.Label();
            this.bt_replace = new System.Windows.Forms.Button();
            this.lb_string_old = new System.Windows.Forms.Label();
            this.tb_string_new = new System.Windows.Forms.TextBox();
            this.tb_string_old = new System.Windows.Forms.TextBox();
            this.rb_file_type2 = new System.Windows.Forms.RadioButton();
            this.rb_file_type1 = new System.Windows.Forms.RadioButton();
            this.rb_file_type0 = new System.Windows.Forms.RadioButton();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_clear = new System.Windows.Forms.Button();
            this.groupBox_replace.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox_replace
            // 
            this.groupBox_replace.Controls.Add(this.lb_path);
            this.groupBox_replace.Controls.Add(this.bt_open_dir);
            this.groupBox_replace.Controls.Add(this.rb_file_type3);
            this.groupBox_replace.Controls.Add(this.lb_string_new);
            this.groupBox_replace.Controls.Add(this.bt_replace);
            this.groupBox_replace.Controls.Add(this.lb_string_old);
            this.groupBox_replace.Controls.Add(this.tb_string_new);
            this.groupBox_replace.Controls.Add(this.tb_string_old);
            this.groupBox_replace.Controls.Add(this.rb_file_type2);
            this.groupBox_replace.Controls.Add(this.rb_file_type1);
            this.groupBox_replace.Controls.Add(this.rb_file_type0);
            this.groupBox_replace.Location = new System.Drawing.Point(12, 12);
            this.groupBox_replace.Name = "groupBox_replace";
            this.groupBox_replace.Size = new System.Drawing.Size(320, 150);
            this.groupBox_replace.TabIndex = 146;
            this.groupBox_replace.TabStop = false;
            this.groupBox_replace.Text = "置換檔案內的文字";
            // 
            // lb_path
            // 
            this.lb_path.AutoSize = true;
            this.lb_path.Font = new System.Drawing.Font("新細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_path.Location = new System.Drawing.Point(12, 130);
            this.lb_path.Name = "lb_path";
            this.lb_path.Size = new System.Drawing.Size(33, 13);
            this.lb_path.TabIndex = 151;
            this.lb_path.Text = "路徑";
            // 
            // bt_open_dir
            // 
            this.bt_open_dir.BackgroundImage = global::vcs_DrAP.Properties.Resources.open_folder;
            this.bt_open_dir.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_dir.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_dir.Location = new System.Drawing.Point(116, 87);
            this.bt_open_dir.Name = "bt_open_dir";
            this.bt_open_dir.Size = new System.Drawing.Size(40, 40);
            this.bt_open_dir.TabIndex = 146;
            this.bt_open_dir.UseVisualStyleBackColor = true;
            this.bt_open_dir.Click += new System.EventHandler(this.bt_open_dir_Click);
            // 
            // rb_file_type3
            // 
            this.rb_file_type3.AutoSize = true;
            this.rb_file_type3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type3.Location = new System.Drawing.Point(228, 96);
            this.rb_file_type3.Name = "rb_file_type3";
            this.rb_file_type3.Size = new System.Drawing.Size(49, 23);
            this.rb_file_type3.TabIndex = 150;
            this.rb_file_type3.Text = "*.*";
            this.rb_file_type3.UseVisualStyleBackColor = true;
            // 
            // lb_string_new
            // 
            this.lb_string_new.AutoSize = true;
            this.lb_string_new.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_string_new.Location = new System.Drawing.Point(4, 58);
            this.lb_string_new.Name = "lb_string_new";
            this.lb_string_new.Size = new System.Drawing.Size(66, 19);
            this.lb_string_new.TabIndex = 149;
            this.lb_string_new.Text = "新字串";
            // 
            // bt_replace
            // 
            this.bt_replace.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_replace.Location = new System.Drawing.Point(10, 87);
            this.bt_replace.Name = "bt_replace";
            this.bt_replace.Size = new System.Drawing.Size(100, 40);
            this.bt_replace.TabIndex = 146;
            this.bt_replace.Text = "置換";
            this.bt_replace.UseVisualStyleBackColor = true;
            this.bt_replace.Click += new System.EventHandler(this.bt_replace_Click);
            // 
            // lb_string_old
            // 
            this.lb_string_old.AutoSize = true;
            this.lb_string_old.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_string_old.Location = new System.Drawing.Point(6, 27);
            this.lb_string_old.Name = "lb_string_old";
            this.lb_string_old.Size = new System.Drawing.Size(66, 19);
            this.lb_string_old.TabIndex = 148;
            this.lb_string_old.Text = "原字串";
            // 
            // tb_string_new
            // 
            this.tb_string_new.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_string_new.Location = new System.Drawing.Point(73, 55);
            this.tb_string_new.Name = "tb_string_new";
            this.tb_string_new.Size = new System.Drawing.Size(150, 30);
            this.tb_string_new.TabIndex = 147;
            // 
            // tb_string_old
            // 
            this.tb_string_old.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_string_old.Location = new System.Drawing.Point(73, 27);
            this.tb_string_old.Name = "tb_string_old";
            this.tb_string_old.Size = new System.Drawing.Size(150, 30);
            this.tb_string_old.TabIndex = 146;
            // 
            // rb_file_type2
            // 
            this.rb_file_type2.AutoSize = true;
            this.rb_file_type2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type2.Location = new System.Drawing.Point(228, 70);
            this.rb_file_type2.Name = "rb_file_type2";
            this.rb_file_type2.Size = new System.Drawing.Size(58, 23);
            this.rb_file_type2.TabIndex = 2;
            this.rb_file_type2.Text = "*.py";
            this.rb_file_type2.UseVisualStyleBackColor = true;
            // 
            // rb_file_type1
            // 
            this.rb_file_type1.AutoSize = true;
            this.rb_file_type1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type1.Location = new System.Drawing.Point(228, 45);
            this.rb_file_type1.Name = "rb_file_type1";
            this.rb_file_type1.Size = new System.Drawing.Size(92, 23);
            this.rb_file_type1.TabIndex = 1;
            this.rb_file_type1.Text = "*.c *.cpp";
            this.rb_file_type1.UseVisualStyleBackColor = true;
            // 
            // rb_file_type0
            // 
            this.rb_file_type0.AutoSize = true;
            this.rb_file_type0.Checked = true;
            this.rb_file_type0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_file_type0.Location = new System.Drawing.Point(228, 20);
            this.rb_file_type0.Name = "rb_file_type0";
            this.rb_file_type0.Size = new System.Drawing.Size(55, 23);
            this.rb_file_type0.TabIndex = 0;
            this.rb_file_type0.TabStop = true;
            this.rb_file_type0.Text = "*.cs";
            this.rb_file_type0.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 168);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 147;
            this.richTextBox1.Text = "";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(41, 225);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 148;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // Form_Replace
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(471, 359);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox_replace);
            this.Name = "Form_Replace";
            this.Text = "Form_Replace";
            this.Load += new System.EventHandler(this.Form_Replace_Load);
            this.groupBox_replace.ResumeLayout(false);
            this.groupBox_replace.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox_replace;
        private System.Windows.Forms.Label lb_path;
        private System.Windows.Forms.Button bt_open_dir;
        private System.Windows.Forms.RadioButton rb_file_type3;
        private System.Windows.Forms.Label lb_string_new;
        private System.Windows.Forms.Button bt_replace;
        private System.Windows.Forms.Label lb_string_old;
        private System.Windows.Forms.TextBox tb_string_new;
        private System.Windows.Forms.TextBox tb_string_old;
        private System.Windows.Forms.RadioButton rb_file_type2;
        private System.Windows.Forms.RadioButton rb_file_type1;
        private System.Windows.Forms.RadioButton rb_file_type0;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_clear;

    }
}