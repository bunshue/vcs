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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改這個方法的內容。
        ///
        /// </summary>
        private void InitializeComponent()
        {
            this.Val1 = new System.Windows.Forms.TextBox();
            this.Val2 = new System.Windows.Forms.TextBox();
            this.addButton = new System.Windows.Forms.Button();
            this.minButton = new System.Windows.Forms.Button();
            this.mulButton = new System.Windows.Forms.Button();
            this.divButton = new System.Windows.Forms.Button();
            this.eqlButton = new System.Windows.Forms.Button();
            this.noteqlButton = new System.Windows.Forms.Button();
            this.biggerButton = new System.Windows.Forms.Button();
            this.smallerButton = new System.Windows.Forms.Button();
            this.resultVal = new System.Windows.Forms.TextBox();
            this.resultLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Val1
            // 
            this.Val1.Location = new System.Drawing.Point(12, 12);
            this.Val1.Name = "Val1";
            this.Val1.Size = new System.Drawing.Size(156, 22);
            this.Val1.TabIndex = 0;
            // 
            // Val2
            // 
            this.Val2.Location = new System.Drawing.Point(174, 12);
            this.Val2.Name = "Val2";
            this.Val2.Size = new System.Drawing.Size(156, 22);
            this.Val2.TabIndex = 1;
            // 
            // addButton
            // 
            this.addButton.Location = new System.Drawing.Point(12, 40);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(75, 23);
            this.addButton.TabIndex = 2;
            this.addButton.Text = "加法";
            this.addButton.UseVisualStyleBackColor = true;
            this.addButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // minButton
            // 
            this.minButton.Location = new System.Drawing.Point(93, 40);
            this.minButton.Name = "minButton";
            this.minButton.Size = new System.Drawing.Size(75, 23);
            this.minButton.TabIndex = 3;
            this.minButton.Text = "減法";
            this.minButton.UseVisualStyleBackColor = true;
            this.minButton.Click += new System.EventHandler(this.minButton_Click);
            // 
            // mulButton
            // 
            this.mulButton.Location = new System.Drawing.Point(174, 40);
            this.mulButton.Name = "mulButton";
            this.mulButton.Size = new System.Drawing.Size(75, 23);
            this.mulButton.TabIndex = 4;
            this.mulButton.Text = "乘法";
            this.mulButton.UseVisualStyleBackColor = true;
            this.mulButton.Click += new System.EventHandler(this.mulButton_Click);
            // 
            // divButton
            // 
            this.divButton.Location = new System.Drawing.Point(255, 40);
            this.divButton.Name = "divButton";
            this.divButton.Size = new System.Drawing.Size(75, 23);
            this.divButton.TabIndex = 5;
            this.divButton.Text = "除法";
            this.divButton.UseVisualStyleBackColor = true;
            this.divButton.Click += new System.EventHandler(this.divButton_Click);
            // 
            // eqlButton
            // 
            this.eqlButton.Location = new System.Drawing.Point(12, 69);
            this.eqlButton.Name = "eqlButton";
            this.eqlButton.Size = new System.Drawing.Size(75, 23);
            this.eqlButton.TabIndex = 6;
            this.eqlButton.Text = "相等?";
            this.eqlButton.UseVisualStyleBackColor = true;
            this.eqlButton.Click += new System.EventHandler(this.eqlButton_Click);
            // 
            // noteqlButton
            // 
            this.noteqlButton.Location = new System.Drawing.Point(93, 69);
            this.noteqlButton.Name = "noteqlButton";
            this.noteqlButton.Size = new System.Drawing.Size(75, 23);
            this.noteqlButton.TabIndex = 7;
            this.noteqlButton.Text = "不相等?";
            this.noteqlButton.UseVisualStyleBackColor = true;
            this.noteqlButton.Click += new System.EventHandler(this.noteqlButton_Click);
            // 
            // biggerButton
            // 
            this.biggerButton.Location = new System.Drawing.Point(174, 69);
            this.biggerButton.Name = "biggerButton";
            this.biggerButton.Size = new System.Drawing.Size(75, 23);
            this.biggerButton.TabIndex = 8;
            this.biggerButton.Text = "大於?";
            this.biggerButton.UseVisualStyleBackColor = true;
            this.biggerButton.Click += new System.EventHandler(this.biggerButton_Click);
            // 
            // smallerButton
            // 
            this.smallerButton.Location = new System.Drawing.Point(255, 69);
            this.smallerButton.Name = "smallerButton";
            this.smallerButton.Size = new System.Drawing.Size(75, 23);
            this.smallerButton.TabIndex = 9;
            this.smallerButton.Text = "小於?";
            this.smallerButton.UseVisualStyleBackColor = true;
            this.smallerButton.Click += new System.EventHandler(this.smallerButton_Click);
            // 
            // resultVal
            // 
            this.resultVal.Location = new System.Drawing.Point(51, 98);
            this.resultVal.Name = "resultVal";
            this.resultVal.Size = new System.Drawing.Size(279, 22);
            this.resultVal.TabIndex = 10;
            // 
            // resultLabel
            // 
            this.resultLabel.AutoSize = true;
            this.resultLabel.Location = new System.Drawing.Point(12, 101);
            this.resultLabel.Name = "resultLabel";
            this.resultLabel.Size = new System.Drawing.Size(32, 12);
            this.resultLabel.TabIndex = 11;
            this.resultLabel.Text = "結果:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(342, 133);
            this.Controls.Add(this.resultLabel);
            this.Controls.Add(this.resultVal);
            this.Controls.Add(this.smallerButton);
            this.Controls.Add(this.biggerButton);
            this.Controls.Add(this.noteqlButton);
            this.Controls.Add(this.eqlButton);
            this.Controls.Add(this.divButton);
            this.Controls.Add(this.mulButton);
            this.Controls.Add(this.minButton);
            this.Controls.Add(this.addButton);
            this.Controls.Add(this.Val2);
            this.Controls.Add(this.Val1);
            this.Name = "Form1";
            this.Text = "簡易計算機程式";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox Val1;
        private System.Windows.Forms.TextBox Val2;
        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button minButton;
        private System.Windows.Forms.Button mulButton;
        private System.Windows.Forms.Button divButton;
        private System.Windows.Forms.Button eqlButton;
        private System.Windows.Forms.Button noteqlButton;
        private System.Windows.Forms.Button biggerButton;
        private System.Windows.Forms.Button smallerButton;
        private System.Windows.Forms.TextBox resultVal;
        private System.Windows.Forms.Label resultLabel;




    }
}

