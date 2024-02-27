namespace vcs_ShowPicture
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
            this.bt_cancel = new System.Windows.Forms.Button();
            this.bt_ok = new System.Windows.Forms.Button();
            this.tb_picture_folder_name = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.bt_open_picture = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rb_mode2 = new System.Windows.Forms.RadioButton();
            this.rb_mode1 = new System.Windows.Forms.RadioButton();
            this.rb_mode0 = new System.Windows.Forms.RadioButton();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // bt_cancel
            // 
            this.bt_cancel.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_cancel.Location = new System.Drawing.Point(47, 462);
            this.bt_cancel.Name = "bt_cancel";
            this.bt_cancel.Size = new System.Drawing.Size(67, 46);
            this.bt_cancel.TabIndex = 13;
            this.bt_cancel.Text = "取消";
            this.bt_cancel.UseVisualStyleBackColor = true;
            this.bt_cancel.Click += new System.EventHandler(this.bt_cancel_Click);
            // 
            // bt_ok
            // 
            this.bt_ok.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_ok.Location = new System.Drawing.Point(47, 400);
            this.bt_ok.Name = "bt_ok";
            this.bt_ok.Size = new System.Drawing.Size(67, 46);
            this.bt_ok.TabIndex = 12;
            this.bt_ok.Text = "確認";
            this.bt_ok.UseVisualStyleBackColor = true;
            this.bt_ok.Click += new System.EventHandler(this.bt_ok_Click);
            // 
            // tb_picture_folder_name
            // 
            this.tb_picture_folder_name.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_picture_folder_name.Location = new System.Drawing.Point(47, 106);
            this.tb_picture_folder_name.Name = "tb_picture_folder_name";
            this.tb_picture_folder_name.Size = new System.Drawing.Size(641, 36);
            this.tb_picture_folder_name.TabIndex = 11;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(43, 50);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(178, 24);
            this.label1.TabIndex = 10;
            this.label1.Text = "選擇瀏覽資料夾";
            // 
            // bt_open_picture
            // 
            this.bt_open_picture.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_open_picture.Location = new System.Drawing.Point(704, 94);
            this.bt_open_picture.Name = "bt_open_picture";
            this.bt_open_picture.Size = new System.Drawing.Size(60, 60);
            this.bt_open_picture.TabIndex = 249;
            this.bt_open_picture.UseVisualStyleBackColor = true;
            this.bt_open_picture.Click += new System.EventHandler(this.bt_open_picture_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rb_mode2);
            this.groupBox1.Controls.Add(this.rb_mode1);
            this.groupBox1.Controls.Add(this.rb_mode0);
            this.groupBox1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox1.Location = new System.Drawing.Point(47, 194);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(182, 200);
            this.groupBox1.TabIndex = 250;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "顯示模式";
            // 
            // rb_mode2
            // 
            this.rb_mode2.AutoSize = true;
            this.rb_mode2.Location = new System.Drawing.Point(16, 156);
            this.rb_mode2.Name = "rb_mode2";
            this.rb_mode2.Size = new System.Drawing.Size(145, 28);
            this.rb_mode2.TabIndex = 2;
            this.rb_mode2.TabStop = true;
            this.rb_mode2.Text = "radioButton3";
            this.rb_mode2.UseVisualStyleBackColor = true;
            // 
            // rb_mode1
            // 
            this.rb_mode1.AutoSize = true;
            this.rb_mode1.Location = new System.Drawing.Point(16, 93);
            this.rb_mode1.Name = "rb_mode1";
            this.rb_mode1.Size = new System.Drawing.Size(145, 28);
            this.rb_mode1.TabIndex = 1;
            this.rb_mode1.TabStop = true;
            this.rb_mode1.Text = "radioButton2";
            this.rb_mode1.UseVisualStyleBackColor = true;
            // 
            // rb_mode0
            // 
            this.rb_mode0.AutoSize = true;
            this.rb_mode0.Location = new System.Drawing.Point(16, 45);
            this.rb_mode0.Name = "rb_mode0";
            this.rb_mode0.Size = new System.Drawing.Size(145, 28);
            this.rb_mode0.TabIndex = 0;
            this.rb_mode0.TabStop = true;
            this.rb_mode0.Text = "radioButton1";
            this.rb_mode0.UseVisualStyleBackColor = true;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.radioButton1);
            this.groupBox2.Controls.Add(this.radioButton2);
            this.groupBox2.Controls.Add(this.radioButton3);
            this.groupBox2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox2.Location = new System.Drawing.Point(274, 194);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(182, 200);
            this.groupBox2.TabIndex = 251;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "圖片大小";
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Location = new System.Drawing.Point(16, 156);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(145, 28);
            this.radioButton1.TabIndex = 2;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "radioButton3";
            this.radioButton1.UseVisualStyleBackColor = true;
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(16, 93);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(145, 28);
            this.radioButton2.TabIndex = 1;
            this.radioButton2.TabStop = true;
            this.radioButton2.Text = "radioButton2";
            this.radioButton2.UseVisualStyleBackColor = true;
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Location = new System.Drawing.Point(16, 45);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(145, 28);
            this.radioButton3.TabIndex = 0;
            this.radioButton3.TabStop = true;
            this.radioButton3.Text = "radioButton1";
            this.radioButton3.UseVisualStyleBackColor = true;
            // 
            // Form_Setup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(915, 550);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_open_picture);
            this.Controls.Add(this.bt_cancel);
            this.Controls.Add(this.bt_ok);
            this.Controls.Add(this.tb_picture_folder_name);
            this.Controls.Add(this.label1);
            this.Name = "Form_Setup";
            this.Text = "Form_Setup";
            this.Load += new System.EventHandler(this.Form_Setup_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_cancel;
        private System.Windows.Forms.Button bt_ok;
        private System.Windows.Forms.TextBox tb_picture_folder_name;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button bt_open_picture;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb_mode2;
        private System.Windows.Forms.RadioButton rb_mode1;
        private System.Windows.Forms.RadioButton rb_mode0;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
    }
}