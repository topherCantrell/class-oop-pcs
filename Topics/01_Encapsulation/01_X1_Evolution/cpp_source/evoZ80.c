
void sayHi() {
}

void sayBye() {
}

int main(int argc, char ** argv) {
return 0;
}

void doFun() {
    char a = 5;

    while(a>0 && a!=10) {   
        if(a==3) {
            continue;
        }
        a = a - 1; 
    }

    sayHi();
    sayBye();

}