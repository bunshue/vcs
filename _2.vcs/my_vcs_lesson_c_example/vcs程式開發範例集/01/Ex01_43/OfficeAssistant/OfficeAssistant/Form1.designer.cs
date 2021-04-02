namespace OfficeAssistant
{
    partial class Form1
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.axAgent1 = new AxAgentObjects.AxAgent();
            this.listBox1 = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.axAgent1)).BeginInit();
            this.SuspendLayout();
            // 
            // axAgent1
            // 
            this.axAgent1.Enabled = true;
            this.axAgent1.Location = new System.Drawing.Point(12, 12);
            this.axAgent1.Name = "axAgent1";
            this.axAgent1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axAgent1.OcxState")));
            this.axAgent1.Size = new System.Drawing.Size(32, 32);
            this.axAgent1.TabIndex = 0;
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 12;
            this.listBox1.Location = new System.Drawing.Point(39, 12);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(164, 160);
            this.listBox1.TabIndex = 1;
            this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(241, 188);
            this.Controls.Add(this.listBox1);
            this.Controls.Add(this.axAgent1);
            this.Name = "Form1";
            this.Text = "如何完成Office小幫手";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.axAgent1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private AxAgentObjects.AxAgent axAgent1;
        private System.Windows.Forms.ListBox listBox1;
    }
}

