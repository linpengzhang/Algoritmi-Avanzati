import javafx.util.Pair;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
import java.util.stream.Collectors;

public class ParallelClustering {

    private class ParallelReduceCluster extends RecursiveTask<Pair<Pair<Double, Double>, Integer>> {
        private List<Integer> cluster; // contiene per ciascun punto l'indice del cluster a cui appartiene
        private final int start; // indice iniziale della porzione di 'cluster' da considerare
        private final int end; // indice finale inclusivo della porzione di 'cluster' da considerare
        private final int h; // indice del cluster di interesse
        private List<City> cities; // lista delle contee
        private final int cutoff;

        ParallelReduceCluster(List<Integer> cluster, int start, int end, int h, List<City> cities) {
            this(cluster, start, end, h, cities, 1);
        }

        ParallelReduceCluster(List<Integer> cluster, int start, int end, int h, List<City> cities, int cutoff) {
            this.cluster = cluster;
            this.start = start;
            this.end = end;
            this.h = h;
            this.cities = cities;
            this.cutoff = cutoff;
        }

        protected Pair<Pair<Double, Double>, Integer> compute() {
            if (end - start < cutoff) {
                double sommaLat = 0d;
                double sommaLon = 0d;
                int size = 0;
                for (int i = start; i <= end; i++) {
                    if (cluster.get(i) == h) {
                        sommaLat += cities.get(i).getLatitude();
                        sommaLon += cities.get(i).getLongitude();
                        size++;
                    }
                }
                return new Pair<>(new Pair<>(sommaLat, sommaLon), size);
            } else {
                int mid = (start + end) / 2;
                ParallelReduceCluster p1 = new ParallelReduceCluster(cluster, start, mid, h, cities, cutoff);
                p1.fork();
                ParallelReduceCluster p2 = new ParallelReduceCluster(cluster, mid + 1, end, h, cities, cutoff);
                Pair<Pair<Double, Double>, Integer> res2 = p2.compute();
                Pair<Pair<Double, Double>, Integer> res1 = p1.join();
                double sum_lat = res1.getKey().getKey() + res2.getKey().getKey();
                double sum_lon = res1.getKey().getValue() + res2.getKey().getValue();
                int size = res1.getValue() + res2.getValue();
                return new Pair<>(new Pair<>(sum_lat, sum_lon), size);
            }
        }
    }

    private class FirstParallelFor extends RecursiveTask<Void> {
        private List<City> cities; // lista delle contee
        private List<Point> centroid; // lista dei centroidi di ciascun cluster
        private List<Integer> cluster; // contiene per ciascun punto l'indice del cluster a cui appartiene
        private final int start; // indice iniziale della porzione di 'cities' da considerare
        private final int end; // indice finale inclusivo della porzione di 'cities' da considerare
        private final int cutoff;

        public FirstParallelFor(List<City> cities, List<Point> centroid, List<Integer> cluster, int start, int end) {
            this(cities, centroid, cluster, start, end, 1);
        }

        public FirstParallelFor(List<City> cities, List<Point> centroid, List<Integer> cluster, int start, int end, int cutoff) {
            this.cities = cities;
            this.centroid = centroid;
            this.cluster = cluster;
            this.start = start;
            this.end = end;
            this.cutoff = cutoff;
        }

        private int getMinCentroid(List<Point> centroid, Point min) {
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

        protected Void compute() {
            if (end - start < cutoff) {
                for (int i = start; i <= end; i++) {
                    int l = getMinCentroid(centroid, cities.get(i));
                    cluster.set(i, l);
                }
            } else {
                int middle = (start + end) / 2;
                FirstParallelFor p1 = new FirstParallelFor(cities, centroid, cluster, start, middle, cutoff);
                p1.fork();
                FirstParallelFor p2 = new FirstParallelFor(cities, centroid, cluster, middle + 1, end, cutoff);
                p2.compute();
                p1.join();
            }
            return null;
        }
    }

    private class SecondParallelFor extends RecursiveTask<Void> {
        private List<Integer> cluster; // contiene per ciascun punto l'indice del cluster a cui appartiene
        private final int start; // indice iniziale della porzione di indici dei cluster da considerare
        private final int end; // indice finale inclusivo della porzione di indici dei cluster da considerare
        private List<City> cities; // lista delle contee
        private List<Point> centroid; // lista dei centroidi di ciascun cluster
        private final int cutoff;

