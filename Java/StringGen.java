package Java;

import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class StringGen{

    public static void main(String[] args) {

            Scanner wejscie = new Scanner(System.in);
            
            String linia;
            char c;
            Random rand = new Random();
            int dlugosc,litera;
            String slowo="";
            List<String> listaSlow = new LinkedList<String>();
            do{
                slowo="";
                dlugosc = rand.nextInt(21-1)+1;
                for(int i=0; i<dlugosc;i++)
                {
                    litera = rand.nextInt(123-97)+97;
                    char doSlowa = (char)litera;
                    slowo+=doSlowa;
                }
                System.out.println("Czy " + slowo + " jest słowem? t/n");
                linia = wejscie.nextLine();
                while (linia.length()!=1){
                    System.out.print("Podaj t lub n");
                    linia = wejscie.nextLine();
                }
                c = linia.charAt(0);
                for(String s : listaSlow){
                    if(slowo==s){
                        int indeksik = listaSlow.indexOf(slowo);
                        listaSlow.remove(indeksik);
                        break;
                    }
                }
                listaSlow.add(slowo);
            }
            while(c=='t');
            wejscie.close();
            for(String s : listaSlow){
                System.out.println(s);
            }
       
    }
}
