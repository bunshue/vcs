/////////////////////////////////////////////////////////////////////////////
//
// (c) 2007 BinaryComponents Ltd.  All Rights Reserved.
//
// http://www.binarycomponents.com/
//
/////////////////////////////////////////////////////////////////////////////

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Xml;
using System.Xml.Linq;
using System.Collections.ObjectModel;

namespace BinaryComponents.WorldClocks.Data
{
	public class Settings : IDisposable
	{
		public Settings()
		{
			string filename = GetFilename();

			if( File.Exists( filename ) )
			{
				XDocument xDoc = XDocument.Load( filename );

				_timeInfos = new List<TimeInfo>();

				foreach( TimeInfo ti in from XElement t in xDoc.Descendants( "TimeInfo" )
																select TimeInfo.Read( t.Attribute( "Zone" ).Value ) )
				{
					if( ti != null )
					{
						_timeInfos.Add( ti );
					}
				}
			}

			if( _timeInfos.Count == 0 )
			{
				_timeInfos.Add( new TimeInfo( TimeZoneInfo.Local ) );
			}
		}

		public List<TimeInfo> TimeInfos
		{
			get
			{
				return _timeInfos;
			}
		}

		#region IDisposable Members

		public void Dispose()
		{
			string filename = GetFilename();

			Directory.CreateDirectory( Path.GetDirectoryName( filename ) );

			XDocument xDoc = new XDocument(
												 new XElement( "Settings",
													 new XElement( "TimeInfos",
														 from TimeInfo ti in _timeInfos
														 select new XElement( "TimeInfo", new XAttribute( "Zone", TimeInfo.Write( ti ) ) ) ) ) );

			xDoc.Save( filename );
		}

		#endregion

		private string GetFilename()
		{
			string filename = Environment.GetFolderPath( Environment.SpecialFolder.ApplicationData );

			filename = Path.Combine( filename, @"BinaryComponents\WorldClocks\Settings.xml" );

			return filename;
		}

		private List<TimeInfo> _timeInfos = new List<TimeInfo>();
	}
}
