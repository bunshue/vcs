using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_DrawA_Radar
{
    public class AxisInfo
    {
        public string Name, FormatString;
        public float Min, Max;

        public AxisInfo(string name, string format_string, float min, float max)
        {
            Name = name;
            FormatString = format_string;
            Min = min;
            Max = max;
        }
    }
}
