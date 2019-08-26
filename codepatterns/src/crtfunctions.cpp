#include <Windows.h>

int main(int argc, char** argv)
{
    return 0;
}

void callStrcmp()
{
    strcmp("a", "b");
}

void callStrncmp()
{
    strncmp("ab", "ba", 1);
}

void callStrcpy()
{
    char buf[10];
    strcpy(buf, "abc");
    strcpy_s(buf, 10, "abc");
}

void callStrncpy()
{
    char buf[10];
    strncpy(buf, "abc", 3);
    strncpy_s(buf, 10, "abc", 3);
}