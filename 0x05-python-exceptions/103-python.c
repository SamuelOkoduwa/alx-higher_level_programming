#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t len, alloc, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    len = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", len);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < len; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);
        PyObject_Print(item, stdout, 0);
        printf("\n");
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 6 bytes: ");
    for (i = 0; i < size && i < 6; i++) {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %.17g\n", PyFloat_AsDouble(p));
}
