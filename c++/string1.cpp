#include<iostream>
#include<string>
int main(){
	using namespace std;
	string one ("Lottery Winner!");
	cout << one << endl;
	string two(20,'$');
	cout << two << endl;
	string three(one);
	cout << three << endl;
	one += "Oops!";
	cout << one << endl;
	two = "Sorry! That was ";
	three[0]='P';
	string four;
	four = two + three; // overloaded +, =
	cout << four << endl;
	char alls[] = "All's well that ends well";
	string five(alls,20); // ctor #5
	cout << five << "!\n";
	string six(alls+6, alls + 10); // ctor #6
	cout << six << ", ";
	string seven(&five[6], &five[10]); // ctor #6 again
	cout << seven << "...\n";
	string eight(four, 7, 16); // ctor #7
	cout << eight << " in motion!" << endl;
	return 0;
}
