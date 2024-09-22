/*
This is the main template to define a program in cpp, otherwise you may except the "using namespace std;", in that case you'll have to implace "std::" in front of any 
variable or function declaration like this: "std::int main()"
*/
#include <iostream>  // Using the operator '#' for the importation of any library or module that we need to use and put between "<in here>" the name of what we're gonna include.
using namespace std;
int main(){
    int variable = 5;   //For the declaration of a variable we start with the type, followed to the name and the asign operator ("=") to finish with the value.(and of course, the ";" in the end)

    int a; //The declaration also can be multiple and doesn't depends of a line space, can be made in a single line
    
    /*
    To print we use the function "cout" (console-out) next to the output operator ("<<") and then we put what we're gonna show on console (variable, value, operation, almost anything).
    Also we may use endl to give a line space or '\n' in an string between "".  
    */

    cout<<variable<<endl; 

    //And to input we use "cin" (console-in) next to the input operator(">>>")
    
    cout<"Insert a digit: ";  cin>>a;
    cout<<"\nAnd here we print the value of a using first a text and followed to the '<<' to print him"<<a;
    return 0;
}


/*
Here 
*/