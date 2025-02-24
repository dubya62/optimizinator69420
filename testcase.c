

struct TestStruct{
    int a;
    int *b;
};

union TestUnion{
    int a;
    int *b;
};


int main(int argc, char** argv){
    struct TestStruct* test;
    struct TestStruct test2;

    union TestUnion* test3;
    union TestUnion test4;

    int a = (unsigned int) -7;
    return 0;
}
