namespace CH1406
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
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.OnPaper = new System.Drawing.Printing.PrintDocument();
            this.dlgPrint = new System.Windows.Forms.PrintDialog();
            this.btnPrint = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // OnPaper
            // 
            this.OnPaper.DocumentName = "CH1406";
            // 
            // dlgPrint
            // 
            this.dlgPrint.Document = this.OnPaper;
            this.dlgPrint.UseEXDialog = true;
            // 
            // btnPrint
            // 
            this.btnPrint.Location = new System.Drawing.Point(71, 90);
            this.btnPrint.Margin = new System.Windows.Forms.Padding(4);
            this.btnPrint.Name = "btnPrint";
            this.btnPrint.Size = new System.Drawing.Size(100, 34);
            this.btnPrint.TabIndex = 1;
            this.btnPrint.Text = "列印";
            this.btnPrint.UseVisualStyleBackColor = true;
            this.btnPrint.Click += new System.EventHandler(this.btnPrint_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(256, 159);
            this.Controls.Add(this.btnPrint);
            this.Name = "Form1";
            this.Text = "CH1406";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Drawing.Printing.PrintDocument OnPaper;
        private System.Windows.Forms.PrintDialog dlgPrint;
        private System.Windows.Forms.Button btnPrint;
    }
}

