﻿using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.Compilation;
using System.Web.Hosting;
using System.Web.Mvc;
using Ivony.Fluent;
using Ivony.Html;
using Ivony.Html.ExpandedAPI;
using Ivony.Web;


namespace Ivony.Html.Web
{
  /// <summary>
  /// 提供视图处理程序
  /// </summary>
  public static class ViewHandlerProvider
  {


    /// <summary>
    /// 获取视图处理程序
    /// </summary>
    /// <param name="virtualPath">视图的虚拟路径</param>
    /// <returns>该虚拟路径的视图处理程序</returns>
    public static IViewHandler GetViewHandler( string virtualPath )
    {
      foreach ( var provider in WebServiceLocator.GetServices<IViewHandlerProvider>( virtualPath ) )
      {
        var handler = provider.FindViewHandler( virtualPath );
        if ( handler != null )
          return handler;
      }

      return GetViewHandlerInternal( virtualPath + ".ashx", true );
    }


    /// <summary>
    /// 查找母板视图的处理程序
    /// </summary>
    /// <param name="virtualPath">母板视图虚拟路径</param>
    /// <returns>视图处理程序</returns>
    public static IViewHandler GetMasterViewHandler( string virtualPath )
    {

      foreach ( var provider in WebServiceLocator.GetServices<IViewHandlerProvider>( virtualPath ) )
      {
        var handler = provider.FindViewHandler( virtualPath );
        if ( handler != null )
          return handler;
      }

      return GetViewHandlerInternal( virtualPath + ".ashx", false );
    }



    /// <summary>
    /// 获取视图处理程序
    /// </summary>
    /// <param name="virtualPath">视图的虚拟路径</param>
    /// <param name="includeDefaultHandler">是否要查找默认视图处理程序</param>
    /// <returns>该虚拟路径的视图处理程序</returns>
    internal static IViewHandler GetViewHandlerInternal( string virtualPath, bool includeDefaultHandler )
    {

      var handler = GetHandlerInternal( virtualPath );

      if ( handler == null && !includeDefaultHandler )
        handler = GetHandlerInternal( VirtualPathHelper.FallbackSearch( virtualPath, "_handler.ashx" ) );

      return handler ?? new ViewHandler();
    }




    private static IViewHandler GetHandlerInternal( string handlerPath )
    {

      if ( handlerPath == null )
        return null;


      if ( HostingEnvironment.VirtualPathProvider.FileExists( handlerPath ) )
      {
        try
        {
          var instance = BuildManager.CreateInstanceFromVirtualPath( handlerPath, typeof( object ) );

          var handler = instance as IViewHandler;
          if ( handler != null )
            return handler;

          var htmlHandler = instance as IHtmlHandler;
          if ( htmlHandler != null )
            return new HtmlViewHandlerWrapper( htmlHandler );
        }
        catch
        {

        }
      }

      return null;
    }



    /// <summary>
    /// 在 HTML 文档中查找 ViewHandler 路径设置。
    /// </summary>
    /// <param name="Scope">要处理的 HTML 文档范畴</param>
    /// <returns>用于处理 HTML 的视图处理程序路径</returns>
    internal static string GetHandlerPath( IHtmlContainer Scope )
    {
      var head = Scope.Document.FindFirstOrDefault( "head" );
      if ( head == null )
        return null;

      var handlerMeta = head.FindFirstOrDefault( "meta[name=handler]" );
      if ( handlerMeta == null )
        return null;

      return handlerMeta.Attribute( "value" ).Value();
    }




  }
}
