﻿namespace WinBaseTerm
{
    partial class GPSReadForm
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.cbDK = new System.Windows.Forms.ComboBox();
            this.bt = new System.Windows.Forms.Button();
            this.rt = new System.Windows.Forms.RichTextBox();
            this.btClear = new System.Windows.Forms.Button();
            this.lbM = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(2, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "端口";
            // 
            // cbDK
            // 
            this.cbDK.FormattingEnabled = true;
            this.cbDK.Location = new System.Drawing.Point(37, 6);
            this.cbDK.Name = "cbDK";
            this.cbDK.Size = new System.Drawing.Size(122, 20);
            this.cbDK.TabIndex = 1;
            // 
            // bt
            // 
            this.bt.Location = new System.Drawing.Point(175, 4);
            this.bt.Name = "bt";
            this.bt.Size = new System.Drawing.Size(75, 23);
            this.bt.TabIndex = 2;
            this.bt.Tag = "0";
            this.bt.Text = "监听";
            this.bt.UseVisualStyleBackColor = true;
            this.bt.Click += new System.EventHandler(this.bt_Click);
            // 
            // rt
            // 
            this.rt.Location = new System.Drawing.Point(4, 61);
            this.rt.Name = "rt";
            this.rt.Size = new System.Drawing.Size(585, 204);
            this.rt.TabIndex = 3;
            this.rt.Text = "";
            this.rt.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // btClear
            // 
            this.btClear.Location = new System.Drawing.Point(12, 32);
            this.btClear.Name = "btClear";
            this.btClear.Size = new System.Drawing.Size(75, 23);
            this.btClear.TabIndex = 2;
            this.btClear.Text = "清除";
            this.btClear.UseVisualStyleBackColor = true;
            this.btClear.Click += new System.EventHandler(this.btClear_Click);
            // 
            // lbM
            // 
            this.lbM.AutoSize = true;
            this.lbM.Location = new System.Drawing.Point(94, 42);
            this.lbM.Name = "lbM";
            this.lbM.Size = new System.Drawing.Size(71, 12);
            this.lbM.TabIndex = 4;
            this.lbM.Text = "收到0条信息";
            // 
            // GPSReadForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(592, 277);
            this.Controls.Add(this.lbM);
            this.Controls.Add(this.rt);
            this.Controls.Add(this.btClear);
            this.Controls.Add(this.bt);
            this.Controls.Add(this.cbDK);
            this.Controls.Add(this.label1);
            this.Name = "GPSReadForm";
            this.Text = "GPS读取";
            this.Load += new System.EventHandler(this.GPSReadForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox cbDK;
        private System.Windows.Forms.Button bt;
        private System.Windows.Forms.RichTextBox rt;
        private System.Windows.Forms.Button btClear;
        private System.Windows.Forms.Label lbM;
    }
}

