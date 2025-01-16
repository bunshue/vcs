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
            this.lb_main_mesg2 = new System.Windows.Forms.Label();
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.bt_save = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.cb_search_video_files = new System.Windows.Forms.CheckBox();
            this.cb_search_audio_files = new System.Windows.Forms.CheckBox();
            this.groupBox_file = new System.Windows.Forms.GroupBox();
            this.cb_file_l = new System.Windows.Forms.CheckBox();
            this.tb_file_s = new System.Windows.Forms.TextBox();
            this.cb_file_m = new System.Windows.Forms.CheckBox();
            this.cb_file_s = new System.Windows.Forms.CheckBox();
            this.tb_file_l = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox_video = new System.Windows.Forms.GroupBox();
            this.cb_video_l = new System.Windows.Forms.CheckBox();
            this.cb_video_m = new System.Windows.Forms.CheckBox();
            this.cb_video_s = new System.Windows.Forms.CheckBox();
            this.groupBox_search = new System.Windows.Forms.GroupBox();
            this.rb_search_all_files = new System.Windows.Forms.RadioButton();
            this.rb_search_big_files = new System.Windows.Forms.RadioButton();
            this.groupBox_search_type = new System.Windows.Forms.GroupBox();
            this.groupBox_text_mode = new System.Windows.Forms.GroupBox();
            this.rb_text_mode_binary = new System.Windows.Forms.RadioButton();
            this.rb_text_mode_ascii = new System.Windows.Forms.RadioButton();
            this.groupBox_auto_save = new System.Windows.Forms.GroupBox();
            this.rb_auto_save_off = new System.Windows.Forms.RadioButton();
            this.rb_auto_save_on = new System.Windows.Forms.RadioButton();
            this.groupBox_file.SuspendLayout();
            this.groupBox_video.SuspendLayout();
            this.groupBox_search.SuspendLayout();
            this.groupBox_search_type.SuspendLayout();
            this.groupBox_text_mode.SuspendLayout();
            this.groupBox_auto_save.SuspendLayout();
            this.SuspendLayout();
            // 
            // tb_filesize_mb
            // 
            this.tb_filesize_mb.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_filesize_mb.Location = new System.Drawing.Point(162, 21);
            this.tb_filesize_mb.Name = "tb_filesize_mb";
            this.tb_filesize_mb.Size = new System.Drawing.Size(73, 30);
            this.tb_filesize_mb.TabIndex = 27;
            this.tb_filesize_mb.Text = "5";
            this.tb_filesize_mb.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.tb_filesize_mb.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.tb_filesize_mb_KeyPress);
            // 
            // lb_main_mesg2
            // 
            this.lb_main_mesg2.AutoSize = true;
            this.lb_main_mesg2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg2.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2.Location = new System.Drawing.Point(346, 56);
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
            this.lb_main_mesg1.Location = new System.Drawing.Point(346, 22);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(135, 24);
            this.lb_main_mesg1.TabIndex = 24;
            this.lb_main_mesg1.Text = "main_mesg1";
            // 
            // bt_save
            // 
            this.bt_save.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_save.Location = new System.Drawing.Point(348, 99);
            this.bt_save.Name = "bt_save";
            this.bt_save.Size = new System.Drawing.Size(94, 32);
            this.bt_save.TabIndex = 23;
            this.bt_save.Text = "儲存";
            this.bt_save.UseVisualStyleBackColor = true;
            this.bt_save.Click += new System.EventHandler(this.bt_save_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(633, 8);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 28;
            this.richTextBox1.Text = "";
            // 
            // cb_search_video_files
            // 
            this.cb_search_video_files.AutoSize = true;
            this.cb_search_video_files.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_search_video_files.Location = new System.Drawing.Point(42, 18);
            this.cb_search_video_files.Name = "cb_search_video_files";
            this.cb_search_video_files.Size = new System.Drawing.Size(173, 28);
            this.cb_search_video_files.TabIndex = 30;
            this.cb_search_video_files.Text = "只搜尋影片檔";
            this.cb_search_video_files.UseVisualStyleBackColor = true;
            // 
            // cb_search_audio_files
            // 
            this.cb_search_audio_files.AutoSize = true;
            this.cb_search_audio_files.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_search_audio_files.Location = new System.Drawing.Point(42, 52);
            this.cb_search_audio_files.Name = "cb_search_audio_files";
            this.cb_search_audio_files.Size = new System.Drawing.Size(173, 28);
            this.cb_search_audio_files.TabIndex = 31;
            this.cb_search_audio_files.Text = "只搜尋音樂檔";
            this.cb_search_audio_files.UseVisualStyleBackColor = true;
            // 
            // groupBox_file
            // 
            this.groupBox_file.Controls.Add(this.cb_file_l);
            this.groupBox_file.Controls.Add(this.tb_file_s);
            this.groupBox_file.Controls.Add(this.cb_file_m);
            this.groupBox_file.Controls.Add(this.cb_file_s);
            this.groupBox_file.Controls.Add(this.tb_file_l);
            this.groupBox_file.Controls.Add(this.label2);
            this.groupBox_file.Location = new System.Drawing.Point(16, 208);
            this.groupBox_file.Name = "groupBox_file";
            this.groupBox_file.Size = new System.Drawing.Size(292, 50);
            this.groupBox_file.TabIndex = 48;
            this.groupBox_file.TabStop = false;
            this.groupBox_file.Text = "檔案大小";
            // 
            // cb_file_l
            // 
            this.cb_file_l.AutoSize = true;
            this.cb_file_l.Checked = true;
            this.cb_file_l.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_l.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_file_l.Location = new System.Drawing.Point(11, 21);
            this.cb_file_l.Name = "cb_file_l";
            this.cb_file_l.Size = new System.Drawing.Size(43, 20);
            this.cb_file_l.TabIndex = 45;
            this.cb_file_l.Text = "大";
            this.cb_file_l.UseVisualStyleBackColor = true;
            // 
            // tb_file_s
            // 
            this.tb_file_s.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_file_s.Location = new System.Drawing.Point(210, 14);
            this.tb_file_s.Name = "tb_file_s";
            this.tb_file_s.Size = new System.Drawing.Size(52, 30);
            this.tb_file_s.TabIndex = 48;
            this.tb_file_s.Text = "10";
            this.tb_file_s.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // cb_file_m
            // 
            this.cb_file_m.AutoSize = true;
            this.cb_file_m.Checked = true;
            this.cb_file_m.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_m.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_file_m.Location = new System.Drawing.Point(60, 21);
            this.cb_file_m.Name = "cb_file_m";
            this.cb_file_m.Size = new System.Drawing.Size(43, 20);
            this.cb_file_m.TabIndex = 44;
            this.cb_file_m.Text = "中";
            this.cb_file_m.UseVisualStyleBackColor = true;
            // 
            // cb_file_s
            // 
            this.cb_file_s.AutoSize = true;
            this.cb_file_s.Checked = true;
            this.cb_file_s.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_file_s.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_file_s.Location = new System.Drawing.Point(109, 21);
            this.cb_file_s.Name = "cb_file_s";
            this.cb_file_s.Size = new System.Drawing.Size(43, 20);
            this.cb_file_s.TabIndex = 43;
            this.cb_file_s.Text = "小";
            this.cb_file_s.UseVisualStyleBackColor = true;
            // 
            // tb_file_l
            // 
            this.tb_file_l.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_file_l.Location = new System.Drawing.Point(153, 14);
            this.tb_file_l.Name = "tb_file_l";
            this.tb_file_l.Size = new System.Drawing.Size(52, 30);
            this.tb_file_l.TabIndex = 17;
            this.tb_file_l.Text = "100";
            this.tb_file_l.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(263, 23);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(23, 12);
            this.label2.TabIndex = 18;
            this.label2.Text = "MB";
            // 
            // groupBox_video
            // 
            this.groupBox_video.Controls.Add(this.cb_video_l);
            this.groupBox_video.Controls.Add(this.cb_video_m);
            this.groupBox_video.Controls.Add(this.cb_video_s);
            this.groupBox_video.Location = new System.Drawing.Point(18, 264);
            this.groupBox_video.Name = "groupBox_video";
            this.groupBox_video.Size = new System.Drawing.Size(160, 50);
            this.groupBox_video.TabIndex = 49;
            this.groupBox_video.TabStop = false;
            this.groupBox_video.Text = "影片大小";
            // 
            // cb_video_l
            // 
            this.cb_video_l.AutoSize = true;
            this.cb_video_l.Checked = true;
            this.cb_video_l.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_l.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_video_l.Location = new System.Drawing.Point(11, 21);
            this.cb_video_l.Name = "cb_video_l";
            this.cb_video_l.Size = new System.Drawing.Size(43, 20);
            this.cb_video_l.TabIndex = 45;
            this.cb_video_l.Text = "大";
            this.cb_video_l.UseVisualStyleBackColor = true;
            // 
            // cb_video_m
            // 
            this.cb_video_m.AutoSize = true;
            this.cb_video_m.Checked = true;
            this.cb_video_m.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_m.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_video_m.Location = new System.Drawing.Point(60, 21);
            this.cb_video_m.Name = "cb_video_m";
            this.cb_video_m.Size = new System.Drawing.Size(43, 20);
            this.cb_video_m.TabIndex = 44;
            this.cb_video_m.Text = "中";
            this.cb_video_m.UseVisualStyleBackColor = true;
            // 
            // cb_video_s
            // 
            this.cb_video_s.AutoSize = true;
            this.cb_video_s.Checked = true;
            this.cb_video_s.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_video_s.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.cb_video_s.Location = new System.Drawing.Point(109, 21);
            this.cb_video_s.Name = "cb_video_s";
            this.cb_video_s.Size = new System.Drawing.Size(43, 20);
            this.cb_video_s.TabIndex = 43;
            this.cb_video_s.Text = "小";
            this.cb_video_s.UseVisualStyleBackColor = true;
            // 
            // groupBox_search
            // 
            this.groupBox_search.Controls.Add(this.rb_search_all_files);
            this.groupBox_search.Controls.Add(this.tb_filesize_mb);
            this.groupBox_search.Controls.Add(this.rb_search_big_files);
            this.groupBox_search.Location = new System.Drawing.Point(18, 12);
            this.groupBox_search.Name = "groupBox_search";
            this.groupBox_search.Size = new System.Drawing.Size(304, 96);
            this.groupBox_search.TabIndex = 50;
            this.groupBox_search.TabStop = false;
            this.groupBox_search.Text = "搜尋檔案";
            // 
            // rb_search_all_files
            // 
            this.rb_search_all_files.AutoSize = true;
            this.rb_search_all_files.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_search_all_files.Location = new System.Drawing.Point(13, 56);
            this.rb_search_all_files.Name = "rb_search_all_files";
            this.rb_search_all_files.Size = new System.Drawing.Size(172, 28);
            this.rb_search_all_files.TabIndex = 29;
            this.rb_search_all_files.TabStop = true;
            this.rb_search_all_files.Text = "搜尋所有檔案";
            this.rb_search_all_files.UseVisualStyleBackColor = true;
            // 
            // rb_search_big_files
            // 
            this.rb_search_big_files.AutoSize = true;
            this.rb_search_big_files.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_search_big_files.Location = new System.Drawing.Point(13, 22);
            this.rb_search_big_files.Name = "rb_search_big_files";
            this.rb_search_big_files.Size = new System.Drawing.Size(268, 28);
            this.rb_search_big_files.TabIndex = 28;
            this.rb_search_big_files.TabStop = true;
            this.rb_search_big_files.Text = "只搜尋大檔        MB";
            this.rb_search_big_files.UseVisualStyleBackColor = true;
            // 
            // groupBox_search_type
            // 
            this.groupBox_search_type.Controls.Add(this.cb_search_video_files);
            this.groupBox_search_type.Controls.Add(this.cb_search_audio_files);
            this.groupBox_search_type.Location = new System.Drawing.Point(16, 114);
            this.groupBox_search_type.Name = "groupBox_search_type";
            this.groupBox_search_type.Size = new System.Drawing.Size(306, 88);
            this.groupBox_search_type.TabIndex = 51;
            this.groupBox_search_type.TabStop = false;
            this.groupBox_search_type.Text = "搜尋類型";
            // 
            // groupBox_text_mode
            // 
            this.groupBox_text_mode.Controls.Add(this.rb_text_mode_binary);
            this.groupBox_text_mode.Controls.Add(this.rb_text_mode_ascii);
            this.groupBox_text_mode.Location = new System.Drawing.Point(18, 320);
            this.groupBox_text_mode.Name = "groupBox_text_mode";
            this.groupBox_text_mode.Size = new System.Drawing.Size(240, 56);
            this.groupBox_text_mode.TabIndex = 52;
            this.groupBox_text_mode.TabStop = false;
            this.groupBox_text_mode.Text = "文字模式";
            // 
            // rb_text_mode_binary
            // 
            this.rb_text_mode_binary.AutoSize = true;
            this.rb_text_mode_binary.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_text_mode_binary.Location = new System.Drawing.Point(119, 21);
            this.rb_text_mode_binary.Name = "rb_text_mode_binary";
            this.rb_text_mode_binary.Size = new System.Drawing.Size(100, 28);
            this.rb_text_mode_binary.TabIndex = 29;
            this.rb_text_mode_binary.TabStop = true;
            this.rb_text_mode_binary.Text = "Binary";
            this.rb_text_mode_binary.UseVisualStyleBackColor = true;
            // 
            // rb_text_mode_ascii
            // 
            this.rb_text_mode_ascii.AutoSize = true;
            this.rb_text_mode_ascii.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_text_mode_ascii.Location = new System.Drawing.Point(25, 21);
            this.rb_text_mode_ascii.Name = "rb_text_mode_ascii";
            this.rb_text_mode_ascii.Size = new System.Drawing.Size(88, 28);
            this.rb_text_mode_ascii.TabIndex = 28;
            this.rb_text_mode_ascii.TabStop = true;
            this.rb_text_mode_ascii.Text = "ASCII";
            this.rb_text_mode_ascii.UseVisualStyleBackColor = true;
            // 
            // groupBox_auto_save
            // 
            this.groupBox_auto_save.Controls.Add(this.rb_auto_save_off);
            this.groupBox_auto_save.Controls.Add(this.rb_auto_save_on);
            this.groupBox_auto_save.Location = new System.Drawing.Point(18, 393);
            this.groupBox_auto_save.Name = "groupBox_auto_save";
            this.groupBox_auto_save.Size = new System.Drawing.Size(240, 56);
            this.groupBox_auto_save.TabIndex = 53;
            this.groupBox_auto_save.TabStop = false;
            this.groupBox_auto_save.Text = "自動存檔";
            // 
            // rb_auto_save_off
            // 
            this.rb_auto_save_off.AutoSize = true;
            this.rb_auto_save_off.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_auto_save_off.Location = new System.Drawing.Point(126, 16);
            this.rb_auto_save_off.Name = "rb_auto_save_off";
            this.rb_auto_save_off.Size = new System.Drawing.Size(76, 28);
            this.rb_auto_save_off.TabIndex = 29;
            this.rb_auto_save_off.TabStop = true;
            this.rb_auto_save_off.Text = "關閉";
            this.rb_auto_save_off.UseVisualStyleBackColor = true;
            // 
            // rb_auto_save_on
            // 
            this.rb_auto_save_on.AutoSize = true;
            this.rb_auto_save_on.Font = new System.Drawing.Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_auto_save_on.Location = new System.Drawing.Point(25, 17);
            this.rb_auto_save_on.Name = "rb_auto_save_on";
            this.rb_auto_save_on.Size = new System.Drawing.Size(76, 28);
            this.rb_auto_save_on.TabIndex = 28;
            this.rb_auto_save_on.TabStop = true;
            this.rb_auto_save_on.Text = "開啟";
            this.rb_auto_save_on.UseVisualStyleBackColor = true;
            // 
            // Form_Setup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(745, 554);
            this.Controls.Add(this.groupBox_auto_save);
            this.Controls.Add(this.groupBox_text_mode);
            this.Controls.Add(this.groupBox_search_type);
            this.Controls.Add(this.groupBox_search);
            this.Controls.Add(this.groupBox_video);
            this.Controls.Add(this.groupBox_file);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.lb_main_mesg2);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.bt_save);
            this.Name = "Form_Setup";
            this.Text = "Form_Setup";
            this.Load += new System.EventHandler(this.Form_Setup_Load);
            this.groupBox_file.ResumeLayout(false);
            this.groupBox_file.PerformLayout();
            this.groupBox_video.ResumeLayout(false);
            this.groupBox_video.PerformLayout();
            this.groupBox_search.ResumeLayout(false);
            this.groupBox_search.PerformLayout();
            this.groupBox_search_type.ResumeLayout(false);
            this.groupBox_search_type.PerformLayout();
            this.groupBox_text_mode.ResumeLayout(false);
            this.groupBox_text_mode.PerformLayout();
            this.groupBox_auto_save.ResumeLayout(false);
            this.groupBox_auto_save.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tb_filesize_mb;
        private System.Windows.Forms.Label lb_main_mesg2;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Button bt_save;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.CheckBox cb_search_video_files;
        private System.Windows.Forms.CheckBox cb_search_audio_files;
        private System.Windows.Forms.GroupBox groupBox_file;
        private System.Windows.Forms.CheckBox cb_file_l;
        private System.Windows.Forms.TextBox tb_file_s;
        private System.Windows.Forms.CheckBox cb_file_m;
        private System.Windows.Forms.CheckBox cb_file_s;
        private System.Windows.Forms.TextBox tb_file_l;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox_video;
        private System.Windows.Forms.CheckBox cb_video_l;
        private System.Windows.Forms.CheckBox cb_video_m;
        private System.Windows.Forms.CheckBox cb_video_s;
        private System.Windows.Forms.GroupBox groupBox_search;
        private System.Windows.Forms.GroupBox groupBox_search_type;
        private System.Windows.Forms.RadioButton rb_search_big_files;
        private System.Windows.Forms.RadioButton rb_search_all_files;
        private System.Windows.Forms.GroupBox groupBox_text_mode;
        private System.Windows.Forms.RadioButton rb_text_mode_binary;
        private System.Windows.Forms.RadioButton rb_text_mode_ascii;
        private System.Windows.Forms.GroupBox groupBox_auto_save;
        private System.Windows.Forms.RadioButton rb_auto_save_off;
        private System.Windows.Forms.RadioButton rb_auto_save_on;
    }
}