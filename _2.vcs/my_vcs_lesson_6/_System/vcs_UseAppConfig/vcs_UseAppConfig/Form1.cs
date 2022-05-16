using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

using System.Configuration; //參考/加入參考/.Net/System.Configuration 


/*
使用.NetFramework4內建的App.Config

目標Framework 改成 .Net Framework 4
出現app.config

修改app.config
並在Form1_Load使用 

*/

namespace vcs_UseAppConfig
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
            richTextBox1.Text += "取得 app.config 的設定值\n";

            string ip = ConfigHelper.GetAppConfig("MySQLServerIP");
            string port = ConfigHelper.GetAppConfig("MySQLServerPort");
            string dbName = ConfigHelper.GetAppConfig("Database");
            string userID = ConfigHelper.GetAppConfig("UserID");
            string password = ConfigHelper.GetAppConfig("Password");
            string retryStr = ConfigHelper.GetAppConfig("Retry");
            string center = ConfigHelper.GetAppConfig("MapCenter");
            string[] centerPoints = center.Split(',');
            string tilePath = ConfigHelper.GetAppConfig("TilePath");

            richTextBox1.Text += "ip : " + ip + "\n";
            richTextBox1.Text += "port : " + port + "\n";
            richTextBox1.Text += "dbName : " + dbName + "\n";
            richTextBox1.Text += "userID : " + userID + "\n";
            richTextBox1.Text += "password : " + password + "\n";
            richTextBox1.Text += "retryStr : " + retryStr + "\n";
            richTextBox1.Text += "center : " + center + "\n";
            //richTextBox1.Text += "centerPoints : " + centerPoints + "\n";
            richTextBox1.Text += "tilePath : " + tilePath + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }

    public static class ConfigHelper
    {
        //依据连接串名字connectionName返回数据连接字符串  
        public static string GetConnectionStringsConfig(string connectionName)
        {
            //指定config文件读取
            string file = System.Windows.Forms.Application.ExecutablePath;
            System.Configuration.Configuration config = ConfigurationManager.OpenExeConfiguration(file);
            string connectionString =
                config.ConnectionStrings.ConnectionStrings[connectionName].ConnectionString.ToString();
            return connectionString;
        }

        ///<summary> 
        ///更新连接字符串  
        ///</summary> 
        ///<param name="newName">连接字符串名称</param> 
        ///<param name="newConString">连接字符串内容</param> 
        ///<param name="newProviderName">数据提供程序名称</param> 
        public static void UpdateConnectionStringsConfig(string newName, string newConString, string newProviderName)
        {
            //指定config文件读取
            string file = System.Windows.Forms.Application.ExecutablePath;
            Configuration config = ConfigurationManager.OpenExeConfiguration(file);

            bool exist = false; //记录该连接串是否已经存在  
            //如果要更改的连接串已经存在  
            if (config.ConnectionStrings.ConnectionStrings[newName] != null)
            {
                exist = true;
            }
            // 如果连接串已存在，首先删除它  
            if (exist)
            {
                config.ConnectionStrings.ConnectionStrings.Remove(newName);
            }
            //新建一个连接字符串实例  
            ConnectionStringSettings mySettings =
                new ConnectionStringSettings(newName, newConString, newProviderName);
            // 将新的连接串添加到配置文件中.  
            config.ConnectionStrings.ConnectionStrings.Add(mySettings);
            // 保存对配置文件所作的更改  
            config.Save(ConfigurationSaveMode.Modified);
            // 强制重新载入配置文件的ConnectionStrings配置节  
            ConfigurationManager.RefreshSection("ConnectionStrings");
        }

        ///<summary> 
        ///返回*.exe.config文件中appSettings配置节的value项  
        ///</summary> 
        ///<param name="strKey"></param> 
        ///<returns></returns> 
        public static string GetAppConfig(string strKey)
        {
            string file = System.Windows.Forms.Application.ExecutablePath;
            Configuration config = ConfigurationManager.OpenExeConfiguration(file);
            foreach (string key in config.AppSettings.Settings.AllKeys)
            {
                if (key == strKey)
                {
                    return config.AppSettings.Settings[strKey].Value.ToString();
                }
            }
            return null;
        }

        ///<summary>  
        ///在*.exe.config文件中appSettings配置节增加一对键值对  
        ///</summary>  
        ///<param name="newKey"></param>  
        ///<param name="newValue"></param>  
        public static void UpdateAppConfig(string newKey, string newValue)
        {
            string file = System.Windows.Forms.Application.ExecutablePath;
            Configuration config = ConfigurationManager.OpenExeConfiguration(file);
            bool exist = false;
            foreach (string key in config.AppSettings.Settings.AllKeys)
            {
                if (key == newKey)
                {
                    exist = true;
                }
            }
            if (exist)
            {
                config.AppSettings.Settings.Remove(newKey);
            }
            config.AppSettings.Settings.Add(newKey, newValue);
            config.Save(ConfigurationSaveMode.Modified);
            ConfigurationManager.RefreshSection("appSettings");
        }

        // 修改system.serviceModel下所有服务终结点的IP地址
        public static void UpdateServiceModelConfig(string configPath, string serverIP)
        {
            Configuration config = ConfigurationManager.OpenExeConfiguration(configPath);
            ConfigurationSectionGroup sec = config.SectionGroups["system.serviceModel"];
            /*
            ServiceModelSectionGroup serviceModelSectionGroup = sec as ServiceModelSectionGroup;
            ClientSection clientSection = serviceModelSectionGroup.Client;
            foreach (ChannelEndpointElement item in clientSection.Endpoints)
            {
                string pattern = @"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b";
                string address = item.Address.ToString();
                string replacement = string.Format("{0}", serverIP);
                address = Regex.Replace(address, pattern, replacement);
                item.Address = new Uri(address);
            }

            config.Save(ConfigurationSaveMode.Modified);
            ConfigurationManager.RefreshSection("system.serviceModel");
            */
        }

        // 修改applicationSettings中App.Properties.Settings中服务的IP地址
        public static void UpdateConfig(string configPath, string serverIP)
        {
            Configuration config = ConfigurationManager.OpenExeConfiguration(configPath);
            ConfigurationSectionGroup sec = config.SectionGroups["applicationSettings"];
            ConfigurationSection configSection = sec.Sections["DataService.Properties.Settings"];
            ClientSettingsSection clientSettingsSection = configSection as ClientSettingsSection;
            if (clientSettingsSection != null)
            {
                SettingElement element1 = clientSettingsSection.Settings.Get("DataService_SystemManagerWS_SystemManagerWS");
                if (element1 != null)
                {
                    clientSettingsSection.Settings.Remove(element1);
                    string oldValue = element1.Value.ValueXml.InnerXml;
                    element1.Value.ValueXml.InnerXml = GetNewIP(oldValue, serverIP);
                    clientSettingsSection.Settings.Add(element1);
                }

                SettingElement element2 = clientSettingsSection.Settings.Get("DataService_EquipManagerWS_EquipManagerWS");
                if (element2 != null)
                {
                    clientSettingsSection.Settings.Remove(element2);
                    string oldValue = element2.Value.ValueXml.InnerXml;
                    element2.Value.ValueXml.InnerXml = GetNewIP(oldValue, serverIP);
                    clientSettingsSection.Settings.Add(element2);
                }
            }
            config.Save(ConfigurationSaveMode.Modified);
            ConfigurationManager.RefreshSection("applicationSettings");
        }

        private static string GetNewIP(string oldValue, string serverIP)
        {
            string pattern = @"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b";
            string replacement = string.Format("{0}", serverIP);
            string newvalue = Regex.Replace(oldValue, pattern, replacement);
            return newvalue;
        }
    }
}
