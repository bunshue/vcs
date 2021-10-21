using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace vcs_StartupScreen
{
    static class Program
    {
        /// <summary>
        /// 應用程式的主要進入點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            // 啟動  
            StartupScreen.ShowSplashScreen();

            // 進行自己的操作：加載組件，加載文件等等  
            // 示例代碼為休眠一會  
            System.Threading.Thread.Sleep(3000);

            // 關閉  
            if (StartupScreen.Instance != null)
            {
                StartupScreen.Instance.BeginInvoke(new MethodInvoker(StartupScreen.Instance.Dispose));
                StartupScreen.Instance = null;
            } 

            Application.Run(new Form1());
        }
    }
}
