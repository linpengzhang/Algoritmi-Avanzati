import javafx.util.Pair;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class ParallelClustering {

    private class ParallelReduceCluster extends RecursiveTask<Pair<Pair<Integer, Integer>, Integer>> {
        private List<Integer> cluster; // contiene per ciascun punto l'indice del cluster a cui appartiene
        private final int start; // indice iniziale
        private final int end; // indice finale
        private final int h;
        private List<City> cities;

        ParallelReduceCluster(List<Integer> cluster, int start, int end, int h, List<City> cities) {
            this.cluster = cluster;
            this.start = start;
            this.end = end;
            this.h = h;
            this.cities = cities;
        }

        protected Pair<Pair<Integer, Integer>, Integer> compute() {
            if (start == end) {
                if (cluster.get(start) == h)
                    return new Pair<>(new Pair<>((int)cities.get(start).getLatitude(), (int)cities.get(start).getLongitude()), 1);
                else
                    return new Pair<>(new Pair<>(0, 0), 0);
            }
            else {
                int mid = (start + end) / 2;
                ParallelReduceCluster p1 = new ParallelReduceCluster(cluster, start, mid, h, cities);
                p1.fork();
                ParallelReduceCluster p2 = new ParallelReduceCluster(cluster, mid + 1, end, h, cities);
                Pair<Pair<Integer, Integer>, Integer> res2 = p2.compute();
                Pair<Pair<Integer, Integer>, Integer> res1 = p1.join();
                int sum_lat = res1.getKey().getKey() + res2.getKey().getKey();
                int sum_lon = res1.getKey().getValue() + res2.getKey().getValue();
                int size = res1.getValue() + res2.getValue();
                return new Pair<>(new Pair<>(sum_lat, sum_lon), size);
            }
        }
    }

    public class firstParallelFor extends RecursiveTask<Void> {
        private City city;
        private List<Point> centroid;
        private List<Integer> cluster;
        final int index;

        private int getMinCentroid(List<Point> centroid, Point min) {
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

        public firstParallelFor(City city, List<Point> centroid, List<Integer> cluster, int index) {
            this.city = city;
            this.centroid = centroid;
            this.cluster = cluster;
            this.index = index;
        }

        public Void compute() {
            int l = getMinCentroid(centroid, city);
            cluster.set(index, l);
            return null;
        }
    }

    private class secondParallelFor extends RecursiveTask<Void>{
        private List<Integer> cluster;
        private final int h;
        private List<City> cities;
        private List<Point> centroid;

        secondParallelFor(List<Integer> cluster, int h, List<City> cities, List<Point> centroid) {
            this.cluster = cluster;
            this.h = h;
            this.cities = cities;
            this.centroid = centroid;
        }

        public Void compute(){
            ParallelReduceCluster task = new ParallelReduceCluster(cluster, 0, cities.size() - 1, h, cities);
            Pair<Pair<Integer, Integer>, Integer> res = task.compute();
            int sum_lat = res.getKey().getKey();
            int sum_lon = res.getKey().getValue();
            int size = res.getValue();
            if (size == 0)
                centroid.set(h, new Point(0, 0));
            else
                centroid.set(h, new Point(sum_lat / size, sum_lon / size));
            return null;
        }
    }

    public List<Integer> parallelKMeansClustering(List<City> cities, int clustNumber, int iterations) {
        ForkJoinPool commonPool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());
        List<Point> centroid = cities.stream().sorted(Comparator.comparing(City::getPopulation)
                .reversed())
                .limit(clustNumber)
                .collect(Collectors.toList());
        List<Integer> cluster = new ArrayList<>(Collections.nCopies(cities.size(), 0));

        for (int i = 0; i < iterations; i++) {

            //-------------------------------------
            //First parallel for
            List<firstParallelFor> firstParallelForTasks = new ArrayList<>();
            for (int j = 0; j < cities.size(); j++) {
                firstParallelFor task = new firstParallelFor(cities.get(j), centroid, cluster, j);
                //task.fork();
                commonPool.execute(task);
                firstParallelForTasks.add(task);
            }
            for (firstParallelFor task : firstParallelForTasks) {
                task.join();
            }
            //-------------------------------------
            //Second parallel for
            List<secondParallelFor> secondParallelForTasks = new ArrayList<>();
            for (int j = 0; j < centroid.size(); j++) {
                secondParallelFor task = new secondParallelFor(cluster, j, cities, centroid);
                //task.fork();
                commonPool.execute(task);
                secondParallelForTasks.add(task);
            }
            for (secondParallelFor task : secondParallelForTasks) {
                task.join();
            }

        }//End for non parallelo

        return cluster;
    }//end funzione parallelKMeansClustering
}
