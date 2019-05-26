import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class SerialClustering {

    private static int getMinCentroid(List<Point> centroid, Point min) {
        int minDistance = centroid.get(0).getDistance(min);
        int pos = 0;
        for (int i = 1; i < centroid.size(); i++) {
            if (centroid.get(i).getDistance(min) < minDistance) {
                minDistance = centroid.get(i).getDistance(min);
                pos = i;
            }
        }
        return pos;
    }

    private static Point getCenter(List<City> cities) {
        float sumLatitude=0;
        float sumLongitude=0;
        for (City city: cities){
            sumLatitude += city.getLatitude();
            sumLongitude += city.getLongitude();
        }
        return new Point(sumLatitude/cities.size(),sumLongitude/cities.size());
    }

    public static List<List<City>> kMeansClustering(List<City> cities, int clustNumber, int iterations) {
        //inizializza i primi k centroidi come le k contee più popolose
        List<Point> centroid = cities.stream().sorted(Comparator.comparing(City::getPopulation)).limit(clustNumber).collect(Collectors.toList());
        List<List<City>> clusters = new ArrayList<>(clustNumber);
        for (int i = 0; i < iterations; i++) {
            // crea k cluster vuoti
        	clusters = new ArrayList<>(clustNumber);
            for (int j = 0; j < clustNumber; j++) {
            	clusters.add(j, new ArrayList<City>());
            }
            //Assegna ciascuna contea al cluster relativo al centroide più vicino
            for (City city : cities) {
                int minCentroid = getMinCentroid(centroid, city);
                clusters.get(minCentroid).add(city);
            }
            //Aggiorna i nuovi centroidi in base ai cluster ottenuti
            for (int j = 0; j < clusters.size(); j++) {
                centroid.set(j, getCenter(clusters.get(j)));
                }
        }
        return clusters;
    }
}