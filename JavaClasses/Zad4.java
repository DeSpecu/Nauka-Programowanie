package JavaClasses;

class Pracownik{

    String imie, nazwisko, stanowisko;
    int stazPracy;
    double pensja;

    public Pracownik(){
        this.imie = "Szymon";
        this.nazwisko = "Boniszewski";
        this.stazPracy = 0;
        this.pensja = 3490.51;
    }

    public Pracownik(String imie, String nazwisko, String stanowisko, int stazPracy){
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.stanowisko = stanowisko;
        this.stazPracy = stazPracy;
        if(stanowisko.equals("manager")){
            this.pensja = 4500.0 + stazPracy*500;
        }
        else if(stanowisko.equals("kierownik")){
            this.pensja = 4500.0 + stazPracy*1000;
        }
        else{
            this.pensja = 4500.0 + stazPracy*150;
        }
    }

    public String getImie(){
        return imie;
    }

    public String getNaziwsko(){
        return nazwisko;
    }
    
    public String getStanowisko(){
        return stanowisko;
    }

    public int getStazPracy(){
        return stazPracy;
    }

    public double getPensja(){
        return pensja;
    }

    public void setImie(String imie){
        this.imie = imie;
    }

    public void setNaziwsko(String naziwsko){
        this.nazwisko = naziwsko;
    }

    public void setStanowisko(String stanowisko){
        this.stanowisko = stanowisko;
    }

    public void setStazPracy(int stazPracy){
        this.stazPracy = stazPracy;
    }

    public void setPensja(double pensja){
        this.pensja = pensja;   
    }
}

public class Zad4 {
    public static void main(String[] args){

    }
}
