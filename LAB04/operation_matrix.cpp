#include <iostream>
#include <vector>
#include <iomanip>   
#include <algorithm>// using to lamba function

using std::cout; using std::cin; using std::vector; using std::endl;

//display our matrix  
void show_matrix(vector<vector<float>>& matrix) {
    for (auto j : matrix) {
        for (auto k : j) {
            
            cout.setf(std::ios::fixed);
            cout.precision(3);
            cout << k << "\t";
        }
        cout << endl;
    }

}

bool determinant_checker(vector<vector<float>> matrix) {
    //create the vector which will be fill value of diagonal matrix
    vector<float> check;


    for (int j = 0; j < matrix.size(); j++) {
        for (int k = 0; k < matrix[0].size(); k++) {
            if (matrix[j][j] != 0) {
                check.push_back(matrix[j][j]);
                
            }
            if (matrix[j][k] != 0) {
                //0 may be mean that is calculative error
                return 0;

            }
                
        }

    }
    //check the elemnts in diagonal is equal, if equal return 1
    if (std::equal(check.begin() + 1, check.end(), check.begin())) {
        return 1;
    }

}

//the old matrix which called matrix_copy is overwriten by element of matrix
void refresh(vector<vector<float>>& matrix_copy, vector<vector<float>>& matrix) {
    for (int j = 0; j < matrix_copy.size(); j++) {
        for (int k = 0; k < matrix_copy[1].size(); k++) {
            matrix_copy[j][k] = matrix[j][k];

        }
    }
}

//function which replace the row in position // 
void swap(vector<vector<float>>& matrix, int counter) {


    vector<vector<float>> copy;

    int row = matrix.size();
    int col = matrix[1].size();

    copy.resize(matrix.size());
    for (int i = 0; i < matrix.size(); i++) {
        copy[i].resize(matrix[0].size());
    }

    for (int i = 0; i < counter; i++) {
        for (int u = 0; u < row; u++) {
            if (u == row - 1) {
                copy[0] = matrix[u];
            }
            else {
                copy[u + 1] = matrix[u];
            }


        }
        //the all element is write to matrix which we get
        refresh(matrix, copy);
       
    }

}


//if we want back to the matrix from using the swap funvtion we use this function
void swap_back(vector<vector<float>>& matrix, int counter) {

    vector<vector<float>> copy;

    int row = matrix.size();
    int col = matrix[1].size();

    copy.resize(matrix.size());
    for (int i = 0; i < matrix.size(); i++) {
        copy[i].resize(matrix[0].size());
    }


    for (int i = 0; i < counter; i++) {
        for (int u = 0; u < row; u++) {
            if (u == row - 1) {
                copy[u] = matrix[0];

            }
            else {
                copy[u] = matrix[u + 1];
            }

        }

        refresh(matrix, copy);
       
    }

}

//is the function which is 
void checker(vector<vector<float>>& matrix) {
    int suma{};

    for (int i = 0; i < matrix.size(); i++) {
        if (matrix[i][i] == 0) {
            swap(matrix, matrix.size() - i-1);
        }
        else {
            suma += 0;
        }

    }

}


vector<vector<float>> odwrotna(vector<vector<float>> matrix) {
    int row = matrix.size();
    int col = matrix[1].size();

    for (int i = 0; i < row; i++) {
        for (int n = 0; n < col; n++) {
            if (n == i)
                matrix[i].push_back(1.0);
            else
                matrix[i].push_back(0.0);
        }
    }

    checker(matrix);

    vector<vector<float>> matrix_copy{ 0 };
    matrix_copy.resize(matrix.size());
    for (int i = 0; i < matrix_copy.size(); i++) {

        matrix_copy[i].resize(matrix[1].size());
    }


    for (int j = 0; j < matrix.size(); j++) {
        for (int k = 0; k < matrix[1].size(); k++) {
            matrix_copy[j][k] = matrix[j][k];

        }
    }


    //iteration by column
    for (int r = 0; r < matrix[0].size()/2; r++) {

        if (r != 0) {
            swap(matrix, row - r);
            swap(matrix_copy, row - r);
        }


        // here it takes the first step, which is dividing by itself to get one.
        for (int i = 0; i < matrix[0].size(); i++) {
            if (matrix_copy[0][r] == 0) {
                cout << "Invert Matrix not exsist" << endl;
                exit(0);

            }
            else
            matrix[0][i] = matrix[0][i] / matrix_copy[0][r];
        }
       
        refresh(matrix_copy, matrix);


        //swapped our columns
        
        
        //defines the loop at which I will jump line by line in the column 
        //row -1 other case we we will go outsied the vector area
        for (int n = 0; n < row - 1; n++) { 

            //resposible for multiply for value the row below
            if (matrix[n + 1][r] == 0) {
                matrix[n + 1][r] = 0;
            }
                
            else {
                for (int i = 0; i < matrix[0].size(); i++) {

                    matrix[0][i] = matrix[0][i] * matrix_copy[n + 1][r];
                }
               
                refresh(matrix_copy, matrix);
                
                // subtract line one from the line below
                for (int i = 0; i < matrix[0].size(); i++) {

                    matrix[n + 1][i] = matrix_copy[n + 1][i] - matrix[0][i];
                }
                
                refresh(matrix_copy, matrix);

                //division to get back one on the diagonal
                for (int i = 0; i < matrix[0].size(); i++) {
                    if (matrix[0][r] == 0) {
                        cout << "Invert matrix not exsist" << endl;
                        exit(0);
                    }
                    else {
                        matrix[0][i] = matrix[0][i] / matrix_copy[0][r];
                    }
                    
                }
               
                refresh(matrix_copy, matrix);

            }
            
        }

        if (r != 0) {
            swap_back(matrix, row - r);
            swap_back(matrix_copy, row - r);

            
        }

    }
  
    //the matrix is cut of to invert matrix, the diagonal matrix is cut.
    for (int i = 0; i < matrix.size(); i++) {
        matrix[i].assign(matrix_copy[i].begin() + (matrix_copy[i].size()/2), matrix_copy[i].end());
     
    }
   
    return matrix;

}

