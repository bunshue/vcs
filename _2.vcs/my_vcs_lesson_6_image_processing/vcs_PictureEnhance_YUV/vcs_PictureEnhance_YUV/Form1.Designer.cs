namespace vcs_PictureEnhance_YUV
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
            this.components = new System.ComponentModel.Container();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.pictureBox3a = new System.Windows.Forms.PictureBox();
            this.button5 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.pictureBox4 = new System.Windows.Forms.PictureBox();
            this.button6 = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.pictureBox3b = new System.Windows.Forms.PictureBox();
            this.button8 = new System.Windows.Forms.Button();
            this.button0 = new System.Windows.Forms.Button();
            this.button9 = new System.Windows.Forms.Button();
            this.button10 = new System.Windows.Forms.Button();
            this.cb_magnify = new System.Windows.Forms.CheckBox();
            this.timer_rgb = new System.Windows.Forms.Timer(this.components);
            this.lb_brightness = new System.Windows.Forms.Label();
            this.button11 = new System.Windows.Forms.Button();
            this.cb_modify = new System.Windows.Forms.CheckBox();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.bt_apply = new System.Windows.Forms.Button();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.timer_enhancement = new System.Windows.Forms.Timer(this.components);
            this.button12 = new System.Windows.Forms.Button();
            this.button13 = new System.Windows.Forms.Button();
            this.button14 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3a)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3b)).BeginInit();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(10, 120);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.TabIndex = 7;
            this.pictureBox2.TabStop = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(10, 10);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(506, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 5;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(239, 100);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(100, 32);
            this.button1.TabIndex = 8;
            this.button1.Text = "跳點量測亮度";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(239, 145);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(100, 32);
            this.button2.TabIndex = 9;
            this.button2.Text = "影像加強";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(240, 191);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(100, 32);
            this.button3.TabIndex = 10;
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(240, 237);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(100, 32);
            this.button4.TabIndex = 11;
            this.button4.Text = "測試";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // pictureBox3a
            // 
            this.pictureBox3a.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox3a.Location = new System.Drawing.Point(120, 10);
            this.pictureBox3a.Name = "pictureBox3a";
            this.pictureBox3a.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3a.TabIndex = 12;
            this.pictureBox3a.TabStop = false;
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(240, 283);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(100, 32);
            this.button5.TabIndex = 13;
            this.button5.Text = "全圖";
            this.button5.UseVisualStyleBackColor = true;
            this.button5.Click += new System.EventHandler(this.button5_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(612, 12);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 14;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // pictureBox4
            // 
            this.pictureBox4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox4.Location = new System.Drawing.Point(120, 230);
            this.pictureBox4.Name = "pictureBox4";
            this.pictureBox4.Size = new System.Drawing.Size(100, 100);
            this.pictureBox4.TabIndex = 15;
            this.pictureBox4.TabStop = false;
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(240, 329);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(100, 32);
            this.button6.TabIndex = 16;
            this.button6.Text = "影像加強 + 亮度分布";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(240, 375);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(100, 32);
            this.button7.TabIndex = 18;
            this.button7.Text = "影像加強 + 亮度分布";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // pictureBox3b
            // 
            this.pictureBox3b.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox3b.Location = new System.Drawing.Point(120, 120);
            this.pictureBox3b.Name = "pictureBox3b";
            this.pictureBox3b.Size = new System.Drawing.Size(100, 100);
            this.pictureBox3b.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox3b.TabIndex = 19;
            this.pictureBox3b.TabStop = false;
            // 
            // button8
            // 
            this.button8.Location = new System.Drawing.Point(341, 56);
            this.button8.Name = "button8";
            this.button8.Size = new System.Drawing.Size(100, 32);
            this.button8.TabIndex = 20;
            this.button8.Text = "info";
            this.button8.UseVisualStyleBackColor = true;
            this.button8.Click += new System.EventHandler(this.button8_Click);
            // 
            // button0
            // 
            this.button0.Location = new System.Drawing.Point(240, 56);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(100, 32);
            this.button0.TabIndex = 21;
            this.button0.Text = "Reset";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button9
            // 
            this.button9.Location = new System.Drawing.Point(341, 100);
            this.button9.Name = "button9";
            this.button9.Size = new System.Drawing.Size(100, 32);
            this.button9.TabIndex = 22;
            this.button9.Text = "2D plot 黑白";
            this.button9.UseVisualStyleBackColor = true;
            this.button9.Click += new System.EventHandler(this.button9_Click);
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(341, 145);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(100, 32);
            this.button10.TabIndex = 23;
            this.button10.Text = "2D plot 彩色";
            this.button10.UseVisualStyleBackColor = true;
            this.button10.Click += new System.EventHandler(this.button10_Click);
            // 
            // cb_magnify
            // 
            this.cb_magnify.AutoSize = true;
            this.cb_magnify.Location = new System.Drawing.Point(351, 22);
            this.cb_magnify.Name = "cb_magnify";
            this.cb_magnify.Size = new System.Drawing.Size(60, 16);
            this.cb_magnify.TabIndex = 24;
            this.cb_magnify.Text = "放大鏡";
            this.cb_magnify.UseVisualStyleBackColor = true;
            // 
            // timer_rgb
            // 
            this.timer_rgb.Enabled = true;
            this.timer_rgb.Tick += new System.EventHandler(this.timer_rgb_Tick);
            // 
            // lb_brightness
            // 
            this.lb_brightness.AutoSize = true;
            this.lb_brightness.Font = new System.Drawing.Font("Consolas", 27.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lb_brightness.ForeColor = System.Drawing.Color.Gold;
            this.lb_brightness.Location = new System.Drawing.Point(242, 10);
            this.lb_brightness.Name = "lb_brightness";
            this.lb_brightness.Size = new System.Drawing.Size(39, 43);
            this.lb_brightness.TabIndex = 203;
            this.lb_brightness.Text = "Y";
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(341, 191);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(100, 32);
            this.button11.TabIndex = 204;
            this.button11.Text = "2D plot test";
            this.button11.UseVisualStyleBackColor = true;
            this.button11.Click += new System.EventHandler(this.button11_Click);
            // 
            // cb_modify
            // 
            this.cb_modify.AutoSize = true;
            this.cb_modify.Checked = true;
            this.cb_modify.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cb_modify.Location = new System.Drawing.Point(351, 37);
            this.cb_modify.Name = "cb_modify";
            this.cb_modify.Size = new System.Drawing.Size(48, 16);
            this.cb_modify.TabIndex = 205;
            this.cb_modify.Text = "調整";
            this.cb_modify.UseVisualStyleBackColor = true;
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.bt_apply);
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Location = new System.Drawing.Point(506, 131);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(582, 76);
            this.groupBox_selection.TabIndex = 206;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "選取區域";
            // 
            // bt_apply
            // 
            this.bt_apply.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_apply.Location = new System.Drawing.Point(433, 13);
            this.bt_apply.Name = "bt_apply";
            this.bt_apply.Size = new System.Drawing.Size(68, 40);
            this.bt_apply.TabIndex = 6;
            this.bt_apply.Text = "加強";
            this.bt_apply.UseVisualStyleBackColor = true;
            this.bt_apply.Click += new System.EventHandler(this.bt_apply_Click);
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(344, 14);
            this.nud_h.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_h.Name = "nud_h";
            this.nud_h.Size = new System.Drawing.Size(74, 33);
            this.nud_h.TabIndex = 16;
            this.nud_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_x_st
            // 
            this.lb_x_st.AutoSize = true;
            this.lb_x_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_x_st.Location = new System.Drawing.Point(12, 18);
            this.lb_x_st.Name = "lb_x_st";
            this.lb_x_st.Size = new System.Drawing.Size(21, 24);
            this.lb_x_st.TabIndex = 6;
            this.lb_x_st.Text = "x";
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(248, 14);
            this.nud_w.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_w.Name = "nud_w";
            this.nud_w.Size = new System.Drawing.Size(74, 33);
            this.nud_w.TabIndex = 15;
            this.nud_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_h
            // 
            this.lb_h.AutoSize = true;
            this.lb_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h.Location = new System.Drawing.Point(328, 19);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(21, 24);
            this.lb_h.TabIndex = 12;
            this.lb_h.Text = "h";
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(146, 18);
            this.nud_y_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_y_st.Name = "nud_y_st";
            this.nud_y_st.Size = new System.Drawing.Size(74, 33);
            this.nud_y_st.TabIndex = 14;
            this.nud_y_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // nud_x_st
            // 
            this.nud_x_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_x_st.Location = new System.Drawing.Point(39, 19);
            this.nud_x_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_x_st.Name = "nud_x_st";
            this.nud_x_st.Size = new System.Drawing.Size(74, 33);
            this.nud_x_st.TabIndex = 13;
            this.nud_x_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_y_st
            // 
            this.lb_y_st.AutoSize = true;
            this.lb_y_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_y_st.Location = new System.Drawing.Point(119, 18);
            this.lb_y_st.Name = "lb_y_st";
            this.lb_y_st.Size = new System.Drawing.Size(21, 24);
            this.lb_y_st.TabIndex = 8;
            this.lb_y_st.Text = "y";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(226, 19);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(26, 24);
            this.lb_w.TabIndex = 10;
            this.lb_w.Text = "w";
            // 
            // timer_enhancement
            // 
            this.timer_enhancement.Enabled = true;
            this.timer_enhancement.Tick += new System.EventHandler(this.timer_enhancement_Tick);
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(341, 237);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(100, 32);
            this.button12.TabIndex = 207;
            this.button12.Text = "save";
            this.button12.UseVisualStyleBackColor = true;
            this.button12.Click += new System.EventHandler(this.button12_Click);
            // 
            // button13
            // 
            this.button13.Location = new System.Drawing.Point(341, 283);
            this.button13.Name = "button13";
            this.button13.Size = new System.Drawing.Size(100, 32);
            this.button13.TabIndex = 208;
            this.button13.Text = "test";
            this.button13.UseVisualStyleBackColor = true;
            this.button13.Click += new System.EventHandler(this.button13_Click);
            // 
            // button14
            // 
            this.button14.Location = new System.Drawing.Point(341, 329);
            this.button14.Name = "button14";
            this.button14.Size = new System.Drawing.Size(100, 32);
            this.button14.TabIndex = 209;
            this.button14.Text = "test";
            this.button14.UseVisualStyleBackColor = true;
            this.button14.Click += new System.EventHandler(this.button14_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1173, 461);
            this.Controls.Add(this.button14);
            this.Controls.Add(this.button13);
            this.Controls.Add(this.button12);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.cb_modify);
            this.Controls.Add(this.button11);
            this.Controls.Add(this.lb_brightness);
            this.Controls.Add(this.cb_magnify);
            this.Controls.Add(this.button10);
            this.Controls.Add(this.button9);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button8);
            this.Controls.Add(this.pictureBox3b);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.pictureBox4);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.pictureBox3a);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form1_FormClosed);
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3a)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox4)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3b)).EndInit();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.PictureBox pictureBox3a;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.PictureBox pictureBox4;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button button7;
        private System.Windows.Forms.PictureBox pictureBox3b;
        private System.Windows.Forms.Button button8;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button9;
        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.CheckBox cb_magnify;
        private System.Windows.Forms.Timer timer_rgb;
        private System.Windows.Forms.Label lb_brightness;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.CheckBox cb_modify;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.Button bt_apply;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.Timer timer_enhancement;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.Button button13;
        private System.Windows.Forms.Button button14;
    }
}

