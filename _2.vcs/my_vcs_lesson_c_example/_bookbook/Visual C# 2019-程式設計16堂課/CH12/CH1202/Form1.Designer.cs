namespace CH1202
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
            this.lblMouse = new System.Windows.Forms.Label();
            this.lblMsg = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lblMouse
            // 
            this.lblMouse.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblMouse.Location = new System.Drawing.Point(22, 79);
            this.lblMouse.Name = "lblMouse";
            this.lblMouse.Size = new System.Drawing.Size(274, 66);
            this.lblMouse.TabIndex = 3;
            this.lblMouse.Text = "label1";
            this.lblMouse.Click += new System.EventHandler(this.lblMouse_Click);
            this.lblMouse.DoubleClick += new System.EventHandler(this.lblMouse_DoubleClick);
            // 
            // lblMsg
            // 
            this.lblMsg.Location = new System.Drawing.Point(22, 22);
            this.lblMsg.Name = "lblMsg";
            this.lblMsg.Size = new System.Drawing.Size(279, 47);
            this.lblMsg.TabIndex = 2;
            this.lblMsg.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(345, 174);
            this.Controls.Add(this.lblMouse);
            this.Controls.Add(this.lblMsg);
            this.Name = "Form1";
            this.Text = "CH1202";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label lblMouse;
        private System.Windows.Forms.Label lblMsg;
    }
}

