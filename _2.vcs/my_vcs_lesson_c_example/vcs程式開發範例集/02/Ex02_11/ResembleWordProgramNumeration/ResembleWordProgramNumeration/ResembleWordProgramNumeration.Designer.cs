namespace ResembleWordProgramNumeration
{
    partial class ResembleWordProgramNumeration
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
            if(disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.hold = new System.Windows.Forms.Button();
            this.unfold = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.figuresNumeration = new System.Windows.Forms.Button();
            this.programNumeration = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.hold);
            this.groupBox1.Controls.Add(this.unfold);
            this.groupBox1.Location = new System.Drawing.Point(7, 3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(383, 234);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "內容區域";
            this.groupBox1.Enter += new System.EventHandler(this.groupBox1_Enter);
            // 
            // hold
            // 
            this.hold.Location = new System.Drawing.Point(323, 205);
            this.hold.Name = "hold";
            this.hold.Size = new System.Drawing.Size(53, 23);
            this.hold.TabIndex = 2;
            this.hold.Text = "保存";
            this.hold.UseVisualStyleBackColor = true;
            this.hold.Click += new System.EventHandler(this.hold_Click);
            // 
            // unfold
            // 
            this.unfold.Location = new System.Drawing.Point(249, 205);
            this.unfold.Name = "unfold";
            this.unfold.Size = new System.Drawing.Size(53, 23);
            this.unfold.TabIndex = 1;
            this.unfold.Text = "打開";
            this.unfold.UseVisualStyleBackColor = true;
            this.unfold.Click += new System.EventHandler(this.unfold_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.figuresNumeration);
            this.groupBox2.Controls.Add(this.programNumeration);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Location = new System.Drawing.Point(7, 243);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(383, 69);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "項目符號和編號";
            // 
            // figuresNumeration
            // 
            this.figuresNumeration.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.figuresNumeration.Image = global::ResembleWordProgramNumeration.Properties.Resources.数字编号;
            this.figuresNumeration.Location = new System.Drawing.Point(252, 17);
            this.figuresNumeration.Name = "figuresNumeration";
            this.figuresNumeration.Size = new System.Drawing.Size(52, 38);
            this.figuresNumeration.TabIndex = 5;
            this.figuresNumeration.UseVisualStyleBackColor = true;
            this.figuresNumeration.Click += new System.EventHandler(this.figuresNumeration_Click);
            // 
            // programNumeration
            // 
            this.programNumeration.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.programNumeration.Image = global::ResembleWordProgramNumeration.Properties.Resources.项目编号;
            this.programNumeration.Location = new System.Drawing.Point(87, 17);
            this.programNumeration.Name = "programNumeration";
            this.programNumeration.Size = new System.Drawing.Size(52, 38);
            this.programNumeration.TabIndex = 4;
            this.programNumeration.UseVisualStyleBackColor = true;
            this.programNumeration.Click += new System.EventHandler(this.programNumeration_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(181, 32);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "數字編號：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "項目符號：";
            // 
            // ResembleWordProgramNumeration
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(396, 319);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "ResembleWordProgramNumeration";
            this.Text = "在RichTextBox中完成項目符號功能";
            this.Load += new System.EventHandler(this.ResembleWordProgramNumeration_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button hold;
        private System.Windows.Forms.Button unfold;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button figuresNumeration;
        private System.Windows.Forms.Button programNumeration;
    }
}

