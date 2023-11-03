namespace CH1104
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
            this.components = new System.ComponentModel.Container();
            this.tmrCount = new System.Windows.Forms.Timer(this.components);
            this.trackTime = new System.Windows.Forms.TrackBar();
            this.btnClear = new System.Windows.Forms.Button();
            this.btnStop = new System.Windows.Forms.Button();
            this.btnStart = new System.Windows.Forms.Button();
            this.txtTime = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.trackTime)).BeginInit();
            this.SuspendLayout();
            // 
            // tmrCount
            // 
            this.tmrCount.Interval = 10;
            this.tmrCount.Tick += new System.EventHandler(this.tmrCount_Tick);
            // 
            // trackTime
            // 
            this.trackTime.Location = new System.Drawing.Point(20, 103);
            this.trackTime.Maximum = 60;
            this.trackTime.Name = "trackTime";
            this.trackTime.Size = new System.Drawing.Size(209, 45);
            this.trackTime.TabIndex = 11;
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(160, 57);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(69, 40);
            this.btnClear.TabIndex = 10;
            this.btnClear.Text = "清除";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // btnStop
            // 
            this.btnStop.Location = new System.Drawing.Point(90, 57);
            this.btnStop.Name = "btnStop";
            this.btnStop.Size = new System.Drawing.Size(69, 40);
            this.btnStop.TabIndex = 9;
            this.btnStop.Text = "停止";
            this.btnStop.UseVisualStyleBackColor = true;
            this.btnStop.Click += new System.EventHandler(this.btnStop_Click);
            // 
            // btnStart
            // 
            this.btnStart.Location = new System.Drawing.Point(20, 57);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(69, 40);
            this.btnStart.TabIndex = 8;
            this.btnStart.Text = "開始";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // txtTime
            // 
            this.txtTime.Location = new System.Drawing.Point(116, 17);
            this.txtTime.Name = "txtTime";
            this.txtTime.Size = new System.Drawing.Size(100, 22);
            this.txtTime.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(28, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(53, 12);
            this.label1.TabIndex = 6;
            this.label1.Text = "經過時間";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(288, 161);
            this.Controls.Add(this.trackTime);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.btnStop);
            this.Controls.Add(this.btnStart);
            this.Controls.Add(this.txtTime);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "CH1104";
            ((System.ComponentModel.ISupportInitialize)(this.trackTime)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer tmrCount;
        private System.Windows.Forms.TrackBar trackTime;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.Button btnStop;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.TextBox txtTime;
        private System.Windows.Forms.Label label1;
    }
}

