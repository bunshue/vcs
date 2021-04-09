namespace vcs_Tictactoe3
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.Start_btn = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.Symbol1_tb = new System.Windows.Forms.TextBox();
            this.Symbol2_tb = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // Start_btn
            // 
            this.Start_btn.Font = new System.Drawing.Font("微軟正黑體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Start_btn.Location = new System.Drawing.Point(34, 106);
            this.Start_btn.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Start_btn.Name = "Start_btn";
            this.Start_btn.Size = new System.Drawing.Size(178, 48);
            this.Start_btn.TabIndex = 0;
            this.Start_btn.Text = "開始遊戲";
            this.Start_btn.UseVisualStyleBackColor = true;
            this.Start_btn.Click += new System.EventHandler(this.Start_btn_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("微軟正黑體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(28, 22);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(84, 19);
            this.label1.TabIndex = 1;
            this.label1.Text = "玩家一符號";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("微軟正黑體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(28, 67);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(84, 19);
            this.label2.TabIndex = 2;
            this.label2.Text = "玩家二符號";
            // 
            // Symbol1_tb
            // 
            this.Symbol1_tb.Location = new System.Drawing.Point(164, 17);
            this.Symbol1_tb.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Symbol1_tb.Name = "Symbol1_tb";
            this.Symbol1_tb.Size = new System.Drawing.Size(48, 27);
            this.Symbol1_tb.TabIndex = 3;
            this.Symbol1_tb.Text = "O";
            this.Symbol1_tb.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // Symbol2_tb
            // 
            this.Symbol2_tb.Location = new System.Drawing.Point(164, 62);
            this.Symbol2_tb.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Symbol2_tb.Name = "Symbol2_tb";
            this.Symbol2_tb.Size = new System.Drawing.Size(48, 27);
            this.Symbol2_tb.TabIndex = 4;
            this.Symbol2_tb.Text = "X";
            this.Symbol2_tb.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.Symbol2_tb);
            this.panel1.Controls.Add(this.Start_btn);
            this.panel1.Controls.Add(this.Symbol1_tb);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Location = new System.Drawing.Point(18, 19);
            this.panel1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(252, 177);
            this.panel1.TabIndex = 5;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 19F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(291, 215);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("微軟正黑體", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form1";
            this.Text = "自訂符號井字遊戲";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button Start_btn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox Symbol1_tb;
        private System.Windows.Forms.TextBox Symbol2_tb;
        private System.Windows.Forms.Panel panel1;
    }
}

