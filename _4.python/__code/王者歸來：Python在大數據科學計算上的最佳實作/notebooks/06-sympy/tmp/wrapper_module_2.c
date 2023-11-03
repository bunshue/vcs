﻿#include "Python.h"
#include "math.h"
#include "numpy/ndarraytypes.h"
#include "numpy/ufuncobject.h"
#include "numpy/halffloat.h"
#include "wrapped_code_2.h"

static PyMethodDef wrapper_module_2Methods[] = {
        {NULL, NULL, 0, NULL}
};

static void autofunc_ufunc(char **args, npy_intp *dimensions, npy_intp* steps, void* data)
{
    npy_intp i;
    npy_intp n = dimensions[0];
    char *in0 = args[0];
    char *in1 = args[1];
    char *in2 = args[2];
    char *out1 = args[3];
    npy_intp in0_step = steps[0];
    npy_intp in1_step = steps[1];
    npy_intp in2_step = steps[2];
    npy_intp out1_step = steps[3];
    for (i = 0; i < n; i++) {
        *((double *)out1) = autofunc(*(double *)in0, *(double *)in1, *(double *)in2);
        in0 += in0_step;
        in1 += in1_step;
        in2 += in2_step;
        out1 += out1_step;
    }
}
PyUFuncGenericFunction autofunc_funcs[1] = {&autofunc_ufunc};
static char autofunc_types[4] = {NPY_DOUBLE, NPY_DOUBLE, NPY_DOUBLE, NPY_DOUBLE};
static void *autofunc_data[1] = {NULL};

#if PY_VERSION_HEX >= 0x03000000
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "wrapper_module_2",
    NULL,
    -1,
    wrapper_module_2Methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_wrapper_module_2(void)
{
    PyObject *m, *d;
    PyObject *ufunc0;
    m = PyModule_Create(&moduledef);
    if (!m) {
        return NULL;
    }
    import_array();
    import_umath();
    d = PyModule_GetDict(m);
    ufunc0 = PyUFunc_FromFuncAndData(autofunc_funcs, autofunc_data, autofunc_types, 1, 3, 1,
            PyUFunc_None, "wrapper_module_2", "Created in SymPy with Ufuncify", 0);
    PyDict_SetItemString(d, "autofunc", ufunc0);
    Py_DECREF(ufunc0);
    return m;
}
#else
PyMODINIT_FUNC initwrapper_module_2(void)
{
    PyObject *m, *d;
    PyObject *ufunc0;
    m = Py_InitModule("wrapper_module_2", wrapper_module_2Methods);
    if (m == NULL) {
        return;
    }
    import_array();
    import_umath();
    d = PyModule_GetDict(m);
    ufunc0 = PyUFunc_FromFuncAndData(autofunc_funcs, autofunc_data, autofunc_types, 1, 3, 1,
            PyUFunc_None, "wrapper_module_2", "Created in SymPy with Ufuncify", 0);
    PyDict_SetItemString(d, "autofunc", ufunc0);
    Py_DECREF(ufunc0);
}
#endif