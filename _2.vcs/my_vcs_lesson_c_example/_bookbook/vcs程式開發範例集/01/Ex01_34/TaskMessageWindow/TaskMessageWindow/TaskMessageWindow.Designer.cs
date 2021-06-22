namespace TaskMessageWindow
{
    partial class TaskMessageWindow
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
            this.label1 = new System.Windows.Forms.Label();
            this.content = new System.Windows.Forms.RichTextBox();
            this.informButton = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.title = new System.Windows.Forms.TextBox();
            this.closeButton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(5, 46);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "通知內容：";
            // 
            // content
            // 
            this.content.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.content.Location = new System.Drawing.Point(76, 46);
            this.content.Name = "content";
            this.content.Size = new System.Drawing.Size(250, 178);
            this.content.TabIndex = 1;
            this.content.Text = "hhh";
            this.content.TextChanged += new System.EventHandler(this.content_TextChanged);
            // 
            // informButton
            // 
            this.informButton.Location = new System.Drawing.Point(218, 235);
            this.informButton.Name = "informButton";
            this.informButton.Size = new System.Drawing.Size(45, 23);
            this.informButton.TabIndex = 2;
            this.informButton.Text = "通知";
            this.informButton.UseVisualStyleBackColor = true;
            this.informButton.Click += new System.EventHandler(this.informButton_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(5, 19);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 0;
            this.label2.Text = "通知標題：";
            // 
            // title
            // 
            this.title.Location = new System.Drawing.Point(76, 16);
            this.title.MaxLength = 7;
            this.title.Name = "title";
            this.title.Size = new System.Drawing.Size(114, 22);
            this.title.TabIndex = 0;
            this.title.Text = "david";
            this.title.TextChanged += new System.EventHandler(this.title_TextChanged);
            // 
            // closeButton
            // 
            this.closeButton.Location = new System.Drawing.Point(279, 235);
            this.closeButton.Name = "closeButton";
            this.closeButton.Size = new System.Drawing.Size(45, 23);
            this.closeButton.TabIndex = 3;
            this.closeButton.Text = "關閉";
            this.closeButton.UseVisualStyleBackColor = true;
            this.closeButton.Click += new System.EventHandler(this.closeInform_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(197, 19);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(131, 12);
            this.label3.TabIndex = 5;
            this.label3.Text = "（最長字符不超過7個）";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(334, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(265, 246);
            this.richTextBox1.TabIndex = 6;
            this.richTextBox1.Text = "";
            // 
            // TaskMessageWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(606, 271);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.closeButton);
            this.Controls.Add(this.title);
            this.Controls.Add(this.informButton);
            this.Controls.Add(this.content);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "TaskMessageWindow";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "任務欄通知窗口";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RichTextBox content;
        private System.Windows.Forms.Button informButton;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox title;
        private System.Windows.Forms.Button closeButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

