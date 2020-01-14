namespace vcs_ox_game
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.Symbol1_tb = new System.Windows.Forms.TextBox();
            this.Symbol2_tb = new System.Windows.Forms.TextBox();
            this.Start_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(12, 21);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(421, 386);
            this.panel1.TabIndex = 0;
            // 
            // Symbol1_tb
            // 
            this.Symbol1_tb.Location = new System.Drawing.Point(462, 21);
            this.Symbol1_tb.Name = "Symbol1_tb";
            this.Symbol1_tb.Size = new System.Drawing.Size(100, 22);
            this.Symbol1_tb.TabIndex = 1;
            this.Symbol1_tb.Text = "O";
            // 
            // Symbol2_tb
            // 
            this.Symbol2_tb.Location = new System.Drawing.Point(462, 66);
            this.Symbol2_tb.Name = "Symbol2_tb";
            this.Symbol2_tb.Size = new System.Drawing.Size(100, 22);
            this.Symbol2_tb.TabIndex = 2;
            this.Symbol2_tb.Text = "X";
            // 
            // Start_btn
            // 
            this.Start_btn.Location = new System.Drawing.Point(462, 127);
            this.Start_btn.Name = "Start_btn";
            this.Start_btn.Size = new System.Drawing.Size(75, 23);
            this.Start_btn.TabIndex = 3;
            this.Start_btn.Text = "button1";
            this.Start_btn.UseVisualStyleBackColor = true;
            this.Start_btn.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(603, 557);
            this.Controls.Add(this.Start_btn);
            this.Controls.Add(this.Symbol2_tb);
            this.Controls.Add(this.Symbol1_tb);
            this.Controls.Add(this.panel1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.TextBox Symbol1_tb;
        private System.Windows.Forms.TextBox Symbol2_tb;
        private System.Windows.Forms.Button Start_btn;
    }
}

