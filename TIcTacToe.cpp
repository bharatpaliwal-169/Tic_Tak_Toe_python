/* TIC - TAC - TOE */
#include<iostream>
using namespace std;

char arr[9] = {'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' } ;
char turn = 'X' ;
int count = 0 ;

void displayGrid (char arr[9])
{
    system("cls") ;

    cout << "\n\t    TIC - TAC - TOE \n\n" ;
    cout << "\t     Player1 = X \n\t     Player2 = O \n\n " ;

    cout << "\t        |       |\n" ;
    cout << "\t    " << arr[0] << "\t|  " << arr[1] << "\t|  " << arr[2] << "\n" ;
    cout << "\t        |       |\n" ;
    cout << "\t _________\n\n" ;

    cout << "\t        |       |\n" ;
    cout << "\t    " << arr[3] << "\t|  " << arr[4] << "\t|  " << arr[5] << "\n" ;
    cout << "\t        |       |\n" ;
    cout << "\t _________\n\n" ;

    cout << "\t        |       |\n" ;
    cout << "\t    " << arr[6] << "\t|  " << arr[7] << "\t|  " << arr[8] << "\n" ;
    cout << "\t        |       |\n" ;

    cout << "\n\n" ;
}

void playerTurn ()
{
    int p;
    ::count++ ;

    if (turn == 'X' )
        cout << "\n\n\t  Player 1 [X] turn \n" ;
    if (turn == 'O' )
        cout << "\n\n\t  Player 2 [O] turn \n" ;

    cout << "\t  Enter the position : " ; cin >> p ;

    if (arr[p-1] != 'X' && arr[p-1] != 'O')
    {

            switch (p)
            {
                case 1:
            	    arr[0] = turn ;
                	break ;
                case 2:
                	arr[1] = turn ;
                	break ;
                case 3:
                	arr[2] = turn ;
                	break ;
                case 4:
                	arr[3] = turn ;
            		break ;
                case 5:
                	arr[4] = turn ;
                	break ;
                case 6:
                	arr[5] = turn ;
                	break ;
                case 7:
            	    arr[6] = turn ;
                	break ;
                case 8:
                	arr[7] = turn ;
                	break ;
                case 9:
            	    arr[8] = turn ;
                	break ;

                default:
                    cout << "invalid position !! ";
                    break;
            }
    }

    else
    {
        cout << "\t  Oops!! This position is filled ! Try again ." ;
        ::count-- ;
        playerTurn();
    }

     if (turn == 'X' )
            turn = 'O' ;
     else
            turn = 'X' ;

    displayGrid(arr) ;
}

bool gameOver()
{
   for (int i=0 ; i<9 ; i+=3)
        if (arr[i] == arr[i+1] && arr[i] == arr[i+2])   // row-wise check
        {
            cout << "\t  Player " << arr[i] << " wins \n\n" ;
            return false ;
        }

    for (int i=0 ; i<3 ; i+=1)
      {

          if (arr[i] == arr[i+3] && arr[i] == arr[i+6])   // column-wise check
           {
            cout << "\t  Player " << arr[i] << " wins \n\n" ;
            return false ;
           }
      }

//diagonal check
    if (arr[0] == arr[4] && arr[0] == arr[8])
      {
        cout << "\t  Player " << arr[0] << " wins \n\n" ;
        return false;
      }

    if (arr[2] == arr[4] && arr[2] == arr[6])

    {
        cout << "\t  Player " << arr[2] << " wins \n\n" ;
        return false ;
    }

    if (::count >= 9)
    {
        cout << "\t  Game Draw !! \n\n" ;
        return false ;
    }

    else
        return true ;

}

int main()
{
    while (gameOver())
    {
        displayGrid(arr);
        playerTurn();
    }
}
