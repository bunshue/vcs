namespace WindowsFormsApplication1
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
            this.numText1 = new System.Windows.Forms.TextBox();
            this.generateButton = new System.Windows.Forms.Button();
            this.numText2 = new System.Windows.Forms.TextBox();
            this.numText3 = new System.Windows.Forms.TextBox();
            this.numText4 = new System.Windows.Forms.TextBox();
            this.numText5 = new System.Windows.Forms.TextBox();
            this.numText6 = new System.Windows.Forms.TextBox();
            this.continuousCheck = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // numText1
            // 
            this.numText1.Location = new System.Drawing.Point(12, 12);
            this.numText1.Name = "numText1";
            this.numText1.Size = new System.Drawing.Size(30, 22);
            this.numText1.TabIndex = 0;
            // 
            // generateButton
            // 
            this.generateButton.Location = new System.Drawing.Point(228, 12);
            this.generateButton.Name = "generateButton";
            this.generateButton.Size = new System.Drawing.Size(75, 23);
            this.generateButton.TabIndex = 1;
            this.generateButton.Text = "產生號碼";
            this.generateButton.UseVisualStyleBackColor = true;
            this.generateButton.Click += new System.EventHandler(this.generateButton_Click);
            // 
            // numText2
            // 
            this.numText2.Location = new System.Drawing.Point(48, 12);
            this.numText2.Name = "numText2";
            this.numText2.Size = new System.Drawing.Size(30, 22);
            this.numText2.TabIndex = 2;
            // 
            // numText3
            // 
            this.numText3.Location = new System.Drawing.Point(84, 12);
            this.numText3.Name = "numText3";
            this.numText3.Size = new System.Drawing.Size(30, 22);
            this.numText3.TabIndex = 3;
            // 
            // numText4
            // 
            this.numText4.Location = new System.Drawing.Point(120, 12);
            this.numText4.Name = "numText4";
            this.numText4.Size = new System.Drawing.Size(30, 22);
            this.numText4.TabIndex = 4;
            // 
            // numText5
            // 
            this.numText5.Location = new System.Drawing.Point(156, 12);
            this.numText5.Name = "numText5";
            this.numText5.Size = new System.Drawing.Size(30, 22);
            this.numText5.TabIndex = 5;
            // 
            // numText6
            // 
            this.numText6.Location = new System.Drawing.Point(192, 12);
            this.numText6.Name = "numText6";
            this.numText6.Size = new System.Drawing.Size(30, 22);
            this.numText6.TabIndex = 6;
            // 
            // continuousCheck
            // 
            this.continuousCheck.AutoSize = true;
            this.continuousCheck.Location = new System.Drawing.Point(309, 16);
            this.continuousCheck.Name = "continuousCheck";
            this.continuousCheck.Size = new System.Drawing.Size(77, 16);
            this.continuousCheck.TabIndex = 7;
            this.continuousCheck.Text = "允許連號?";
            this.continuousCheck.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(389, 46);
            this.Controls.Add(this.continuousCheck);
            this.Controls.Add(this.numText6);
            this.Controls.Add(this.numText5);
            this.Controls.Add(this.numText4);
            this.Controls.Add(this.numText3);
            this.Controls.Add(this.numText2);
            this.Controls.Add(this.generateButton);
            this.Controls.Add(this.numText1);
            this.Name = "Form1";
            this.Text = "樂透電腦選號程式";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox numText1;
        private System.Windows.Forms.Button generateButton;
        private System.Windows.Forms.TextBox numText2;
        private System.Windows.Forms.TextBox numText3;
        private System.Windows.Forms.TextBox numText4;
        private System.Windows.Forms.TextBox numText5;
        private System.Windows.Forms.TextBox numText6;
        private System.Windows.Forms.CheckBox continuousCheck;
    }
}

