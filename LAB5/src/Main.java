import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        System.out.println("Script start");
        System.out.println("Parsing file...");
        List<City> cities = CityParser.parseFile("src/inputFiles/cities-and-towns-of-usa.csv");

        System.out.println("Creating population arrays...");
        List<City> cities_250 = cities.stream().filter(c -> c.getPopulation() > 250).collect(Collectors.toList());
        List<City> cities_2000 = cities.stream().filter(c -> c.getPopulation() > 2000).collect(Collectors.toList());
        List<City> cities_5000 = cities.stream().filter(c -> c.getPopulation() > 5000).collect(Collectors.toList());
        List<City> cities_15000 = cities.stream().filter(c -> c.getPopulation() > 15000).collect(Collectors.toList());
        List<City> cities_50000 = cities.stream().filter(c -> c.getPopulation() > 50000).collect(Collectors.toList());
        List<City> cities_100000 = cities.stream().filter(c -> c.getPopulation() > 100000).collect(Collectors.toList());

        System.out.println("Computing Serial...");
        long inizio = System.currentTimeMillis();
        List<List<City>> A = SerialClustering.kMeansClustering(cities_15000, 50, 100);
        long fine = System.currentTimeMillis();
        System.out.println(fine-inizio);        


        System.out.println("Computing Parallel...");
        inizio = System.currentTimeMillis();
        List<Integer> B = new ParallelClustering().parallelKMeansClustering(cities_15000, 50, 100);
        fine = System.currentTimeMillis();
        System.out.println(fine-inizio);

        test(A, B, cities_15000);

        //grafico
        Plot plot = Plot.plot(null).
                series(null, Plot.data().xy(1, 2).xy(3, 4), null);
        try {
            plot.save("sample_minimal", "png");
        } catch (Exception e) {
            System.out.println(e);
        }    
    }

    private static void test(List<List<City>> clustering_1, List<Integer> clustering_2, List<City> cities){
        int clustNumber = clustering_1.size();
        List<List<City>> n_clustering_2 = new ArrayList<>();
        for (int j = 0; j < clustNumber; j++) {
            n_clustering_2.add(j, new ArrayList<City>());
        }
        for (int i = 0; i < clustering_2.size(); i++) {
            n_clustering_2.get(clustering_2.get(i)).add(cities.get(i));
        }

        for (int j = 0; j < clustNumber; j++) {
            int s1 = clustering_1.get(j).size();
            int s2 = n_clustering_2.get(j).size();
            if(s1 != s2)
                System.out.println("W: Cluster " + j + ": " + s1 + " - " + s2);
            else
                System.out.println("Cluster " + j + ": " + s1);
        }
    }
}