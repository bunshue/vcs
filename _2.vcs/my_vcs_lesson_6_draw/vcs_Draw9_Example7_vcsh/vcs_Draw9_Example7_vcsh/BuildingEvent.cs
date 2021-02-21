using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Draw9_Example7_vcsh
{
    public class BuildingEvent : IComparable<BuildingEvent>
    {
        public enum EventTypes
        {
            Start,
            End
        };
        public int X;
        public EventTypes EventType;
        public int BuildingIndex;
        public BuildingEvent(int x, EventTypes event_type, int building_index)
        {
            X = x;
            EventType = event_type;
            BuildingIndex = building_index;
        }

        public int CompareTo(BuildingEvent other)
        {
            return X.CompareTo(other.X);
        }
    }
}
