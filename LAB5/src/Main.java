import java.util.List;
import java.util.stream.Collectors;

public class Main{
    public static void main(String[] args){
        System.out.println("Script start");
        System.out.println("Parsing file...");
        List<City> cities = CityParser.parseFile("./inputFiles/cities-and-towns-of-usa.csv");

        System.out.println("Creating population arrays...");

        List<City> cities_250 = cities
            .stream()
            .filter(c -> c.getPopulation() > 250)
            .collect(Collectors.toList());

        List<City> cities_2000 = cities
            .stream()
            .filter(c -> c.getPopulation() > 2000)
            .collect(Collectors.toList());

        List<City> cities_5000 = cities
            .stream()
            .filter(c -> c.getPopulation() > 5000)
            .collect(Collectors.toList());

        List<City> cities_15000 = cities
            .stream()
            .filter(c -> c.getPopulation() > 15000)
            .collect(Collectors.toList());

        List<City> cities_50000 = cities
            .stream()
            .filter(c -> c.getPopulation() > 50000)
            .collect(Collectors.toList());

        List<City> cities_100000 = cities
            .stream()
            .filter(c -> c.getPopulation() > 100000)
            .collect(Collectors.toList());
        System.out.println("Computing...");
        List<List<City>> A = SerialClustering.kMeansClustering(cities_250, 20, 5);
        System.out.println(A.size());
        System.out.println("Computing...");
        List<Integer> B = new ParallelClustering().parallelKMeansClustering(cities_250, 20, 5);
        System.out.println(B);
    }
}