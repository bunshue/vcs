namespace iMS_Link
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
            this.components = new System.ComponentModel.Container();
            this.lb_setup1 = new System.Windows.Forms.Label();
            this.tb_setup1 = new System.Windows.Forms.TextBox();
            this.bt_setup1 = new System.Windows.Forms.Button();
            this.lb_setup0 = new System.Windows.Forms.Label();
            this.tb_setup0 = new System.Windows.Forms.TextBox();
            this.bt_setup0 = new System.Windows.Forms.Button();
            this.bt_setup6 = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.lb_main_mesg1 = new System.Windows.Forms.Label();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.lb_main_mesg2 = new System.Windows.Forms.Label();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.panel_data_write = new System.Windows.Forms.Panel();
            this.panel_awb = new System.Windows.Forms.Panel();
            this.rb_operation_mode2 = new System.Windows.Forms.RadioButton();
            this.rb_operation_mode1 = new System.Windows.Forms.RadioButton();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.panel_plc = new System.Windows.Forms.Panel();
            this.rb_use_plc2 = new System.Windows.Forms.RadioButton();
            this.rb_use_plc1 = new System.Windows.Forms.RadioButton();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.panel_ims = new System.Windows.Forms.Panel();
            this.rb_use_ims2 = new System.Windows.Forms.RadioButton();
            this.rb_use_ims1 = new System.Windows.Forms.RadioButton();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.panel_egd_type = new System.Windows.Forms.Panel();
            this.rb_egd_type2 = new System.Windows.Forms.RadioButton();
            this.rb_egd_type1 = new System.Windows.Forms.RadioButton();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.rb_language3 = new System.Windows.Forms.RadioButton();
            this.panel_language = new System.Windows.Forms.Panel();
            this.rb_language2 = new System.Windows.Forms.RadioButton();
            this.rb_language1 = new System.Windows.Forms.RadioButton();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.bt_setup7 = new System.Windows.Forms.Button();
            this.bt_setup8 = new System.Windows.Forms.Button();
            this.cb_auto_start = new System.Windows.Forms.CheckBox();
            this.groupBox0.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.SuspendLayout();
            // 
            // lb_setup1
            // 
            this.lb_setup1.AutoSize = true;
            this.lb_setup1.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_setup1.Location = new System.Drawing.Point(12, 166);
            this.lb_setup1.Name = "lb_setup1";
            this.lb_setup1.Size = new System.Drawing.Size(99, 19);
            this.lb_setup1.TabIndex = 0;
            this.lb_setup1.Text = "lb_setup1";
            // 
            // tb_setup1
            // 
            this.tb_setup1.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_setup1.Location = new System.Drawing.Point(114, 158);
            this.tb_setup1.Name = "tb_setup1";
            this.tb_setup1.Size = new System.Drawing.Size(574, 30);
            this.tb_setup1.TabIndex = 2;
            // 
            // bt_setup1
            // 
            this.bt_setup1.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup1.Location = new System.Drawing.Point(692, 156);
            this.bt_setup1.Name = "bt_setup1";
            this.bt_setup1.Size = new System.Drawing.Size(80, 40);
            this.bt_setup1.TabIndex = 2;
            this.bt_setup1.Text = "修改";
            this.bt_setup1.UseVisualStyleBackColor = true;
            this.bt_setup1.Click += new System.EventHandler(this.bt_setup1_Click);
            // 
            // lb_setup0
            // 
            this.lb_setup0.AutoSize = true;
            this.lb_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_setup0.Location = new System.Drawing.Point(12, 122);
            this.lb_setup0.Name = "lb_setup0";
            this.lb_setup0.Size = new System.Drawing.Size(99, 19);
            this.lb_setup0.TabIndex = 7;
            this.lb_setup0.Text = "lb_setup0";
            // 
            // tb_setup0
            // 
            this.tb_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_setup0.Location = new System.Drawing.Point(114, 119);
            this.tb_setup0.Name = "tb_setup0";
            this.tb_setup0.Size = new System.Drawing.Size(574, 30);
            this.tb_setup0.TabIndex = 1;
            // 
            // bt_setup0
            // 
            this.bt_setup0.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup0.Location = new System.Drawing.Point(692, 115);
            this.bt_setup0.Name = "bt_setup0";
            this.bt_setup0.Size = new System.Drawing.Size(80, 40);
            this.bt_setup0.TabIndex = 17;
            this.bt_setup0.Text = "修改";
            this.bt_setup0.UseVisualStyleBackColor = true;
            this.bt_setup0.Click += new System.EventHandler(this.bt_setup0_Click);
            // 
            // bt_setup6
            // 
            this.bt_setup6.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup6.Location = new System.Drawing.Point(692, 194);
            this.bt_setup6.Name = "bt_setup6";
            this.bt_setup6.Size = new System.Drawing.Size(80, 40);
            this.bt_setup6.TabIndex = 18;
            this.bt_setup6.Text = "儲存";
            this.bt_setup6.UseVisualStyleBackColor = true;
            this.bt_setup6.Click += new System.EventHandler(this.bt_setup6_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // lb_main_mesg1
            // 
            this.lb_main_mesg1.AutoSize = true;
            this.lb_main_mesg1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg1.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg1.Location = new System.Drawing.Point(15, 191);
            this.lb_main_mesg1.Name = "lb_main_mesg1";
            this.lb_main_mesg1.Size = new System.Drawing.Size(135, 24);
            this.lb_main_mesg1.TabIndex = 19;
            this.lb_main_mesg1.Text = "main_mesg1";
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // lb_main_mesg2
            // 
            this.lb_main_mesg2.AutoSize = true;
            this.lb_main_mesg2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_main_mesg2.ForeColor = System.Drawing.Color.Red;
            this.lb_main_mesg2.Location = new System.Drawing.Point(15, 225);
            this.lb_main_mesg2.Name = "lb_main_mesg2";
            this.lb_main_mesg2.Size = new System.Drawing.Size(135, 24);
            this.lb_main_mesg2.TabIndex = 20;
            this.lb_main_mesg2.Text = "main_mesg2";
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.panel_data_write);
            this.groupBox0.Controls.Add(this.panel_awb);
            this.groupBox0.Controls.Add(this.rb_operation_mode2);
            this.groupBox0.Controls.Add(this.rb_operation_mode1);
            this.groupBox0.Location = new System.Drawing.Point(10, 10);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(140, 100);
            this.groupBox0.TabIndex = 46;
            this.groupBox0.TabStop = false;
            // 
            // panel_data_write
            // 
            this.panel_data_write.Location = new System.Drawing.Point(95, 54);
            this.panel_data_write.Name = "panel_data_write";
            this.panel_data_write.Size = new System.Drawing.Size(40, 40);
            this.panel_data_write.TabIndex = 48;
            // 
            // panel_awb
            // 
            this.panel_awb.Location = new System.Drawing.Point(90, 11);
            this.panel_awb.Name = "panel_awb";
            this.panel_awb.Size = new System.Drawing.Size(40, 40);
            this.panel_awb.TabIndex = 47;
            // 
            // rb_operation_mode2
            // 
            this.rb_operation_mode2.AutoSize = true;
            this.rb_operation_mode2.Location = new System.Drawing.Point(14, 64);
            this.rb_operation_mode2.Name = "rb_operation_mode2";
            this.rb_operation_mode2.Size = new System.Drawing.Size(71, 16);
            this.rb_operation_mode2.TabIndex = 46;
            this.rb_operation_mode2.Text = "資料燒錄";
            this.rb_operation_mode2.UseVisualStyleBackColor = true;
            this.rb_operation_mode2.CheckedChanged += new System.EventHandler(this.rb_operation_mode_CheckedChanged);
            // 
            // rb_operation_mode1
            // 
            this.rb_operation_mode1.AutoSize = true;
            this.rb_operation_mode1.Checked = true;
            this.rb_operation_mode1.Location = new System.Drawing.Point(9, 30);
            this.rb_operation_mode1.Name = "rb_operation_mode1";
            this.rb_operation_mode1.Size = new System.Drawing.Size(71, 16);
            this.rb_operation_mode1.TabIndex = 45;
            this.rb_operation_mode1.TabStop = true;
            this.rb_operation_mode1.Text = "色彩調教";
            this.rb_operation_mode1.UseVisualStyleBackColor = true;
            this.rb_operation_mode1.CheckedChanged += new System.EventHandler(this.rb_operation_mode_CheckedChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.panel_plc);
            this.groupBox1.Controls.Add(this.rb_use_plc2);
            this.groupBox1.Controls.Add(this.rb_use_plc1);
            this.groupBox1.Location = new System.Drawing.Point(160, 10);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(140, 100);
            this.groupBox1.TabIndex = 47;
            this.groupBox1.TabStop = false;
            // 
            // panel_plc
            // 
            this.panel_plc.Location = new System.Drawing.Point(85, 37);
            this.panel_plc.Name = "panel_plc";
            this.panel_plc.Size = new System.Drawing.Size(40, 40);
            this.panel_plc.TabIndex = 48;
            // 
            // rb_use_plc2
            // 
            this.rb_use_plc2.AutoSize = true;
            this.rb_use_plc2.Location = new System.Drawing.Point(20, 69);
            this.rb_use_plc2.Name = "rb_use_plc2";
            this.rb_use_plc2.Size = new System.Drawing.Size(59, 16);
            this.rb_use_plc2.TabIndex = 48;
            this.rb_use_plc2.Text = "假上位";
            this.rb_use_plc2.UseVisualStyleBackColor = true;
            this.rb_use_plc2.CheckedChanged += new System.EventHandler(this.rb_use_plc_CheckedChanged);
            // 
            // rb_use_plc1
            // 
            this.rb_use_plc1.AutoSize = true;
            this.rb_use_plc1.Checked = true;
            this.rb_use_plc1.Location = new System.Drawing.Point(20, 37);
            this.rb_use_plc1.Name = "rb_use_plc1";
            this.rb_use_plc1.Size = new System.Drawing.Size(59, 16);
            this.rb_use_plc1.TabIndex = 47;
            this.rb_use_plc1.TabStop = true;
            this.rb_use_plc1.Text = "真上位";
            this.rb_use_plc1.UseVisualStyleBackColor = true;
            this.rb_use_plc1.CheckedChanged += new System.EventHandler(this.rb_use_plc_CheckedChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.panel_ims);
            this.groupBox2.Controls.Add(this.rb_use_ims2);
            this.groupBox2.Controls.Add(this.rb_use_ims1);
            this.groupBox2.Location = new System.Drawing.Point(310, 10);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(140, 100);
            this.groupBox2.TabIndex = 49;
            this.groupBox2.TabStop = false;
            // 
            // panel_ims
            // 
            this.panel_ims.Location = new System.Drawing.Point(94, 35);
            this.panel_ims.Name = "panel_ims";
            this.panel_ims.Size = new System.Drawing.Size(40, 40);
            this.panel_ims.TabIndex = 48;
            // 
            // rb_use_ims2
            // 
            this.rb_use_ims2.AutoSize = true;
            this.rb_use_ims2.Location = new System.Drawing.Point(20, 69);
            this.rb_use_ims2.Name = "rb_use_ims2";
            this.rb_use_ims2.Size = new System.Drawing.Size(59, 16);
            this.rb_use_ims2.TabIndex = 48;
            this.rb_use_ims2.Text = "假下位";
            this.rb_use_ims2.UseVisualStyleBackColor = true;
            this.rb_use_ims2.CheckedChanged += new System.EventHandler(this.rb_use_ims_CheckedChanged);
            // 
            // rb_use_ims1
            // 
            this.rb_use_ims1.AutoSize = true;
            this.rb_use_ims1.Checked = true;
            this.rb_use_ims1.Location = new System.Drawing.Point(20, 35);
            this.rb_use_ims1.Name = "rb_use_ims1";
            this.rb_use_ims1.Size = new System.Drawing.Size(59, 16);
            this.rb_use_ims1.TabIndex = 47;
            this.rb_use_ims1.TabStop = true;
            this.rb_use_ims1.Text = "真下位";
            this.rb_use_ims1.UseVisualStyleBackColor = true;
            this.rb_use_ims1.CheckedChanged += new System.EventHandler(this.rb_use_ims_CheckedChanged);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.panel_egd_type);
            this.groupBox3.Controls.Add(this.rb_egd_type2);
            this.groupBox3.Controls.Add(this.rb_egd_type1);
            this.groupBox3.Location = new System.Drawing.Point(460, 10);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(140, 100);
            this.groupBox3.TabIndex = 50;
            this.groupBox3.TabStop = false;
            // 
            // panel_egd_type
            // 
            this.panel_egd_type.Location = new System.Drawing.Point(73, 23);
            this.panel_egd_type.Name = "panel_egd_type";
            this.panel_egd_type.Size = new System.Drawing.Size(40, 40);
            this.panel_egd_type.TabIndex = 48;
            // 
            // rb_egd_type2
            // 
            this.rb_egd_type2.AutoSize = true;
            this.rb_egd_type2.Location = new System.Drawing.Point(20, 69);
            this.rb_egd_type2.Name = "rb_egd_type2";
            this.rb_egd_type2.Size = new System.Drawing.Size(59, 16);
            this.rb_egd_type2.TabIndex = 48;
            this.rb_egd_type2.Text = "食道鏡";
            this.rb_egd_type2.UseVisualStyleBackColor = true;
            this.rb_egd_type2.CheckedChanged += new System.EventHandler(this.rb_egd_type_CheckedChanged);
            // 
            // rb_egd_type1
            // 
            this.rb_egd_type1.AutoSize = true;
            this.rb_egd_type1.Checked = true;
            this.rb_egd_type1.Location = new System.Drawing.Point(20, 37);
            this.rb_egd_type1.Name = "rb_egd_type1";
            this.rb_egd_type1.Size = new System.Drawing.Size(47, 16);
            this.rb_egd_type1.TabIndex = 47;
            this.rb_egd_type1.TabStop = true;
            this.rb_egd_type1.Text = "胃鏡";
            this.rb_egd_type1.UseVisualStyleBackColor = true;
            this.rb_egd_type1.CheckedChanged += new System.EventHandler(this.rb_egd_type_CheckedChanged);
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.rb_language3);
            this.groupBox4.Controls.Add(this.panel_language);
            this.groupBox4.Controls.Add(this.rb_language2);
            this.groupBox4.Controls.Add(this.rb_language1);
            this.groupBox4.Location = new System.Drawing.Point(610, 10);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Size = new System.Drawing.Size(140, 100);
            this.groupBox4.TabIndex = 51;
            this.groupBox4.TabStop = false;
            // 
            // rb_language3
            // 
            this.rb_language3.AutoSize = true;
            this.rb_language3.Location = new System.Drawing.Point(10, 65);
            this.rb_language3.Name = "rb_language3";
            this.rb_language3.Size = new System.Drawing.Size(58, 16);
            this.rb_language3.TabIndex = 49;
            this.rb_language3.Text = "English";
            this.rb_language3.UseVisualStyleBackColor = true;
            this.rb_language3.CheckedChanged += new System.EventHandler(this.rb_language_CheckedChanged);
            // 
            // panel_language
            // 
            this.panel_language.Location = new System.Drawing.Point(80, 43);
            this.panel_language.Name = "panel_language";
            this.panel_language.Size = new System.Drawing.Size(40, 40);
            this.panel_language.TabIndex = 48;
            // 
            // rb_language2
            // 
            this.rb_language2.AutoSize = true;
            this.rb_language2.Location = new System.Drawing.Point(10, 43);
            this.rb_language2.Name = "rb_language2";
            this.rb_language2.Size = new System.Drawing.Size(71, 16);
            this.rb_language2.TabIndex = 48;
            this.rb_language2.Text = "簡體中文";
            this.rb_language2.UseVisualStyleBackColor = true;
            this.rb_language2.CheckedChanged += new System.EventHandler(this.rb_language_CheckedChanged);
            // 
            // rb_language1
            // 
            this.rb_language1.AutoSize = true;
            this.rb_language1.Checked = true;
            this.rb_language1.Location = new System.Drawing.Point(10, 21);
            this.rb_language1.Name = "rb_language1";
            this.rb_language1.Size = new System.Drawing.Size(71, 16);
            this.rb_language1.TabIndex = 47;
            this.rb_language1.TabStop = true;
            this.rb_language1.Text = "正體中文";
            this.rb_language1.UseVisualStyleBackColor = true;
            this.rb_language1.CheckedChanged += new System.EventHandler(this.rb_language_CheckedChanged);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(16, 350);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 52;
            this.richTextBox1.Text = "";
            // 
            // bt_setup7
            // 
            this.bt_setup7.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup7.Location = new System.Drawing.Point(692, 232);
            this.bt_setup7.Name = "bt_setup7";
            this.bt_setup7.Size = new System.Drawing.Size(80, 80);
            this.bt_setup7.TabIndex = 53;
            this.bt_setup7.Text = "恢復 預設";
            this.bt_setup7.UseVisualStyleBackColor = true;
            this.bt_setup7.Click += new System.EventHandler(this.bt_setup7_Click);
            // 
            // bt_setup8
            // 
            this.bt_setup8.Font = new System.Drawing.Font("標楷體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_setup8.Location = new System.Drawing.Point(598, 232);
            this.bt_setup8.Name = "bt_setup8";
            this.bt_setup8.Size = new System.Drawing.Size(80, 80);
            this.bt_setup8.TabIndex = 54;
            this.bt_setup8.Text = "開啟 工廠 模式";
            this.bt_setup8.UseVisualStyleBackColor = true;
            this.bt_setup8.Click += new System.EventHandler(this.bt_setup8_Click);
            // 
            // cb_auto_start
            // 
            this.cb_auto_start.AutoSize = true;
            this.cb_auto_start.Checked = true;
            this.cb_auto_start.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_auto_start.Location = new System.Drawing.Point(768, 21);
            this.cb_auto_start.Name = "cb_auto_start";
            this.cb_auto_start.Size = new System.Drawing.Size(132, 16);
            this.cb_auto_start.TabIndex = 55;
            this.cb_auto_start.Text = "開機啟動自動化測試";
            this.cb_auto_start.UseVisualStyleBackColor = true;
            // 
            // Form_Setup
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(899, 469);
            this.Controls.Add(this.cb_auto_start);
            this.Controls.Add(this.bt_setup8);
            this.Controls.Add(this.bt_setup7);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox4);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.lb_main_mesg2);
            this.Controls.Add(this.lb_main_mesg1);
            this.Controls.Add(this.bt_setup6);
            this.Controls.Add(this.bt_setup0);
            this.Controls.Add(this.tb_setup0);
            this.Controls.Add(this.lb_setup0);
            this.Controls.Add(this.bt_setup1);
            this.Controls.Add(this.tb_setup1);
            this.Controls.Add(this.lb_setup1);
            this.Name = "Form_Setup";
            this.Text = "Form_Setup";
            this.Load += new System.EventHandler(this.Form_Setup_Load);
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox4.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lb_setup1;
        private System.Windows.Forms.TextBox tb_setup1;
        private System.Windows.Forms.Button bt_setup1;
        private System.Windows.Forms.Label lb_setup0;
        private System.Windows.Forms.TextBox tb_setup0;
        private System.Windows.Forms.Button bt_setup0;
        private System.Windows.Forms.Button bt_setup6;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Label lb_main_mesg1;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.Label lb_main_mesg2;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.RadioButton rb_operation_mode2;
        private System.Windows.Forms.RadioButton rb_operation_mode1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rb_use_plc2;
        private System.Windows.Forms.RadioButton rb_use_plc1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton rb_use_ims2;
        private System.Windows.Forms.RadioButton rb_use_ims1;
        private System.Windows.Forms.Panel panel_awb;
        private System.Windows.Forms.Panel panel_data_write;
        private System.Windows.Forms.Panel panel_plc;
        private System.Windows.Forms.Panel panel_ims;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Panel panel_egd_type;
        private System.Windows.Forms.RadioButton rb_egd_type2;
        private System.Windows.Forms.RadioButton rb_egd_type1;
        private System.Windows.Forms.GroupBox groupBox4;
        private System.Windows.Forms.RadioButton rb_language3;
        private System.Windows.Forms.Panel panel_language;
        private System.Windows.Forms.RadioButton rb_language2;
        private System.Windows.Forms.RadioButton rb_language1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button bt_setup7;
        private System.Windows.Forms.Button bt_setup8;
        private System.Windows.Forms.CheckBox cb_auto_start;
    }
}