//function to cont our detrminant
float wyznaczik(vector<vector<float>> matrix){

    vector<vector<float>> matrix_copy{ 0 };
    matrix_copy.resize(matrix.size());
    for (int i = 0; i < matrix_copy.size(); i++) {

        matrix_copy[i].resize(matrix[1].size());
    }


    for (int j = 0; j < matrix.size(); j++) {
        for (int k = 0; k < matrix[1].size(); k++) {
            matrix_copy[j][k] = matrix[j][k];

        }
    }
    int row = matrix.size();
    int col = matrix[0].size();


    //p_operator is a element of diagonal matrix which is couting during the loo, the first 


    vector<float>p_operator{ 1 };

    for (int i = 0; i < row; i++) {
        
        for (int j = 0; j < row; j++) {
            if (i == j) {
                continue;
            }

            for (int k = 0; k < col; k++) {
                
                matrix[k][j] = (matrix_copy[i][i] * matrix_copy[k][j] - matrix_copy[k][i] * matrix_copy[i][j])/p_operator[i];

            }


        }
        refresh(matrix_copy, matrix);
        p_operator.push_back(matrix[i][i]);
    }
    
    //update our matrix
    refresh(matrix_copy, matrix);



    //chceck the element of diagonal, if element is the same i get our determinant
    if (determinant_checker) {
        return matrix[0][0];
    }
    else {
        matrix.clear();
        cout << "Mathemtaical Error" << endl;
    }
    
}

void transpose(vector<vector<float>> &matrix) {
    if (matrix.size() == 0)
        return;
    
    auto compareToFirstRow = [firstRowSize = matrix[0].size()](std::vector<float>& row) {
        return firstRowSize == row.size();
    };
    //lambda function return 1 when all rows will be the same length
    bool rowsAreTheSame = std::all_of(matrix.begin() + 1, matrix.end(), compareToFirstRow);
    //transposition
    vector<vector<float> > trans_vec(matrix[0].size(), vector<float>());
    if (rowsAreTheSame) {
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                trans_vec[j].push_back(matrix[i][j]);
            }
        }

        matrix = trans_vec;    
    }
}


//multiplu matrix function
vector<vector<float> > mnozenie(vector<vector<float>> &matrixA, vector<vector<float>> &matrixB) {


    transpose(matrixB);
    vector<vector<float>> wynik;
    wynik.resize(matrixA.size());
    for (int i = 0; i < matrixA.size(); i++) {
        wynik[i].resize(matrixA[0].size());
    }

    for (int row = 0; row < matrixA.size(); row++) {
        for (int col = 0; col < matrixA[0].size(); col++) {
            for (int i = 0; i < matrixA.size(); i++) {
                wynik[row][col] = wynik[row][col] + (matrixA[row][i] * matrixB[col][i]);
            }

        }
    }
    return wynik;
}

//algebraic multibly function a * matirx[]
void algebraic_multiplication(float multipler ,vector<vector<float>>& matrix) {
    for (int j = 0; j < matrix.size(); j++) {
        for (int k = 0; k < matrix[0].size(); k++) {

            matrix[j][k] = multipler * matrix[j][k];


        }

    }


}




int main() {
    /*
    vector<vector<float>> matrixA{
        {7,2,1,2,2},
        {6,2,2,3,1},
        {1,2,4,4,8},
        {7,8,5,1,5},
        {7,8,5,1,3}
    };
    */

    vector<vector<float>> matrixA{
        {1,2,5},
        {2,10,7},
        {5,4,8}

    };

   
    vector<vector<float>> matrixB;
    matrixB.resize(matrixA.size());
    for (int i = 0; i < matrixA.size(); i++) {
        matrixB[i].resize(matrixA[0].size());
    }

    vector<vector<float>> matrixC;
    matrixC.resize(matrixA.size());
    for (int i = 0; i < matrixA.size(); i++) {
        matrixC[i].resize(matrixA[0].size());
    }

    matrixB=odwrotna(matrixA);
    cout << "Macierz odwrotna\n";
    cout << "\n";
    show_matrix(matrixB);
    cout << endl;
    cout << endl;
    matrixC = mnozenie(matrixB, matrixA);
    cout << "Mnozymy macierz pierwotna razy macierz odwrotna\n";
    cout << "\n";
    show_matrix(matrixC);
    cout << endl;
    cout << endl;
    cout << "Wyznacznik: " << wyznaczik(matrixA) << endl;

    return 0;
}


