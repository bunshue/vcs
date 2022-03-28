using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_BackgroundWorker5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            BackgroundWorkerInit.BackgroundWorker1_Init();
        }
    }

    public class BackgroundWorkerInit
    {
        public static void BackgroundWorker1_Init()
        {
            BackgroundWorker backgroundWorker1 = new BackgroundWorker();
            backgroundWorker1.WorkerReportsProgress = true;//能否報告進度更新。
            backgroundWorker1.WorkerSupportsCancellation = true;//是否支援非同步取消
            //繫結事件
            backgroundWorker1.DoWork += new DoWorkEventHandler(BackgroundWorker1_DoWork);
            backgroundWorker1.ProgressChanged += new ProgressChangedEventHandler(BackgroundWorker1_ProgressChanged);
            backgroundWorker1.RunWorkerCompleted += new RunWorkerCompletedEventHandler(BackgroundWorker1_RunWorkerCompleted);

            //啟動BackgroundWorker
            if (backgroundWorker1.IsBusy != true)//判斷BackgroundWorker 是否正在執行非同步操作。
            {
                backgroundWorker1.RunWorkerAsync("object argument");//啟動非同步操作，有兩種過載（有參和無參）,將觸發BackgroundWorker.DoWork事件
            }
        }

        /// <summary>
        /// 控制代碼sender指向的就是該BackgroundWorker。
        /// e.Argument 獲取非同步操作引數的值  
        /// e.Cancel 是否應該取消事件
        /// e.Result  獲取或設定非同步操作結果的值(在RunWorkerCompleted事件可能會使用到)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private static void BackgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            object value = e.Argument;//獲取RunWorkerAsync(object argument)傳入的值
            BackgroundWorker worker = sender as BackgroundWorker;

            for (int i = 1; i <= 10; i++)
            {
                if (worker.CancellationPending == true)//在耗時操作中判斷CancellationPending屬性，如果為true則退出
                {
                    e.Cancel = true;
                    break;
                }
                else
                {
                    // 執行耗時操作
                    System.Threading.Thread.Sleep(1000);
                    worker.ReportProgress(i * 10, "Object userState");// 將觸發BackgroundWorker.ProgressChanged事件，向ProgressChanged報告進度
                }
            }
            e.Result = "結束";
        }


        /// <summary>
        /// e.Cancelled指示非同步操作是否已被取消
        /// e.Error 指示非同步操作期間發生的錯誤
        /// e.Result 獲取非同步操作結果的值,即DoWork事件中，Result設定的值。    
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private static void BackgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            //判斷是否使用者手動取消，若程式要支援此處功能，需要程式中有cancel的動作，並在該動作中將e.cancel置為true
            if (e.Cancelled == true)
            {
                //新增使用者手動取消的動作，並在標籤控制元件中進行提示  
                Console.WriteLine("操作已經被取消！");
            }
            //判斷是否由錯誤造成意外中止
            else if (e.Error != null)
            {
                //若發生錯誤，在標籤控制元件中顯示錯誤資訊
                Console.WriteLine("操作發生錯誤！");
            }
            //判斷是否正常結束
            else
            {
                //新增正常結束之後的收尾動作，並在標籤控制元件中進行提示
                Console.WriteLine("執行結果：{e.Result.ToString()}！");
            }
        }


        /// <summary>
        /// 進度重新整理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private static void BackgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            //接收ReportProgress方法傳遞過來的userState
            string state = (string)e.UserState;

            //e.ProgressPercentage  獲取非同步操作進度的百分比
            Console.WriteLine("進度 : " + e.ProgressPercentage.ToString() + " %");
        }
    }
}

