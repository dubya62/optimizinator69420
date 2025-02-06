
void test(unsigned char c){
    c = 2;
}

int add(int a, int b){
    int c = a + b;
}

int mul(int a, int b){
    int c = a * b;
}

int main(int argc, char** argv){
    char* test = "Hello, World!\n";

    int example = (int) (*test);

    add(2, 3);
    mul(3, 4);

}
