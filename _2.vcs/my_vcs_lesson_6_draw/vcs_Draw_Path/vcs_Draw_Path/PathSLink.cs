using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Draw_Path
{
    class PathSLink
    {
        public enum LinkUseageType
        {
            Unused,
            InTree,
            InPath
        }

        public PathSNode Node1, Node2;
        public int Cost;
        public LinkUseageType LinkUsage = LinkUseageType.Unused;
    }
}
