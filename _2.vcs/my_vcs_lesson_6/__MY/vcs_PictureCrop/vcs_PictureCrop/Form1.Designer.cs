namespace vcs_PictureCrop
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
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.rb_filetype2 = new System.Windows.Forms.RadioButton();
            this.bt_open_folder = new System.Windows.Forms.Button();
            this.rb_filetype1 = new System.Windows.Forms.RadioButton();
            this.button6 = new System.Windows.Forms.Button();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            this.button3 = new System.Windows.Forms.Button();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.bt_clear = new System.Windows.Forms.Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.button0 = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(929, 218);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(300, 100);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.rb_filetype2);
            this.groupBox_selection.Controls.Add(this.bt_open_folder);
            this.groupBox_selection.Controls.Add(this.rb_filetype1);
            this.groupBox_selection.Controls.Add(this.button6);
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Controls.Add(this.button3);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Location = new System.Drawing.Point(929, 12);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(300, 200);
            this.groupBox_selection.TabIndex = 17;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "選取區域";
            // 
            // rb_filetype2
            // 
            this.rb_filetype2.AutoSize = true;
            this.rb_filetype2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_filetype2.Location = new System.Drawing.Point(183, 159);
            this.rb_filetype2.Name = "rb_filetype2";
            this.rb_filetype2.Size = new System.Drawing.Size(54, 20);
            this.rb_filetype2.TabIndex = 21;
            this.rb_filetype2.Text = "bmp";
            this.rb_filetype2.UseVisualStyleBackColor = true;
            // 
            // bt_open_folder
            // 
            this.bt_open_folder.Location = new System.Drawing.Point(240, 137);
            this.bt_open_folder.Name = "bt_open_folder";
            this.bt_open_folder.Size = new System.Drawing.Size(40, 40);
            this.bt_open_folder.TabIndex = 20;
            this.bt_open_folder.UseVisualStyleBackColor = true;
            this.bt_open_folder.Click += new System.EventHandler(this.bt_open_folder_Click);
            // 
            // rb_filetype1
            // 
            this.rb_filetype1.AutoSize = true;
            this.rb_filetype1.Checked = true;
            this.rb_filetype1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.rb_filetype1.Location = new System.Drawing.Point(183, 137);
            this.rb_filetype1.Name = "rb_filetype1";
            this.rb_filetype1.Size = new System.Drawing.Size(46, 20);
            this.rb_filetype1.TabIndex = 20;
            this.rb_filetype1.TabStop = true;
            this.rb_filetype1.Text = "jpg";
            this.rb_filetype1.UseVisualStyleBackColor = true;
            // 
            // button6
            // 
            this.button6.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button6.Location = new System.Drawing.Point(185, 80);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(90, 40);
            this.button6.TabIndex = 6;
            this.button6.Text = "save";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(83, 152);
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
            this.lb_x_st.Location = new System.Drawing.Point(30, 27);
            this.lb_x_st.Name = "lb_x_st";
            this.lb_x_st.Size = new System.Drawing.Size(47, 24);
            this.lb_x_st.TabIndex = 6;
            this.lb_x_st.Text = "x_st";
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(83, 110);
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
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(185, 26);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(90, 40);
            this.button3.TabIndex = 5;
            this.button3.Text = "Info";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // lb_h
            // 
            this.lb_h.AutoSize = true;
            this.lb_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h.Location = new System.Drawing.Point(42, 153);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(21, 24);
            this.lb_h.TabIndex = 12;
            this.lb_h.Text = "h";
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(83, 69);
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
            this.nud_x_st.Location = new System.Drawing.Point(83, 26);
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
            this.lb_y_st.Location = new System.Drawing.Point(30, 69);
            this.lb_y_st.Name = "lb_y_st";
            this.lb_y_st.Size = new System.Drawing.Size(47, 24);
            this.lb_y_st.TabIndex = 8;
            this.lb_y_st.Text = "y_st";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(42, 111);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(26, 24);
            this.lb_w.TabIndex = 10;
            this.lb_w.Text = "w";
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(1169, 238);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(60, 32);
            this.bt_clear.TabIndex = 18;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(131, 12);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 100);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.pictureBox2.TabIndex = 19;
            this.pictureBox2.TabStop = false;
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(833, 12);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(90, 40);
            this.button0.TabIndex = 20;
            this.button0.Text = "test";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // panel1
            // 
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel1.Location = new System.Drawing.Point(12, 118);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(100, 100);
            this.panel1.TabIndex = 21;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1265, 744);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_w;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button bt_open_folder;
        private System.Windows.Forms.RadioButton rb_filetype2;
        private System.Windows.Forms.RadioButton rb_filetype1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Panel panel1;
    }
}

