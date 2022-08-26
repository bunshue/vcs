using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace howto_k_means
{
    public class PointData
    {
        public PointF Location;
        public int ClusterNum;
        public PointData(PointF location, int cluster_num)
        {
            Location = location;
            ClusterNum = cluster_num;
        }
        public PointData(float x, float y, int set)
            : this(new PointF(x, y), set)
        {
        }
    }
}
