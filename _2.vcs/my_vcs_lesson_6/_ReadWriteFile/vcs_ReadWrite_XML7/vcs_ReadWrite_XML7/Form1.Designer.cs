namespace vcs_ReadWrite_XML7
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.button6 = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.button7 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(133, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(440, 614);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // treeView1
            // 
            this.treeView1.Location = new System.Drawing.Point(591, 12);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(446, 614);
            this.treeView1.TabIndex = 5;
            // 
            // button6
            // 
            this.button6.Location = new System.Drawing.Point(12, 22);
            this.button6.Name = "button6";
            this.button6.Size = new System.Drawing.Size(97, 50);
            this.button6.TabIndex = 7;
            this.button6.Text = "開啟XML檔案到TreeView";
            this.button6.UseVisualStyleBackColor = true;
            this.button6.Click += new System.EventHandler(this.button6_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(516, 593);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(57, 33);
            this.bt_clear.TabIndex = 8;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // button7
            // 
            this.button7.Location = new System.Drawing.Point(12, 108);
            this.button7.Name = "button7";
            this.button7.Size = new System.Drawing.Size(97, 50);
            this.button7.TabIndex = 9;
            this.button7.Text = "開啟XML檔案到TreeView";
            this.button7.UseVisualStyleBackColor = true;
            this.button7.Click += new System.EventHandler(this.button7_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1049, 638);
            this.Controls.Add(this.button7);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.button6);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.Button button6;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.Button button7;
    }
}

