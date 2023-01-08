package JavaClasses;

class Lancuch{
    String lancuch, koncowka;
    char pierwszaLitera;

    public Lancuch(){
        lancuch = "tak";
        koncowka = "hij";
        pierwszaLitera = 'a';
    }

    public Lancuch(String lancuch){
        if(lancuch.length()>=5){
            this.lancuch = lancuch;
        }
        while(lancuch.length()<5){
            int forchar = lancuch.charAt(lancuch.length()-1);
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

    public void Merge(String s){
        StringBuilder sb = new StringBuilder();
        int len = (s.length()>lancuch.length()) ? lancuch.length():s.length();

        for(int i=0; i<len; i++){

            sb.append(lancuch.charAt(i));
            sb.append(s.charAt(i));
        }

        this.lancuch = sb.toString();
    }

    public int IleASCII(){
        int toSum;
        int sum=0;
        for(int i=0; i<lancuch.length(); i++){
            toSum = lancuch.charAt(i);
            sum+=toSum;
        }
        return sum;
    }
}

public class Zad2 {
    public static void main(String[] args){

        Lancuch l = new Lancuch();
        System.out.println(l.IleASCII());
    }
}
