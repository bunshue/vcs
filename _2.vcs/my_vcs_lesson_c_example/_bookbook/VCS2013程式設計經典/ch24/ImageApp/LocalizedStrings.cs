using ImageApp.Resources;

namespace ImageApp
{
    /// <summary>
    /// 提供字串資源的存取權。
    /// </summary>
    public class LocalizedStrings
    {
        private static AppResources _localizedResources = new AppResources();

        public AppResources LocalizedResources { get { return _localizedResources; } }
    }
}