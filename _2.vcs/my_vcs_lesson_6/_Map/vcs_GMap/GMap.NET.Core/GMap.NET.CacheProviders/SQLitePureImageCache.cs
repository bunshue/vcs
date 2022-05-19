
namespace GMap.NET.CacheProviders
{
#if SQLite

   using System.Collections.Generic;
   using System.Data.Common;
   using System.IO;
   using System.Text;
   using System;
   using System.Diagnostics;
   using System.Globalization;
   using GMap.NET.MapProviders;
   using System.Threading;

   /// <summary>
   /// ultra fast cache system for tiles
   /// </summary>
   public class SQLitePureImageCache : PureImageCache
   {
#if !PocketPC
#if !MONO
      static SQLitePureImageCache()
      {
         AppDomain.CurrentDomain.AssemblyResolve += new ResolveEventHandler(CurrentDomain_AssemblyResolve);
      }

      static System.Reflection.Assembly CurrentDomain_AssemblyResolve(object sender, ResolveEventArgs args)
      {
         return null;
      }

      static int ping = 0;

      /// <summary>
      /// </summary>
      public static void Ping()
      {
      }
#endif
#endif

      string cache;
      string gtileCache;
      string dir;
      string db;
      bool Created = false;

      public string GtileCache
      {
         get
         {
            return gtileCache;
         }
      }

      /// <summary>
      /// local cache location
      /// </summary>
      public string CacheLocation
      {
         get
         {
            return cache;
         }
         set
         {
            cache = value;

            gtileCache = Path.Combine(cache, "TileDBv5") + Path.DirectorySeparatorChar;

            dir = gtileCache + GMapProvider.LanguageStr + Path.DirectorySeparatorChar;

            // precreate dir
            if(!Directory.Exists(dir))
            {
               Directory.CreateDirectory(dir);
            }

            // make empty db
            {
               db = dir + "Data.gmdb";

               if(!File.Exists(db))
               {
                  Created = CreateEmptyDB(db);
               }
               else
               {
                  Created = AlterDBAddTimeColumn(db);
               }

               CheckPreAllocation();
            }

            // clear old attachments
            AttachedCaches.Clear();
            RebuildFinnalSelect();

            // attach all databases from main cache location
#if !PocketPC
            var dbs = Directory.GetFiles(dir, "*.gmdb", SearchOption.AllDirectories);
#else
            var dbs = Directory.GetFiles(dir, "*.gmdb");
#endif
            foreach(var d in dbs)
            {
               if(d != db)
               {
                  Attach(d);
               }
            }
         }
      }

      /// <summary>
      /// pre-allocate 32MB free space 'ahead' if needed,
      /// decreases fragmentation
      /// </summary>
      void CheckPreAllocation()
      {
         {
            byte[] pageSizeBytes = new byte[2];
            byte[] freePagesBytes = new byte[4];

            lock(this)
            {
               using(var dbf = File.Open(db, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
               {
                  dbf.Seek(16, SeekOrigin.Begin);

#if (!PocketPC && !MONO)
                  dbf.Lock(16, 2);
                  dbf.Read(pageSizeBytes, 0, 2);
                  dbf.Unlock(16, 2);

                  dbf.Seek(36, SeekOrigin.Begin);

                  dbf.Lock(36, 4);
                  dbf.Read(freePagesBytes, 0, 4);
                  dbf.Unlock(36, 4);
#else
                  dbf.Read(pageSizeBytes, 0, 2);
                  dbf.Seek(36, SeekOrigin.Begin);
                  dbf.Read(freePagesBytes, 0, 4);
#endif

                  dbf.Close();
               }
            }

            if(BitConverter.IsLittleEndian)
            {
               Array.Reverse(pageSizeBytes);
               Array.Reverse(freePagesBytes);
            }
            UInt16 pageSize = BitConverter.ToUInt16(pageSizeBytes, 0);
            UInt32 freePages = BitConverter.ToUInt32(freePagesBytes, 0);

            var freeMB = (pageSize * freePages) / (1024.0 * 1024.0);

#if !PocketPC
            int addSizeMB = 32;
            int waitUntilMB = 4;
#else
            int addSizeMB = 4; // reduce due to test in emulator
            int waitUntilMB = 2;
#endif

            Debug.WriteLine("FreePageSpace in cache: " + freeMB + "MB | " + freePages + " pages");

            if(freeMB <= waitUntilMB)
            {
               PreAllocateDB(db, addSizeMB);
            }
         }
      }

      #region -- import / export --
      public static bool CreateEmptyDB(string file)
      {
         bool ret = true;

         return ret;
      }

      public static bool PreAllocateDB(string file, int addSizeInMBytes)
      {
         bool ret = true;

         return ret;
      }

      private static bool AlterDBAddTimeColumn(string file)
      {
         bool ret = true;
         return ret;
      }

      public static bool VacuumDb(string file)
      {
         bool ret = true;
         return ret;
      }

      public static bool ExportMapDataToDB(string sourceFile, string destFile)
      {
         bool ret = true;
         return ret;
      }
      #endregion

      string ConnectionString;

      readonly List<string> AttachedCaches = new List<string>();

      void RebuildFinnalSelect()
      {
      }

      public void Attach(string db)
      {
         if(!AttachedCaches.Contains(db))
         {
            AttachedCaches.Add(db);
            RebuildFinnalSelect();
         }
      }

      public void Detach(string db)
      {
         if(AttachedCaches.Contains(db))
         {
            AttachedCaches.Remove(db);
            RebuildFinnalSelect();
         }
      }

      #region PureImageCache Members

      int preAllocationPing = 0;

      bool PureImageCache.PutImageToCache(byte[] tile, int type, GPoint pos, int zoom)
      {
         bool ret = true;
         return ret;
      }

      PureImage PureImageCache.GetImageFromCache(int type, GPoint pos, int zoom)
      {
         PureImage ret = null;
         return ret;
      }

      int PureImageCache.DeleteOlderThan(DateTime date, int? type)
      {
         int affectedRows = 0;
         return affectedRows;
      }

      #endregion
   }
#endif
}
