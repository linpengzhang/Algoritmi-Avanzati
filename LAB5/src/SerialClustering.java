import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import javafx.util.Pair;

public class SerialClustering {

    private static int getMinCentroid(List<Point> centroid, Point min) {
        int minDistance = centroid.get(0).getDistance(min);
        int pos = 0;
        for (int i = 1; i < centroid.size(); i++) {
            int curDistance = centroid.get(i).getDistance(min);
            if (curDistance < minDistance) {
                minDistance = curDistance;
                pos = i;
            }
        }
        return pos;
    }

    private static Point getCenter(List<City> cities) {
        if (cities.isEmpty())
            return new Point(0, 0);
        else {
            double sumLatitude = 0;
            double sumLongitude = 0;
            for (City city : cities) {
                sumLatitude += city.getLatitude();
                sumLongitude += city.getLongitude();
            }
            return new Point(sumLatitude / cities.size(), sumLongitude / cities.size());
        }
    }

    public static List<List<City>> kMeansClustering(List<City> cities, int clustNumber, int iterations) {
        // inizializza i primi k centroidi come le k contee più popolose
        List<Point> centroid = cities.stream()
                .sorted(Comparator.comparing(City::getPopulation).reversed())
                .limit(clustNumber).collect(Collectors.toList());
        List<List<City>> clusters = new ArrayList<>(clustNumber);
        for (int i = 0; i < iterations; i++) {
            // crea k cluster vuoti
            clusters = new ArrayList<>(clustNumber);
            for (int j = 0; j < clustNumber; j++) {
                clusters.add(j, new ArrayList<City>());
            }
            // Assegna ciascuna contea al cluster relativo al centroide più vicino
            for (City city : cities) {
                int minCentroid = getMinCentroid(centroid, city);
                clusters.get(minCentroid).add(city);
            }
            // Aggiorna i nuovi centroidi in base ai cluster ottenuti
            for (int j = 0; j < clusters.size(); j++) {
                centroid.set(j, getCenter(clusters.get(j)));
            }
        }
        return clusters;
    }

    public static Pair<List<List<City>>, List<Long>> kMeansClusteringWithTime(List<City> cities, int clustNumber, int iterations) {
        List<Long> time = new ArrayList<>();
        time.add(System.nanoTime());
        // inizializza i primi k centroidi come le k contee più popolose
        List<Point> centroid = cities.stream()
                .sorted(Comparator.comparing(City::getPopulation).reversed())
                .limit(clustNumber).collect(Collectors.toList());
        List<List<City>> clusters = new ArrayList<>(clustNumber);
        for (int i = 0; i < iterations; i++) {
            // crea k cluster vuoti
            clusters = new ArrayList<>(clustNumber);
            for (int j = 0; j < clustNumber; j++) {
                clusters.add(j, new ArrayList<City>());
            }
            // Assegna ciascuna contea al cluster relativo al centroide più vicino
            for (City city : cities) {
                int minCentroid = getMinCentroid(centroid, city);
                clusters.get(minCentroid).add(city);
            }
            // Aggiorna i nuovi centroidi in base ai cluster ottenuti
            for (int j = 0; j < clusters.size(); j++) {
                centroid.set(j, getCenter(clusters.get(j)));
            }
            time.add(System.nanoTime());
        }
        return new Pair<>(clusters, time);
    }
}