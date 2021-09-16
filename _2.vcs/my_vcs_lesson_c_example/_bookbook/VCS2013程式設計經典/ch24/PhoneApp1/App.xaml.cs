using System;
using System.Diagnostics;
using System.Resources;
using System.Windows;
using System.Windows.Markup;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using PhoneApp1.Resources;

namespace PhoneApp1
{
    public partial class App : Application
    {
        /// <summary>
        /// 提供簡單的方法，來存取電話應用程式的根畫面。
        /// </summary>
        /// <returns>電話應用程式的根畫面。</returns>
        public static PhoneApplicationFrame RootFrame { get; private set; }

        /// <summary>
        /// Application 物件的建構函式。
        /// </summary>
        public App()
        {
            // 無法攔截之例外狀況的全域處理常式。
            UnhandledException += Application_UnhandledException;

            // 標準 XAML 初始化
            InitializeComponent();

            // 電話特有初始化
            InitializePhoneApplication();

            // 語言顯示初始化
            InitializeLanguage();

            // 偵錯時顯示圖形分析資訊。
            if (Debugger.IsAttached)
            {
                // 顯示目前的畫面播放速率計數器。
                Application.Current.Host.Settings.EnableFrameRateCounter = true;

                // 顯示每個畫面中重新繪製的應用程式區域。
                //Application.Current.Host.Settings.EnableRedrawRegions = true;

                // 啟用非實際執行分析視覺化模式，
                // 用彩色重疊在頁面上顯示交給 GPU 的區域。
                //Application.Current.Host.Settings.EnableCacheVisualization = true;

                // 防止螢幕在執行偵錯工具時關閉，方法是停用
                // 應用程式的閒置偵測。
                // 注意: 這項功能僅限偵錯模式使用。當使用者不使用電話時，停用使用者閒置偵測
                // 的應用程式仍會繼續執行，並消耗電池的電力。
                PhoneApplicationService.Current.UserIdleDetectionMode = IdleDetectionMode.Disabled;
            }

        }

        // 啟動應用程式 (例如，從 [開始]) 時要執行的程式碼
        // 重新啟動應用程式時不會執行這段程式碼
        private void Application_Launching(object sender, LaunchingEventArgs e)
        {
        }

        // 啟動應用程式 (帶到前景) 時要執行的程式碼
        // 第一次啟動應用程式時不會執行這段程式碼
        private void Application_Activated(object sender, ActivatedEventArgs e)
        {
        }

        // 停用應用程式 (移到背景) 時要執行的程式碼
        // 關閉應用程式時不會執行這段程式碼
        private void Application_Deactivated(object sender, DeactivatedEventArgs e)
        {
        }

        // 關閉應用程式 (例如，使用者按 [上一頁]) 時要執行的程式碼
        // 停用應用程式時不會執行這段程式碼
        private void Application_Closing(object sender, ClosingEventArgs e)
        {
        }

        // 巡覽失敗時要執行的程式碼
        private void RootFrame_NavigationFailed(object sender, NavigationFailedEventArgs e)
        {
            if (Debugger.IsAttached)
            {
                // 巡覽失敗; 切換到偵錯工具
                Debugger.Break();
            }
        }

        // 發生未處理的例外狀況時要執行的程式碼
        private void Application_UnhandledException(object sender, ApplicationUnhandledExceptionEventArgs e)
        {
            if (Debugger.IsAttached)
            {
                // 發生未處理的例外狀況; 切換到偵錯工具
                Debugger.Break();
            }
        }

        #region 電話應用程式初始化

        // 避免重複初始化
        private bool phoneApplicationInitialized = false;

        // 請勿在這個方法中加入任何其他程式碼
        private void InitializePhoneApplication()
        {
            if (phoneApplicationInitialized)
                return;

            // 建立畫面，但還不將它設為 RootVisual; 這樣可以讓啟動顯示
            // 畫面保持作用中狀態，直到應用程式準備好呈現為止。
            RootFrame = new PhoneApplicationFrame();
            RootFrame.Navigated += CompleteInitializePhoneApplication;

            // 處理巡覽失敗
            RootFrame.NavigationFailed += RootFrame_NavigationFailed;

            // 處理清除 backstack 的重設要求
            RootFrame.Navigated += CheckForResetNavigation;

            // 確定不會重新初始化
            phoneApplicationInitialized = true;
        }

