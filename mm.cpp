#include<iostream>
using namespace std;

int main(){
    int r1,r2,c1,c2;
    bool condition = false;
    while(true){
    cout << "Enter number of rows and columns for first matrix: ";
    cin >> r1 >> c1;
    cout << "Enter number of rows and columns for second matrix: ";
    cin >> r2 >> c2;
    if(c1 != r2){
        cout << "Error! column of first matrix not equal to row of second." << endl;
        cout << "Please enter the dimensions again." << endl;
    }
    else{
        condition = true;
    }
    if(condition) break;
    }
    int first[r1][c1], second[r2][c2];
    cout << "Enter elements of first matrix:" << endl;
    for(int i=0; i<r1; i++){
        for(int j=0; j<c1; j++){
            cin >> first[i][j];
        }
    }
    cout << "Enter elements of second matrix:" << endl;
    for(int i=0; i<r2; i++){
        for(int j=0; j<c2; j++){
            cin >> second[i][j];
        }
    }
    int newMatrix[r1][c2];
    for(int i=0; i<r1; i++){
        for(int j=0; j<c2; j++){
            newMatrix[i][j] = 0;
            for(int k=0; k<c1; k++){
                newMatrix[i][j] += first[i][k] * second[k][j];
            }
        }
    }
    cout << "Resultant Matrix:" << endl;
    for(int i=0; i<r1; i++){
        for(int j=0; j<c2; j++){
            cout << newMatrix[i][j] << " ";
        }
        cout << endl;
    }
}