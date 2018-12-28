namespace myson_link
{
    partial class Form2
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form2));
            this.labelTimer = new System.Windows.Forms.Label();
            this.buttonStart = new System.Windows.Forms.Button();
            this.buttonReset = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.buttonTop = new System.Windows.Forms.Button();
            this.buttonExit = new System.Windows.Forms.Button();
            this.labelTimer1 = new System.Windows.Forms.Label();
            this.labelTimer2 = new System.Windows.Forms.Label();
            this.labelTimer3 = new System.Windows.Forms.Label();
            this.labelTimer4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // labelTimer
            // 
            this.labelTimer.AutoSize = true;
            this.labelTimer.Font = new System.Drawing.Font("標楷體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.labelTimer.Location = new System.Drawing.Point(19, 60);
            this.labelTimer.Name = "labelTimer";
            this.labelTimer.Size = new System.Drawing.Size(116, 48);
            this.labelTimer.TabIndex = 1;
            this.labelTimer.Text = "-.--";
            this.labelTimer.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // buttonStart
            // 
            this.buttonStart.Font = new System.Drawing.Font("標楷體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.buttonStart.Location = new System.Drawing.Point(27, 411);
            this.buttonStart.Name = "buttonStart";
            this.buttonStart.Size = new System.Drawing.Size(127, 47);
            this.buttonStart.TabIndex = 2;
            this.buttonStart.Text = "START";
            this.buttonStart.UseVisualStyleBackColor = true;
            this.buttonStart.Click += new System.EventHandler(this.buttonStart_Click);
            // 
            // buttonReset
            // 
            this.buttonReset.Font = new System.Drawing.Font("標楷體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.buttonReset.Location = new System.Drawing.Point(185, 411);
            this.buttonReset.Name = "buttonReset";
            this.buttonReset.Size = new System.Drawing.Size(127, 47);
            this.buttonReset.TabIndex = 3;
            this.buttonReset.Text = "STOP";
            this.buttonReset.UseVisualStyleBackColor = true;
            this.buttonReset.Click += new System.EventHandler(this.buttonReset_Click);
            // 
            // timer1
            // 
            this.timer1.Interval = 10;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // buttonTop
            // 
            this.buttonTop.Font = new System.Drawing.Font("標楷體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.buttonTop.Location = new System.Drawing.Point(497, 386);
            this.buttonTop.Name = "buttonTop";
            this.buttonTop.Size = new System.Drawing.Size(42, 39);
            this.buttonTop.TabIndex = 4;
            this.buttonTop.Text = "上";
            this.buttonTop.UseVisualStyleBackColor = true;
            this.buttonTop.Click += new System.EventHandler(this.buttonTop_Click);
            // 
            // buttonExit
            // 
            this.buttonExit.Font = new System.Drawing.Font("標楷體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.buttonExit.Location = new System.Drawing.Point(497, 431);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(42, 39);
            this.buttonExit.TabIndex = 5;
            this.buttonExit.Text = "離";
            this.buttonExit.UseVisualStyleBackColor = true;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // labelTimer1
            // 
            this.labelTimer1.AutoSize = true;
            this.labelTimer1.Font = new System.Drawing.Font("標楷體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.labelTimer1.Location = new System.Drawing.Point(19, 124);
            this.labelTimer1.Name = "labelTimer1";
            this.labelTimer1.Size = new System.Drawing.Size(116, 48);
            this.labelTimer1.TabIndex = 6;
            this.labelTimer1.Text = "-.--";
            this.labelTimer1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelTimer2
            // 
            this.labelTimer2.AutoSize = true;
            this.labelTimer2.Font = new System.Drawing.Font("標楷體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.labelTimer2.Location = new System.Drawing.Point(19, 187);
            this.labelTimer2.Name = "labelTimer2";
            this.labelTimer2.Size = new System.Drawing.Size(116, 48);
            this.labelTimer2.TabIndex = 7;
            this.labelTimer2.Text = "-.--";
            this.labelTimer2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelTimer3
            // 
            this.labelTimer3.AutoSize = true;
            this.labelTimer3.Font = new System.Drawing.Font("標楷體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.labelTimer3.Location = new System.Drawing.Point(19, 252);
            this.labelTimer3.Name = "labelTimer3";
            this.labelTimer3.Size = new System.Drawing.Size(116, 48);
            this.labelTimer3.TabIndex = 8;
            this.labelTimer3.Text = "-.--";
            this.labelTimer3.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelTimer4
            // 
            this.labelTimer4.AutoSize = true;
            this.labelTimer4.Font = new System.Drawing.Font("標楷體", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.labelTimer4.Location = new System.Drawing.Point(19, 320);
            this.labelTimer4.Name = "labelTimer4";
            this.labelTimer4.Size = new System.Drawing.Size(116, 48);
            this.labelTimer4.TabIndex = 9;
            this.labelTimer4.Text = "-.--";
            this.labelTimer4.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(551, 482);
            this.Controls.Add(this.labelTimer4);
            this.Controls.Add(this.labelTimer3);
            this.Controls.Add(this.labelTimer2);
            this.Controls.Add(this.labelTimer1);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.buttonTop);
            this.Controls.Add(this.buttonReset);
            this.Controls.Add(this.buttonStart);
            this.Controls.Add(this.labelTimer);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Form2";
            this.Text = "DigitalClock";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label labelTimer;
        private System.Windows.Forms.Button buttonStart;
        private System.Windows.Forms.Button buttonReset;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Button buttonTop;
        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Label labelTimer1;
        private System.Windows.Forms.Label labelTimer2;
        private System.Windows.Forms.Label labelTimer3;
        private System.Windows.Forms.Label labelTimer4;
    }
}