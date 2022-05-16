using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Text;
using GMap.NET;
using GMap.NET.MapProviders;
using log4net;
using System.Windows.Forms;
using System.Data;
using GMap.NET.WindowsForms;
using GMapProvidersExt.Baidu;

namespace GMapExport
{
    public class TileExport
    {
        private static readonly ILog log = LogManager.GetLogger(typeof(TileExport));

        private BackgroundWorker worker = new BackgroundWorker();

        public event EventHandler<TileExportEventArgs> TileExportStart;
        public event EventHandler<TileExportEventArgs> TileExportComplete;
        public event EventHandler<TileExportEventArgs> TileExportProgress;

        private string connString;
        private ExportParameter exportParameter;
        private GMapProvider mapProvider;

        public TileExport()
        {
            worker.WorkerReportsProgress = true;
            worker.WorkerSupportsCancellation = true;
            worker.ProgressChanged += new ProgressChangedEventHandler(worker_ProgressChanged);
            worker.DoWork += new DoWorkEventHandler(worker_DoWork);
            worker.RunWorkerCompleted += new RunWorkerCompletedEventHandler(worker_RunWorkerCompleted);
        }

        public bool IsBusy
        {
            get { return worker.IsBusy; }
        }

        public void Start(ExportParameter exportParameter, string mysqlConnString)
        {
        }

        public void Stop()
        {
            if (worker.IsBusy)
            {
                worker.CancelAsync();
            }
        }

        #region Background Worker

        void worker_DoWork(object sender, DoWorkEventArgs e)
        {
        }

        public void RectifyBaiduOrTMSTile(PureImage img, int zoom, GPoint p)
        {
            long y = this.mapProvider.Projection.FromLatLngToTileXY(this.mapProvider.Projection.Bounds.Top, this.mapProvider.Projection.Bounds.Left, zoom).Y;
            long y0 = this.mapProvider.Projection.FromLatLngToTileXY(this.mapProvider.Projection.Bounds.Bottom, this.mapProvider.Projection.Bounds.Right, zoom).Y;

            if (this.exportParameter.ExportType == ExportType.TMSTile)
            {
                long p_y = (y + y0) - p.Y;
                p.Y = p_y;
            }
            else if (this.exportParameter.ExportType == ExportType.BaiduTile)
            {
                long p_x;
                long p_y;
                long x = this.mapProvider.Projection.FromLatLngToTileXY(this.mapProvider.Projection.Bounds.LocationTopLeft, zoom).X;
                long x0 = this.mapProvider.Projection.FromLatLngToTileXY(this.mapProvider.Projection.Bounds.LocationRightBottom, zoom).X;
                if (this.mapProvider is BaiduMapProviderBase)
                {
                    int num = Convert.ToInt32(Math.Pow(2.0, (double)(zoom - 1)));
                    p_x = p.X - num;
                    p_y = (num - p.Y) - 1;
                }
                else
                {
                    long delta_x = (x0 - y) + 1;
                    long delta_y = (y0 - y) + 1;
                    p_x = p.X - (delta_x / 2);
                    p_y = (p.Y + 1) - (delta_y / 2);
                }
                p.X = p_x;
                p.Y = p_y;
            }
        }

        private string BuildTileExportPath(PureImage img, int zoom, GPoint p)
        {
            string tileSuffix = "png";
            if (this.exportParameter.ExportType == ExportType.ArcGISTile)
            {
                DirectoryInfo dir = new DirectoryInfo(exportParameter.ExportPath + "/Layer/_alllayers");
                string zoomStr = string.Format("{0:D2}", zoom);
                long x = p.X;
                long y = p.Y;
                string col = string.Format("{0:x8}", x).ToLower();
                string row = string.Format("{0:x8}", y).ToLower();
                string pathDir = dir.FullName + "/" + "L" + zoomStr + "/" + "R" + row + "/";
                string path = pathDir + "C" + col + "."+tileSuffix;
                return path;
            }
            if ((this.exportParameter.ExportType == ExportType.TMSTile) || (this.exportParameter.ExportType == ExportType.BaiduTile))
            {
                RectifyBaiduOrTMSTile(img, zoom, p);
            }
            if (exportParameter.ExportType == ExportType.DefaultYXTile)
            {
                return string.Format("{0}/{1}/{2}/{3}/{4}.{5}", new object[] { this.exportParameter.ExportPath, "tiles", zoom, p.Y, p.X, tileSuffix });
            }

            return string.Format("{0}/{1}/{2}/{3}/{4}.{5}", new object[] { this.exportParameter.ExportPath, "tiles", zoom, p.X, p.Y, tileSuffix });
        }

        private void WriteTileToDisk(PureImage img, int zoom, GPoint p)
        {
            string path = BuildTileExportPath(img, zoom, p);
            string pathDir = path.Substring(0, path.LastIndexOf('/'));
            if (!Directory.Exists(pathDir))
            {
                Directory.CreateDirectory(pathDir);
            }
            FileStream fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write);
            BinaryWriter sw = new BinaryWriter(fs);
            //读出图片字节数组至byte[]
            byte[] imageByte = img.Data.ToArray();
            sw.Write(imageByte);
            sw.Close();
            fs.Close();
        }

        void worker_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            if (e != null)
            {
                if (this.TileExportProgress != null)
                {
                    TileExportProgress(this, e.UserState as TileExportEventArgs);
                }
            }
        }

        void worker_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (this.TileExportComplete != null)
            {
                TileExportComplete(this, new TileExportEventArgs());
            }
        }

        #endregion
    }
}
