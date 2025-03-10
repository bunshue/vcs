
      this.backgroundWorker1.RunWorkerCompleted+=new RunWorkerCompletedEventHandler(backgroundWorker1_RunWorkerCompleted); 
      this.backgroundWorker1.ProgressChanged+=new ProgressChangedEventHandler(backgroundWorker1_ProgressChanged); 
      this.backgroundWorker1.DoWork+=new DoWorkEventHandler(backgroundWorker1_DoWork); 




C# BackgroundWorker的使用

此方法可以實現後台程序調用、創建線程、遮屏的效果。
BackgroundWorker主要有三個事件:RunWorkerCompleted,ProgressChanged,DoWork
[csharp]


當點擊一個按鈕想實現讀條的方法時，需要調用BackgroundWorker對象的RunWorkerAsync方法，該方法會觸發DoWork事件，該事件的方法中
可以用兩種方式獲得BackgroundWorker對象，
[csharp] 
private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e) 
 
        { 
 
            BackgroundWorker worker = (BackgroundWorker)sender; 
 
lt; 
        }
或者 直接可以獲得類中的BackgroundWorker，在DoWork方法中主要是讀條處理的細節方面，通過BackgroundWorker 對象的ReportProgress把百分數傳出,
for循環中最大值是100可以表示為百分數的分母，與progressBar的Maximum的屬性保持一致。此處還要注意的是，要加上 Thread.Sleep(100),否則線程一直執行，主面板其他控件則無法使用， 也就無法取消當前線程。在每次循環中，一定要校驗下CancellationPending是否為真，表示當前線程是否被用戶中斷。
[csharp] 
 for (int i = 0; i < 100; i++) 
 
            { 
 
                if (bk.CancellationPending) //這裡判斷一下是否用戶要求取消後台進行，並可以盡早退出。 
 
                { 
 
                    bk.ReportProgress(i, String.Format("當前值是 {0},操作被用戶申請中斷", i)); 
 
                    return false; 
 
                } 
 
                Thread.Sleep(100); 
 
                //處理的過程中，通過這個函數，向主線程報告處理進度，最好是折算成百分比，與外邊的進度條的最大值必須要對應。這裡，我沒有折算，而是把界面線程的進度條最大值調整為與這裡的總數一致。 
 
                bk.ReportProgress(i, String.Format(" {0}% ", i)); 
 
            } 
通過調用CancelAsync方法可以實現後台線程的終止，不管任何方式的終止都會出發RunWorkerCompleted方法。
最後要說的是progressChanged這個事件，該事件被ReportProgress引發，一般用來做後台線程值變化時響應消息，來處理界面的顯示工作
比如:
[csharp] 
    private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e) 
        { 
 
            this.progressBar1.Value = e.ProgressPercentage; 
 
            this.label1.Text = e.UserState.ToString(); 
 
            this.label1.Update(); 
 
        } 
