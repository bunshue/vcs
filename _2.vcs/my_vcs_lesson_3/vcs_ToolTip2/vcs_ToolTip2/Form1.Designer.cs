namespace vcs_ToolTip2
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
            this.button10 = new System.Windows.Forms.Button();
            this.button11 = new System.Windows.Forms.Button();
            this.button12 = new System.Windows.Forms.Button();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.toolTip0 = new System.Windows.Forms.ToolTip(this.components);
            this.textBox0 = new System.Windows.Forms.TextBox();
            this.button00 = new System.Windows.Forms.Button();
            this.button01 = new System.Windows.Forms.Button();
            this.button02 = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox0.SuspendLayout();
            this.SuspendLayout();
            // 
            // button10
            // 
            this.button10.Location = new System.Drawing.Point(53, 53);
            this.button10.Name = "button10";
            this.button10.Size = new System.Drawing.Size(113, 81);
            this.button10.TabIndex = 0;
            this.button10.Text = "button10";
            this.button10.UseVisualStyleBackColor = true;
            // 
            // button11
            // 
            this.button11.Location = new System.Drawing.Point(204, 53);
            this.button11.Name = "button11";
            this.button11.Size = new System.Drawing.Size(113, 81);
            this.button11.TabIndex = 1;
            this.button11.Text = "button11";
            this.button11.UseVisualStyleBackColor = true;
            // 
            // button12
            // 
            this.button12.Location = new System.Drawing.Point(357, 53);
            this.button12.Name = "button12";
            this.button12.Size = new System.Drawing.Size(113, 81);
            this.button12.TabIndex = 2;
            this.button12.Text = "button12";
            this.button12.UseVisualStyleBackColor = true;
            // 
            // toolTip1
            // 
            this.toolTip1.Draw += new System.Windows.Forms.DrawToolTipEventHandler(this.toolTip1_Draw);
            this.toolTip1.Popup += new System.Windows.Forms.PopupEventHandler(this.toolTip1_Popup);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.button10);
            this.groupBox1.Controls.Add(this.button11);
            this.groupBox1.Controls.Add(this.button12);
            this.groupBox1.Location = new System.Drawing.Point(12, 212);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(579, 183);
            this.groupBox1.TabIndex = 3;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "groupBox1";
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.button02);
            this.groupBox0.Controls.Add(this.button01);
            this.groupBox0.Controls.Add(this.button00);
            this.groupBox0.Controls.Add(this.textBox0);
            this.groupBox0.Location = new System.Drawing.Point(12, 12);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(579, 183);
            this.groupBox0.TabIndex = 4;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "groupBox0";
            // 
            // textBox0
            // 
            this.textBox0.Location = new System.Drawing.Point(23, 38);
            this.textBox0.Name = "textBox0";
            this.textBox0.Size = new System.Drawing.Size(242, 22);
            this.textBox0.TabIndex = 0;
            this.textBox0.TextChanged += new System.EventHandler(this.textBox0_TextChanged);
            // 
            // button00
            // 
            this.button00.Location = new System.Drawing.Point(23, 78);
            this.button00.Name = "button00";
            this.button00.Size = new System.Drawing.Size(113, 81);
            this.button00.TabIndex = 3;
            this.button00.Text = "設定";
            this.button00.UseVisualStyleBackColor = true;
            this.button00.Click += new System.EventHandler(this.button00_Click);
            // 
            // button01
            // 
            this.button01.Location = new System.Drawing.Point(152, 78);
            this.button01.Name = "button01";
            this.button01.Size = new System.Drawing.Size(113, 81);
            this.button01.TabIndex = 3;
            this.button01.Text = "取得";
            this.button01.UseVisualStyleBackColor = true;
            this.button01.Click += new System.EventHandler(this.button01_Click);
            // 
            // button02
            // 
            this.button02.Location = new System.Drawing.Point(287, 78);
            this.button02.Name = "button02";
            this.button02.Size = new System.Drawing.Size(113, 81);
            this.button02.TabIndex = 3;
            this.button02.Text = "全部移除";
            this.button02.UseVisualStyleBackColor = true;
            this.button02.Click += new System.EventHandler(this.button02_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(845, 575);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button10;
        private System.Windows.Forms.Button button11;
        private System.Windows.Forms.Button button12;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.ToolTip toolTip0;
        private System.Windows.Forms.Button button02;
        private System.Windows.Forms.Button button01;
        private System.Windows.Forms.Button button00;
        private System.Windows.Forms.TextBox textBox0;
    }
}

