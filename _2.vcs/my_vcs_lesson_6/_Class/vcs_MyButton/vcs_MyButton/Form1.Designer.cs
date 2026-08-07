namespace vcs_MyButton
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
            this.aquaButton1 = new vcs_MyButton.AquaButton();
            this.aquaButton2 = new vcs_MyButton.AquaButton();
            this.aquaButton3 = new vcs_MyButton.AquaButton();
            this.aquaButton4 = new vcs_MyButton.AquaButton();
            this.aquaButton5 = new vcs_MyButton.AquaButton();
            this.aquaButton6 = new vcs_MyButton.AquaButton();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // aquaButton1
            // 
            this.aquaButton1.BackColor = System.Drawing.Color.DarkTurquoise;
            this.aquaButton1.Font = new System.Drawing.Font("Arial Black", 12F, System.Drawing.FontStyle.Bold);
            this.aquaButton1.Location = new System.Drawing.Point(10, 10);
            this.aquaButton1.Name = "aquaButton1";
            this.aquaButton1.PulseOnFocus = true;
            this.aquaButton1.Size = new System.Drawing.Size(200, 60);
            this.aquaButton1.TabIndex = 0;
            this.aquaButton1.Text = "aquaButton1";
            this.aquaButton1.UseVisualStyleBackColor = false;
            this.aquaButton1.Click += new System.EventHandler(this.aquaButton_Click);
            // 
            // aquaButton2
            // 
            this.aquaButton2.BackColor = System.Drawing.Color.Tomato;
            this.aquaButton2.Font = new System.Drawing.Font("Arial Black", 12F, System.Drawing.FontStyle.Bold);
            this.aquaButton2.Location = new System.Drawing.Point(220, 10);
            this.aquaButton2.Name = "aquaButton2";
            this.aquaButton2.Size = new System.Drawing.Size(200, 60);
            this.aquaButton2.TabIndex = 1;
            this.aquaButton2.Text = "aquaButton2";
            this.aquaButton2.UseVisualStyleBackColor = false;
            this.aquaButton2.Click += new System.EventHandler(this.aquaButton_Click);
            // 
            // aquaButton3
            // 
            this.aquaButton3.BackColor = System.Drawing.Color.RosyBrown;
            this.aquaButton3.Font = new System.Drawing.Font("Arial Black", 12F, System.Drawing.FontStyle.Bold);
            this.aquaButton3.Location = new System.Drawing.Point(10, 80);
            this.aquaButton3.Name = "aquaButton3";
            this.aquaButton3.PulseOnFocus = true;
            this.aquaButton3.Size = new System.Drawing.Size(200, 60);
            this.aquaButton3.TabIndex = 2;
            this.aquaButton3.Text = "aquaButton3";
            this.aquaButton3.UseVisualStyleBackColor = false;
            this.aquaButton3.Click += new System.EventHandler(this.aquaButton_Click);
            // 
            // aquaButton4
            // 
            this.aquaButton4.BackColor = System.Drawing.Color.DodgerBlue;
            this.aquaButton4.Font = new System.Drawing.Font("Arial Black", 12F, System.Drawing.FontStyle.Bold);
            this.aquaButton4.Location = new System.Drawing.Point(220, 80);
            this.aquaButton4.Name = "aquaButton4";
            this.aquaButton4.Size = new System.Drawing.Size(200, 60);
            this.aquaButton4.TabIndex = 3;
            this.aquaButton4.Text = "aquaButton4";
            this.aquaButton4.UseVisualStyleBackColor = false;
            this.aquaButton4.Click += new System.EventHandler(this.aquaButton_Click);
            // 
            // aquaButton5
            // 
            this.aquaButton5.BackColor = System.Drawing.Color.MediumSeaGreen;
            this.aquaButton5.Font = new System.Drawing.Font("Arial Black", 12F, System.Drawing.FontStyle.Bold);
            this.aquaButton5.Location = new System.Drawing.Point(10, 150);
            this.aquaButton5.Name = "aquaButton5";
            this.aquaButton5.PulseOnFocus = true;
            this.aquaButton5.Size = new System.Drawing.Size(200, 60);
            this.aquaButton5.TabIndex = 4;
            this.aquaButton5.Text = "aquaButton5";
            this.aquaButton5.UseVisualStyleBackColor = false;
            this.aquaButton5.Click += new System.EventHandler(this.aquaButton_Click);
            // 
            // aquaButton6
            // 
            this.aquaButton6.BackColor = System.Drawing.Color.Violet;
            this.aquaButton6.Font = new System.Drawing.Font("Arial Black", 12F, System.Drawing.FontStyle.Bold);
            this.aquaButton6.Location = new System.Drawing.Point(220, 150);
            this.aquaButton6.Name = "aquaButton6";
            this.aquaButton6.Size = new System.Drawing.Size(200, 60);
            this.aquaButton6.TabIndex = 5;
            this.aquaButton6.Text = "aquaButton6";
            this.aquaButton6.UseVisualStyleBackColor = false;
            this.aquaButton6.Click += new System.EventHandler(this.aquaButton_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(430, 10);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(340, 540);
            this.richTextBox1.TabIndex = 7;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 561);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.aquaButton6);
            this.Controls.Add(this.aquaButton5);
            this.Controls.Add(this.aquaButton4);
            this.Controls.Add(this.aquaButton3);
            this.Controls.Add(this.aquaButton2);
            this.Controls.Add(this.aquaButton1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private AquaButton aquaButton1;
        private AquaButton aquaButton2;
        private AquaButton aquaButton3;
        private AquaButton aquaButton4;
        private AquaButton aquaButton5;
        private AquaButton aquaButton6;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

