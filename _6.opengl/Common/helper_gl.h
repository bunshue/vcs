// These are helper functions for the SDK samples (OpenGL)
#ifndef HELPER_GL_H
#define HELPER_GL_H

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
    #include <GL/glew.h>
#endif

#include <GL/gl.h>

#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <assert.h>


/* Prototypes */
namespace __HelperGL {
    static int isGLVersionSupported(unsigned reqMajor, unsigned reqMinor);
    static int areGLExtensionsSupported(const std::string &);
}


namespace __HelperGL {
    namespace __Int {
        static std::vector<std::string> split(const std::string &str)
        {
            std::istringstream ss(str);
            std::istream_iterator<std::string> it(ss);
            return std::vector<std::string> (it, std::istream_iterator<std::string>());
        }

        /* Sort the vector passed by reference */
        template<typename T> static inline void sort(std::vector<T> &a)
        {
            std::sort(a.begin(), a.end());
        }

        /* Compare two vectors */
        template<typename T> static int equals(std::vector<T> a, std::vector<T> b)
        {
            if (a.size() != b.size()) return 0;
            sort(a);
            sort(b);

            return std::equal(a.begin(), a.end(), b.begin());
        }

        template<typename T> static std::vector<T> getIntersection(std::vector<T> a, std::vector<T> b)
        {
            sort(a);
            sort(b);

            std::vector<T> rc;
            std::set_intersection(a.begin(), a.end(), b.begin(), b.end(),
                             std::back_inserter<std::vector<std::string> >(rc));
            return rc;
        }

        static std::vector<std::string> getGLExtensions()
        {
            std::string extensionsStr( (const char *)glGetString(GL_EXTENSIONS));
            return split (extensionsStr);
        }
    }

    static int areGLExtensionsSupported(const std::string &extensions)
    {
        std::vector<std::string> all = __Int::getGLExtensions();

        std::vector<std::string> requested = __Int::split(extensions);
        std::vector<std::string> matched = __Int::getIntersection(all, requested);

        return __Int::equals(matched, requested);
    }

    static int isGLVersionSupported(unsigned reqMajor, unsigned reqMinor)
    {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
        if (glewInit() != GLEW_OK)
        {
            std::cerr << "glewInit() failed!" << std::endl;
            return 0;
        }
#endif
        std::string version ((const char *) glGetString (GL_VERSION));
        std::stringstream stream (version);
        unsigned major, minor;
        char dot;

        stream >> major >> dot >> minor;

        assert (dot == '.');
        return major > reqMajor || (major == reqMajor && minor >= reqMinor);
    }

    static inline const char* glErrorToString(GLenum err)
    {
#define CASE_RETURN_MACRO(arg) case arg: return #arg
        switch(err)
        {
            CASE_RETURN_MACRO(GL_NO_ERROR);
            CASE_RETURN_MACRO(GL_INVALID_ENUM);
            CASE_RETURN_MACRO(GL_INVALID_VALUE);
            CASE_RETURN_MACRO(GL_INVALID_OPERATION);
            CASE_RETURN_MACRO(GL_OUT_OF_MEMORY);
            CASE_RETURN_MACRO(GL_STACK_UNDERFLOW);
            CASE_RETURN_MACRO(GL_STACK_OVERFLOW);
#ifdef GL_INVALID_FRAMEBUFFER_OPERATION
            CASE_RETURN_MACRO(GL_INVALID_FRAMEBUFFER_OPERATION);
#endif
            default: break;
        }
#undef CASE_RETURN_MACRO
        return "*UNKNOWN*";
    }

////////////////////////////////////////////////////////////////////////////
//! Check for OpenGL error
//! @return bool if no GL error has been encountered, otherwise 0
//! @param file  __FILE__ macro
//! @param line  __LINE__ macro
//! @note The GL error is listed on stderr
//! @note This function should be used via the CHECK_ERROR_GL() macro
////////////////////////////////////////////////////////////////////////////
    inline bool sdkCheckErrorGL(const char *file, const int line)
    {
        bool ret_val = true;

        // check for error
        GLenum gl_error = glGetError();

        if (gl_error != GL_NO_ERROR)
        {
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
            char tmpStr[512];
            // NOTE: "%s(%i) : " allows Visual Studio to directly jump to the file at the right line
            // when the user double clicks on the error line in the Output pane. Like any compile error.
            sprintf_s(tmpStr, 255, "\n%s(%i) : GL Error : %s\n\n", file, line, glErrorToString(gl_error));
            fprintf(stderr, "%s", tmpStr);
#endif
            fprintf(stderr, "GL Error in file '%s' in line %d :\n", file, line);
            fprintf(stderr, "%s\n", glErrorToString(gl_error));
            ret_val = false;
        }

        return ret_val;
    }

#define SDK_CHECK_ERROR_GL()                                              \
    if( false == sdkCheckErrorGL( __FILE__, __LINE__)) {                  \
        exit(EXIT_FAILURE);                                               \
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

} /* of namespace __HelperGL*/

using namespace __HelperGL;

#endif /*HELPER_GL_H*/
