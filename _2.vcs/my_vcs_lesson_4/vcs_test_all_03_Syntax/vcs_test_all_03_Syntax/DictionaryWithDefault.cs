using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_test_all_03_Syntax
{
    class DictionaryWithDefault<TKey, TValue>
    {
        // Store items here.
        private Dictionary<TKey, TValue> Entries
            = new Dictionary<TKey, TValue>(); 

        // The default value.
        private TValue DefaultValue;

        // Constructor.
        public DictionaryWithDefault(TValue default_value)
        {
            DefaultValue = default_value;
        }

        // Make the indexer property.
        public TValue this[TKey key]
        {
            get
            {
                // Return the value for this key or the default value.
                if (Entries.ContainsKey(key)) return Entries[key];
                return DefaultValue;
            }
            set
            {
                // Set the property's value for the key.
                Entries.Add(key, value);
            }
        }
    }
}
