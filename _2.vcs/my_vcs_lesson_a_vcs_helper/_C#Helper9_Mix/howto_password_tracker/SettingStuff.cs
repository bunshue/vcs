using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Windows.Forms;
using Microsoft.Win32;

namespace howto_password_tracker
{
    public static class SettingStuff
    {
        public static string APP_NAME = Application.ProductName;

        // Save the form's size and position.
        public static void SaveFormPosition(Form frm, string section_name)
        {
            SaveFormPosition(frm, APP_NAME, section_name);
        }
        public static void SaveFormPosition(Form frm, string app_name, string section_name)
        {
            SaveSetting(app_name, section_name, "WindowState", (int)frm.WindowState);

            if (frm.WindowState == FormWindowState.Normal)
            {
                SaveSetting(app_name, section_name, "Left", frm.Left);
                SaveSetting(app_name, section_name, "Top", frm.Top);
                SaveSetting(app_name, section_name, "Width", frm.Width);
                SaveSetting(app_name, section_name, "Height", frm.Height);
            }
            else
            {
                SaveSetting(app_name, section_name, "Left", frm.RestoreBounds.Left);
                SaveSetting(app_name, section_name, "Top", frm.RestoreBounds.Top);
                SaveSetting(app_name, section_name, "Width", frm.RestoreBounds.Width);
                SaveSetting(app_name, section_name, "Height", frm.RestoreBounds.Height);
            }
        }

        // Restore the form's size and position.
        public static void RestoreFormPosition(Form frm, string section_name)
        {
            RestoreFormPosition(frm, APP_NAME, section_name);
        }
        public static void RestoreFormPosition(Form frm, string app_name, string section_name)
        {
            frm.SetBounds(
                GetSetting(app_name, section_name, "Left", frm.RestoreBounds.Left),
                GetSetting(app_name, section_name, "Top", frm.RestoreBounds.Top),
                GetSetting(app_name, section_name, "Width", frm.RestoreBounds.Width),
                GetSetting(app_name, section_name, "Height", frm.RestoreBounds.Height)
            );
            int window_state = GetSetting(app_name, section_name, "WindowState", (int)frm.WindowState);
            frm.WindowState = (FormWindowState)window_state;
        }

        // Save a DataGridView's column widths.
        public static void SaveDgvSettings(DataGridView dgv, string section_name)
        {
            SaveDgvSettings(dgv, APP_NAME, section_name);
        }
        public static void SaveDgvSettings(DataGridView dgv, string app_name, string section_name)
        {
            for (int i = 0; i < dgv.ColumnCount; i++)
            {
                SaveSetting(app_name, section_name,
                    "DgvColWidth" + i.ToString(),
                    dgv.Columns[i].Width);
            }
        }

        // Restore a DataGridView's column widths.
        public static void RestoreDgvSettings(DataGridView dgv, string section_name)
        {
            RestoreDgvSettings(dgv, APP_NAME, section_name);
        }
        public static void RestoreDgvSettings(DataGridView dgv, string app_name, string section_name)
        {
            for (int i = 0; i < dgv.ColumnCount; i++)
            {
                dgv.Columns[i].Width =
                    GetSetting(app_name, section_name,
                        "DgvColWidth" + i.ToString(),
                        dgv.Columns[i].Width);
            }
        }

        // Save a value.
        public static void SaveSetting<T>(string app_name, string section_name, string name, T value)
        {
            string key_name = KeyName(app_name, section_name);
            using (RegistryKey reg_key = Registry.CurrentUser.CreateSubKey(key_name))
            {
                reg_key.SetValue(name, value);
            }
        }

        // Delete a setting.
        public static void DeleteSettingSection(string app_name, string section_name)
        {
            string key_name = "Software\\C# Programs\\" + app_name;
            using (RegistryKey reg_key = Registry.CurrentUser.OpenSubKey(key_name, true))
            {
                reg_key.DeleteSubKeyTree(section_name, false);
            }
        }

        // Get a value.
        public static T GetSetting<T>(string app_name, string section_name, string name, T default_value)
        {
            string key_name = KeyName(app_name, section_name);
            using (RegistryKey reg_key = Registry.CurrentUser.OpenSubKey(key_name, false))
            {
                if (reg_key == null) return default_value;
                return (T)reg_key.GetValue(name, default_value);
            }
        }

        // Compose a key name.
        private static string KeyName(string app_name, string section_name)
        {
            return "Software\\C# Programs\\" + app_name + "\\" + section_name;
        }
    }
}
