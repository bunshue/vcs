namespace vcs_Class2
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
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.bt_class04 = new System.Windows.Forms.Button();
            this.bt_class03 = new System.Windows.Forms.Button();
            this.lb_count1 = new System.Windows.Forms.Label();
            this.bt_class02 = new System.Windows.Forms.Button();
            this.bt_class01 = new System.Windows.Forms.Button();
            this.bt_class00 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.lb_count2 = new System.Windows.Forms.Label();
            this.bt_class12 = new System.Windows.Forms.Button();
            this.bt_class11 = new System.Windows.Forms.Button();
            this.bt_class10 = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.bt_class23 = new System.Windows.Forms.Button();
            this.bt_class22 = new System.Windows.Forms.Button();
            this.bt_class21 = new System.Windows.Forms.Button();
            this.bt_class20 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(441, 155);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(72, 36);
            this.bt_clear.TabIndex = 131;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.richTextBox1.Location = new System.Drawing.Point(421, 121);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 122;
            this.richTextBox1.Text = "";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.bt_class04);
            this.groupBox1.Controls.Add(this.bt_class03);
            this.groupBox1.Controls.Add(this.lb_count1);
            this.groupBox1.Controls.Add(this.bt_class02);
            this.groupBox1.Controls.Add(this.bt_class01);
            this.groupBox1.Controls.Add(this.bt_class00);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(200, 366);
            this.groupBox1.TabIndex = 156;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "人員管理";
            // 
            // bt_class04
            // 
            this.bt_class04.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class04.Location = new System.Drawing.Point(14, 291);
            this.bt_class04.Name = "bt_class04";
            this.bt_class04.Size = new System.Drawing.Size(180, 60);
            this.bt_class04.TabIndex = 19;
            this.bt_class04.Text = "匯入";
            this.bt_class04.UseVisualStyleBackColor = true;
            this.bt_class04.Click += new System.EventHandler(this.bt_class04_Click);
            // 
            // bt_class03
            // 
            this.bt_class03.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class03.Location = new System.Drawing.Point(14, 236);
            this.bt_class03.Name = "bt_class03";
            this.bt_class03.Size = new System.Drawing.Size(180, 60);
            this.bt_class03.TabIndex = 18;
            this.bt_class03.Text = "儲存";
            this.bt_class03.UseVisualStyleBackColor = true;
            this.bt_class03.Click += new System.EventHandler(this.bt_class03_Click);
            // 
            // lb_count1
            // 
            this.lb_count1.AutoSize = true;
            this.lb_count1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_count1.Location = new System.Drawing.Point(18, 18);
            this.lb_count1.Name = "lb_count1";
            this.lb_count1.Size = new System.Drawing.Size(37, 24);
            this.lb_count1.TabIndex = 17;
            this.lb_count1.Text = "cnt";
            // 
            // bt_class02
            // 
            this.bt_class02.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class02.Location = new System.Drawing.Point(14, 178);
            this.bt_class02.Name = "bt_class02";
            this.bt_class02.Size = new System.Drawing.Size(180, 60);
            this.bt_class02.TabIndex = 16;
            this.bt_class02.Text = "info";
            this.bt_class02.UseVisualStyleBackColor = true;
            this.bt_class02.Click += new System.EventHandler(this.bt_class02_Click);
            // 
            // bt_class01
            // 
            this.bt_class01.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class01.Location = new System.Drawing.Point(14, 119);
            this.bt_class01.Name = "bt_class01";
            this.bt_class01.Size = new System.Drawing.Size(180, 60);
            this.bt_class01.TabIndex = 15;
            this.bt_class01.Text = "新增學生資料";
            this.bt_class01.UseVisualStyleBackColor = true;
            this.bt_class01.Click += new System.EventHandler(this.bt_class01_Click);
            // 
            // bt_class00
            // 
            this.bt_class00.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class00.Location = new System.Drawing.Point(14, 63);
            this.bt_class00.Name = "bt_class00";
            this.bt_class00.Size = new System.Drawing.Size(180, 60);
            this.bt_class00.TabIndex = 14;
            this.bt_class00.Text = "新增老師資料";
            this.bt_class00.UseVisualStyleBackColor = true;
            this.bt_class00.Click += new System.EventHandler(this.bt_class00_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.lb_count2);
            this.groupBox2.Controls.Add(this.bt_class12);
            this.groupBox2.Controls.Add(this.bt_class11);
            this.groupBox2.Controls.Add(this.bt_class10);
            this.groupBox2.Location = new System.Drawing.Point(218, 14);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(200, 366);
            this.groupBox2.TabIndex = 157;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "圖形管理";
            // 
            // lb_count2
            // 
            this.lb_count2.AutoSize = true;
            this.lb_count2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_count2.Location = new System.Drawing.Point(18, 18);
            this.lb_count2.Name = "lb_count2";
            this.lb_count2.Size = new System.Drawing.Size(37, 24);
            this.lb_count2.TabIndex = 17;
            this.lb_count2.Text = "cnt";
            // 
            // bt_class12
            // 
            this.bt_class12.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class12.Location = new System.Drawing.Point(14, 178);
            this.bt_class12.Name = "bt_class12";
            this.bt_class12.Size = new System.Drawing.Size(180, 60);
            this.bt_class12.TabIndex = 16;
            this.bt_class12.Text = "info";
            this.bt_class12.UseVisualStyleBackColor = true;
            this.bt_class12.Click += new System.EventHandler(this.bt_class12_Click);
            // 
            // bt_class11
            // 
            this.bt_class11.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class11.Location = new System.Drawing.Point(14, 119);
            this.bt_class11.Name = "bt_class11";
            this.bt_class11.Size = new System.Drawing.Size(180, 60);
            this.bt_class11.TabIndex = 15;
            this.bt_class11.Text = "新增矩形";
            this.bt_class11.UseVisualStyleBackColor = true;
            this.bt_class11.Click += new System.EventHandler(this.bt_class11_Click);
            // 
            // bt_class10
            // 
            this.bt_class10.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class10.Location = new System.Drawing.Point(14, 63);
            this.bt_class10.Name = "bt_class10";
            this.bt_class10.Size = new System.Drawing.Size(180, 60);
            this.bt_class10.TabIndex = 14;
            this.bt_class10.Text = "新增三角形";
            this.bt_class10.UseVisualStyleBackColor = true;
            this.bt_class10.Click += new System.EventHandler(this.bt_class10_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pictureBox1.Location = new System.Drawing.Point(424, 14);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 158;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // bt_class23
            // 
            this.bt_class23.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class23.Location = new System.Drawing.Point(424, 358);
            this.bt_class23.Name = "bt_class23";
            this.bt_class23.Size = new System.Drawing.Size(100, 36);
            this.bt_class23.TabIndex = 162;
            this.bt_class23.Text = "info";
            this.bt_class23.UseVisualStyleBackColor = true;
            this.bt_class23.Click += new System.EventHandler(this.bt_class23_Click);
            // 
            // bt_class22
            // 
            this.bt_class22.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class22.Location = new System.Drawing.Point(424, 316);
            this.bt_class22.Name = "bt_class22";
            this.bt_class22.Size = new System.Drawing.Size(100, 36);
            this.bt_class22.TabIndex = 161;
            this.bt_class22.Text = "加入藍球";
            this.bt_class22.UseVisualStyleBackColor = true;
            this.bt_class22.Click += new System.EventHandler(this.bt_class22_Click);
            // 
            // bt_class21
            // 
            this.bt_class21.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class21.Location = new System.Drawing.Point(424, 278);
            this.bt_class21.Name = "bt_class21";
            this.bt_class21.Size = new System.Drawing.Size(100, 36);
            this.bt_class21.TabIndex = 160;
            this.bt_class21.Tag = "";
            this.bt_class21.Text = "加入綠球";
            this.bt_class21.UseVisualStyleBackColor = true;
            this.bt_class21.Click += new System.EventHandler(this.bt_class21_Click);
            // 
            // bt_class20
            // 
            this.bt_class20.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_class20.Location = new System.Drawing.Point(424, 236);
            this.bt_class20.Name = "bt_class20";
            this.bt_class20.Size = new System.Drawing.Size(100, 36);
            this.bt_class20.TabIndex = 159;
            this.bt_class20.Tag = "";
            this.bt_class20.Text = "加入紅球";
            this.bt_class20.UseVisualStyleBackColor = true;
            this.bt_class20.Click += new System.EventHandler(this.bt_class20_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(774, 581);
            this.Controls.Add(this.bt_class23);
            this.Controls.Add(this.bt_class22);
            this.Controls.Add(this.bt_class21);
            this.Controls.Add(this.bt_class20);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button bt_class04;
        private System.Windows.Forms.Button bt_class03;
        private System.Windows.Forms.Label lb_count1;
        private System.Windows.Forms.Button bt_class02;
        private System.Windows.Forms.Button bt_class01;
        private System.Windows.Forms.Button bt_class00;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label lb_count2;
        private System.Windows.Forms.Button bt_class12;
        private System.Windows.Forms.Button bt_class11;
        private System.Windows.Forms.Button bt_class10;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Button bt_class23;
        private System.Windows.Forms.Button bt_class22;
        private System.Windows.Forms.Button bt_class21;
        private System.Windows.Forms.Button bt_class20;
    }
}

