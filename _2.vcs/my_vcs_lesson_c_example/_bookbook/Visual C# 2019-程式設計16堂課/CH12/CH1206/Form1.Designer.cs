namespace CH1206
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
            this.lblTarget = new System.Windows.Forms.Label();
            this.lblMsg = new System.Windows.Forms.Label();
            this.lblState = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // lblTarget
            // 
            this.lblTarget.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.lblTarget.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblTarget.Location = new System.Drawing.Point(14, 63);
            this.lblTarget.Name = "lblTarget";
            this.lblTarget.Size = new System.Drawing.Size(112, 66);
            this.lblTarget.TabIndex = 5;
            this.lblTarget.Text = "label3";
            // 
            // lblMsg
            // 
            this.lblMsg.AutoSize = true;
            this.lblMsg.Location = new System.Drawing.Point(12, 9);
            this.lblMsg.Name = "lblMsg";
            this.lblMsg.Size = new System.Drawing.Size(33, 12);
            this.lblMsg.TabIndex = 4;
            this.lblMsg.Text = "label2";
            // 
            // lblState
            // 
            this.lblState.AutoSize = true;
            this.lblState.Location = new System.Drawing.Point(99, 9);
            this.lblState.Name = "lblState";
            this.lblState.Size = new System.Drawing.Size(33, 12);
            this.lblState.TabIndex = 3;
            this.lblState.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(249, 166);
            this.Controls.Add(this.lblTarget);
            this.Controls.Add(this.lblMsg);
            this.Controls.Add(this.lblState);
            this.Name = "Form1";
            this.Text = "CH1206";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblTarget;
        private System.Windows.Forms.Label lblMsg;
        private System.Windows.Forms.Label lblState;
    }
}

