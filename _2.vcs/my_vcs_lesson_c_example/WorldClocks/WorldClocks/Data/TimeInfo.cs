/////////////////////////////////////////////////////////////////////////////
//
// (c) 2007 BinaryComponents Ltd.  All Rights Reserved.
//
// http://www.binarycomponents.com/
//
/////////////////////////////////////////////////////////////////////////////

using System;
using System.Collections.Generic;
using System.Text;
using System.Xml.Linq;

namespace BinaryComponents.WorldClocks.Data
{
	public sealed class TimeInfo
	{
		public TimeInfo( TimeZoneInfo tz )
		{
			_timezone = tz;
		}

		public static string Write( TimeInfo ti )
		{
			XDocument xDoc = new XDocument(
									 new XElement( "TimeInfo",
										 new XAttribute( "TimeZoneInfo", ti._timezone.ToSerializedString() ),
										 new XAttribute( "DisplayName", ti._displayName ?? string.Empty ) ) );

			return xDoc.ToString();
		}

		public static TimeInfo Read( string s )
		{
			try
			{
				XDocument xDoc = XDocument.Parse( s );

				TimeZoneInfo tzi = TimeZoneInfo.FromSerializedString( xDoc.Element( "TimeInfo" ).Attribute( "TimeZoneInfo" ).Value );

				TimeInfo ti = new TimeInfo( tzi );

				string displayName = xDoc.Element( "TimeInfo" ).Attribute( "DisplayName" ).Value.Trim();

				if( displayName != string.Empty )
				{
					ti.DisplayName = displayName;
				}

				return ti;
			}
			catch
			{
				return null;
			}
		}

		public static TimeInfo Copy( TimeInfo ti )
		{
			TimeInfo copy = new TimeInfo( ti.TimeZoneInfo );

			if( ti.IsDisplayNameOverridden )
			{
				copy.DisplayName = ti.DisplayName;
			}

			return copy;
		}

		public bool IsDisplayNameOverridden
		{
			get
			{
				return _displayName != null;
			}
		}

		public string OffsetName
		{
			get
			{
				if( _timezone.BaseUtcOffset == TimeSpan.Zero )
				{
					return "GMT";
				}
				else if( _timezone.BaseUtcOffset.Hours < 0 )
				{
					return string.Format( "GMT-{0}:{1:00}", -_timezone.BaseUtcOffset.Hours, -_timezone.BaseUtcOffset.Minutes );
				}
				else
				{
					return string.Format( "GMT+{0}:{1:00}", _timezone.BaseUtcOffset.Hours, _timezone.BaseUtcOffset.Minutes );
				}
			}
		}

		public string DisplayName
		{
			get
			{
				return _displayName ?? _timezone.DisplayName;
			}
			set
			{
				if( value == _timezone.DisplayName )
				{
					_displayName = null;
				}
				else
				{
					_displayName = value;
				}
			}
		}

		public TimeZoneInfo TimeZoneInfo
		{
			get
			{
				return _timezone;
			}
		}

		public DateTime GetAdjusted( DateTime start )
		{
			return start.Add( _timezone.GetUtcOffset( start ) );
		}

		private TimeZoneInfo _timezone;
		private string _displayName;
	}
}
