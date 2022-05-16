using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using log4net;

namespace GMapPOI
{
    public class MySQLPoiCache
    {
        private static readonly ILog log = LogManager.GetLogger(typeof(MySQLPoiCache));

        public MySQLPoiCache(string connString)
        {
            this.ConnectionString = connString;
        }

        private string connectionString = string.Empty;
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

                    if (Initialized)
                    {
                        Initialize();
                    }
                }
            }
        }

        bool initialized = false;
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

        public bool Initialize()
        {
            lock (this)
            {
                if (!initialized)
                {
                }
                return initialized;
            }
        }

        public bool PutPoiDataToCache(PoiData data)
        {
            try
            {
                if (!Initialized)
                {
                    this.Initialize();
                }

                return true;
            }
            catch (Exception ex)
            {
                return false;
                log.Error(ex);
            }
        }
    }
}
