﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using Ivony.Fluent;

namespace Ivony.Html.Web
{

  /// <summary>
  /// 默认的内容视图渲染代理
  /// </summary>
  public class ContentAdapter : IHtmlRenderAdapter
  {


    /// <summary>
    /// 获取内容视图
    /// </summary>
    protected JumonyView View { get; private set; }

    /// <summary>
    /// 获取内容视图文档
    /// </summary>
    protected IHtmlDocument Document
    {
      get { return (IHtmlDocument) View.Scope; }
    }

    /// <summary>
    /// 获取内容视图的渲染代理
    /// </summary>
    protected IHtmlRenderAdapter[] RenderAdapters { get; private set; }


    /// <summary>
    /// 创建 ContentAdapter 对象
    /// </summary>
    /// <param name="view">要渲染的内容视图</param>
    public ContentAdapter( JumonyView view )
    {
      if ( view.IsPartialView )
        throw new InvalidOperationException( "部分视图不能套用母板" );

      View = view;
      RenderAdapters = view.RenderAdapters.ToArray();
    }

    bool IHtmlRenderAdapter.Render( IHtmlNode node, IHtmlRenderContext context )
    {
      var element = node as IHtmlElement;

      if ( element == null )
        return false;

      if ( element.Name.EqualsIgnoreCase( "content" ) )
      {
        GetContentBody( element ).RenderChilds( context.Writer, RenderAdapters );
        return true;
      }
      else if ( element.Name.EqualsIgnoreCase( "head" ) )
      {

        View.ViewContext.HttpContext.Trace.Write( "ContentView", "Begin Merge Head" );
        var head = MergeHead( element, Document.FindSingle( "head" ) );
        View.ViewContext.HttpContext.Trace.Write( "ContentView", "End Merge Head" );

        head.Render( context.Writer, RenderAdapters );

        return true;
      }
      else
        return false;
    }



    /// <summary>
    /// 获取内容视图需要被的渲染内容
    /// </summary>
    /// <param name="element">位于母板视图上的 &lt;content&gt; 标签</param>
    /// <returns>该 &lt;content&gt; 标签需要被渲染的内容</returns>
    protected virtual IHtmlContainer GetContentBody( IHtmlElement element )
    {
      var body = Document.FindSingle( "body" );
      var contentBodyId = body.Attribute( "content-body" ).Value();

      if ( !string.IsNullOrEmpty( contentBodyId ) )
        body = Document.GetElementById( contentBodyId );

      return body;
    }


    /// <summary>
    /// 合并内容视图与母板视图的文档头
    /// </summary>
    /// <param name="masterHead">母板视图的文档头</param>
    /// <param name="contentHead">内容视图的文档头</param>
    /// <returns>合并后的 &lt;head&gt; 元素</returns>
    protected virtual IHtmlElement MergeHead( IHtmlElement masterHead, IHtmlElement contentHead )
    {

      var head = masterHead.Document.CreateFragment().AddElement( "head" );

      head.AddCopy( contentHead.Elements().Where( e => e.Attribute( "ignore" ) == null ) );

      if ( !head.Find( "title" ).Any() )
      {
        var title = masterHead.Find( "title" ).FirstOrDefault();
        head.AddCopy( title );
      }


      {
        var existsStyleSheets = new HashSet<string>( head.Find( "link[rel=stylesheet]" ).Select( e => e.Attribute( "href" ).Value() ), StringComparer.OrdinalIgnoreCase );
        foreach ( var element in masterHead.Find( "link[rel=stylesheet]" ) )
        {
          if ( !existsStyleSheets.Contains( element.Attribute( "href" ).Value() ) )
            head.AddCopy( element );
        }
      }

      {
        var existsScripts = new HashSet<string>( head.Find( "script[src]" ).Select( e => e.Attribute( "src" ).Value() ), StringComparer.OrdinalIgnoreCase );
        foreach ( var element in masterHead.Find( "script[src]" ) )
        {
          if ( !existsScripts.Contains( element.Attribute( "src" ).Value() ) )
            head.AddCopy( element );
        }
      }

      return head;
    }


  }
}