        SecondParallelFor(List<Integer> cluster, int start, int end, List<City> cities, List<Point> centroid) {
            this(cluster, start, end, cities, centroid, 1);
        }

        SecondParallelFor(List<Integer> cluster, int start, int end, List<City> cities, List<Point> centroid, int cutoff) {
            this.cluster = cluster;
            this.start = start;
            this.end = end;
            this.cities = cities;
            this.centroid = centroid;
            this.cutoff = cutoff;
        }

        public Void compute() {
            if (end - start < cutoff) {
                for (int i = start; i <= end; i++) {
                    ParallelReduceCluster task = new ParallelReduceCluster(cluster, 0, cluster.size() - 1, i, cities, cutoff);
                    Pair<Pair<Double, Double>, Integer> res = task.compute();
                    double sum_lat = res.getKey().getKey();
                    double sum_lon = res.getKey().getValue();
                    int size = res.getValue();
                    if (size == 0)
                        centroid.set(i, new Point(0, 0));
                    else
                        centroid.set(i, new Point(sum_lat / size, sum_lon / size));
                }
            } else {
                int middle = (start + end) / 2;
                SecondParallelFor p1 = new SecondParallelFor(cluster, start, middle, cities, centroid, cutoff);
                p1.fork();
                SecondParallelFor p2 = new SecondParallelFor(cluster, middle + 1, end, cities, centroid, cutoff);
                p2.compute();
                p1.join();
            }
            return null;
        }
    }

    public List<Integer> parallelKMeansClustering(List<City> cities, int clustNumber, int iterations, int cutoff) {
        ForkJoinPool commonPool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());

        // centroids[h] associa al cluster C_h il suo centroide
        // (i centroidi iniziali sono le 'clustNumber' contee più popolose)
        List<Point> centroid = cities.stream()
                .sorted(Comparator.comparing(City::getPopulation).reversed())
                .limit(clustNumber).collect(Collectors.toList());
        // cluster[j] associa city[j] all'indice l del cluster C_l a cui appartiene
        List<Integer> cluster = new ArrayList<>(Collections.nCopies(cities.size(), 0));

        for (int i = 0; i < iterations; i++) {

            //First parallel for
            FirstParallelFor firstTask = new FirstParallelFor(cities, centroid, cluster, 0, cities.size() - 1, cutoff);
            commonPool.invoke(firstTask); //execute and join first parallel for

            //Second parallel for
            SecondParallelFor secondTask = new SecondParallelFor(cluster, 0, centroid.size() - 1, cities, centroid, cutoff);
            commonPool.invoke(secondTask); //execute and join second parallel for

        }
        return cluster;
    }

    public Pair<List<Integer>, List<Long>> parallelKMeansClusteringWithTime(List<City> cities, int clustNumber, int iterations, int cutoff) {
        List<Long> time = new ArrayList<>();
        time.add(System.nanoTime());
        ForkJoinPool commonPool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());

        // centroids[h] associa al cluster C_h il suo centroide
        // (i centroidi iniziali sono le 'clustNumber' contee più popolose)
        List<Point> centroid = cities.stream()
                .sorted(Comparator.comparing(City::getPopulation).reversed())
                .limit(clustNumber).collect(Collectors.toList());
        // cluster[j] associa city[j] all'indice l del cluster C_l a cui appartiene
        List<Integer> cluster = new ArrayList<>(Collections.nCopies(cities.size(), 0));

        for (int i = 0; i < iterations; i++) {

            //First parallel for
            FirstParallelFor firstTask = new FirstParallelFor(cities, centroid, cluster, 0, cities.size() - 1, cutoff);
            commonPool.invoke(firstTask); //execute and join first parallel for

            //Second parallel for
            SecondParallelFor secondTask = new SecondParallelFor(cluster, 0, centroid.size() - 1, cities, centroid, cutoff);
            commonPool.invoke(secondTask); //execute and join second parallel for

            time.add(System.nanoTime());
        }
        return new Pair<>(cluster, time);
    }
}
