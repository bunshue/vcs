namespace CH0202
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
         this.lblData = new System.Windows.Forms.Label();
         this.txtName = new System.Windows.Forms.TextBox();
         this.BtnShow = new System.Windows.Forms.Button();
         this.lblName = new System.Windows.Forms.Label();
         this.SuspendLayout();
         // 
         // lblData
         // 
         this.lblData.AutoSize = true;
         this.lblData.Location = new System.Drawing.Point(56, 59);
         this.lblData.Name = "lblData";
         this.lblData.Size = new System.Drawing.Size(71, 27);
         this.lblData.TabIndex = 7;
         this.lblData.Text = "label2";
         // 
         // txtName
         // 
         this.txtName.Location = new System.Drawing.Point(107, 9);
         this.txtName.Margin = new System.Windows.Forms.Padding(4);
         this.txtName.Name = "txtName";
         this.txtName.Size = new System.Drawing.Size(102, 34);
         this.txtName.TabIndex = 6;
         // 
         // BtnShow
         // 
         this.BtnShow.Location = new System.Drawing.Point(61, 106);
         this.BtnShow.Margin = new System.Windows.Forms.Padding(4);
         this.BtnShow.Name = "BtnShow";
         this.BtnShow.Size = new System.Drawing.Size(85, 34);
         this.BtnShow.TabIndex = 5;
         this.BtnShow.Text = "顯示";
         this.BtnShow.UseVisualStyleBackColor = true;
         this.BtnShow.Click += new System.EventHandler(this.BtnShow_Click);
         // 
         // lblName
         // 
         this.lblName.AutoSize = true;
         this.lblName.Location = new System.Drawing.Point(13, 16);
         this.lblName.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
         this.lblName.Name = "lblName";
         this.lblName.Size = new System.Drawing.Size(117, 27);
         this.lblName.TabIndex = 4;
         this.lblName.Text = "輸入名稱：";
         // 
         // Form1
         // 
         this.AutoScaleDimensions = new System.Drawing.SizeF(12F, 25F);
         this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
         this.ClientSize = new System.Drawing.Size(263, 153);
         this.Controls.Add(this.lblData);
         this.Controls.Add(this.txtName);
         this.Controls.Add(this.BtnShow);
         this.Controls.Add(this.lblName);
         this.Font = new System.Drawing.Font("微軟正黑體", 10.74627F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
         this.Margin = new System.Windows.Forms.Padding(4);
         this.Name = "Form1";
         this.Text = "顯示日期";
         this.ResumeLayout(false);
         this.PerformLayout();

      }

      #endregion

      private System.Windows.Forms.Label lblData;
      private System.Windows.Forms.TextBox txtName;
      private System.Windows.Forms.Button BtnShow;
      private System.Windows.Forms.Label lblName;
   }
}

