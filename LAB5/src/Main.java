import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Main {
    public static void main(String[] args) {
        final int number_of_iter = 100;
        Set<String> exercises_to_run = new HashSet<>(Arrays.asList("1"));

        System.out.println("Script start");
        System.out.println("Parsing file...");
        List<City> cities = CityParser.parseFile("./inputFiles/cities-and-towns-of-usa.csv");
        System.out.println("Creating population arrays...");
        List<City> cities_250 = cities.stream().filter(c -> c.getPopulation() > 250).collect(Collectors.toList());
        List<City> cities_2000 = cities.stream().filter(c -> c.getPopulation() > 2000).collect(Collectors.toList());
        List<City> cities_5000 = cities.stream().filter(c -> c.getPopulation() > 5000).collect(Collectors.toList());
        List<City> cities_15000 = cities.stream().filter(c -> c.getPopulation() > 15000).collect(Collectors.toList());
        List<City> cities_50000 = cities.stream().filter(c -> c.getPopulation() > 50000).collect(Collectors.toList());
        List<City> cities_100000 = cities.stream().filter(c -> c.getPopulation() > 100000).collect(Collectors.toList());

        List<Pair<Integer, List<City>>> cities_list = new ArrayList<>();
        cities_list.add(new Pair<>(cities_100000.size(), cities_100000));
        cities_list.add(new Pair<>(cities_50000.size(), cities_50000));
        cities_list.add(new Pair<>(cities_15000.size(), cities_15000));
        cities_list.add(new Pair<>(cities_5000.size(), cities_5000));
        cities_list.add(new Pair<>(cities_2000.size(), cities_2000));
        cities_list.add(new Pair<>(cities_250.size(), cities_250));
        cities_list.add(new Pair<>(cities.size(), cities));

        System.out.println("JVM available threads: " + Runtime.getRuntime().availableProcessors());
        System.out.println("Exercises to run:" + exercises_to_run.toString());
        System.out.println("----------------");

        List<Pair<Integer, Pair<Long, Long>>> values = new ArrayList<>();
        List<Pair<Integer, Double>> speedup = new ArrayList<>();
        if (exercises_to_run.contains("1")) {
            int i = 1;
            final int citiesSize = cities_list.size();
            System.out.println("Running exercise: 1");
            for (Pair<Integer, List<City>> couple : cities_list) {
                System.out.println("Es 1 - Iteration:" + i + "/" + citiesSize + " (cities:" + couple.getKey() + ")");
                i++;
                long inizio = System.nanoTime();
                SerialClustering.kMeansClustering(couple.getValue(), 50, number_of_iter);
                long fine = System.nanoTime();
                long seriale = (fine - inizio) / 1000000;
                inizio = System.nanoTime();
                new ParallelClustering().parallelKMeansClustering(couple.getValue(), 50, number_of_iter, 1);
                fine = System.nanoTime();
                long parallelo = (fine - inizio) / 1000000;
                Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
                Pair<Integer, Pair<Long, Long>> punto = new Pair<>(couple.getKey(), tempi);
                values.add(punto);
                speedup.add(new Pair<>(couple.getKey(), (double) tempi.getKey()/ (double) tempi.getValue()));
            }

            //Plot
            PlotManager p1 = new PlotManager("Domanda 1 - Numero di punti variabile", "es1",
                    "Numero di punti", "Tempo di calcolo (ms)");
            p1.drawSeries("Seriale", values, true);
            p1.drawSeries("Parallelo", values, false);
            p1.saveToFile();
            new PlotManager("Domanda 1 - Speedup", "es1_speed",
                    "Numero di punti", "Speedup").drawSeriesD("Speedup", speedup).saveToFile();
        } else {
            System.out.println("Skipping exercise 1...");
        }

        //ES 2
        if (exercises_to_run.contains("2")) {
            System.out.println("Running exercise: 2");
            values = new ArrayList<>();
            speedup = new ArrayList<>();
            final int iterations = 100;
            for (int i = 10; i <= iterations; i++) {
                System.out.println("Es 2 - Iteration:" + i + "/" + iterations);
                long inizio = System.nanoTime();
                SerialClustering.kMeansClustering(cities, i, number_of_iter);
                long fine = System.nanoTime();
                long seriale = (fine - inizio) / 1000000;
                inizio = System.nanoTime();
                new ParallelClustering().parallelKMeansClustering(cities, i, number_of_iter, 1);
                fine = System.nanoTime();
                long parallelo = (fine - inizio) / 1000000;
                Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
                Pair<Integer, Pair<Long, Long>> punto = new Pair<>(i, tempi);
                Pair<Integer, Pair<Long, Long>> speed = new Pair<>(i, tempi);
                values.add(punto);
                speedup.add(new Pair<>(i, (double) tempi.getKey()/ (double) tempi.getValue()));
            }
            //Plot
            PlotManager p2 = new PlotManager("Domanda 2 - Numero di cluster variabile", "es2",
                    "Numero di cluster", "Tempo di calcolo (ms)");
            p2.drawSeries("Seriale", values, true);
            p2.drawSeries("Parallelo", values, false);
            p2.saveToFile();
            new PlotManager("Domanda 1 - Speedup", "es1_speed",
            "Numero di cluster", "Speedup").drawSeriesD("Speedup", speedup).saveToFile();

        } else {
            System.out.println("Skipping exercise 2...");
        }

        //ES 3
        if (exercises_to_run.contains("3")) {
            System.out.println("Running exercise: 3");
            System.out.println("Es 3 - Computing times...");
            values = new ArrayList<>();
            speedup = new ArrayList<>();
            System.out.println("Es 3 - Running serial clustering...");
            List<Long> serialTime = SerialClustering.kMeansClusteringWithTime(cities, 50, 1000).getValue();
            System.out.println("Es 3 - Running parallel clustering...");
            List<Long> parallelTime = new ParallelClustering().parallelKMeansClusteringWithTime(cities, 50, 1000, 1).getValue();
            System.out.println("Es 3 - Preparing the graph...");
            for (int i = 10; i <= 1000; i++) {
                Pair<Long, Long> tempi = new Pair<>(
                        (serialTime.get(i) - serialTime.get(0)) / 1000000,
                        (parallelTime.get(i) - parallelTime.get(0) / 1000000)
                );
                Pair<Integer, Pair<Long, Long>> punto = new Pair<>(i, tempi);
                values.add(punto);
                speedup.add(new Pair<>(i, (double) tempi.getKey()/ (double) tempi.getValue()));
            }
            //Plot
            PlotManager p3 = new PlotManager("Domanda 3 - Numero di iterazioni variabile", "es3",
                    "Numero di iterazioni", "Tempo di calcolo (ms)");
            p3.drawSeries("Seriale", values, true);
            p3.drawSeries("Parallelo", values, false);
            p3.saveToFile();
            new PlotManager("Domanda 1 - Speedup", "es1_speed",
            "Numero di iterazioni", "Speedup").drawSeriesD("Speedup", speedup).saveToFile();

        } else {
            System.out.println("Skipping exercise 3...");
        }

        //ES 4
        if (exercises_to_run.contains("4")) {
            System.out.println("Running exercise: 4");
            List<Pair<Integer, Long>> values_es_four = new ArrayList<>();
            final int citiesSize = cities.size();
            for (int i = 1; i <= citiesSize; i = i + 100) {
                System.out.println("Es 4 - Iteration:" + i + "/" + citiesSize);
                long inizio = System.nanoTime();
                new ParallelClustering().parallelKMeansClustering(cities, 50, number_of_iter, i);
                long fine = System.nanoTime();
                Pair<Integer, Long> punto = new Pair<>(i, (fine - inizio) / 1000000);
                values_es_four.add(punto);
            }
            //Plot
            PlotManager p4 = new PlotManager("Domanda 4 - Valore di Cutoff variabile", "es4",
                    "Valore di cutoff", "Tempo di calcolo (ms)", 1500, 800);
            p4.drawSeries("Parallelo", values_es_four);
            p4.saveToFile();
        } else {
            System.out.println("Skipping exercise 4...");
        }
        System.out.println("Script end");
    }
}