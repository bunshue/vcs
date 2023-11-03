namespace CH1106
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.chkPlumTea = new System.Windows.Forms.CheckBox();
            this.chkLemonTea = new System.Windows.Forms.CheckBox();
            this.chkYeast = new System.Windows.Forms.CheckBox();
            this.chkMilkTea = new System.Windows.Forms.CheckBox();
            this.chkBlackTea = new System.Windows.Forms.CheckBox();
            this.chkGreenTea = new System.Windows.Forms.CheckBox();
            this.lblShow = new System.Windows.Forms.Label();
            this.btnTotal = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.chkPlumTea);
            this.groupBox1.Controls.Add(this.chkLemonTea);
            this.groupBox1.Controls.Add(this.chkYeast);
            this.groupBox1.Controls.Add(this.chkMilkTea);
            this.groupBox1.Controls.Add(this.chkBlackTea);
            this.groupBox1.Controls.Add(this.chkGreenTea);
            this.groupBox1.Location = new System.Drawing.Point(13, 13);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(4);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(4);
            this.groupBox1.Size = new System.Drawing.Size(291, 129);
            this.groupBox1.TabIndex = 3;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "勾選欲買飲料";
            // 
            // chkPlumTea
            // 
            this.chkPlumTea.AutoSize = true;
            this.chkPlumTea.Location = new System.Drawing.Point(130, 96);
            this.chkPlumTea.Name = "chkPlumTea";
            this.chkPlumTea.Size = new System.Drawing.Size(100, 16);
            this.chkPlumTea.TabIndex = 5;
            this.chkPlumTea.Text = "梅子綠茶-40元";
            this.chkPlumTea.UseVisualStyleBackColor = true;
            // 
            // chkLemonTea
            // 
            this.chkLemonTea.AutoSize = true;
            this.chkLemonTea.Location = new System.Drawing.Point(130, 59);
            this.chkLemonTea.Name = "chkLemonTea";
            this.chkLemonTea.Size = new System.Drawing.Size(100, 16);
            this.chkLemonTea.TabIndex = 4;
            this.chkLemonTea.Text = "冬瓜檸檬-55元";
            this.chkLemonTea.UseVisualStyleBackColor = true;
            // 
            // chkYeast
            // 
            this.chkYeast.AutoSize = true;
            this.chkYeast.Location = new System.Drawing.Point(130, 30);
            this.chkYeast.Name = "chkYeast";
            this.chkYeast.Size = new System.Drawing.Size(100, 16);
            this.chkYeast.TabIndex = 3;
            this.chkYeast.Text = "綠茶多多-42元";
            this.chkYeast.UseVisualStyleBackColor = true;
            // 
            // chkMilkTea
            // 
            this.chkMilkTea.AutoSize = true;
            this.chkMilkTea.Location = new System.Drawing.Point(6, 96);
            this.chkMilkTea.Name = "chkMilkTea";
            this.chkMilkTea.Size = new System.Drawing.Size(76, 16);
            this.chkMilkTea.TabIndex = 2;
            this.chkMilkTea.Text = "奶茶-45元";
            this.chkMilkTea.UseVisualStyleBackColor = true;
            // 
            // chkBlackTea
            // 
            this.chkBlackTea.AutoSize = true;
            this.chkBlackTea.Location = new System.Drawing.Point(6, 60);
            this.chkBlackTea.Name = "chkBlackTea";
            this.chkBlackTea.Size = new System.Drawing.Size(76, 16);
            this.chkBlackTea.TabIndex = 1;
            this.chkBlackTea.Text = "紅茶-30元";
            this.chkBlackTea.UseVisualStyleBackColor = true;
            // 
            // chkGreenTea
            // 
            this.chkGreenTea.AutoSize = true;
            this.chkGreenTea.Location = new System.Drawing.Point(6, 30);
            this.chkGreenTea.Name = "chkGreenTea";
            this.chkGreenTea.Size = new System.Drawing.Size(76, 16);
            this.chkGreenTea.TabIndex = 0;
            this.chkGreenTea.Text = "綠茶-35元";
            this.chkGreenTea.UseVisualStyleBackColor = true;
            // 
            // lblShow
            // 
            this.lblShow.AutoSize = true;
            this.lblShow.Location = new System.Drawing.Point(138, 152);
            this.lblShow.Name = "lblShow";
            this.lblShow.Size = new System.Drawing.Size(33, 12);
            this.lblShow.TabIndex = 5;
            this.lblShow.Text = "label1";
            // 
            // btnTotal
            // 
            this.btnTotal.Location = new System.Drawing.Point(57, 149);
            this.btnTotal.Name = "btnTotal";
            this.btnTotal.Size = new System.Drawing.Size(75, 30);
            this.btnTotal.TabIndex = 4;
            this.btnTotal.Text = "總計";
            this.btnTotal.UseVisualStyleBackColor = true;
            this.btnTotal.Click += new System.EventHandler(this.btnTotal_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(322, 185);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.lblShow);
            this.Controls.Add(this.btnTotal);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.CheckBox chkPlumTea;
        private System.Windows.Forms.CheckBox chkLemonTea;
        private System.Windows.Forms.CheckBox chkYeast;
        private System.Windows.Forms.CheckBox chkMilkTea;
        private System.Windows.Forms.CheckBox chkBlackTea;
        private System.Windows.Forms.CheckBox chkGreenTea;
        private System.Windows.Forms.Label lblShow;
        private System.Windows.Forms.Button btnTotal;
    }
}

