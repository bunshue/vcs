namespace BetrayRTFDocument
{
    partial class BetrayRTFDocument
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.unwrap = new System.Windows.Forms.Button();
            this.openRTFImplement = new System.Windows.Forms.OpenFileDialog();
            this.kept = new System.Windows.Forms.Button();
            this.saveRTFImplement = new System.Windows.Forms.SaveFileDialog();
            this.liquidate = new System.Windows.Forms.Button();
            this.Exit = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(3, 13);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(306, 223);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            this.richTextBox1.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // unwrap
            // 
            this.unwrap.Location = new System.Drawing.Point(54, 20);
            this.unwrap.Name = "unwrap";
            this.unwrap.Size = new System.Drawing.Size(48, 29);
            this.unwrap.TabIndex = 1;
            this.unwrap.Text = "打開";
            this.unwrap.UseVisualStyleBackColor = true;
            this.unwrap.Click += new System.EventHandler(this.unwrap_Click);
            // 
            // openRTFImplement
            // 
            this.openRTFImplement.FileName = "openFileDialog1";
            // 
            // kept
            // 
            this.kept.Enabled = false;
            this.kept.Location = new System.Drawing.Point(54, 60);
            this.kept.Name = "kept";
            this.kept.Size = new System.Drawing.Size(48, 29);
            this.kept.TabIndex = 2;
            this.kept.Text = "保存";
            this.kept.UseVisualStyleBackColor = true;
            this.kept.Click += new System.EventHandler(this.kept_Click);
            // 
            // liquidate
            // 
            this.liquidate.Location = new System.Drawing.Point(191, 20);
            this.liquidate.Name = "liquidate";
            this.liquidate.Size = new System.Drawing.Size(48, 29);
            this.liquidate.TabIndex = 3;
            this.liquidate.Text = "清空";
            this.liquidate.UseVisualStyleBackColor = true;
            this.liquidate.Click += new System.EventHandler(this.liquidate_Click);
            // 
            // Exit
            // 
            this.Exit.Location = new System.Drawing.Point(191, 60);
            this.Exit.Name = "Exit";
            this.Exit.Size = new System.Drawing.Size(48, 29);
            this.Exit.TabIndex = 4;
            this.Exit.Text = "退出";
            this.Exit.UseVisualStyleBackColor = true;
            this.Exit.Click += new System.EventHandler(this.Exit_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.unwrap);
            this.groupBox1.Controls.Add(this.Exit);
            this.groupBox1.Controls.Add(this.liquidate);
            this.groupBox1.Controls.Add(this.kept);
            this.groupBox1.Location = new System.Drawing.Point(5, 250);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(313, 101);
            this.groupBox1.TabIndex = 5;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "操作區域";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.richTextBox1);
            this.groupBox2.Location = new System.Drawing.Point(5, 1);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(313, 241);
            this.groupBox2.TabIndex = 6;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "文字內容";
            // 
            // BetrayRTFDocument
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(323, 356);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "BetrayRTFDocument";
            this.Text = "在RichTextBox中顯示RTF格式文件";
            this.Load += new System.EventHandler(this.BetrayRTFDocument_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button unwrap;
        private System.Windows.Forms.OpenFileDialog openRTFImplement;
        private System.Windows.Forms.Button kept;
        private System.Windows.Forms.SaveFileDialog saveRTFImplement;
        private System.Windows.Forms.Button liquidate;
        private System.Windows.Forms.Button Exit;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
    }
}

