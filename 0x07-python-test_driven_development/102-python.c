#include <Python.h>

/**
 * print_python_string - Prints Python string object information
 * @p: Pointer to a Python object
 */
void print_python_string(PyObject *p)
{
    PyUnicodeObject *unicode;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    unicode = (PyUnicodeObject *)p;
    printf("  type: compact %s\n", (unicode->state.ascii) ? "ascii" : "unicode object");
    printf("  length: %ld\n", unicode->length);
    printf("  value: %s\n", PyUnicode_AsUTF8(unicode));
}
