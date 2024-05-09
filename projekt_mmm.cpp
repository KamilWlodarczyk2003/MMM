#include <iostream>
#include <fstream>
using namespace std;

int main(){
	//setup**************************************
ifstream wejscie("dane.txt");
ofstream wyjscie("wyjscie.txt");
double m1,m2,k1,k2,b1,b2,u=1,X1,X2,dT=0.1,V1,V2,A1,A2;
wejscie>>m1>>m2>>k1>>k2>>b1>>b2;
V1=0;
V2=0;
A1=0;
A2=0;
X1=0;
X2=0;
	//matma**************************************
for(int i=0;i<600;i++){
	A2=u/m2-(X2-X1)*k2/m2-(V2-V1)*b2/m2;
	A1=-k1*X1/m1+k2*(X2-X1)/m1-b1*V1/m1+b2*(V2-V1)/m1;
	V2=V2+A2*dT;
	V1=V1+A1*dT;
	X2=X2+V2*dT;
	X1=X1+V1*dT;
	wyjscie<<i*dT<<";";
	wyjscie<<X1<<";";
	wyjscie<<X2<<endl;
	if(i==100){
		u=0;
	}
}


wyjscie.close();
wejscie.close();

return 0;
}

