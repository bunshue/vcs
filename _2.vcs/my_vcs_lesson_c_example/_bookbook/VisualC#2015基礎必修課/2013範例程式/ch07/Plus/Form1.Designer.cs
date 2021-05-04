namespace Plus
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
            this.label3 = new System.Windows.Forms.Label();
            this.lblAns = new System.Windows.Forms.Label();
            this.btnOK = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.nudPoint = new System.Windows.Forms.NumericUpDown();
            this.nudNo2 = new System.Windows.Forms.NumericUpDown();
            this.nudNo1 = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.nudPoint)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudNo2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudNo1)).BeginInit();
            this.SuspendLayout();
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(46, 92);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 26;
            this.label3.Text = "小數位數：";
            // 
            // lblAns
            // 
            this.lblAns.AutoSize = true;
            this.lblAns.Font = new System.Drawing.Font("新細明體", 12F);
            this.lblAns.Location = new System.Drawing.Point(255, 40);
            this.lblAns.Name = "lblAns";
            this.lblAns.Size = new System.Drawing.Size(46, 16);
            this.lblAns.TabIndex = 25;
            this.lblAns.Text = "label2";
            // 
            // btnOK
            // 
            this.btnOK.Font = new System.Drawing.Font("新細明體", 12F);
            this.btnOK.Location = new System.Drawing.Point(196, 37);
            this.btnOK.Name = "btnOK";
            this.btnOK.Size = new System.Drawing.Size(53, 23);
            this.btnOK.TabIndex = 24;
            this.btnOK.Text = " = ";
            this.btnOK.UseVisualStyleBackColor = true;
            this.btnOK.Click += new System.EventHandler(this.btnOK_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 20F);
            this.label1.Location = new System.Drawing.Point(85, 33);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(26, 27);
            this.label1.TabIndex = 23;
            this.label1.Text = "+";
            // 
            // nudPoint
            // 
            this.nudPoint.Font = new System.Drawing.Font("新細明體", 12F);
            this.nudPoint.Location = new System.Drawing.Point(117, 87);
            this.nudPoint.Name = "nudPoint";
            this.nudPoint.Size = new System.Drawing.Size(63, 27);
            this.nudPoint.TabIndex = 20;
            this.nudPoint.ValueChanged += new System.EventHandler(this.nudPoint_ValueChanged);
            // 
            // nudNo2
            // 
            this.nudNo2.Font = new System.Drawing.Font("新細明體", 12F);
            this.nudNo2.Location = new System.Drawing.Point(117, 36);
            this.nudNo2.Name = "nudNo2";
            this.nudNo2.Size = new System.Drawing.Size(63, 27);
            this.nudNo2.TabIndex = 21;
            // 
            // nudNo1
            // 
            this.nudNo1.Font = new System.Drawing.Font("新細明體", 12F);
            this.nudNo1.Location = new System.Drawing.Point(16, 36);
            this.nudNo1.Name = "nudNo1";
            this.nudNo1.Size = new System.Drawing.Size(63, 27);
            this.nudNo1.TabIndex = 22;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(316, 146);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.lblAns);
            this.Controls.Add(this.btnOK);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.nudPoint);
            this.Controls.Add(this.nudNo2);
            this.Controls.Add(this.nudNo1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.nudPoint)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudNo2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudNo1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label lblAns;
        private System.Windows.Forms.Button btnOK;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown nudPoint;
        private System.Windows.Forms.NumericUpDown nudNo2;
        private System.Windows.Forms.NumericUpDown nudNo1;
    }
}

