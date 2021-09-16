namespace WinFormPolymorphism4
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
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.txtX = new System.Windows.Forms.TextBox();
            this.txtY = new System.Windows.Forms.TextBox();
            this.txtAns = new System.Windows.Forms.TextBox();
            this.rdbAdd = new System.Windows.Forms.RadioButton();
            this.rdbSub = new System.Windows.Forms.RadioButton();
            this.rdbMul = new System.Windows.Forms.RadioButton();
            this.rdbDiv = new System.Windows.Forms.RadioButton();
            this.btnCal = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(45, 48);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(27, 16);
            this.label1.TabIndex = 0;
            this.label1.Text = "X :";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(44, 111);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(27, 16);
            this.label2.TabIndex = 1;
            this.label2.Text = "Y :";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(44, 172);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(40, 16);
            this.label3.TabIndex = 2;
            this.label3.Text = "結果";
            // 
            // txtX
            // 
            this.txtX.Location = new System.Drawing.Point(99, 45);
            this.txtX.Margin = new System.Windows.Forms.Padding(4);
            this.txtX.Name = "txtX";
            this.txtX.Size = new System.Drawing.Size(132, 27);
            this.txtX.TabIndex = 3;
            // 
            // txtY
            // 
            this.txtY.Location = new System.Drawing.Point(99, 108);
            this.txtY.Margin = new System.Windows.Forms.Padding(4);
            this.txtY.Name = "txtY";
            this.txtY.Size = new System.Drawing.Size(132, 27);
            this.txtY.TabIndex = 4;
            // 
            // txtAns
            // 
            this.txtAns.Location = new System.Drawing.Point(99, 169);
            this.txtAns.Margin = new System.Windows.Forms.Padding(4);
            this.txtAns.Name = "txtAns";
            this.txtAns.Size = new System.Drawing.Size(138, 27);
            this.txtAns.TabIndex = 5;
            // 
            // rdbAdd
            // 
            this.rdbAdd.AutoSize = true;
            this.rdbAdd.Checked = true;
            this.rdbAdd.Location = new System.Drawing.Point(276, 44);
            this.rdbAdd.Margin = new System.Windows.Forms.Padding(4);
            this.rdbAdd.Name = "rdbAdd";
            this.rdbAdd.Size = new System.Drawing.Size(42, 20);
            this.rdbAdd.TabIndex = 6;
            this.rdbAdd.TabStop = true;
            this.rdbAdd.Text = "加";
            this.rdbAdd.UseVisualStyleBackColor = true;
            this.rdbAdd.CheckedChanged += new System.EventHandler(this.rdbAdd_CheckedChanged);
            // 
            // rdbSub
            // 
            this.rdbSub.AutoSize = true;
            this.rdbSub.Location = new System.Drawing.Point(276, 85);
            this.rdbSub.Margin = new System.Windows.Forms.Padding(4);
            this.rdbSub.Name = "rdbSub";
            this.rdbSub.Size = new System.Drawing.Size(42, 20);
            this.rdbSub.TabIndex = 7;
            this.rdbSub.Text = "減";
            this.rdbSub.UseVisualStyleBackColor = true;
            this.rdbSub.CheckedChanged += new System.EventHandler(this.rdbSub_CheckedChanged);
            // 
            // rdbMul
            // 
            this.rdbMul.AutoSize = true;
            this.rdbMul.Location = new System.Drawing.Point(276, 132);
            this.rdbMul.Margin = new System.Windows.Forms.Padding(4);
            this.rdbMul.Name = "rdbMul";
            this.rdbMul.Size = new System.Drawing.Size(42, 20);
            this.rdbMul.TabIndex = 8;
            this.rdbMul.Text = "乘";
            this.rdbMul.UseVisualStyleBackColor = true;
            this.rdbMul.CheckedChanged += new System.EventHandler(this.rdbMul_CheckedChanged);
            // 
            // rdbDiv
            // 
            this.rdbDiv.AutoSize = true;
            this.rdbDiv.Location = new System.Drawing.Point(276, 176);
            this.rdbDiv.Margin = new System.Windows.Forms.Padding(4);
            this.rdbDiv.Name = "rdbDiv";
            this.rdbDiv.Size = new System.Drawing.Size(42, 20);
            this.rdbDiv.TabIndex = 9;
            this.rdbDiv.Text = "除";
            this.rdbDiv.UseVisualStyleBackColor = true;
            this.rdbDiv.CheckedChanged += new System.EventHandler(this.rdbDiv_CheckedChanged);
            // 
            // btnCal
            // 
            this.btnCal.Location = new System.Drawing.Point(250, 226);
            this.btnCal.Margin = new System.Windows.Forms.Padding(4);
            this.btnCal.Name = "btnCal";
            this.btnCal.Size = new System.Drawing.Size(88, 33);
            this.btnCal.TabIndex = 10;
            this.btnCal.Text = "計算";
            this.btnCal.UseVisualStyleBackColor = true;
            this.btnCal.Click += new System.EventHandler(this.btnCal_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(377, 283);
            this.Controls.Add(this.btnCal);
            this.Controls.Add(this.rdbDiv);
            this.Controls.Add(this.rdbMul);
            this.Controls.Add(this.rdbSub);
            this.Controls.Add(this.rdbAdd);
            this.Controls.Add(this.txtAns);
            this.Controls.Add(this.txtY);
            this.Controls.Add(this.txtX);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "多型-範例一";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtX;
        private System.Windows.Forms.TextBox txtY;
        private System.Windows.Forms.TextBox txtAns;
        private System.Windows.Forms.RadioButton rdbAdd;
        private System.Windows.Forms.RadioButton rdbSub;
        private System.Windows.Forms.RadioButton rdbMul;
        private System.Windows.Forms.RadioButton rdbDiv;
        private System.Windows.Forms.Button btnCal;
    }
}

