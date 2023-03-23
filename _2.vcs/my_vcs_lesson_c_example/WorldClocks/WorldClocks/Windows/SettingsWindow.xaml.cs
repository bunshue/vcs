/////////////////////////////////////////////////////////////////////////////
//
// (c) 2007 BinaryComponents Ltd.  All Rights Reserved.
//
// http://www.binarycomponents.com/
//
/////////////////////////////////////////////////////////////////////////////

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Collections.ObjectModel;

namespace BinaryComponents.WorldClocks.Windows
{
	/// <summary>
	/// Interaction logic for SettingsWindow.xaml
	/// </summary>

	public partial class SettingsWindow : Window
	{
		public SettingsWindow()
		{
			InitializeComponent();

			App app = (App) App.Current;

			foreach( Data.TimeInfo ti in app.Settings.TimeInfos )
			{
				_timeInfos.Add( Data.TimeInfo.Copy( ti ) );
			}

			_listBox.ItemsSource = _timeInfos;
		}

		private void _okButton_OnExecuted( object sender, ExecutedRoutedEventArgs e )
		{
			App app = (App) App.Current;

			app.Settings.TimeInfos.Clear();
			app.Settings.TimeInfos.AddRange( _timeInfos );

			DialogResult = true;
		}

		private void _cancelButton_OnExecuted( object sender, ExecutedRoutedEventArgs e )
		{
			DialogResult = false;
		}

		private void _addButton_OnExecuted( object sender, ExecutedRoutedEventArgs e )
		{
			ChooseTimeZoneWindow chooseTimeZoneWindow = new ChooseTimeZoneWindow();

			Data.TimeInfo ti = chooseTimeZoneWindow.Add( this );

			if( ti != null )
			{
				if( SelectedTimeInfo == null )
				{
					_timeInfos.Add( ti );
				}
				else
				{
					_timeInfos.Insert( _timeInfos.IndexOf( SelectedTimeInfo ) + 1, ti );
				}

				SelectedTimeInfo = ti;
			}
		}

		private void _editButton_OnExecuted( object sender, ExecutedRoutedEventArgs e )
		{
			Data.TimeInfo ti = SelectedTimeInfo;
			ChooseTimeZoneWindow chooseTimeZoneWindow = new ChooseTimeZoneWindow();

			if( chooseTimeZoneWindow.Edit( this, ti ) )
			{
				_listBox.ItemsSource = null;
				_listBox.ItemsSource = _timeInfos;
				_listBox.SelectedItem = ti;
			}
		}

		private void _removeButton_OnExecuted( object sender, ExecutedRoutedEventArgs e )
		{
			_timeInfos.Remove( SelectedTimeInfo );
		}

		private void _editButton_CanExecute( object sender, CanExecuteRoutedEventArgs e )
		{
			e.CanExecute = ( _listBox.SelectedItem != null );
		}

		private void _removeButton_CanExecute( object sender, CanExecuteRoutedEventArgs e )
		{
			e.CanExecute = ( _listBox.SelectedItem != null );
		}

		private Data.TimeInfo SelectedTimeInfo
		{
			get
			{
				return (Data.TimeInfo) _listBox.SelectedItem;
			}
			set
			{
				_listBox.SelectedItem = value;
			}
		}

		public readonly static RoutedUICommand Ok = new RoutedUICommand();
		public readonly static RoutedUICommand Cancel = new RoutedUICommand();
		public readonly static RoutedUICommand Add = new RoutedUICommand();
		public readonly static RoutedUICommand Edit = new RoutedUICommand();
		public readonly static RoutedUICommand Remove = new RoutedUICommand();

		private ObservableCollection<Data.TimeInfo> _timeInfos = new ObservableCollection<Data.TimeInfo>();
	}
}
