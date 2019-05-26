

public class City extends Point{
    private int id;
    private String name;
    private int population;

    public City(int id, String name, int pop, float lat, float lon) {
        super(lat, lon);
        this.id = id;
        this.name = name;
        population = pop;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getPopulation() {
        return population;
    }
}