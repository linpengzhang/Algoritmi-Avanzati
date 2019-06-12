import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Main {
    public static void main(String[] args) {
        final int number_of_iter = 5;
        Set<String> exercises_to_run = new HashSet<>(Arrays.asList("1"/*, "2", "3", "4"*/));

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
        cities_list.add(new Pair<>(250, cities_250));
        cities_list.add(new Pair<>(2000, cities_2000));
        cities_list.add(new Pair<>(5000, cities_5000));
        cities_list.add(new Pair<>(15000, cities_15000));
        cities_list.add(new Pair<>(50000, cities_50000));
        cities_list.add(new Pair<>(100000, cities_100000));
        cities_list.add(new Pair<>(38183, cities));

        System.out.println("Exercises to run:" + exercises_to_run.toString());

        List<Pair<Integer, Pair<Long, Long>>> values = new ArrayList<>();
        if (exercises_to_run.contains("1")) {
            System.out.println("Running exercise: 1");
            for (Pair<Integer, List<City>> couple : cities_list) {
                long inizio = System.currentTimeMillis();
                SerialClustering.kMeansClustering(couple.getValue(), 50, number_of_iter);
                long fine = System.currentTimeMillis();
                long seriale = fine - inizio;
                inizio = System.currentTimeMillis();
                new ParallelClustering().parallelKMeansClustering(couple.getValue(), 50, number_of_iter, 1);
                fine = System.currentTimeMillis();
                long parallelo = fine - inizio;
                Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
                Pair<Integer, Pair<Long, Long>> punto = new Pair<>(couple.getKey(), tempi);
                values.add(punto);
            }
            //Plot
            PlotManager p1 = new PlotManager("Domanda 1 - Numero di punti variabile", "es1");
            p1.drawSeries("Seriale", values, true);
            p1.drawSeries("Parallelo", values, false);
            p1.saveToFile();
        } else {
            System.out.println("Skipping exercise 1...");
        }

        //ES 2
        if (exercises_to_run.contains("2")) {
            System.out.println("Running exercise: 2");
            values = new ArrayList<>();
            for (int i = 10; i < 100; i++) {
                long inizio = System.currentTimeMillis();
                SerialClustering.kMeansClustering(cities, i, number_of_iter);
                long fine = System.currentTimeMillis();
                long seriale = fine - inizio;
                inizio = System.currentTimeMillis();
                new ParallelClustering().parallelKMeansClustering(cities, i, number_of_iter, 1);
                fine = System.currentTimeMillis();
                long parallelo = fine - inizio;
                Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
                Pair<Integer, Pair<Long, Long>> punto = new Pair<>(i, tempi);
                values.add(punto);
            }
            //Plot
            PlotManager p2 = new PlotManager("Domanda 2 - Numero di cluster variabile", "es2");
            p2.drawSeries("Seriale", values, true);
            p2.drawSeries("Parallelo", values, false);
            p2.saveToFile();
        } else {
            System.out.println("Skipping exercise 2...");
        }

        //ES 3
        if (exercises_to_run.contains("3")) {
            System.out.println("Running exercise: 3");
            values = new ArrayList<>();
            for (int i = 10; i < 1000; i++) {
                long inizio = System.currentTimeMillis();
                SerialClustering.kMeansClustering(cities, 50, i);
                long fine = System.currentTimeMillis();
                long seriale = fine - inizio;
                inizio = System.currentTimeMillis();
                new ParallelClustering().parallelKMeansClustering(cities, 50, i, 1);
                fine = System.currentTimeMillis();
                long parallelo = fine - inizio;
                Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
                Pair<Integer, Pair<Long, Long>> punto = new Pair<>(i, tempi);
                values.add(punto);
            }
            //Plot
            PlotManager p3 = new PlotManager("Domanda 3 - Numero di iterazioni variabile", "es3");
            p3.drawSeries("Seriale", values, true);
            p3.drawSeries("Parallelo", values, false);
            p3.saveToFile();
        } else {
            System.out.println("Skipping exercise 3...");
        }

        //ES 4
        if (exercises_to_run.contains("4")) {
            System.out.println("Running exercise: 4");
            List<Pair<Integer, Long>> values_es_four = new ArrayList<>();
            for (int i = 1; i < 100; i++) {
                long inizio = System.currentTimeMillis();
                new ParallelClustering().parallelKMeansClustering(cities, 50, number_of_iter, i);
                long fine = System.currentTimeMillis();
                Pair<Integer, Long> punto = new Pair<>(i, fine - inizio);
                values_es_four.add(punto);
            }
            //Plot
            PlotManager p4 = new PlotManager("Domanda 4 - Valore di Cutoff variabile", "es4");
            p4.drawSeries("Parallelo", values_es_four);
            p4.saveToFile();
        } else {
            System.out.println("Skipping exercise 4...");
        }
        System.out.println("Script end");
    }
}