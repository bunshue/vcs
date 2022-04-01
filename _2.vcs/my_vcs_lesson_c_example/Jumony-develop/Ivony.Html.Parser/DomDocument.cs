﻿using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using Ivony.Fluent;

namespace Ivony.Html.Parser
{
  /// <summary>
  /// IHtmlDocument 的实现
  /// </summary>
  public class DomDocument : DomObject, IHtmlDocument, IDomContainer, INotifyDomChanged, IVersionCacheContainer
  {

    /// <summary>
    /// 创建 DomDocument 对象
    /// </summary>
    /// <param name="uri">文档的 URL</param>
    /// <param name="fragementParserProvider">文档碎片解析器提供程序，用于提供相似行为的文档碎片解析器</param>
    public DomDocument( Uri uri, IDomFragmentParserProvider fragementParserProvider )
    {

      if ( fragementParserProvider == null )
        throw new ArgumentNullException( "fragementParserProvider" );

      _uri = uri;
      _manager = new DomFragmentManager( this, fragementParserProvider );
      _modifier = new DomModifier();

      _modifier.HtmlDomChanged += OnDomChanged;
    }



    private Uri _uri;

    /// <summary>
    /// 获取文档的 URL
    /// </summary>
    public Uri DocumentUri
    {
      get { return _uri; }
      internal set { _uri = value; }
    }

    /// <summary>
    /// 获取当前对象所属的文档，总是返回自身
    /// </summary>
    public override IHtmlDocument Document
    {
      get { return this; }
    }

    /// <summary>
    /// 获取文档类型的声明，不支持，总是返回null
    /// </summary>
    public string DocumentDeclaration
    {
      get { return null; }
    }



    private DomNodeCollection _nodeCollection;

    /// <summary>
    /// 获取节点容器
    /// </summary>
    public DomNodeCollection NodeCollection
    {
      get
      {
        if ( _nodeCollection == null )
          _nodeCollection = new DomNodeCollection( this );

        return _nodeCollection;
      }
    }

    /// <summary>
    /// 获取所有子节点
    /// </summary>
    public IEnumerable<IHtmlNode> Nodes()
    {
      if ( _nodeCollection == null )
        _nodeCollection = new DomNodeCollection( this );

      return _nodeCollection.HtmlNodes;
    }



    private DomFragmentManager _manager;
    /// <summary>
    /// 文档碎片管理器
    /// </summary>
    public DomFragmentManager FragmentManager
    {
      get { return _manager; }
    }

    IHtmlFragmentManager IHtmlDocument.FragmentManager
    {
      get { return _manager; }
    }


    private DomModifier _modifier;

    /// <summary>
    /// 文档模型修改器
    /// </summary>
    public DomModifier DomModifier
    {
      get { return _modifier; }
    }

    /// <summary>
    /// 文档模型修改器
    /// </summary>
    IHtmlDomModifier IHtmlDocument.DomModifier
    {
      get { return _modifier; }
    }



    private readonly object _sync = new object();

    /// <summary>
    /// 用于同步操作的同步对象
    /// </summary>
    public object SyncRoot
    {
      get { return _sync; }
    }



    /// <summary>
    /// 当文档任何部分被修改时会引发的事件。
    /// </summary>
    public event EventHandler<HtmlDomChangedEventArgs> HtmlDomChanged;

    /// <summary>
    /// 引发 HtmlDomChanged 事件
    /// </summary>
    /// <param name="sender">引发事件的事件源</param>
    /// <param name="e">HtmlDomChanged 事件参数</param>
    protected virtual void OnDomChanged( object sender, HtmlDomChangedEventArgs e )
    {

      _currentVersionCache = null;//抛弃旧的版本缓存

      if ( HtmlDomChanged != null )
      {
        if ( object.Equals( this, e.Node.Document ) )
          HtmlDomChanged( sender, e );
      }
    }



    private Hashtable _currentVersionCache;

    Hashtable IVersionCacheContainer.CurrenctVersionCache
    {
      get
      {
        if ( _currentVersionCache == null )
          Interlocked.CompareExchange( ref _currentVersionCache, new Hashtable(), null );

        return _currentVersionCache;
      }
    }

    /// <summary>
    /// 文档所采用的 HTML 规范。
    /// </summary>
    public HtmlSpecificationBase HtmlSpecification
    {
      get;
      internal set;
    }
  }
}
