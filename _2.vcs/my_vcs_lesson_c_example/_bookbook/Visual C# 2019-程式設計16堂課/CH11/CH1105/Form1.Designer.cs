namespace CH1105
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
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.rabSpecial = new System.Windows.Forms.RadioButton();
            this.rabNormal = new System.Windows.Forms.RadioButton();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.rabThree = new System.Windows.Forms.RadioButton();
            this.rabTwo = new System.Windows.Forms.RadioButton();
            this.rabOne = new System.Windows.Forms.RadioButton();
            this.btnInfo = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.lblTotal = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.rabSpecial);
            this.groupBox1.Controls.Add(this.rabNormal);
            this.groupBox1.Location = new System.Drawing.Point(14, 37);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(158, 76);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "選擇車票種類";
            this.groupBox1.MouseCaptureChanged += new System.EventHandler(this.rabTicket_CheckedChanged);
            // 
            // rabSpecial
            // 
            this.rabSpecial.AutoSize = true;
            this.rabSpecial.Location = new System.Drawing.Point(82, 31);
            this.rabSpecial.Name = "rabSpecial";
            this.rabSpecial.Size = new System.Drawing.Size(47, 16);
            this.rabSpecial.TabIndex = 1;
            this.rabSpecial.TabStop = true;
            this.rabSpecial.Text = "商務";
            this.rabSpecial.UseVisualStyleBackColor = true;
            this.rabSpecial.CheckedChanged += new System.EventHandler(this.rabTicket_CheckedChanged);
            // 
            // rabNormal
            // 
            this.rabNormal.AutoSize = true;
            this.rabNormal.Location = new System.Drawing.Point(13, 31);
            this.rabNormal.Name = "rabNormal";
            this.rabNormal.Size = new System.Drawing.Size(47, 16);
            this.rabNormal.TabIndex = 0;
            this.rabNormal.TabStop = true;
            this.rabNormal.Text = "一般";
            this.rabNormal.UseVisualStyleBackColor = true;
            this.rabNormal.CheckedChanged += new System.EventHandler(this.rabTicket_CheckedChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.rabThree);
            this.groupBox2.Controls.Add(this.rabTwo);
            this.groupBox2.Controls.Add(this.rabOne);
            this.groupBox2.Location = new System.Drawing.Point(174, 38);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(177, 78);
            this.groupBox2.TabIndex = 7;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "購票資訊(限3張)";
            this.groupBox2.MouseCaptureChanged += new System.EventHandler(this.rabVarious_CheckedChanged);
            // 
            // rabThree
            // 
            this.rabThree.Appearance = System.Windows.Forms.Appearance.Button;
            this.rabThree.AutoSize = true;
            this.rabThree.Location = new System.Drawing.Point(114, 30);
            this.rabThree.Name = "rabThree";
            this.rabThree.Size = new System.Drawing.Size(33, 22);
            this.rabThree.TabIndex = 2;
            this.rabThree.TabStop = true;
            this.rabThree.Text = "3張";
            this.rabThree.UseVisualStyleBackColor = true;
            this.rabThree.CheckedChanged += new System.EventHandler(this.rabVarious_CheckedChanged);
            // 
            // rabTwo
            // 
            this.rabTwo.Appearance = System.Windows.Forms.Appearance.Button;
            this.rabTwo.AutoSize = true;
            this.rabTwo.Location = new System.Drawing.Point(60, 30);
            this.rabTwo.Name = "rabTwo";
            this.rabTwo.Size = new System.Drawing.Size(33, 22);
            this.rabTwo.TabIndex = 1;
            this.rabTwo.TabStop = true;
            this.rabTwo.Text = "2張";
            this.rabTwo.UseVisualStyleBackColor = true;
            this.rabTwo.CheckedChanged += new System.EventHandler(this.rabVarious_CheckedChanged);
            // 
            // rabOne
            // 
            this.rabOne.Appearance = System.Windows.Forms.Appearance.Button;
            this.rabOne.AutoSize = true;
            this.rabOne.Location = new System.Drawing.Point(6, 30);
            this.rabOne.Name = "rabOne";
            this.rabOne.Size = new System.Drawing.Size(33, 22);
            this.rabOne.TabIndex = 0;
            this.rabOne.TabStop = true;
            this.rabOne.Text = "1張";
            this.rabOne.UseVisualStyleBackColor = true;
            this.rabOne.CheckedChanged += new System.EventHandler(this.rabVarious_CheckedChanged);
            // 
            // btnInfo
            // 
            this.btnInfo.Location = new System.Drawing.Point(268, 117);
            this.btnInfo.Name = "btnInfo";
            this.btnInfo.Size = new System.Drawing.Size(75, 32);
            this.btnInfo.TabIndex = 11;
            this.btnInfo.Text = "計算";
            this.btnInfo.UseVisualStyleBackColor = true;
            this.btnInfo.Click += new System.EventHandler(this.btnInfo_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("微軟正黑體", 11.8209F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.ForeColor = System.Drawing.Color.Blue;
            this.label2.Location = new System.Drawing.Point(91, 6);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(105, 20);
            this.label2.TabIndex = 10;
            this.label2.Text = "高鐵購票系統";
            // 
            // lblTotal
            // 
            this.lblTotal.AutoSize = true;
            this.lblTotal.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(224)))), ((int)(((byte)(192)))));
            this.lblTotal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblTotal.Location = new System.Drawing.Point(111, 122);
            this.lblTotal.Name = "lblTotal";
            this.lblTotal.Size = new System.Drawing.Size(35, 14);
            this.lblTotal.TabIndex = 9;
            this.lblTotal.Text = "label2";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(24, 122);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 8;
            this.label1.Text = "總票價：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(363, 171);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.btnInfo);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.lblTotal);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "CH1105";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton rabSpecial;
        private System.Windows.Forms.RadioButton rabNormal;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton rabThree;
        private System.Windows.Forms.RadioButton rabTwo;
        private System.Windows.Forms.RadioButton rabOne;
        private System.Windows.Forms.Button btnInfo;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label lblTotal;
        private System.Windows.Forms.Label label1;
    }
}

