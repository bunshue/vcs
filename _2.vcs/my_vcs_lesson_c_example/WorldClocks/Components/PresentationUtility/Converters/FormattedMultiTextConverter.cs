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
using System.Windows.Data;

namespace BinaryComponents.PresentationUtility.Converters
{
	public class FormattedMultiTextConverter : IMultiValueConverter
	{
		#region IMultiValueConverter Members

		public object Convert( object[] values, Type targetType, object parameter, System.Globalization.CultureInfo culture )
		{
			return string.Format( (string) parameter, values );
		}

		public object[] ConvertBack( object value, Type[] targetTypes, object parameter, System.Globalization.CultureInfo culture )
		{
			return null;
		}

		#endregion
	}
}
