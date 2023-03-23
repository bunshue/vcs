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
using System.Windows;

namespace BinaryComponents.PresentationUtility.Management
{
	public static class SingleInstanceWindow<T> where T : Window, new()
	{
		public static void Show()
		{
			if( !Create() )
			{
				return;
			}

			_window.Show();
		}

		public static void ShowDialog()
		{
			if( !Create() )
			{
				return;
			}

			_window.ShowDialog();
		}

		private static bool Create()
		{
			if( _window != null )
			{
				_window.Focus();
				return false;
			}

			_window = new T();
			_window.Closed += new EventHandler( _window_Closed );

			return true;
		}

		private static void _window_Closed( object sender, EventArgs e )
		{
			_window.Closed -= new EventHandler( _window_Closed );
			_window = null;
		}

		private static T _window;
	}
}
