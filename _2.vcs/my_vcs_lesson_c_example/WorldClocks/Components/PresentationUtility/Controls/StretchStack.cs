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
using System.Windows.Controls;
using System.Windows;

namespace BinaryComponents.PresentationUtility.Controls
{
	public class StretchStack : Panel
	{
		protected override Size MeasureOverride( Size availableSize )
		{
			if( InternalChildren.Count == 0 )
			{
				return new Size( 0, 0 );
			}

			Size childSize = new Size( availableSize.Width / InternalChildren.Count, availableSize.Height );
			double maxWidth = 0, maxHeight = 0;

			foreach( FrameworkElement child in InternalChildren )
			{
				child.Measure( childSize );

				maxWidth = Math.Max( maxWidth, child.DesiredSize.Width );
				maxHeight = Math.Max( maxHeight, child.DesiredSize.Height );
			}

			return new Size( InternalChildren.Count * maxWidth, maxHeight );
		}

		protected override Size ArrangeOverride( Size finalSize )
		{
			if( InternalChildren.Count == 0 )
			{
				return new Size( 0, 0 );
			}

			Size childSize = new Size( finalSize.Width / InternalChildren.Count, finalSize.Height );

			for( int i = 0; i < InternalChildren.Count; ++i )
			{
				Rect childRect = new Rect( i * childSize.Width, 0, childSize.Width, childSize.Height );

				InternalChildren[i].Arrange( childRect );
			}

			return finalSize;
		}
	}
}
