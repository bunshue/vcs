
namespace GMap.NET.CacheProviders
{
    using System;
    using System.Data;
    using System.Diagnostics;
    using System.IO;
    using GMap.NET;
    using GMap.NET.MapProviders;

    /// <summary>
    /// </summary>
    public class MySQLPureImageCacheMulti : PureImageCache, IDisposable
    {
        string connectionString = string.Empty;
        public string ConnectionString
        {
            get
            {
                return connectionString;
            }
            set
            {
                if (connectionString != value)
                {
                    connectionString = value;
                    initialized = false;
                    Initialize();
                }
            }
        }

        bool initialized = false;

        /// <summary>
        /// is cache initialized
        /// </summary>
        public bool Initialized
        {
            get
            {
                lock (this)
                {
                    return initialized;
                }
            }
            private set
            {
                lock (this)
                {
                    initialized = value;
                }
            }
        }

        /// <summary>
        /// inits connection to server
        /// </summary>
        /// <returns></returns>
        public bool Initialize()
        {
                return initialized;
        }

        #region IDisposable Members

        public void Dispose()
        {
        }
        #endregion

        #region PureImageCache Members
        public bool PutImageToCache(byte[] tile, int type, GPoint pos, int zoom)
        {
            bool ret = true;
            return ret;
        }

        public PureImage GetImageFromCache(int type, GPoint pos, int zoom)
        {
            PureImage ret = null;
            return ret;
        }

        int PureImageCache.DeleteOlderThan(DateTime date, int? type)
        {
            throw new NotImplementedException();
        }
        #endregion
    }
}

