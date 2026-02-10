namespace Linq_to_Object2
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
            this.label1 = new System.Windows.Forms.Label();
            this.txtInput = new System.Windows.Forms.TextBox();
            this.btnSearch = new System.Windows.Forms.Button();
            this.txtFileName = new System.Windows.Forms.TextBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 23);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "檔案路徑";
            // 
            // txtInput
            // 
            this.txtInput.Location = new System.Drawing.Point(82, 20);
            this.txtInput.Name = "txtInput";
            this.txtInput.Size = new System.Drawing.Size(100, 22);
            this.txtInput.TabIndex = 1;
            // 
            // btnSearch
            // 
            this.btnSearch.Location = new System.Drawing.Point(197, 15);
            this.btnSearch.Name = "btnSearch";
            this.btnSearch.Size = new System.Drawing.Size(75, 28);
            this.btnSearch.TabIndex = 2;
            this.btnSearch.Text = "搜尋";
            this.btnSearch.UseVisualStyleBackColor = true;
            this.btnSearch.Click += new System.EventHandler(this.btnSearch_Click);
            // 
            // txtFileName
            // 
            this.txtFileName.Location = new System.Drawing.Point(26, 63);
            this.txtFileName.Margin = new System.Windows.Forms.Padding(2);
            this.txtFileName.Multiline = true;
            this.txtFileName.Name = "txtFileName";
            this.txtFileName.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtFileName.Size = new System.Drawing.Size(318, 241);
            this.txtFileName.TabIndex = 3;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(349, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(235, 421);
            this.richTextBox1.TabIndex = 4;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(596, 445);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.txtFileName);
            this.Controls.Add(this.btnSearch);
            this.Controls.Add(this.txtInput);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtInput;
        private System.Windows.Forms.Button btnSearch;
        private System.Windows.Forms.TextBox txtFileName;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

