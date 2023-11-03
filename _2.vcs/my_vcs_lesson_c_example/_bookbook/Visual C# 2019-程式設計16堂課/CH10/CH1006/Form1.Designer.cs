namespace CH1006
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
            this.btnMod = new System.Windows.Forms.Button();
            this.btnSubtract = new System.Windows.Forms.Button();
            this.btnAdd = new System.Windows.Forms.Button();
            this.txtNum2 = new System.Windows.Forms.TextBox();
            this.txtNum1 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnMod
            // 
            this.btnMod.Location = new System.Drawing.Point(151, 90);
            this.btnMod.Name = "btnMod";
            this.btnMod.Size = new System.Drawing.Size(75, 37);
            this.btnMod.TabIndex = 13;
            this.btnMod.Text = "餘數";
            this.btnMod.UseVisualStyleBackColor = true;
            this.btnMod.Click += new System.EventHandler(this.btnMod_Click);
            // 
            // btnSubtract
            // 
            this.btnSubtract.Location = new System.Drawing.Point(151, 47);
            this.btnSubtract.Name = "btnSubtract";
            this.btnSubtract.Size = new System.Drawing.Size(75, 37);
            this.btnSubtract.TabIndex = 12;
            this.btnSubtract.Text = "減";
            this.btnSubtract.UseVisualStyleBackColor = true;
            this.btnSubtract.Click += new System.EventHandler(this.btnSubtract_Click);
            // 
            // btnAdd
            // 
            this.btnAdd.Location = new System.Drawing.Point(151, 4);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(75, 37);
            this.btnAdd.TabIndex = 11;
            this.btnAdd.Text = "加";
            this.btnAdd.UseVisualStyleBackColor = true;
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // txtNum2
            // 
            this.txtNum2.Location = new System.Drawing.Point(70, 52);
            this.txtNum2.Name = "txtNum2";
            this.txtNum2.Size = new System.Drawing.Size(75, 22);
            this.txtNum2.TabIndex = 10;
            // 
            // txtNum1
            // 
            this.txtNum1.Location = new System.Drawing.Point(70, 6);
            this.txtNum1.Name = "txtNum1";
            this.txtNum1.Size = new System.Drawing.Size(75, 22);
            this.txtNum1.TabIndex = 9;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(24, 58);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(47, 12);
            this.label2.TabIndex = 8;
            this.label2.Text = "數字2：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(24, 16);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 12);
            this.label1.TabIndex = 7;
            this.label1.Text = "數字1：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(245, 134);
            this.Controls.Add(this.btnMod);
            this.Controls.Add(this.btnSubtract);
            this.Controls.Add(this.btnAdd);
            this.Controls.Add(this.txtNum2);
            this.Controls.Add(this.txtNum1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "CH1006";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnMod;
        private System.Windows.Forms.Button btnSubtract;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.TextBox txtNum2;
        private System.Windows.Forms.TextBox txtNum1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}

