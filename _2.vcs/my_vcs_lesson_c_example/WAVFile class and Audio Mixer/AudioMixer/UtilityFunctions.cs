/* This file contains utility functions for use in the AudioMerger project.
 *
 * Date       Author         Description
 * 2009-03-24 erico          Created
 */

using System;
using System.IO;

namespace AudioMerger
{
    class UtilityFunctions
    {
        /// <summary>
        /// Removes a directory, including all the files in it.
        /// </summary>
        /// <param name="pPath">The directory to remove</param>
        /// <returns>A blank string upon success, or a warning upon error.  If the directory does not exist, that is not an error.</returns>
        public static String DeleteDir(String pPath)
        {
            String retval = "";

            if (Directory.Exists(pPath))
            {
                try
                {
                    // Delete all the files
                    String[] filenames = Directory.GetFiles(pPath);
                    foreach (String filename in filenames)
                        File.Delete(filename);
                    // Delete the directory
                    Directory.Delete(pPath, true);
                }
                catch (System.Exception exc)
                {
                    retval = exc.Message;
                }
            }

            return retval;
        }
    }
}