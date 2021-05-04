namespace _14._6_s2
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
            this.components = new System.ComponentModel.Container();
            this.turtleButton = new System.Windows.Forms.RadioButton();
            this.rabbitButton = new System.Windows.Forms.RadioButton();
            this.startButton = new System.Windows.Forms.Button();
            this.turtleLabel = new System.Windows.Forms.Label();
            this.rabbitLabel = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // turtleButton
            // 
            this.turtleButton.AutoSize = true;
            this.turtleButton.Location = new System.Drawing.Point(124, 77);
            this.turtleButton.Name = "turtleButton";
            this.turtleButton.Size = new System.Drawing.Size(59, 16);
            this.turtleButton.TabIndex = 0;
            this.turtleButton.TabStop = true;
            this.turtleButton.Text = "烏龜贏";
            this.turtleButton.UseVisualStyleBackColor = true;
            // 
            // rabbitButton
            // 
            this.rabbitButton.AutoSize = true;
            this.rabbitButton.Location = new System.Drawing.Point(189, 77);
            this.rabbitButton.Name = "rabbitButton";
            this.rabbitButton.Size = new System.Drawing.Size(59, 16);
            this.rabbitButton.TabIndex = 1;
            this.rabbitButton.TabStop = true;
            this.rabbitButton.Text = "兔子贏";
            this.rabbitButton.UseVisualStyleBackColor = true;
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(254, 74);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(75, 23);
            this.startButton.TabIndex = 2;
            this.startButton.Text = "開始比賽";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // turtleLabel
            // 
            this.turtleLabel.AutoSize = true;
            this.turtleLabel.Location = new System.Drawing.Point(12, 20);
            this.turtleLabel.Name = "turtleLabel";
            this.turtleLabel.Size = new System.Drawing.Size(29, 12);
            this.turtleLabel.TabIndex = 3;
            this.turtleLabel.Text = "烏龜";
            // 
            // rabbitLabel
            // 
            this.rabbitLabel.AutoSize = true;
            this.rabbitLabel.Location = new System.Drawing.Point(12, 45);
            this.rabbitLabel.Name = "rabbitLabel";
            this.rabbitLabel.Size = new System.Drawing.Size(29, 12);
            this.rabbitLabel.TabIndex = 4;
            this.rabbitLabel.Text = "兔子";
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(341, 112);
            this.Controls.Add(this.rabbitLabel);
            this.Controls.Add(this.turtleLabel);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.rabbitButton);
            this.Controls.Add(this.turtleButton);
            this.Name = "Form1";
            this.Text = "龜兔賽跑預測遊戲";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton turtleButton;
        private System.Windows.Forms.RadioButton rabbitButton;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Label turtleLabel;
        private System.Windows.Forms.Label rabbitLabel;
        private System.Windows.Forms.Timer timer1;
    }
}

