package Java;

import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Palindrom {
    
    public static void main(String[] args){

        Scanner wejscie = new Scanner(System.in);
        String litera;
        List<String> literki = new LinkedList<String>();
        do{
            System.out.println("Podaj literę, lub '/' żeby zakończyć");
            litera = wejscie.nextLine();
            literki.add(litera);
        }
        while(!litera.equals("/"));
        literki.remove(literki.size()-1);
        wejscie.close();

        String wyjscie="";
        Random rand = new Random();
        for(int i =0; i<literki.size();i++)
        {
            int index = rand.nextInt(literki.size());
            wyjscie+=literki.get(index);
            wyjscie=literki.get(index)+wyjscie;
        }
        System.out.println(wyjscie);
    }
}
