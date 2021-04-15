namespace vcs_Label
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
            this.label4 = new System.Windows.Forms.Label();
            this.lblRotated3 = new System.Windows.Forms.Label();
            this.lblRotated2 = new System.Windows.Forms.Label();
            this.lblRotated1 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label_AutoSizeFalse = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.lb_moving = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(585, 170);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(52, 12);
            this.label4.TabIndex = 20;
            this.label4.Text = "Column 4";
            // 
            // lblRotated3
            // 
            this.lblRotated3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblRotated3.Location = new System.Drawing.Point(375, 280);
            this.lblRotated3.Name = "lblRotated3";
            this.lblRotated3.Size = new System.Drawing.Size(22, 45);
            this.lblRotated3.TabIndex = 19;
            this.lblRotated3.Text = "Row 3";
            // 
            // lblRotated2
            // 
            this.lblRotated2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblRotated2.Location = new System.Drawing.Point(375, 235);
            this.lblRotated2.Name = "lblRotated2";
            this.lblRotated2.Size = new System.Drawing.Size(22, 45);
            this.lblRotated2.TabIndex = 18;
            this.lblRotated2.Text = "Row 2";
            // 
            // lblRotated1
            // 
            this.lblRotated1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblRotated1.Location = new System.Drawing.Point(375, 190);
            this.lblRotated1.Name = "lblRotated1";
            this.lblRotated1.Size = new System.Drawing.Size(22, 45);
            this.lblRotated1.TabIndex = 17;
            this.lblRotated1.Text = "Row 1";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(528, 170);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(52, 12);
            this.label3.TabIndex = 16;
            this.label3.Text = "Column 3";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(471, 170);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(52, 12);
            this.label2.TabIndex = 15;
            this.label2.Text = "Column 2";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(414, 170);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 12);
            this.label1.TabIndex = 14;
            this.label1.Text = "Column 1";
            // 
            // label_AutoSizeFalse
            // 
            this.label_AutoSizeFalse.BackColor = System.Drawing.Color.Pink;
            this.label_AutoSizeFalse.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label_AutoSizeFalse.Location = new System.Drawing.Point(12, 458);
            this.label_AutoSizeFalse.Name = "label_AutoSizeFalse";
            this.label_AutoSizeFalse.Size = new System.Drawing.Size(500, 100);
            this.label_AutoSizeFalse.TabIndex = 21;
            this.label_AutoSizeFalse.Text = "文字在lable內向右下對齊";
            this.label_AutoSizeFalse.TextAlign = System.Drawing.ContentAlignment.BottomRight;
            // 
            // label5
            // 
            this.label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(14, 403);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(400, 50);
            this.label5.TabIndex = 22;
            this.label5.Text = "Label Fixed3D + TextAlign置中";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lb_moving
            // 
            this.lb_moving.AutoSize = true;
            this.lb_moving.Font = new System.Drawing.Font("標楷體", 26.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_moving.Location = new System.Drawing.Point(473, 577);
            this.lb_moving.Name = "lb_moving";
            this.lb_moving.Size = new System.Drawing.Size(1167, 35);
            this.lb_moving.TabIndex = 23;
            this.lb_moving.Text = "青山隱隱水迢迢，秋盡江南草未凋。二十四橋明月夜，玉人何處教吹簫。";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 150;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(764, 628);
            this.Controls.Add(this.lb_moving);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label_AutoSizeFalse);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.lblRotated3);
            this.Controls.Add(this.lblRotated2);
            this.Controls.Add(this.lblRotated1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label lblRotated3;
        private System.Windows.Forms.Label lblRotated2;
        private System.Windows.Forms.Label lblRotated1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label_AutoSizeFalse;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label lb_moving;
        private System.Windows.Forms.Timer timer1;
    }
}

