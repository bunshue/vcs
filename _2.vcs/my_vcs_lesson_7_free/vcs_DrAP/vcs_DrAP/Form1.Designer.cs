namespace vcs_DrAP
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.listView1 = new System.Windows.Forms.ListView();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.tb_search = new System.Windows.Forms.TextBox();
            this.bt_clear1 = new System.Windows.Forms.Button();
            this.bt_clear2 = new System.Windows.Forms.Button();
            this.cb_option1 = new System.Windows.Forms.CheckBox();
            this.bt_clear3 = new System.Windows.Forms.Button();
            this.groupbox_python = new System.Windows.Forms.GroupBox();
            this.bt_edit_python_files = new System.Windows.Forms.Button();
            this.bt_search_pattern_python = new System.Windows.Forms.Button();
            this.groupbox_result = new System.Windows.Forms.GroupBox();
            this.lb_search_result2 = new System.Windows.Forms.Label();
            this.lb_search_result1 = new System.Windows.Forms.Label();
            this.bt_replace = new System.Windows.Forms.Button();
            this.bt_compare = new System.Windows.Forms.Button();
            this.bt_open_dir2 = new System.Windows.Forms.Button();
            this.bt_copy_rtb_data = new System.Windows.Forms.Button();
            this.bt_setup = new System.Windows.Forms.Button();
            this.bt_search_pattern_vcs = new System.Windows.Forms.Button();
            this.bt_open_with_vcs = new System.Windows.Forms.Button();
            this.bt_open_with_ue = new System.Windows.Forms.Button();
            this.groupbox_python.SuspendLayout();
            this.groupbox_result.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(12, 227);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 10;
            this.richTextBox1.Text = "";
            this.richTextBox1.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // listView1
            // 
            this.listView1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.listView1.Location = new System.Drawing.Point(12, 124);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(100, 100);
            this.listView1.TabIndex = 14;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.View = System.Windows.Forms.View.Details;
            this.listView1.KeyDown += new System.Windows.Forms.KeyEventHandler(this.listView1_KeyDown);
            this.listView1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseClick);
            this.listView1.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.listView1_MouseDoubleClick);
            // 
            // richTextBox2
            // 
            this.richTextBox2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox2.Location = new System.Drawing.Point(12, 333);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(100, 100);
            this.richTextBox2.TabIndex = 19;
            this.richTextBox2.Text = "";
            this.richTextBox2.TextChanged += new System.EventHandler(this.richTextBox2_TextChanged);
            // 
            // tb_search
            // 
            this.tb_search.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_search.Location = new System.Drawing.Point(6, 12);
            this.tb_search.Name = "tb_search";
            this.tb_search.Size = new System.Drawing.Size(150, 30);
            this.tb_search.TabIndex = 24;
            this.tb_search.Text = "TBGBMBKB";
            this.tb_search.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.tb_search.Click += new System.EventHandler(this.tb_search_Click);
            this.tb_search.KeyDown += new System.Windows.Forms.KeyEventHandler(this.tb_search_KeyDown);
            this.tb_search.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.tb_search_KeyPress);
            // 
            // bt_clear1
            // 
            this.bt_clear1.Font = new System.Drawing.Font("細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear1.Location = new System.Drawing.Point(32, 241);
            this.bt_clear1.Name = "bt_clear1";
            this.bt_clear1.Size = new System.Drawing.Size(72, 36);
            this.bt_clear1.TabIndex = 36;
            this.bt_clear1.Text = "清除";
            this.bt_clear1.UseVisualStyleBackColor = true;
            this.bt_clear1.Click += new System.EventHandler(this.bt_clear1_Click);
            // 
            // bt_clear2
            // 
            this.bt_clear2.Font = new System.Drawing.Font("細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear2.Location = new System.Drawing.Point(32, 354);
            this.bt_clear2.Name = "bt_clear2";
            this.bt_clear2.Size = new System.Drawing.Size(72, 36);
            this.bt_clear2.TabIndex = 37;
            this.bt_clear2.Text = "清除";
            this.bt_clear2.UseVisualStyleBackColor = true;
            this.bt_clear2.Click += new System.EventHandler(this.bt_clear2_Click);
            // 
            // cb_option1
            // 
            this.cb_option1.AutoSize = true;
            this.cb_option1.Checked = true;
            this.cb_option1.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_option1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_option1.Location = new System.Drawing.Point(21, 61);
            this.cb_option1.Name = "cb_option1";
            this.cb_option1.Size = new System.Drawing.Size(103, 23);
            this.cb_option1.TabIndex = 51;
            this.cb_option1.Text = "滿30結束";
            this.cb_option1.UseVisualStyleBackColor = true;
            // 
            // bt_clear3
            // 
            this.bt_clear3.Font = new System.Drawing.Font("細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear3.Location = new System.Drawing.Point(32, 149);
            this.bt_clear3.Name = "bt_clear3";
            this.bt_clear3.Size = new System.Drawing.Size(72, 36);
            this.bt_clear3.TabIndex = 57;
            this.bt_clear3.Text = "清除";
            this.bt_clear3.UseVisualStyleBackColor = true;
            this.bt_clear3.Click += new System.EventHandler(this.bt_clear3_Click);
            // 
            // groupbox_python
            // 
            this.groupbox_python.Controls.Add(this.bt_edit_python_files);
            this.groupbox_python.Controls.Add(this.bt_search_pattern_python);
            this.groupbox_python.Location = new System.Drawing.Point(118, 124);
            this.groupbox_python.Name = "groupbox_python";
            this.groupbox_python.Size = new System.Drawing.Size(131, 132);
            this.groupbox_python.TabIndex = 64;
            this.groupbox_python.TabStop = false;
            this.groupbox_python.Text = "Python";
            // 
            // bt_edit_python_files
            // 
            this.bt_edit_python_files.BackgroundImage = global::vcs_DrAP.Properties.Resources.python2;
            this.bt_edit_python_files.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_edit_python_files.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_edit_python_files.Location = new System.Drawing.Point(71, 70);
            this.bt_edit_python_files.Name = "bt_edit_python_files";
            this.bt_edit_python_files.Size = new System.Drawing.Size(50, 50);
            this.bt_edit_python_files.TabIndex = 62;
            this.bt_edit_python_files.UseVisualStyleBackColor = true;
            this.bt_edit_python_files.Click += new System.EventHandler(this.bt_edit_python_files_Click);
            // 
            // bt_search_pattern_python
            // 
            this.bt_search_pattern_python.BackgroundImage = global::vcs_DrAP.Properties.Resources.python;
            this.bt_search_pattern_python.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_search_pattern_python.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_pattern_python.Location = new System.Drawing.Point(13, 70);
            this.bt_search_pattern_python.Name = "bt_search_pattern_python";
            this.bt_search_pattern_python.Size = new System.Drawing.Size(50, 50);
            this.bt_search_pattern_python.TabIndex = 39;
            this.bt_search_pattern_python.UseVisualStyleBackColor = true;
            this.bt_search_pattern_python.Click += new System.EventHandler(this.bt_search_pattern_python_Click);
            // 
            // groupbox_result
            // 
            this.groupbox_result.Controls.Add(this.lb_search_result2);
            this.groupbox_result.Controls.Add(this.lb_search_result1);
            this.groupbox_result.Location = new System.Drawing.Point(263, 124);
            this.groupbox_result.Name = "groupbox_result";
            this.groupbox_result.Size = new System.Drawing.Size(173, 132);
            this.groupbox_result.TabIndex = 65;
            this.groupbox_result.TabStop = false;
            this.groupbox_result.Text = "搜尋結果";
            // 
            // lb_search_result2
            // 
            this.lb_search_result2.AutoSize = true;
            this.lb_search_result2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_search_result2.ForeColor = System.Drawing.Color.Red;
            this.lb_search_result2.Location = new System.Drawing.Point(18, 65);
            this.lb_search_result2.Name = "lb_search_result2";
            this.lb_search_result2.Size = new System.Drawing.Size(78, 24);
            this.lb_search_result2.TabIndex = 67;
            this.lb_search_result2.Text = "result2";
            // 
            // lb_search_result1
            // 
            this.lb_search_result1.AutoSize = true;
            this.lb_search_result1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_search_result1.ForeColor = System.Drawing.Color.Red;
            this.lb_search_result1.Location = new System.Drawing.Point(18, 29);
            this.lb_search_result1.Name = "lb_search_result1";
            this.lb_search_result1.Size = new System.Drawing.Size(78, 24);
            this.lb_search_result1.TabIndex = 66;
            this.lb_search_result1.Text = "result1";
            // 
            // bt_replace
            // 
            this.bt_replace.BackColor = System.Drawing.Color.White;
            this.bt_replace.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_replace.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_replace.Location = new System.Drawing.Point(287, 64);
            this.bt_replace.Name = "bt_replace";
            this.bt_replace.Size = new System.Drawing.Size(50, 50);
            this.bt_replace.TabIndex = 69;
            this.bt_replace.Text = "置換";
            this.bt_replace.UseVisualStyleBackColor = false;
            this.bt_replace.Click += new System.EventHandler(this.bt_replace_Click);
            // 
            // bt_compare
            // 
            this.bt_compare.BackColor = System.Drawing.Color.White;
            this.bt_compare.BackgroundImage = global::vcs_DrAP.Properties.Resources.winmerge;
            this.bt_compare.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_compare.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_compare.Location = new System.Drawing.Point(287, 7);
            this.bt_compare.Name = "bt_compare";
            this.bt_compare.Size = new System.Drawing.Size(50, 50);
            this.bt_compare.TabIndex = 66;
            this.bt_compare.UseVisualStyleBackColor = false;
            this.bt_compare.Click += new System.EventHandler(this.bt_compare_Click);
            // 
            // bt_open_dir2
            // 
            this.bt_open_dir2.BackgroundImage = global::vcs_DrAP.Properties.Resources.open_folder;
            this.bt_open_dir2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_dir2.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_dir2.Location = new System.Drawing.Point(231, 7);
            this.bt_open_dir2.Name = "bt_open_dir2";
            this.bt_open_dir2.Size = new System.Drawing.Size(50, 50);
            this.bt_open_dir2.TabIndex = 59;
            this.bt_open_dir2.UseVisualStyleBackColor = true;
            this.bt_open_dir2.Click += new System.EventHandler(this.bt_open_dir2_Click);
            // 
            // bt_copy_rtb_data
            // 
            this.bt_copy_rtb_data.BackgroundImage = global::vcs_DrAP.Properties.Resources.clipboard;
            this.bt_copy_rtb_data.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_copy_rtb_data.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_copy_rtb_data.Location = new System.Drawing.Point(32, 383);
            this.bt_copy_rtb_data.Name = "bt_copy_rtb_data";
            this.bt_copy_rtb_data.Size = new System.Drawing.Size(45, 45);
            this.bt_copy_rtb_data.TabIndex = 53;
            this.bt_copy_rtb_data.UseVisualStyleBackColor = true;
            this.bt_copy_rtb_data.Click += new System.EventHandler(this.bt_copy_rtb_data_Click);
            // 
            // bt_setup
            // 
            this.bt_setup.BackgroundImage = global::vcs_DrAP.Properties.Resources.setup;
            this.bt_setup.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_setup.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup.Location = new System.Drawing.Point(343, 7);
            this.bt_setup.Name = "bt_setup";
            this.bt_setup.Size = new System.Drawing.Size(50, 50);
            this.bt_setup.TabIndex = 52;
            this.bt_setup.UseVisualStyleBackColor = true;
            this.bt_setup.Click += new System.EventHandler(this.bt_setup_Click);
            // 
            // bt_search_pattern_vcs
            // 
            this.bt_search_pattern_vcs.BackgroundImage = global::vcs_DrAP.Properties.Resources.vcs;
            this.bt_search_pattern_vcs.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_search_pattern_vcs.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_search_pattern_vcs.Location = new System.Drawing.Point(175, 7);
            this.bt_search_pattern_vcs.Name = "bt_search_pattern_vcs";
            this.bt_search_pattern_vcs.Size = new System.Drawing.Size(50, 50);
            this.bt_search_pattern_vcs.TabIndex = 26;
            this.bt_search_pattern_vcs.UseVisualStyleBackColor = true;
            this.bt_search_pattern_vcs.Click += new System.EventHandler(this.bt_search_pattern_vcs_Click);
            // 
            // bt_open_with_vcs
            // 
            this.bt_open_with_vcs.BackgroundImage = global::vcs_DrAP.Properties.Resources.vcs2;
            this.bt_open_with_vcs.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_with_vcs.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_with_vcs.Location = new System.Drawing.Point(175, 64);
            this.bt_open_with_vcs.Name = "bt_open_with_vcs";
            this.bt_open_with_vcs.Size = new System.Drawing.Size(50, 50);
            this.bt_open_with_vcs.TabIndex = 70;
            this.bt_open_with_vcs.UseVisualStyleBackColor = true;
            this.bt_open_with_vcs.Click += new System.EventHandler(this.bt_open_with_vcs_Click);
            // 
            // bt_open_with_ue
            // 
            this.bt_open_with_ue.BackgroundImage = global::vcs_DrAP.Properties.Resources.ultraedit;
            this.bt_open_with_ue.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_with_ue.Font = new System.Drawing.Font("細明體", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_open_with_ue.Location = new System.Drawing.Point(231, 64);
            this.bt_open_with_ue.Name = "bt_open_with_ue";
            this.bt_open_with_ue.Size = new System.Drawing.Size(50, 50);
            this.bt_open_with_ue.TabIndex = 71;
            this.bt_open_with_ue.UseVisualStyleBackColor = true;
            this.bt_open_with_ue.Click += new System.EventHandler(this.bt_open_with_ue_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(635, 466);
            this.Controls.Add(this.bt_open_with_ue);
            this.Controls.Add(this.bt_open_with_vcs);
            this.Controls.Add(this.bt_replace);
            this.Controls.Add(this.bt_compare);
            this.Controls.Add(this.groupbox_result);
            this.Controls.Add(this.groupbox_python);
            this.Controls.Add(this.bt_open_dir2);
            this.Controls.Add(this.bt_clear3);
            this.Controls.Add(this.bt_copy_rtb_data);
            this.Controls.Add(this.bt_setup);
            this.Controls.Add(this.cb_option1);
            this.Controls.Add(this.bt_clear2);
            this.Controls.Add(this.bt_clear1);
            this.Controls.Add(this.bt_search_pattern_vcs);
            this.Controls.Add(this.tb_search);
            this.Controls.Add(this.richTextBox2);
            this.Controls.Add(this.listView1);
            this.Controls.Add(this.richTextBox1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form1";
            this.Text = "DrAP";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupbox_python.ResumeLayout(false);
            this.groupbox_result.ResumeLayout(false);
            this.groupbox_result.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.RichTextBox richTextBox2;
        private System.Windows.Forms.TextBox tb_search;
        private System.Windows.Forms.Button bt_search_pattern_vcs;
        private System.Windows.Forms.Button bt_clear1;
        private System.Windows.Forms.Button bt_clear2;
        private System.Windows.Forms.Button bt_search_pattern_python;
        private System.Windows.Forms.CheckBox cb_option1;
        private System.Windows.Forms.Button bt_setup;
        private System.Windows.Forms.Button bt_copy_rtb_data;
        private System.Windows.Forms.Button bt_clear3;
        private System.Windows.Forms.Button bt_open_dir2;
        private System.Windows.Forms.Button bt_edit_python_files;
        private System.Windows.Forms.GroupBox groupbox_python;
        private System.Windows.Forms.GroupBox groupbox_result;
        private System.Windows.Forms.Label lb_search_result2;
        private System.Windows.Forms.Label lb_search_result1;
        private System.Windows.Forms.Button bt_compare;
        private System.Windows.Forms.Button bt_replace;
        private System.Windows.Forms.Button bt_open_with_vcs;
        private System.Windows.Forms.Button bt_open_with_ue;
    }
}

