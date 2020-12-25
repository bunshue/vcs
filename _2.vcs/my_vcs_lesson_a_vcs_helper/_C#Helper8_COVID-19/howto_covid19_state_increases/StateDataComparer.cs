using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace howto_covid19_state_increases
{
    public class StateDataComparer : IComparer<StateData>
    {
        public enum CompareTypes
        {
            ByName,
            ByMaxCases,
        }
        private CompareTypes CompareType = CompareTypes.ByName;

        public StateDataComparer(CompareTypes type)
        {
            CompareType = type;
        }

        public int Compare(StateData x, StateData y)
        {
            switch (CompareType)
            {
                case CompareTypes.ByName:
                    return x.Name.CompareTo(y.Name);
                case CompareTypes.ByMaxCases:
                default:
                    return -x.MaxDataValue.CompareTo(y.MaxDataValue);
            }
        }
    }
}
