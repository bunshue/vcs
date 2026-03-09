namespace vcs_ProgressBar
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
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.bt_stop = new System.Windows.Forms.Button();
            this.bt_start = new System.Windows.Forms.Button();
            this.bt_clear = new System.Windows.Forms.Button();
            this.progressBar0 = new System.Windows.Forms.ProgressBar();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.lb_status0 = new System.Windows.Forms.Label();
            this.groupBox0.SuspendLayout();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(20, 185);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(100, 100);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.lb_status0);
            this.groupBox0.Controls.Add(this.bt_stop);
            this.groupBox0.Controls.Add(this.bt_start);
            this.groupBox0.Location = new System.Drawing.Point(20, 20);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(300, 150);
            this.groupBox0.TabIndex = 4;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "ProgressBar";
            // 
            // bt_stop
            // 
            this.bt_stop.Location = new System.Drawing.Point(97, 103);
            this.bt_stop.Name = "bt_stop";
            this.bt_stop.Size = new System.Drawing.Size(69, 32);
            this.bt_stop.TabIndex = 12;
            this.bt_stop.Text = "停止";
            this.bt_stop.UseVisualStyleBackColor = true;
            this.bt_stop.Click += new System.EventHandler(this.bt_stop_Click);
            // 
            // bt_start
            // 
            this.bt_start.Location = new System.Drawing.Point(22, 103);
            this.bt_start.Name = "bt_start";
            this.bt_start.Size = new System.Drawing.Size(69, 32);
            this.bt_start.TabIndex = 11;
            this.bt_start.Text = "開始";
            this.bt_start.UseVisualStyleBackColor = true;
            this.bt_start.Click += new System.EventHandler(this.bt_start_Click);
            // 
            // bt_clear
            // 
            this.bt_clear.Location = new System.Drawing.Point(42, 226);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(69, 32);
            this.bt_clear.TabIndex = 9;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // progressBar0
            // 
            this.progressBar0.Location = new System.Drawing.Point(42, 50);
            this.progressBar0.Name = "progressBar0";
            this.progressBar0.Size = new System.Drawing.Size(261, 23);
            this.progressBar0.Style = System.Windows.Forms.ProgressBarStyle.Marquee;
            this.progressBar0.TabIndex = 10;
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // lb_status0
            // 
            this.lb_status0.AutoSize = true;
            this.lb_status0.Location = new System.Drawing.Point(22, 70);
            this.lb_status0.Name = "lb_status0";
            this.lb_status0.Size = new System.Drawing.Size(33, 12);
            this.lb_status0.TabIndex = 13;
            this.lb_status0.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(661, 384);
            this.Controls.Add(this.progressBar0);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.ProgressBar progressBar0;
        private System.Windows.Forms.Button bt_stop;
        private System.Windows.Forms.Button bt_start;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label lb_status0;
    }
}

