namespace FontColorDialog
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
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.lblMsg = new System.Windows.Forms.Label();
            this.btnFont = new System.Windows.Forms.Button();
            this.btnBColor = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // fontDialog1
            // 
            this.fontDialog1.ShowApply = true;
            this.fontDialog1.ShowColor = true;
            this.fontDialog1.ShowHelp = true;
            // 
            // lblMsg
            // 
            this.lblMsg.Location = new System.Drawing.Point(13, 17);
            this.lblMsg.Name = "lblMsg";
            this.lblMsg.Size = new System.Drawing.Size(188, 67);
            this.lblMsg.TabIndex = 0;
            this.lblMsg.Text = "label1";
            // 
            // btnFont
            // 
            this.btnFont.Location = new System.Drawing.Point(15, 104);
            this.btnFont.Name = "btnFont";
            this.btnFont.Size = new System.Drawing.Size(84, 23);
            this.btnFont.TabIndex = 1;
            this.btnFont.Text = "設定字型";
            this.btnFont.UseVisualStyleBackColor = true;
            this.btnFont.Click += new System.EventHandler(this.btnFont_Click);
            // 
            // btnBColor
            // 
            this.btnBColor.Location = new System.Drawing.Point(116, 104);
            this.btnBColor.Name = "btnBColor";
            this.btnBColor.Size = new System.Drawing.Size(85, 23);
            this.btnBColor.TabIndex = 2;
            this.btnBColor.Text = "設定背景顏色";
            this.btnBColor.UseVisualStyleBackColor = true;
            this.btnBColor.Click += new System.EventHandler(this.btnBColor_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(220, 139);
            this.Controls.Add(this.btnBColor);
            this.Controls.Add(this.btnFont);
            this.Controls.Add(this.lblMsg);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.Label lblMsg;
        private System.Windows.Forms.Button btnFont;
        private System.Windows.Forms.Button btnBColor;
    }
}

