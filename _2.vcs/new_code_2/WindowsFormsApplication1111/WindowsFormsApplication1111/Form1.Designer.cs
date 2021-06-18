namespace WindowsFormsApplication1111
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
            this.label1 = new System.Windows.Forms.Label();
            this.drawListBox1 = new WindowsFormsApplication1111.DrawListBox();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(325, 89);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(459, 386);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            this.richTextBox1.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.richTextBox1_KeyPress);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(190, 153);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 21);
            this.label1.TabIndex = 2;
            this.label1.Text = "label1";
            // 
            // drawListBox1
            // 
            this.drawListBox1.Color1 = System.Drawing.Color.CornflowerBlue;
            this.drawListBox1.Color1Gradual = System.Drawing.Color.Thistle;
            this.drawListBox1.Color2 = System.Drawing.Color.PaleGreen;
            this.drawListBox1.Color2Gradual = System.Drawing.Color.DarkKhaki;
            this.drawListBox1.ColorSelect = System.Drawing.Color.Gainsboro;
            this.drawListBox1.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.drawListBox1.FormattingEnabled = true;
            this.drawListBox1.GradualC = true;
            this.drawListBox1.Items.AddRange(new object[] {
            "明日科技",
            "C#编程词典（体验版）",
            "C#编程词典（学习版）",
            "C#编程词典（全能版）",
            "C#编程词典（标准版）",
            "C#编程词典（珍藏版）",
            "C#编程词典（企业版）",
            "C#编程词典（钻石版）"});
            this.drawListBox1.Location = new System.Drawing.Point(12, 217);
            this.drawListBox1.Name = "drawListBox1";
            this.drawListBox1.Size = new System.Drawing.Size(307, 251);
            this.drawListBox1.TabIndex = 3;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(796, 487);
            this.Controls.Add(this.drawListBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label1;
        private DrawListBox drawListBox1;
    }
}