        // 請勿在這個方法中加入任何其他程式碼
        private void CompleteInitializePhoneApplication(object sender, NavigationEventArgs e)
        {
            // 設定根 Visual，使應用程式能夠呈現
            if (RootVisual != RootFrame)
                RootVisual = RootFrame;

            // 移除這個處理常式，因為已不再需要
            RootFrame.Navigated -= CompleteInitializePhoneApplication;
        }

        private void CheckForResetNavigation(object sender, NavigationEventArgs e)
        {
            // 如果應用程式收到 '重設' 巡覽，則我們需要檢查
            // 在下一次巡覽中查看頁面堆疊是否應該重設
            if (e.NavigationMode == NavigationMode.Reset)
                RootFrame.Navigated += ClearBackStackAfterReset;
        }

        private void ClearBackStackAfterReset(object sender, NavigationEventArgs e)
        {
            // 移除註冊事件，使它不會再次被呼叫
            RootFrame.Navigated -= ClearBackStackAfterReset;

            // 只清除 '新' (下一頁) 和 '重新整理' 巡覽的堆疊
            if (e.NavigationMode != NavigationMode.New && e.NavigationMode != NavigationMode.Refresh)
                return;

            // 為了 UI 的一致性，清除整個頁面堆疊
            while (RootFrame.RemoveBackEntry() != null)
            {
                ; // 不執行任何動作
            }
        }

        #endregion

        // 依照應用程式的當地語系化資源字串的定義，將應用程式的字型和文字方向初始化。
        //
        // 為了確保應用程式的字型與其支援的語言一致，並確保
        // 這些語言的 FlowDirection 都是依照其傳統方向，ResourceLanguage
        // 且 ResourceFlowDirection 應該在每個 resx 檔案中初始化，以符合這些值
        // 檔案的文化特性。例如:
        //
        // AppResources.es-ES.resx
        //    ResourceLanguage 的值必須是 "es-ES"
        //    ResourceFlowDirection 的值必須是 "LeftToRight"
        //
        // AppResources.ar-SA.resx
        //     ResourceLanguage 的值必須是 "ar-SA"
        //     ResourceFlowDirection 的值必須是 "RightToLeft"
        //
        // 如需將 Windows Phone 應用程式當地語系化的詳細資訊，請參閱 http://go.microsoft.com/fwlink/?LinkId=262072。
        //
        private void InitializeLanguage()
        {
            try
            {
                // 設定字型以符合顯示語言，該顯示語言設定於
                // 每個支援的語言的 ResourceLanguage 資源字串。
                //
                // 回復為中性語言的字型，如果顯示
                // 不支援電話的語言。
                //
                // 如果發生編譯器錯誤，則表示以下項目中將遺漏 ResourceLanguage
                // 資源檔。
                RootFrame.Language = XmlLanguage.GetLanguage(AppResources.ResourceLanguage);

                // 設定根畫面下的所有項目的 FlowDirection
                // 在 ResourceFlowDirection 資源字串上，相對於每個
                // 支援的語言。
                //
                // 如果發生編譯器錯誤，則表示以下項目中將遺漏 ResourceFlowDirection
                // 資源檔。
                FlowDirection flow = (FlowDirection)Enum.Parse(typeof(FlowDirection), AppResources.ResourceFlowDirection);
                RootFrame.FlowDirection = flow;
            }
            catch
            {
                // 如果在這裡攔截到例外狀況，最有可能是因為
                // ResourceLangauge 未被正確地設定為支援的語言
                // 代碼，或 ResourceFlowDirection 設定的值不是 LeftToRight
                // 或 RightToLeft。

                if (Debugger.IsAttached)
                {
                    Debugger.Break();
                }

                throw;
            }
        }
    }
}