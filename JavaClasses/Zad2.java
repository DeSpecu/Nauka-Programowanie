package JavaClasses;

class Lancuch{
    String lancuch, koncowka;
    char pierwszaLitera;

    public Lancuch(){
        lancuch = "abcdefghij";
        koncowka = "hij";
        pierwszaLitera = 'a';
    }

    public Lancuch(String lancuch){
        if(lancuch.length()>=5){
            this.lancuch = lancuch;
        }
        while(lancuch.length()<5){
            int forchar = (int)lancuch.charAt(lancuch.length()-1);
            StringBuilder sb = new StringBuilder(lancuch);
            sb.append((char)(forchar+1));
            lancuch = sb.toString();
        }
        this.lancuch = lancuch;
        int index = lancuch.length();
        koncowka = lancuch.substring(index-3, index);
        pierwszaLitera = lancuch.charAt(0);
    }

    public String getLancuch(){
        return lancuch;
    }

    public String gerKoncowka(){
        return koncowka;
    }

    public char getPierwszaLitera(){
        return pierwszaLitera;
    }
}

public class Zad2 {
    public static void main(String[] args){

        Lancuch l = new Lancuch("si");
        System.out.println(l.lancuch);
    }
}
