namespace PcDiy
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.lblSum = new System.Windows.Forms.Label();
            this.cbxCRT = new System.Windows.Forms.ComboBox();
            this.lstdeskPC = new System.Windows.Forms.ListBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lblSum
            // 
            this.lblSum.AutoSize = true;
            this.lblSum.Location = new System.Drawing.Point(218, 192);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(41, 12);
            this.lblSum.TabIndex = 11;
            this.lblSum.Text = "合計：";
            // 
            // cbxCRT
            // 
            this.cbxCRT.FormattingEnabled = true;
            this.cbxCRT.Location = new System.Drawing.Point(221, 113);
            this.cbxCRT.Name = "cbxCRT";
            this.cbxCRT.Size = new System.Drawing.Size(121, 20);
            this.cbxCRT.TabIndex = 10;
            this.cbxCRT.SelectedIndexChanged += new System.EventHandler(this.cbxCRT_SelectedIndexChanged);
            // 
            // lstdeskPC
            // 
            this.lstdeskPC.FormattingEnabled = true;
            this.lstdeskPC.ItemHeight = 12;
            this.lstdeskPC.Location = new System.Drawing.Point(45, 113);
            this.lstdeskPC.Name = "lstdeskPC";
            this.lstdeskPC.Size = new System.Drawing.Size(120, 88);
            this.lstdeskPC.TabIndex = 9;
            this.lstdeskPC.SelectedIndexChanged += new System.EventHandler(this.lstdeskPC_SelectedIndexChanged);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(218, 86);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(77, 12);
            this.label3.TabIndex = 8;
            this.label3.Text = "液晶螢幕尺寸";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(42, 86);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 12);
            this.label2.TabIndex = 7;
            this.label2.Text = "主機廠牌";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(104, 34);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(180, 24);
            this.label1.TabIndex = 6;
            this.label1.Text = "PC DIY配件試算";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(384, 238);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.cbxCRT);
            this.Controls.Add(this.lstdeskPC);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "清單和下拉式清單應用程式";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblSum;
        private System.Windows.Forms.ComboBox cbxCRT;
        private System.Windows.Forms.ListBox lstdeskPC;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}

