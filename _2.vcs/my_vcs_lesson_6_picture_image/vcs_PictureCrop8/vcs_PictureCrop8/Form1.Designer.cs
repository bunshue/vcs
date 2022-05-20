namespace vcs_PictureCrop8
{
    partial class Form1
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的程式碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用程式碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pictureBox3 = new System.Windows.Forms.PictureBox();
            this.button1 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.tb_h = new System.Windows.Forms.TextBox();
            this.tb_w = new System.Windows.Forms.TextBox();
            this.tb_y_st = new System.Windows.Forms.TextBox();
            this.tb_x_st = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox_selection = new System.Windows.Forms.GroupBox();
            this.lb_x_st = new System.Windows.Forms.Label();
            this.nud_x_st = new System.Windows.Forms.NumericUpDown();
            this.lb_h = new System.Windows.Forms.Label();
            this.nud_y_st = new System.Windows.Forms.NumericUpDown();
            this.nud_h = new System.Windows.Forms.NumericUpDown();
            this.lb_y_st = new System.Windows.Forms.Label();
            this.lb_w = new System.Windows.Forms.Label();
            this.nud_w = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox_selection.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(315, 410);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 453);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(467, 251);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // pictureBox2
            // 
            this.pictureBox2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox2.Location = new System.Drawing.Point(333, 12);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(315, 410);
            this.pictureBox2.TabIndex = 3;
            this.pictureBox2.TabStop = false;
            this.pictureBox2.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox2_MouseDown);
            // 
            // pictureBox3
            // 
            this.pictureBox3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox3.Location = new System.Drawing.Point(654, 12);
            this.pictureBox3.Name = "pictureBox3";
            this.pictureBox3.Size = new System.Drawing.Size(315, 410);
            this.pictureBox3.TabIndex = 4;
            this.pictureBox3.TabStop = false;
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(84, 127);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(81, 45);
            this.button1.TabIndex = 5;
            this.button1.Text = "save";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.tb_h);
            this.groupBox1.Controls.Add(this.tb_w);
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.tb_y_st);
            this.groupBox1.Controls.Add(this.tb_x_st);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Location = new System.Drawing.Point(603, 453);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(221, 196);
            this.groupBox1.TabIndex = 7;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "指明部分截取";
            // 
            // tb_h
            // 
            this.tb_h.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_h.Location = new System.Drawing.Point(146, 84);
            this.tb_h.Name = "tb_h";
            this.tb_h.Size = new System.Drawing.Size(61, 30);
            this.tb_h.TabIndex = 10;
            // 
            // tb_w
            // 
            this.tb_w.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_w.Location = new System.Drawing.Point(42, 84);
            this.tb_w.Name = "tb_w";
            this.tb_w.Size = new System.Drawing.Size(61, 30);
            this.tb_w.TabIndex = 9;
            // 
            // tb_y_st
            // 
            this.tb_y_st.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_y_st.Location = new System.Drawing.Point(146, 24);
            this.tb_y_st.Name = "tb_y_st";
            this.tb_y_st.Size = new System.Drawing.Size(61, 30);
            this.tb_y_st.TabIndex = 8;
            // 
            // tb_x_st
            // 
            this.tb_x_st.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.tb_x_st.Location = new System.Drawing.Point(42, 24);
            this.tb_x_st.Name = "tb_x_st";
            this.tb_x_st.Size = new System.Drawing.Size(61, 30);
            this.tb_x_st.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(16, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(130, 16);
            this.label1.TabIndex = 11;
            this.label1.Text = "X                         Y";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(15, 91);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(129, 16);
            this.label2.TabIndex = 12;
            this.label2.Text = "W                        H";
            // 
            // groupBox_selection
            // 
            this.groupBox_selection.Controls.Add(this.lb_x_st);
            this.groupBox_selection.Controls.Add(this.nud_x_st);
            this.groupBox_selection.Controls.Add(this.lb_h);
            this.groupBox_selection.Controls.Add(this.nud_y_st);
            this.groupBox_selection.Controls.Add(this.nud_h);
            this.groupBox_selection.Controls.Add(this.lb_y_st);
            this.groupBox_selection.Controls.Add(this.lb_w);
            this.groupBox_selection.Controls.Add(this.nud_w);
            this.groupBox_selection.Location = new System.Drawing.Point(866, 457);
            this.groupBox_selection.Name = "groupBox_selection";
            this.groupBox_selection.Size = new System.Drawing.Size(230, 192);
            this.groupBox_selection.TabIndex = 15;
            this.groupBox_selection.TabStop = false;
            this.groupBox_selection.Text = "選取區域";
            // 
            // lb_x_st
            // 
            this.lb_x_st.AutoSize = true;
            this.lb_x_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_x_st.Location = new System.Drawing.Point(47, 18);
            this.lb_x_st.Name = "lb_x_st";
            this.lb_x_st.Size = new System.Drawing.Size(47, 24);
            this.lb_x_st.TabIndex = 6;
            this.lb_x_st.Text = "x_st";
            // 
            // nud_x_st
            // 
            this.nud_x_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_x_st.Location = new System.Drawing.Point(97, 16);
            this.nud_x_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_x_st.Name = "nud_x_st";
            this.nud_x_st.Size = new System.Drawing.Size(89, 36);
            this.nud_x_st.TabIndex = 5;
            this.nud_x_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_h
            // 
            this.lb_h.AutoSize = true;
            this.lb_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_h.Location = new System.Drawing.Point(59, 144);
            this.lb_h.Name = "lb_h";
            this.lb_h.Size = new System.Drawing.Size(21, 24);
            this.lb_h.TabIndex = 12;
            this.lb_h.Text = "h";
            // 
            // nud_y_st
            // 
            this.nud_y_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_y_st.Location = new System.Drawing.Point(97, 58);
            this.nud_y_st.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_y_st.Name = "nud_y_st";
            this.nud_y_st.Size = new System.Drawing.Size(89, 36);
            this.nud_y_st.TabIndex = 7;
            this.nud_y_st.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // nud_h
            // 
            this.nud_h.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_h.Location = new System.Drawing.Point(97, 142);
            this.nud_h.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_h.Name = "nud_h";
            this.nud_h.Size = new System.Drawing.Size(89, 36);
            this.nud_h.TabIndex = 11;
            this.nud_h.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // lb_y_st
            // 
            this.lb_y_st.AutoSize = true;
            this.lb_y_st.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_y_st.Location = new System.Drawing.Point(47, 60);
            this.lb_y_st.Name = "lb_y_st";
            this.lb_y_st.Size = new System.Drawing.Size(47, 24);
            this.lb_y_st.TabIndex = 8;
            this.lb_y_st.Text = "y_st";
            // 
            // lb_w
            // 
            this.lb_w.AutoSize = true;
            this.lb_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_w.Location = new System.Drawing.Point(59, 102);
            this.lb_w.Name = "lb_w";
            this.lb_w.Size = new System.Drawing.Size(26, 24);
            this.lb_w.TabIndex = 10;
            this.lb_w.Text = "w";
            // 
            // nud_w
            // 
            this.nud_w.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.nud_w.Location = new System.Drawing.Point(97, 100);
            this.nud_w.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.nud_w.Name = "nud_w";
            this.nud_w.Size = new System.Drawing.Size(89, 36);
            this.nud_w.TabIndex = 9;
            this.nud_w.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1108, 716);
            this.Controls.Add(this.groupBox_selection);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox3);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox1);
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "擷取圖片的一部分複製到新圖框";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox_selection.ResumeLayout(false);
            this.groupBox_selection.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nud_x_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_y_st)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_h)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nud_w)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pictureBox3;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox tb_h;
        private System.Windows.Forms.TextBox tb_w;
        private System.Windows.Forms.TextBox tb_y_st;
        private System.Windows.Forms.TextBox tb_x_st;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox_selection;
        private System.Windows.Forms.Label lb_x_st;
        private System.Windows.Forms.NumericUpDown nud_x_st;
        private System.Windows.Forms.Label lb_h;
        private System.Windows.Forms.NumericUpDown nud_y_st;
        private System.Windows.Forms.NumericUpDown nud_h;
        private System.Windows.Forms.Label lb_y_st;
        private System.Windows.Forms.Label lb_w;
        private System.Windows.Forms.NumericUpDown nud_w;
    }
}

