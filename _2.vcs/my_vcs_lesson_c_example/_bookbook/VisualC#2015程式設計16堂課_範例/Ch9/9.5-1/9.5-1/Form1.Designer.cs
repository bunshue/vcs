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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.finalList = new System.Windows.Forms.ListBox();
            this.startButton = new System.Windows.Forms.Button();
            this.listLength = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // finalList
            // 
            this.finalList.FormattingEnabled = true;
            this.finalList.ItemHeight = 12;
            this.finalList.Location = new System.Drawing.Point(12, 38);
            this.finalList.Name = "finalList";
            this.finalList.Size = new System.Drawing.Size(181, 112);
            this.finalList.TabIndex = 0;
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(118, 10);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(75, 23);
            this.startButton.TabIndex = 4;
            this.startButton.Text = "開始列表";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // listLength
            // 
            this.listLength.Location = new System.Drawing.Point(12, 10);
            this.listLength.Name = "listLength";
            this.listLength.Size = new System.Drawing.Size(100, 22);
            this.listLength.TabIndex = 5;
            this.listLength.Text = "0";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(206, 164);
            this.Controls.Add(this.listLength);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.finalList);
            this.Name = "Form1";
            this.Text = "費式數列產生器";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox finalList;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.TextBox listLength;









    }
}

