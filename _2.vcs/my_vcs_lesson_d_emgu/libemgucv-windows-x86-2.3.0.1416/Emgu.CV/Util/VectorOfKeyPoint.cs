//----------------------------------------------------------------------------
//  Copyright (C) 2004-2011 by EMGU. All rights reserved.       
//----------------------------------------------------------------------------

﻿using System;
using System.Runtime.InteropServices;
using System.Text;
using System.Drawing;
using Emgu.CV.Structure;

namespace Emgu.CV.Util
{
   /// <summary>
   /// Wraped class of the C++ standard vector of MKeyPoint.
   /// </summary>
   public class VectorOfKeyPoint : Emgu.Util.UnmanagedObject
   {
      #region PInvoke
      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern IntPtr VectorOfKeyPointCreate();

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern IntPtr VectorOfKeyPointCreateSize(int size);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointRelease(IntPtr v);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern int VectorOfKeyPointGetSize(IntPtr v);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointCopyData(IntPtr v, IntPtr data);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern IntPtr VectorOfKeyPointGetStartAddress(IntPtr v);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointPushMulti(IntPtr v, IntPtr values, int count);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointClear(IntPtr v);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointFilterByImageBorder(IntPtr keypoints, Size imageSize, int borderSize);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointFilterByKeypointSize(IntPtr keypoints, float minSize, float maxSize);

      [DllImport(CvInvoke.EXTERN_LIBRARY, CallingConvention = CvInvoke.CvCallingConvention)]
      private static extern void VectorOfKeyPointFilterByPixelsMask(IntPtr keypoints, IntPtr mask);
      #endregion

      /// <summary>
      /// Create an empty standard vector of KeyPoint
      /// </summary>
      public VectorOfKeyPoint()
      {
         _ptr = VectorOfKeyPointCreate();
      }

      /// <summary>
      /// Create an standard vector of KeyPoint of the specific size
      /// </summary>
      /// <param name="size">The size of the vector</param>
      public VectorOfKeyPoint(int size)
      {
         _ptr = VectorOfKeyPointCreateSize(size);
      }

      /// <summary>
      /// Push an array of value into the standard vector
      /// </summary>
      /// <param name="value">The value to be pushed to the vector</param>
      public void Push(MKeyPoint[] value)
      {
         if (value.Length > 0)
         {
            GCHandle handle = GCHandle.Alloc(value, GCHandleType.Pinned);
            VectorOfKeyPointPushMulti(_ptr, handle.AddrOfPinnedObject(), value.Length);
            handle.Free();
         }
      }

      /// <summary>
      /// Get the size of the vector
      /// </summary>
      public int Size
      {
         get
         {
            return VectorOfKeyPointGetSize(_ptr);
         }
      }

      /// <summary>
      /// Clear the vector
      /// </summary>
      public void Clear()
      {
         VectorOfKeyPointClear(_ptr);
      }

      /// <summary>
      /// The pointer to the first element on the vector. In case of an empty vector, IntPtr.Zero will be returned.
      /// </summary>
      public IntPtr StartAddress
      {
         get
         {
            return VectorOfKeyPointGetStartAddress(_ptr);
         }
      }

      /// <summary>
      /// Convert the standard vector to an array of KeyPoint
      /// </summary>
      /// <returns>An array of KeyPoint</returns>
      public MKeyPoint[] ToArray()
      {
         MKeyPoint[] res = new MKeyPoint[Size];
         if (res.Length > 0)
         {
            GCHandle handle = GCHandle.Alloc(res, GCHandleType.Pinned);
            VectorOfKeyPointCopyData(_ptr, handle.AddrOfPinnedObject());
            handle.Free();
         }
         return res;
      }
      /// <summary>
      /// Remove keypoints within borderPixels of an image edge.
      /// </summary>
      /// <param name="imageSize">Image size</param>
      /// <param name="borderSize">Border size in pixel</param>
      public void FilterByImageBorder(Size imageSize, int borderSize)
      {
         VectorOfKeyPointFilterByImageBorder(Ptr, imageSize, borderSize);
      }

      /// <summary>
      /// Remove keypoints of sizes out of range.
      /// </summary>
      /// <param name="minSize">Minimum size</param>
      /// <param name="maxSize">Maximum size</param>
      public void FilterByKeypointSize(float minSize, float maxSize)
      {
         VectorOfKeyPointFilterByKeypointSize(Ptr, minSize, maxSize);
      }

      /// <summary>
      /// Remove keypoints from some image by mask for pixels of this image.
      /// </summary>
      /// <param name="mask">The mask</param>
      public void FilterByPixelsMask(Image<Gray, Byte> mask)
      {
         VectorOfKeyPointFilterByPixelsMask(Ptr, mask);
      }

      /// <summary>
      /// Release the standard vector
      /// </summary>
      protected override void DisposeObject()
      {
         VectorOfKeyPointRelease(_ptr);
      }
   }
}
