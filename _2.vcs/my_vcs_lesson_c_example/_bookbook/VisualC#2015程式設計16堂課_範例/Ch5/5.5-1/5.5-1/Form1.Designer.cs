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
            this.xSquare = new System.Windows.Forms.TextBox();
            this.xSquareLabel = new System.Windows.Forms.Label();
            this.x = new System.Windows.Forms.TextBox();
            this.xLabel = new System.Windows.Forms.Label();
            this.constant = new System.Windows.Forms.TextBox();
            this.zeroLabel = new System.Windows.Forms.Label();
            this.computeButton = new System.Windows.Forms.Button();
            this.result = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // xSquare
            // 
            this.xSquare.Location = new System.Drawing.Point(12, 12);
            this.xSquare.Name = "xSquare";
            this.xSquare.Size = new System.Drawing.Size(50, 22);
            this.xSquare.TabIndex = 0;
            // 
            // xSquareLabel
            // 
            this.xSquareLabel.AutoSize = true;
            this.xSquareLabel.Location = new System.Drawing.Point(68, 15);
            this.xSquareLabel.Name = "xSquareLabel";
            this.xSquareLabel.Size = new System.Drawing.Size(33, 12);
            this.xSquareLabel.TabIndex = 1;
            this.xSquareLabel.Text = "X^2 +";
            // 
            // x
            // 
            this.x.Location = new System.Drawing.Point(107, 12);
            this.x.Name = "x";
            this.x.Size = new System.Drawing.Size(50, 22);
            this.x.TabIndex = 2;
            // 
            // xLabel
            // 
            this.xLabel.AutoSize = true;
            this.xLabel.Location = new System.Drawing.Point(163, 15);
            this.xLabel.Name = "xLabel";
            this.xLabel.Size = new System.Drawing.Size(22, 12);
            this.xLabel.TabIndex = 3;
            this.xLabel.Text = "X +";
            // 
            // constant
            // 
            this.constant.Location = new System.Drawing.Point(191, 12);
            this.constant.Name = "constant";
            this.constant.Size = new System.Drawing.Size(50, 22);
            this.constant.TabIndex = 4;
            // 
            // zeroLabel
            // 
            this.zeroLabel.AutoSize = true;
            this.zeroLabel.Location = new System.Drawing.Point(247, 15);
            this.zeroLabel.Name = "zeroLabel";
            this.zeroLabel.Size = new System.Drawing.Size(20, 12);
            this.zeroLabel.TabIndex = 5;
            this.zeroLabel.Text = "= 0";
            // 
            // computeButton
            // 
            this.computeButton.Location = new System.Drawing.Point(12, 40);
            this.computeButton.Name = "computeButton";
            this.computeButton.Size = new System.Drawing.Size(75, 23);
            this.computeButton.TabIndex = 6;
            this.computeButton.Text = "計算結果";
            this.computeButton.UseVisualStyleBackColor = true;
            this.computeButton.Click += new System.EventHandler(this.computeButton_Click);
            // 
            // result
            // 
            this.result.Location = new System.Drawing.Point(91, 42);
            this.result.Name = "result";
            this.result.Size = new System.Drawing.Size(246, 22);
            this.result.TabIndex = 7;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(349, 78);
            this.Controls.Add(this.result);
            this.Controls.Add(this.computeButton);
            this.Controls.Add(this.zeroLabel);
            this.Controls.Add(this.constant);
            this.Controls.Add(this.xLabel);
            this.Controls.Add(this.x);
            this.Controls.Add(this.xSquareLabel);
            this.Controls.Add(this.xSquare);
            this.Name = "Form1";
            this.Text = "一元二次方程式求解";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox xSquare;
        private System.Windows.Forms.Label xSquareLabel;
        private System.Windows.Forms.TextBox x;
        private System.Windows.Forms.Label xLabel;
        private System.Windows.Forms.TextBox constant;
        private System.Windows.Forms.Label zeroLabel;
        private System.Windows.Forms.Button computeButton;
        private System.Windows.Forms.TextBox result;





    }
}

