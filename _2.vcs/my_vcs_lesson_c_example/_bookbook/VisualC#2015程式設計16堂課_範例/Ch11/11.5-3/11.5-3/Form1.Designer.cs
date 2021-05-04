namespace WindowsFormsApplication1
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
            this.menuList = new System.Windows.Forms.ListBox();
            this.loadButton = new System.Windows.Forms.Button();
            this.priceLabel = new System.Windows.Forms.Label();
            this.priceText = new System.Windows.Forms.TextBox();
            this.openDialog = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            // 
            // menuList
            // 
            this.menuList.FormattingEnabled = true;
            this.menuList.ItemHeight = 12;
            this.menuList.Location = new System.Drawing.Point(12, 41);
            this.menuList.Name = "menuList";
            this.menuList.Size = new System.Drawing.Size(168, 184);
            this.menuList.TabIndex = 0;
            this.menuList.SelectedIndexChanged += new System.EventHandler(this.menuList_SelectedIndexChanged);
            // 
            // loadButton
            // 
            this.loadButton.Location = new System.Drawing.Point(12, 12);
            this.loadButton.Name = "loadButton";
            this.loadButton.Size = new System.Drawing.Size(168, 23);
            this.loadButton.TabIndex = 1;
            this.loadButton.Text = "讀取菜單";
            this.loadButton.UseVisualStyleBackColor = true;
            this.loadButton.Click += new System.EventHandler(this.loadButton_Click);
            // 
            // priceLabel
            // 
            this.priceLabel.AutoSize = true;
            this.priceLabel.Location = new System.Drawing.Point(12, 231);
            this.priceLabel.Name = "priceLabel";
            this.priceLabel.Size = new System.Drawing.Size(32, 12);
            this.priceLabel.TabIndex = 2;
            this.priceLabel.Text = "價格:";
            // 
            // priceText
            // 
            this.priceText.Location = new System.Drawing.Point(51, 228);
            this.priceText.Name = "priceText";
            this.priceText.Size = new System.Drawing.Size(129, 22);
            this.priceText.TabIndex = 3;
            // 
            // openDialog
            // 
            this.openDialog.FileName = "openFileDialog1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(192, 260);
            this.Controls.Add(this.priceText);
            this.Controls.Add(this.priceLabel);
            this.Controls.Add(this.loadButton);
            this.Controls.Add(this.menuList);
            this.Name = "Form1";
            this.Text = "菜單讀取顯示程式";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox menuList;
        private System.Windows.Forms.Button loadButton;
        private System.Windows.Forms.Label priceLabel;
        private System.Windows.Forms.TextBox priceText;
        private System.Windows.Forms.OpenFileDialog openDialog;
    }
}

