# Algoritmi Avanzati - Laboratorio 5
## Clustering k-means parallelo

To read the assignment's instructions see [TASK.md](TASK.md).

## Warning
This code run and compare the execution of the serial version of K-means with the parallel version.

The execution of exercises 2 and 4 may take **more than 2/3 hours** (each, depends on your processor), we used an Azure VM to let it execute for hours.

Exercise 3 should take ~30min, exercise 1 is the fastest and shouldn't give you any problem.

## How to run
* First, enter the `src/` folder and build the java sources:
```java
cd src
javac *.java
```
* Then run the Main class:
```java
java Main
```

Considering you have to add a library to the classpath, just use `build.bat`/`.sh` and `run.bat`/`.sh`