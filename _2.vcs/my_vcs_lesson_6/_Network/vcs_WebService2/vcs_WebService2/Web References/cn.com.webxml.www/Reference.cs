﻿//------------------------------------------------------------------------------
// <auto-generated>
//     這段程式碼是由工具產生的。
//     執行階段版本:4.0.30319.42000
//
//     對這個檔案所做的變更可能會造成錯誤的行為，而且如果重新產生程式碼，
//     變更將會遺失。
// </auto-generated>
//------------------------------------------------------------------------------

// 
// 原始程式碼已由 Microsoft.VSDesigner 自動產生，版本 4.0.30319.42000。
// 
#pragma warning disable 1591

namespace vcs_WebService2.cn.com.webxml.www {
    using System;
    using System.Web.Services;
    using System.Diagnostics;
    using System.Web.Services.Protocols;
    using System.Xml.Serialization;
    using System.ComponentModel;
    using System.Data;
    
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Web.Services.WebServiceBindingAttribute(Name="WeatherWebServiceSoap", Namespace="http://WebXml.com.cn/")]
    public partial class WeatherWebService : System.Web.Services.Protocols.SoapHttpClientProtocol {
        
        private System.Threading.SendOrPostCallback getSupportCityOperationCompleted;
        
        private System.Threading.SendOrPostCallback getSupportProvinceOperationCompleted;
        
        private System.Threading.SendOrPostCallback getSupportDataSetOperationCompleted;
        
        private System.Threading.SendOrPostCallback getWeatherbyCityNameOperationCompleted;
        
        private System.Threading.SendOrPostCallback getWeatherbyCityNameProOperationCompleted;
        
        private bool useDefaultCredentialsSetExplicitly;
        
        /// <remarks/>
        public WeatherWebService() {
            this.Url = global::vcs_WebService2.Properties.Settings.Default.WindowsFormsApplication1wwwww_cn_com_webxml_www_WeatherWebService;
            if ((this.IsLocalFileSystemWebService(this.Url) == true)) {
                this.UseDefaultCredentials = true;
                this.useDefaultCredentialsSetExplicitly = false;
            }
            else {
                this.useDefaultCredentialsSetExplicitly = true;
            }
        }
        
        public new string Url {
            get {
                return base.Url;
            }
            set {
                if ((((this.IsLocalFileSystemWebService(base.Url) == true) 
                            && (this.useDefaultCredentialsSetExplicitly == false)) 
                            && (this.IsLocalFileSystemWebService(value) == false))) {
                    base.UseDefaultCredentials = false;
                }
                base.Url = value;
            }
        }
        
        public new bool UseDefaultCredentials {
            get {
                return base.UseDefaultCredentials;
            }
            set {
                base.UseDefaultCredentials = value;
                this.useDefaultCredentialsSetExplicitly = true;
            }
        }
        
        /// <remarks/>
        public event getSupportCityCompletedEventHandler getSupportCityCompleted;
        
        /// <remarks/>
        public event getSupportProvinceCompletedEventHandler getSupportProvinceCompleted;
        
        /// <remarks/>
        public event getSupportDataSetCompletedEventHandler getSupportDataSetCompleted;
        
        /// <remarks/>
        public event getWeatherbyCityNameCompletedEventHandler getWeatherbyCityNameCompleted;
        
        /// <remarks/>
        public event getWeatherbyCityNameProCompletedEventHandler getWeatherbyCityNameProCompleted;
        
        /// <remarks/>
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://WebXml.com.cn/getSupportCity", RequestNamespace="http://WebXml.com.cn/", ResponseNamespace="http://WebXml.com.cn/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
        public string[] getSupportCity(string byProvinceName) {
            object[] results = this.Invoke("getSupportCity", new object[] {
                        byProvinceName});
            return ((string[])(results[0]));
        }
        
        /// <remarks/>
        public void getSupportCityAsync(string byProvinceName) {
            this.getSupportCityAsync(byProvinceName, null);
        }
        
        /// <remarks/>
        public void getSupportCityAsync(string byProvinceName, object userState) {
            if ((this.getSupportCityOperationCompleted == null)) {
                this.getSupportCityOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetSupportCityOperationCompleted);
            }
            this.InvokeAsync("getSupportCity", new object[] {
                        byProvinceName}, this.getSupportCityOperationCompleted, userState);
        }
        
        private void OngetSupportCityOperationCompleted(object arg) {
            if ((this.getSupportCityCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getSupportCityCompleted(this, new getSupportCityCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        /// <remarks/>
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://WebXml.com.cn/getSupportProvince", RequestNamespace="http://WebXml.com.cn/", ResponseNamespace="http://WebXml.com.cn/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
        public string[] getSupportProvince() {
            object[] results = this.Invoke("getSupportProvince", new object[0]);
            return ((string[])(results[0]));
        }
        
        /// <remarks/>
        public void getSupportProvinceAsync() {
            this.getSupportProvinceAsync(null);
        }
        
        /// <remarks/>
        public void getSupportProvinceAsync(object userState) {
            if ((this.getSupportProvinceOperationCompleted == null)) {
                this.getSupportProvinceOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetSupportProvinceOperationCompleted);
            }
            this.InvokeAsync("getSupportProvince", new object[0], this.getSupportProvinceOperationCompleted, userState);
        }
        
        private void OngetSupportProvinceOperationCompleted(object arg) {
            if ((this.getSupportProvinceCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getSupportProvinceCompleted(this, new getSupportProvinceCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        /// <remarks/>
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://WebXml.com.cn/getSupportDataSet", RequestNamespace="http://WebXml.com.cn/", ResponseNamespace="http://WebXml.com.cn/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
        public System.Data.DataSet getSupportDataSet() {
            object[] results = this.Invoke("getSupportDataSet", new object[0]);
            return ((System.Data.DataSet)(results[0]));
        }
        
        /// <remarks/>
        public void getSupportDataSetAsync() {
            this.getSupportDataSetAsync(null);
        }
        
        /// <remarks/>
        public void getSupportDataSetAsync(object userState) {
            if ((this.getSupportDataSetOperationCompleted == null)) {
                this.getSupportDataSetOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetSupportDataSetOperationCompleted);
            }
            this.InvokeAsync("getSupportDataSet", new object[0], this.getSupportDataSetOperationCompleted, userState);
        }
        
        private void OngetSupportDataSetOperationCompleted(object arg) {
            if ((this.getSupportDataSetCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getSupportDataSetCompleted(this, new getSupportDataSetCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        /// <remarks/>
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://WebXml.com.cn/getWeatherbyCityName", RequestNamespace="http://WebXml.com.cn/", ResponseNamespace="http://WebXml.com.cn/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
        public string[] getWeatherbyCityName(string theCityName) {
            object[] results = this.Invoke("getWeatherbyCityName", new object[] {
                        theCityName});
            return ((string[])(results[0]));
        }
        
        /// <remarks/>
        public void getWeatherbyCityNameAsync(string theCityName) {
            this.getWeatherbyCityNameAsync(theCityName, null);
        }
        
        /// <remarks/>
        public void getWeatherbyCityNameAsync(string theCityName, object userState) {
            if ((this.getWeatherbyCityNameOperationCompleted == null)) {
                this.getWeatherbyCityNameOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetWeatherbyCityNameOperationCompleted);
            }
            this.InvokeAsync("getWeatherbyCityName", new object[] {
                        theCityName}, this.getWeatherbyCityNameOperationCompleted, userState);
        }
        
        private void OngetWeatherbyCityNameOperationCompleted(object arg) {
            if ((this.getWeatherbyCityNameCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getWeatherbyCityNameCompleted(this, new getWeatherbyCityNameCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        /// <remarks/>
        [System.Web.Services.Protocols.SoapDocumentMethodAttribute("http://WebXml.com.cn/getWeatherbyCityNamePro", RequestNamespace="http://WebXml.com.cn/", ResponseNamespace="http://WebXml.com.cn/", Use=System.Web.Services.Description.SoapBindingUse.Literal, ParameterStyle=System.Web.Services.Protocols.SoapParameterStyle.Wrapped)]
        public string[] getWeatherbyCityNamePro(string theCityName, string theUserID) {
            object[] results = this.Invoke("getWeatherbyCityNamePro", new object[] {
                        theCityName,
                        theUserID});
            return ((string[])(results[0]));
        }
        
        /// <remarks/>
        public void getWeatherbyCityNameProAsync(string theCityName, string theUserID) {
            this.getWeatherbyCityNameProAsync(theCityName, theUserID, null);
        }
        
        /// <remarks/>
        public void getWeatherbyCityNameProAsync(string theCityName, string theUserID, object userState) {
            if ((this.getWeatherbyCityNameProOperationCompleted == null)) {
                this.getWeatherbyCityNameProOperationCompleted = new System.Threading.SendOrPostCallback(this.OngetWeatherbyCityNameProOperationCompleted);
            }
            this.InvokeAsync("getWeatherbyCityNamePro", new object[] {
                        theCityName,
                        theUserID}, this.getWeatherbyCityNameProOperationCompleted, userState);
        }
        
        private void OngetWeatherbyCityNameProOperationCompleted(object arg) {
            if ((this.getWeatherbyCityNameProCompleted != null)) {
                System.Web.Services.Protocols.InvokeCompletedEventArgs invokeArgs = ((System.Web.Services.Protocols.InvokeCompletedEventArgs)(arg));
                this.getWeatherbyCityNameProCompleted(this, new getWeatherbyCityNameProCompletedEventArgs(invokeArgs.Results, invokeArgs.Error, invokeArgs.Cancelled, invokeArgs.UserState));
            }
        }
        
        /// <remarks/>
        public new void CancelAsync(object userState) {
            base.CancelAsync(userState);
        }
        
        private bool IsLocalFileSystemWebService(string url) {
            if (((url == null) 
                        || (url == string.Empty))) {
                return false;
            }
            System.Uri wsUri = new System.Uri(url);
            if (((wsUri.Port >= 1024) 
                        && (string.Compare(wsUri.Host, "localHost", System.StringComparison.OrdinalIgnoreCase) == 0))) {
                return true;
            }
            return false;
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    public delegate void getSupportCityCompletedEventHandler(object sender, getSupportCityCompletedEventArgs e);
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class getSupportCityCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getSupportCityCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        /// <remarks/>
        public string[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string[])(this.results[0]));
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    public delegate void getSupportProvinceCompletedEventHandler(object sender, getSupportProvinceCompletedEventArgs e);
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class getSupportProvinceCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getSupportProvinceCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        /// <remarks/>
        public string[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string[])(this.results[0]));
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    public delegate void getSupportDataSetCompletedEventHandler(object sender, getSupportDataSetCompletedEventArgs e);
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class getSupportDataSetCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getSupportDataSetCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        /// <remarks/>
        public System.Data.DataSet Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((System.Data.DataSet)(this.results[0]));
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    public delegate void getWeatherbyCityNameCompletedEventHandler(object sender, getWeatherbyCityNameCompletedEventArgs e);
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class getWeatherbyCityNameCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getWeatherbyCityNameCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        /// <remarks/>
        public string[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string[])(this.results[0]));
            }
        }
    }
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    public delegate void getWeatherbyCityNameProCompletedEventHandler(object sender, getWeatherbyCityNameProCompletedEventArgs e);
    
    /// <remarks/>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.Web.Services", "4.8.4084.0")]
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    public partial class getWeatherbyCityNameProCompletedEventArgs : System.ComponentModel.AsyncCompletedEventArgs {
        
        private object[] results;
        
        internal getWeatherbyCityNameProCompletedEventArgs(object[] results, System.Exception exception, bool cancelled, object userState) : 
                base(exception, cancelled, userState) {
            this.results = results;
        }
        
        /// <remarks/>
        public string[] Result {
            get {
                this.RaiseExceptionIfNecessary();
                return ((string[])(this.results[0]));
            }
        }
    }
}

#pragma warning restore 1591