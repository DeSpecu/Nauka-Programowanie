package Java;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class Nauka {

    public static void main(String[] args)
    {
        Scanner wejscie = new Scanner(System.in);
        // int a = Integer.parseInt(wejscie.nextLine());
        // int b = Integer.parseInt(wejscie.nextLine());
        // wejscie.close();

        // if(a>10 && b>10){
        //     System.out.println(a+b);
        // }
        // else if(a<10 && b<10 && a>0 && b>0){
        //     System.out.println(a-b);
        // }
        // else if((a>0 && b<0)||(a<0 && b>0)){
        //     System.out.println(b-a);
        // }
        // else if(a<0 && b<0){
        //     System.out.println("Obie ujemne");
        // }


        // int nowy = wejscie.nextInt();
        // if(nowy>10 || nowy<0)
        // {
        //     System.out.println("Pusto");
        // }
        // for(int i=1; i<5; i++)
        // {
        //     String wyjscie = String.valueOf(nowy);
        //     System.out.println(wyjscie.repeat(i));
        // }


        // double n = wejscie.nextDouble();
        // double suma = 0.0;
        // int x;
        // while(n!=0)
        // {
        //     x = (int)n;
        //     n = n-x;
        //     suma = suma+n;
        //     n = wejscie.nextDouble();
        // }
        // System.out.println(suma);

        
        // String n = wejscie.nextLine();
        // char c = n.charAt(0);
        // System.out.println(c);
        // char[] chars = {'a','o','i','e','u','y'};
        // int ile = 0;
        // while(c!='k')
        // {
        //     boolean contains = false;
        //     for (char ch : chars) 
        //     {
        //         if (ch == c) 
        //         {
        //         contains = true;
        //         break;
        //         }
        //     }
            
        //     if(contains)
        //     {
        //         ile = ile +1;
        //     }
        //     n = wejscie.nextLine();
        //     c = n.charAt(0);
        // } 
        // System.out.println(ile);


        //Kolos zadanie 1!!!!!!!!!!
        // String dane = wejscie.nextLine();

        // int a = wejscie.nextInt();
        // while(a<1 || a > dane.length()-2)
        // {
        //     System.out.println("Podaj liczbę z zakresu 1 - długość napisu-2");
        //     a = wejscie.nextInt();
        // }
        // int b = wejscie.nextInt();
        // while(b<a || b > dane.length()-2)
        // {
        //     System.out.println("Podaj liczbę z zakresu 1 - długość napisu-2 i większą od a");
        //     b = wejscie.nextInt();
        // }
        // List<String> wyjscie = new LinkedList<String>();

        // String zeroA="";
        // String adoB="";
        // String bKoniec="";
        // char[] petla = dane.toCharArray();
        // int doascii;
        // for(int i = 0; i<dane.length(); i++)
        // {
        //     if(i<=a)
        //     {
        //         zeroA=zeroA+petla[i];
        //     }
        //     else if(i>=a && i<=b)
        //     {
        //         if((int)petla[i]>96 && (int)petla[i]<123)
        //         {
        //             doascii=petla[i]-32;
        //             adoB=adoB+(char)doascii;
        //         }
        //         else{
        //             adoB=adoB + petla[i];
        //         }
        //     }
        //     else if(i>=b)
        //     {
        //         bKoniec=bKoniec+petla[i];
        //     }
        // }
        // wyjscie.add(zeroA);
        // wyjscie.add(adoB);
        // wyjscie.add(bKoniec);

        // for(String s : wyjscie)
        // {
        //     System.out.println(s);
        // }


        //Zadanie 2
        // int k = wejscie.nextInt();
        // int n = wejscie.nextInt();
        // int m = wejscie.nextInt();
        // int losowa;
        // Random rand = new Random();
        // Boolean[] tablica = new Boolean[k];
        // for(int i =0; i<tablica.length; i++)
        // {
        //     losowa = rand.nextInt(1,5);
        //     if(losowa<4)
        //     {
        //         tablica[i]=true;
        //     }
        //     else
        //     {
        //         tablica[i]=false;
        //     }
        // }
        // Boolean[][] tablica2d = new Boolean[n][m];
        // if(n*m==k)
        // {
        //     int indeks = 0;
        //     for(int i =0; i<n; i++)
        //     {
        //         for(int j =0; j<m; j++)
        //         {
        //             tablica2d[i][j] = tablica[indeks];
        //             indeks++;
        //         }
        //     }
        // }
    }
}
