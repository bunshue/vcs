using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace howto_covid19_align_starts
{
    public class CountryDataComparer : IComparer<CountryData>
    {
        public enum CompareTypes
        {
            ByName,
            ByMaxCases,
        }
        private CompareTypes CompareType = CompareTypes.ByName;

        public CountryDataComparer(CompareTypes type)
        {
            CompareType = type;
        }

        public int Compare(CountryData x, CountryData y)
        {
            switch (CompareType)
            {
                case CompareTypes.ByName:
                    return x.Name.CompareTo(y.Name);
                case CompareTypes.ByMaxCases:
                default:
                    return -x.MaxCases.CompareTo(y.MaxCases);
            }
        }
    }
}
