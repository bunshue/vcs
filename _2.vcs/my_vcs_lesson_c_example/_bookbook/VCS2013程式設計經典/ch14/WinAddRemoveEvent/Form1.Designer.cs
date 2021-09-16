namespace WinAddRemoveEvent
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
            this.btnRemoveEvent = new System.Windows.Forms.Button();
            this.btnAddEvent = new System.Windows.Forms.Button();
            this.lblAns = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btnRemoveEvent
            // 
            this.btnRemoveEvent.Location = new System.Drawing.Point(180, 89);
            this.btnRemoveEvent.Name = "btnRemoveEvent";
            this.btnRemoveEvent.Size = new System.Drawing.Size(105, 33);
            this.btnRemoveEvent.TabIndex = 12;
            this.btnRemoveEvent.Text = "移除事件";
            this.btnRemoveEvent.UseVisualStyleBackColor = true;
            this.btnRemoveEvent.Click += new System.EventHandler(this.btnRemoveEvent_Click);
            // 
            // btnAddEvent
            // 
            this.btnAddEvent.Location = new System.Drawing.Point(37, 89);
            this.btnAddEvent.Name = "btnAddEvent";
            this.btnAddEvent.Size = new System.Drawing.Size(105, 33);
            this.btnAddEvent.TabIndex = 11;
            this.btnAddEvent.Text = "新增事件";
            this.btnAddEvent.UseVisualStyleBackColor = true;
            this.btnAddEvent.Click += new System.EventHandler(this.btnAddEvent_Click);
            // 
            // lblAns
            // 
            this.lblAns.AutoSize = true;
            this.lblAns.Font = new System.Drawing.Font("新細明體", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lblAns.Location = new System.Drawing.Point(257, 33);
            this.lblAns.Name = "lblAns";
            this.lblAns.Size = new System.Drawing.Size(53, 19);
            this.lblAns.TabIndex = 10;
            this.lblAns.Text = "label3";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(230, 33);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(19, 19);
            this.label2.TabIndex = 8;
            this.label2.Text = "=";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(119, 33);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(19, 19);
            this.label1.TabIndex = 9;
            this.label1.Text = "+";
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(147, 29);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(74, 31);
            this.textBox2.TabIndex = 7;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(37, 29);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(74, 31);
            this.textBox1.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(339, 164);
            this.Controls.Add(this.btnRemoveEvent);
            this.Controls.Add(this.btnAddEvent);
            this.Controls.Add(this.lblAns);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnRemoveEvent;
        private System.Windows.Forms.Button btnAddEvent;
        private System.Windows.Forms.Label lblAns;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox textBox1;
    }
}

