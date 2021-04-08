using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.IO;

namespace vcs_PictureMontageHex
{
    public class Hexagon
    {
        public int Row, Column;
        public Bitmap Picture;
        public string FileName;
        public Hexagon(int row, int column, Bitmap picture, string file_name)
        {
            Row = row;
            Column = column;
            Picture = picture;

            // Remove the file path.
            FileInfo file_info = new FileInfo(file_name);
            FileName = file_info.Name;
        }
    }
}
