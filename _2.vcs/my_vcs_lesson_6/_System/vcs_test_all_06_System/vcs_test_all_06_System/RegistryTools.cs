using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Microsoft.Win32;

namespace vcs_test_all_06_System
{
    class RegistryTools
    {
        // Get a registry value.
        public static object GetRegistryValue(RegistryKey hive, string subkey_name, string value_name, object default_value)
        {
            RegistryKey subkey = hive.OpenSubKey(subkey_name, false);
            object result = subkey.GetValue(value_name, default_value);
            subkey.Close();
            return result;
        }

        // Set a registry value.
        public static void SetRegistryValue(RegistryKey hive, string subkey_name, string value_name, object value)
        {
            RegistryKey subkey = hive.OpenSubKey(subkey_name, true);
            subkey.SetValue(value_name, value);
            subkey.Close();
        }
    }
}
