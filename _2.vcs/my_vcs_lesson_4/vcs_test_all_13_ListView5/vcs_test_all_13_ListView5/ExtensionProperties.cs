using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_13_ListView5
{
    public static class ExtensionProperties
    {
        // Storage for the properties.
        private static Dictionary<object, Dictionary<string, object>> PropertyValues =
                   new Dictionary<object, Dictionary<string, object>>();

        // Set a property value for the item.
        public static void SetValue(this object item, string name, object value)
        {
            // If we don't have a dictionary for this item yet, make one.
            if (!PropertyValues.ContainsKey(item))
                PropertyValues[item] = new Dictionary<string, object>();

            // Set the value in the item's dictionary.
            PropertyValues[item][name] = value;
        }

        // Return a property value for the item.
        public static object GetValue(this object item, string name, object default_value)
        {
            // If we don't have a dictionary for
            // this item yet, return the default value.
            if (!PropertyValues.ContainsKey(item)) return default_value;

            // If the value isn't in the dictionary,
            // return the default value.
            if (!PropertyValues[item].ContainsKey(name)) return default_value;

            // Return the saved value.
            return PropertyValues[item][name];
        }

        // Remove the property.
        public static void RemoveValue(this object item, string name)
        {
            // If we don't have a dictionary for this item, do nothing.
            if (!PropertyValues.ContainsKey(item)) return;

            // If the value isn't in the dictionary, do nothing.
            if (!PropertyValues[item].ContainsKey(name)) return;

            // Remove the value.
            PropertyValues[item].Remove(name);
        }
    }
}
