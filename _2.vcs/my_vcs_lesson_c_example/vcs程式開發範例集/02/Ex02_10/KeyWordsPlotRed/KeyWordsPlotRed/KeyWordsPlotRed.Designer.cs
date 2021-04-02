namespace KeyWordsPlotRed
{
    partial class KeyWordsPlotRed
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
            this.unfold = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.plotRed = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.keyWord = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.unfold);
            this.groupBox1.Controls.Add(this.richTextBox1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(309, 196);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "內容區域";
            // 
            // unfold
            // 
            this.unfold.Location = new System.Drawing.Point(253, 167);
            this.unfold.Name = "unfold";
            this.unfold.Size = new System.Drawing.Size(45, 23);
            this.unfold.TabIndex = 3;
            this.unfold.Text = "打開";
            this.unfold.UseVisualStyleBackColor = true;
            this.unfold.Click += new System.EventHandler(this.unfold_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(5, 14);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(299, 148);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.plotRed);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Controls.Add(this.keyWord);
            this.groupBox2.Location = new System.Drawing.Point(13, 214);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(308, 78);
            this.groupBox2.TabIndex = 0;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "操作區域";
            // 
            // plotRed
            // 
            this.plotRed.Location = new System.Drawing.Point(252, 31);
            this.plotRed.Name = "plotRed";
            this.plotRed.Size = new System.Drawing.Size(45, 23);
            this.plotRed.TabIndex = 2;
            this.plotRed.Text = "描紅";
            this.plotRed.UseVisualStyleBackColor = true;
            this.plotRed.Click += new System.EventHandler(this.plotRed_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(3, 35);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "關鍵字：";
            // 
            // keyWord
            // 
            this.keyWord.Location = new System.Drawing.Point(59, 31);
            this.keyWord.Name = "keyWord";
            this.keyWord.Size = new System.Drawing.Size(183, 22);
            this.keyWord.TabIndex = 0;
            this.keyWord.TextChanged += new System.EventHandler(this.keyWord_TextChanged);
            // 
            // KeyWordsPlotRed
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(333, 304);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "KeyWordsPlotRed";
            this.Text = "在RichTextBox中完成關鍵字描紅";
            this.Load += new System.EventHandler(this.KeyWordsPlotRed_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button plotRed;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox keyWord;
        private System.Windows.Forms.Button unfold;
    }
}

