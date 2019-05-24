import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class SerialClustering {

    private int getMinCentroid(List<City> centroid, City min) {
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

    private float getCenter(List<City> cities) {
        return 0.0f;
    }

    public List<List<City>> kMeansClustering(List<City> cities, int clustNumber, int iterations) {
        int numberOfCities = cities.size();

        //inizializza i primi k centroidi come le k contee più popolose
        List<City> centroid = cities.stream().sorted(Comparator.comparing(City::getCityPopulation)).limit(clustNumber).collect(Collectors.toList());

        List<List<City>> clusters = new ArrayList<>(clustNumber);
        for (int i = 0; i < iterations; i++) {
            // crea k cluster vuoti
            clusters = new ArrayList<>(clustNumber);
            for (int j = 0; j < clusters.size(); j++) {
                clusters.set(j, new ArrayList<>());
            }

            //Assegna ciascuna contea al cluster relativo al centroide più vicino
            for (City city : cities) {
                int minCentroid = getMinCentroid(centroid, city);

                clusters.get(minCentroid).add(city);
            }
            //Aggiorna i nuovi centroidi in base ai cluster ottenuti
            for (int j = 0; j < clusters.size(); j++) {
                //TOFIX
                //centroid.set(j, getCenter(clusters.get(j)));
            }
        }
        return clusters;
    }
}