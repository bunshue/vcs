namespace CH1407
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.OnPaper = new System.Drawing.Printing.PrintDocument();
            this.dlgPreview = new System.Windows.Forms.PrintPreviewDialog();
            this.dlgPrint = new System.Windows.Forms.PrintDialog();
            this.printPreview = new System.Windows.Forms.PrintPreviewControl();
            this.btnPreview = new System.Windows.Forms.Button();
            this.btnPrint = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // OnPaper
            // 
            this.OnPaper.DocumentName = "CH1407";
            // 
            // dlgPreview
            // 
            this.dlgPreview.AutoScrollMargin = new System.Drawing.Size(0, 0);
            this.dlgPreview.AutoScrollMinSize = new System.Drawing.Size(0, 0);
            this.dlgPreview.ClientSize = new System.Drawing.Size(400, 300);
            this.dlgPreview.Document = this.OnPaper;
            this.dlgPreview.Enabled = true;
            this.dlgPreview.Icon = ((System.Drawing.Icon)(resources.GetObject("dlgPreview.Icon")));
            this.dlgPreview.Name = "dlgPreview";
            this.dlgPreview.Visible = false;
            // 
            // dlgPrint
            // 
            this.dlgPrint.Document = this.OnPaper;
            this.dlgPrint.UseEXDialog = true;
            // 
            // printPreview
            // 
            this.printPreview.Location = new System.Drawing.Point(24, 12);
            this.printPreview.Name = "printPreview";
            this.printPreview.Size = new System.Drawing.Size(225, 99);
            this.printPreview.TabIndex = 5;
            this.printPreview.Visible = false;
            // 
            // btnPreview
            // 
            this.btnPreview.Location = new System.Drawing.Point(146, 128);
            this.btnPreview.Name = "btnPreview";
            this.btnPreview.Size = new System.Drawing.Size(84, 36);
            this.btnPreview.TabIndex = 4;
            this.btnPreview.Text = "預覽列印";
            this.btnPreview.UseVisualStyleBackColor = true;
            this.btnPreview.Click += new System.EventHandler(this.btnPreview_Click);
            // 
            // btnPrint
            // 
            this.btnPrint.Location = new System.Drawing.Point(48, 128);
            this.btnPrint.Margin = new System.Windows.Forms.Padding(4);
            this.btnPrint.Name = "btnPrint";
            this.btnPrint.Size = new System.Drawing.Size(80, 36);
            this.btnPrint.TabIndex = 3;
            this.btnPrint.Text = "列印";
            this.btnPrint.UseVisualStyleBackColor = true;
            this.btnPrint.Click += new System.EventHandler(this.btnPrint_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(267, 178);
            this.Controls.Add(this.printPreview);
            this.Controls.Add(this.btnPreview);
            this.Controls.Add(this.btnPrint);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Drawing.Printing.PrintDocument OnPaper;
        private System.Windows.Forms.PrintPreviewDialog dlgPreview;
        private System.Windows.Forms.PrintDialog dlgPrint;
        private System.Windows.Forms.PrintPreviewControl printPreview;
        private System.Windows.Forms.Button btnPreview;
        private System.Windows.Forms.Button btnPrint;
    }
}

