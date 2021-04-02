namespace ChatService
{
    partial class ChatService
    {
        /// <summary> 
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region 組件設計器產生的程式碼

        /// <summary> 
        /// 設計器支援所需的方法 - 不要
        /// 使用程式碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.serviceController1 = new System.ServiceProcess.ServiceController();
            // 
            // serviceController1
            // 
            this.serviceController1.ServiceName = "ChatService";
            // 
            // Service1
            // 
            this.CanPauseAndContinue = true;
            this.CanShutdown = true;
            this.ServiceName = "ChatService";

        }

        #endregion

        private System.ServiceProcess.ServiceController serviceController1;
    }
}
