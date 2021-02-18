namespace howto_get_stock_prices
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.txtSymbol1 = new System.Windows.Forms.TextBox();
            this.txtSymbol2 = new System.Windows.Forms.TextBox();
            this.txtSymbol4 = new System.Windows.Forms.TextBox();
            this.txtSymbol3 = new System.Windows.Forms.TextBox();
            this.btnGetPrices = new System.Windows.Forms.Button();
            this.txtPrice4 = new System.Windows.Forms.TextBox();
            this.txtPrice3 = new System.Windows.Forms.TextBox();
            this.txtPrice2 = new System.Windows.Forms.TextBox();
            this.txtPrice1 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(21, 19);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "Symbol";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // txtSymbol1
            // 
            this.txtSymbol1.Location = new System.Drawing.Point(21, 34);
            this.txtSymbol1.Name = "txtSymbol1";
            this.txtSymbol1.Size = new System.Drawing.Size(54, 22);
            this.txtSymbol1.TabIndex = 1;
            this.txtSymbol1.Text = "MCI";
            // 
            // txtSymbol2
            // 
            this.txtSymbol2.Location = new System.Drawing.Point(21, 58);
            this.txtSymbol2.Name = "txtSymbol2";
            this.txtSymbol2.Size = new System.Drawing.Size(54, 22);
            this.txtSymbol2.TabIndex = 2;
            this.txtSymbol2.Text = "DIS";
            // 
            // txtSymbol4
            // 
            this.txtSymbol4.Location = new System.Drawing.Point(21, 106);
            this.txtSymbol4.Name = "txtSymbol4";
            this.txtSymbol4.Size = new System.Drawing.Size(54, 22);
            this.txtSymbol4.TabIndex = 4;
            this.txtSymbol4.Text = "PEP";
            // 
            // txtSymbol3
            // 
            this.txtSymbol3.Location = new System.Drawing.Point(21, 82);
            this.txtSymbol3.Name = "txtSymbol3";
            this.txtSymbol3.Size = new System.Drawing.Size(54, 22);
            this.txtSymbol3.TabIndex = 3;
            this.txtSymbol3.Text = "COKE";
            // 
            // btnGetPrices
            // 
            this.btnGetPrices.Location = new System.Drawing.Point(96, 63);
            this.btnGetPrices.Name = "btnGetPrices";
            this.btnGetPrices.Size = new System.Drawing.Size(75, 21);
            this.btnGetPrices.TabIndex = 5;
            this.btnGetPrices.Text = "Get Prices";
            this.btnGetPrices.UseVisualStyleBackColor = true;
            this.btnGetPrices.Click += new System.EventHandler(this.btnGetPrices_Click);
            // 
            // txtPrice4
            // 
            this.txtPrice4.Location = new System.Drawing.Point(192, 106);
            this.txtPrice4.Name = "txtPrice4";
            this.txtPrice4.ReadOnly = true;
            this.txtPrice4.Size = new System.Drawing.Size(54, 22);
            this.txtPrice4.TabIndex = 10;
            this.txtPrice4.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtPrice3
            // 
            this.txtPrice3.Location = new System.Drawing.Point(192, 82);
            this.txtPrice3.Name = "txtPrice3";
            this.txtPrice3.ReadOnly = true;
            this.txtPrice3.Size = new System.Drawing.Size(54, 22);
            this.txtPrice3.TabIndex = 9;
            this.txtPrice3.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtPrice2
            // 
            this.txtPrice2.Location = new System.Drawing.Point(192, 58);
            this.txtPrice2.Name = "txtPrice2";
            this.txtPrice2.ReadOnly = true;
            this.txtPrice2.Size = new System.Drawing.Size(54, 22);
            this.txtPrice2.TabIndex = 8;
            this.txtPrice2.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtPrice1
            // 
            this.txtPrice1.Location = new System.Drawing.Point(192, 34);
            this.txtPrice1.Name = "txtPrice1";
            this.txtPrice1.ReadOnly = true;
            this.txtPrice1.Size = new System.Drawing.Size(54, 22);
            this.txtPrice1.TabIndex = 7;
            this.txtPrice1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(192, 19);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(54, 12);
            this.label2.TabIndex = 6;
            this.label2.Text = "Prices";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(21, 144);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(716, 414);
            this.richTextBox1.TabIndex = 11;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnGetPrices;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(749, 570);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.txtPrice4);
            this.Controls.Add(this.txtPrice3);
            this.Controls.Add(this.txtPrice2);
            this.Controls.Add(this.txtPrice1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.btnGetPrices);
            this.Controls.Add(this.txtSymbol4);
            this.Controls.Add(this.txtSymbol3);
            this.Controls.Add(this.txtSymbol2);
            this.Controls.Add(this.txtSymbol1);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "howto_get_stock_prices";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtSymbol1;
        private System.Windows.Forms.TextBox txtSymbol2;
        private System.Windows.Forms.TextBox txtSymbol4;
        private System.Windows.Forms.TextBox txtSymbol3;
        private System.Windows.Forms.Button btnGetPrices;
        private System.Windows.Forms.TextBox txtPrice4;
        private System.Windows.Forms.TextBox txtPrice3;
        private System.Windows.Forms.TextBox txtPrice2;
        private System.Windows.Forms.TextBox txtPrice1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

