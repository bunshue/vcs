namespace PlantTextAlignMode
{
    partial class PlantTextAlignMode
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
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.hold = new System.Windows.Forms.Button();
            this.unfold = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.justifyRight = new System.Windows.Forms.Button();
            this.justifyCenter = new System.Windows.Forms.Button();
            this.justifyLeft = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(120, 32);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(41, 12);
            this.label3.TabIndex = 2;
            this.label3.Text = "居中：";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.hold);
            this.groupBox1.Controls.Add(this.unfold);
            this.groupBox1.Controls.Add(this.richTextBox1);
            this.groupBox1.Location = new System.Drawing.Point(7, 5);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(383, 418);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "內容區域";
            // 
            // hold
            // 
            this.hold.Location = new System.Drawing.Point(323, 380);
            this.hold.Name = "hold";
            this.hold.Size = new System.Drawing.Size(53, 23);
            this.hold.TabIndex = 2;
            this.hold.Text = "保存";
            this.hold.UseVisualStyleBackColor = true;
            this.hold.Click += new System.EventHandler(this.hold_Click);
            // 
            // unfold
            // 
            this.unfold.Location = new System.Drawing.Point(249, 380);
            this.unfold.Name = "unfold";
            this.unfold.Size = new System.Drawing.Size(53, 23);
            this.unfold.TabIndex = 1;
            this.unfold.Text = "打開";
            this.unfold.UseVisualStyleBackColor = true;
            this.unfold.Click += new System.EventHandler(this.unfold_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(5, 13);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(371, 348);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            this.richTextBox1.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.justifyRight);
            this.groupBox2.Controls.Add(this.justifyCenter);
            this.groupBox2.Controls.Add(this.justifyLeft);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Location = new System.Drawing.Point(12, 460);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(383, 69);
            this.groupBox2.TabIndex = 3;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "對齊方式";
            // 
            // justifyRight
            // 
            this.justifyRight.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.justifyRight.Location = new System.Drawing.Point(301, 24);
            this.justifyRight.Name = "justifyRight";
            this.justifyRight.Size = new System.Drawing.Size(37, 25);
            this.justifyRight.TabIndex = 6;
            this.justifyRight.UseVisualStyleBackColor = true;
            this.justifyRight.Click += new System.EventHandler(this.justifyRight_Click);
            // 
            // justifyCenter
            // 
            this.justifyCenter.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.justifyCenter.Location = new System.Drawing.Point(184, 24);
            this.justifyCenter.Name = "justifyCenter";
            this.justifyCenter.Size = new System.Drawing.Size(37, 25);
            this.justifyCenter.TabIndex = 5;
            this.justifyCenter.UseVisualStyleBackColor = true;
            this.justifyCenter.Click += new System.EventHandler(this.justifyCenter_Click);
            // 
            // justifyLeft
            // 
            this.justifyLeft.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.justifyLeft.Location = new System.Drawing.Point(68, 24);
            this.justifyLeft.Name = "justifyLeft";
            this.justifyLeft.Size = new System.Drawing.Size(37, 25);
            this.justifyLeft.TabIndex = 4;
            this.justifyLeft.UseVisualStyleBackColor = true;
            this.justifyLeft.Click += new System.EventHandler(this.justifyLeft_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(249, 32);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 12);
            this.label2.TabIndex = 1;
            this.label2.Text = "靠右：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(16, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "靠左：";
            // 
            // PlantTextAlignMode
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(539, 559);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Name = "PlantTextAlignMode";
            this.Text = "設定RichTextBox的文字對齊方式";
            this.Load += new System.EventHandler(this.PlantTextAlignMode_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button hold;
        private System.Windows.Forms.Button unfold;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button justifyLeft;
        private System.Windows.Forms.Button justifyRight;
        private System.Windows.Forms.Button justifyCenter;
    }
}

