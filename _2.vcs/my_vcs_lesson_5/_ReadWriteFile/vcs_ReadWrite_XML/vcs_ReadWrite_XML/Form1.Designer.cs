namespace vcs_ReadWrite_XML
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
            this.btnGet = new System.Windows.Forms.Button();
            this.btnCreateNode = new System.Windows.Forms.Button();
            this.btnDeleteNode = new System.Windows.Forms.Button();
            this.lbXmlValue = new System.Windows.Forms.ListBox();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(12, 322);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(714, 324);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            // 
            // btnGet
            // 
            this.btnGet.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnGet.Location = new System.Drawing.Point(732, 12);
            this.btnGet.Name = "btnGet";
            this.btnGet.Size = new System.Drawing.Size(167, 45);
            this.btnGet.TabIndex = 1;
            this.btnGet.Text = "讀取XML檔";
            this.btnGet.UseVisualStyleBackColor = true;
            this.btnGet.Click += new System.EventHandler(this.btnGet_Click);
            // 
            // btnCreateNode
            // 
            this.btnCreateNode.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnCreateNode.Location = new System.Drawing.Point(732, 85);
            this.btnCreateNode.Name = "btnCreateNode";
            this.btnCreateNode.Size = new System.Drawing.Size(167, 45);
            this.btnCreateNode.TabIndex = 2;
            this.btnCreateNode.Text = "增加節點並存檔";
            this.btnCreateNode.UseVisualStyleBackColor = true;
            this.btnCreateNode.Click += new System.EventHandler(this.btnCreateNode_Click);
            // 
            // btnDeleteNode
            // 
            this.btnDeleteNode.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.btnDeleteNode.Location = new System.Drawing.Point(732, 156);
            this.btnDeleteNode.Name = "btnDeleteNode";
            this.btnDeleteNode.Size = new System.Drawing.Size(167, 45);
            this.btnDeleteNode.TabIndex = 3;
            this.btnDeleteNode.Text = "刪除節點並存檔";
            this.btnDeleteNode.UseVisualStyleBackColor = true;
            this.btnDeleteNode.Click += new System.EventHandler(this.btnDeleteNode_Click);
            // 
            // lbXmlValue
            // 
            this.lbXmlValue.FormattingEnabled = true;
            this.lbXmlValue.ItemHeight = 12;
            this.lbXmlValue.Location = new System.Drawing.Point(12, 12);
            this.lbXmlValue.Name = "lbXmlValue";
            this.lbXmlValue.Size = new System.Drawing.Size(714, 304);
            this.lbXmlValue.TabIndex = 4;
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(732, 601);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(167, 45);
            this.button1.TabIndex = 5;
            this.button1.Text = "clear";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(911, 658);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.lbXmlValue);
            this.Controls.Add(this.btnDeleteNode);
            this.Controls.Add(this.btnCreateNode);
            this.Controls.Add(this.btnGet);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button btnGet;
        private System.Windows.Forms.Button btnCreateNode;
        private System.Windows.Forms.Button btnDeleteNode;
        private System.Windows.Forms.ListBox lbXmlValue;
        private System.Windows.Forms.Button button1;
    }
}

