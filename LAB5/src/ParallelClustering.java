import javafx.util.Pair;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class ParallelClustering {

    private class ParallelReduceCluster extends RecursiveTask<Pair<Integer, Integer>> {
        private int h;
        private List<City> cluster;

        ParallelReduceCluster(List<City> cluster, int h) {
            this.cluster = cluster;
            this.h = h;
        }

        protected Pair<Integer, Integer> compute() {
            //Todo
            //Ritorna un pair per ritornare <sum, size>
        }//end compute
    }

    public class firstParallelFor implements Callable<Integer> {
        private City city;
        private List<Point> centroid;

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

        public firstParallelFor(City city, List<Point> centroid) {
            this.city = city;
            this.centroid = centroid;
        }

        public Integer call() {
            return getMinCentroid(centroid, city);
        }
    }

    private class secondParallelFor implements Callable<Pair<Integer, Integer>>{
        private int h;
        private List<City> cluster;

        secondParallelFor(List<City> cluster, int h) {
            this.cluster = cluster;
            this.h = h;
        }

        public Pair<Integer, Integer> call(){
            ParallelReduceCluster task = new ParallelReduceCluster(cluster, h);
            //Chiamo ParallelReduceCluster che è ricorsiva parallela e attendo che finisca
            try {
                task.join();
                return task.get();
            } catch (ExecutionException | InterruptedException e) {
                e.printStackTrace();
                return null;
            }
        }
    }

    public void parallelKMeansClustering(List<City> cities, int clustNumber, int iterations) {
        ForkJoinPool commonPool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());

        List<Point> centroid = cities.stream().sorted(Comparator.comparing(City::getPopulation))
                .limit(clustNumber)
                .collect(Collectors.toList());
        List<City> cluster = new ArrayList<>(cities.size());

        for (int i = 0; i < iterations; i++) {
            //-------------------------------------
            //First parallel for
            List<ForkJoinTask<Integer>> firstParallelForTasks = new ArrayList<>();
            //Eseguo tutte le task in parallelo, creandone una per ogni elemento del for
            for (City city : cities) {
                firstParallelForTasks.add(commonPool.submit(new firstParallelFor(city, centroid)));
            }
            //Prendo tutti i risultati (fa anche il join aspettando i risultati)
            for (int j = 0; j < cities.size(); j++) {
                try {
                    //TODO TOFIX
                    //cluster.set(j, firstParallelForTasks.get(j).get());
                } catch (ExecutionException | InterruptedException e) {
                    e.printStackTrace();
                }
            }
            //-------------------------------------
            //Second parallel for
            List<ForkJoinTask<Pair<Integer, Integer>>> secondParallelForTasks = new ArrayList<>();
            //Eseguo tutte le task in parallelo, creandone una per ogni elemento del for
            for (int f=0; f < clustNumber; f++) {
                secondParallelForTasks.add(commonPool.submit(new secondParallelFor(cluster, f)));
            }
            //Prendo tutti i risultati (fa anche il join aspettando i risultati)
            for (int j = 0; j < cities.size(); j++) {
                try {
                    //TODO TOFIX
                    //centroid.set(f, new Point());
                } catch (ExecutionException | InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }//End for non parallelo
    }//end funzione parallelKMeansClustering
}
