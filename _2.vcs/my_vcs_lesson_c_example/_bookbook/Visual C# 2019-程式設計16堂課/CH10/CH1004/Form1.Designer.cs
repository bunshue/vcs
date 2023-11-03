namespace CH1004
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
            this.btnCalc = new System.Windows.Forms.Button();
            this.txtGrade = new System.Windows.Forms.TextBox();
            this.txtName = new System.Windows.Forms.TextBox();
            this.lblShow = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btnCalc
            // 
            this.btnCalc.Location = new System.Drawing.Point(188, 13);
            this.btnCalc.Name = "btnCalc";
            this.btnCalc.Size = new System.Drawing.Size(75, 33);
            this.btnCalc.TabIndex = 11;
            this.btnCalc.Text = "計算";
            this.btnCalc.UseVisualStyleBackColor = true;
            this.btnCalc.Click += new System.EventHandler(this.btnCalc_Click);
            // 
            // txtGrade
            // 
            this.txtGrade.Location = new System.Drawing.Point(84, 49);
            this.txtGrade.Name = "txtGrade";
            this.txtGrade.Size = new System.Drawing.Size(100, 22);
            this.txtGrade.TabIndex = 10;
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(84, 13);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 22);
            this.txtName.TabIndex = 9;
            // 
            // lblShow
            // 
            this.lblShow.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.lblShow.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblShow.Font = new System.Drawing.Font("微軟正黑體", 11.8209F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblShow.Location = new System.Drawing.Point(14, 91);
            this.lblShow.Name = "lblShow";
            this.lblShow.Size = new System.Drawing.Size(229, 67);
            this.lblShow.TabIndex = 8;
            this.lblShow.Text = "label3";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("微軟正黑體", 10.20895F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(7, 51);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(64, 18);
            this.label2.TabIndex = 7;
            this.label2.Text = "學分數：";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("微軟正黑體", 10.20895F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(26, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(50, 18);
            this.label1.TabIndex = 6;
            this.label1.Text = "名稱：";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(281, 172);
            this.Controls.Add(this.btnCalc);
            this.Controls.Add(this.txtGrade);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.lblShow);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "CH1004";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnCalc;
        private System.Windows.Forms.TextBox txtGrade;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label lblShow;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}

