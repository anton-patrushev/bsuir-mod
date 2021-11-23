import java.util.ArrayList;
import java.util.Random;

public class PracticalQS {
    public static final double TICKS_COUNT = 10000.;
    public static final int ACCURACY = 5;

    private Random random = new Random();
    private double[] delays = {nextDoubleExp(App.l), Double.MAX_VALUE, Double.MAX_VALUE};
    private double time = 0.;
    private boolean[] serviceIsBusy = {false, false};

    private int generatedAppCount = 0;
    private int deniedAppCount = 0;
    private ArrayList<Double> processingTimes = new ArrayList<>();

    private double[] stateProbabilities = new double[App.STATE_COUNT];
    private double[] loadCoefficients = new double[2];
    private double denialProbability;
    private double averageTime;

    public PracticalQS() {
        for (int i = 0; i < App.STATE_COUNT; i++) {
            stateProbabilities[i] = 0.;
        }
    }

    private static double myRound(double value) {
        double scale = Math.pow(10, ACCURACY);
        return Math.round(value * scale) / scale;
    }

    private double nextDoubleExp(double lambda) {
        return myRound((-1. / lambda) * Math.log(random.nextDouble()));
    }

    private int getMinDelayIndex() {
        int minDelayIndex = 0;
        for (int i = 1; i < delays.length; i++) {
            if (delays[i] < delays[minDelayIndex]) {
                minDelayIndex = i;
            }
        }
        return minDelayIndex;
    }

    private void changeTime(double timeToShift) {
        if      (!serviceIsBusy[0] && !serviceIsBusy[1])
            stateProbabilities[0] += timeToShift;
        else if (serviceIsBusy[0] && !serviceIsBusy[1])
            stateProbabilities[1] += timeToShift;
        else if (!serviceIsBusy[0] && serviceIsBusy[1])
            stateProbabilities[2] += timeToShift;
        else if (serviceIsBusy[0] && serviceIsBusy[1])
            stateProbabilities[3] += timeToShift;

        time += timeToShift;
        for (int i = 0; i < delays.length; i++) {
            if (delays[i] == timeToShift) {
                delays[i] = Double.MAX_VALUE;
            }
            else {
                delays[i] -= timeToShift;
            }
        }
    }

    public void run() {
        while (time < TICKS_COUNT) {
            int minDelayIndex = getMinDelayIndex();
            changeTime(delays[minDelayIndex]);

            if (minDelayIndex == 0) {
                generatedAppCount++;
                delays[0] = nextDoubleExp(App.l);
                if (!serviceIsBusy[0]) {
                    serviceIsBusy[0] = true;
                    delays[1] = nextDoubleExp(App.m1);
                    processingTimes.add(delays[1]);
                }
                else if (!serviceIsBusy[1]) {
                    serviceIsBusy[1] = true;
                    delays[2] = nextDoubleExp(App.m2);
                    processingTimes.add(delays[2]);
                }
                else {
                    deniedAppCount++;
//                    processingTimes.add(0.);
                }
            }
            else {
                serviceIsBusy[minDelayIndex - 1] = false;
            }
        }
    }

    public void calculateValues() {
        for (int i = 0; i < App.STATE_COUNT; i++) {
            stateProbabilities[i] /= time;
        }
        loadCoefficients[0] = stateProbabilities[1] + stateProbabilities[3];
        loadCoefficients[1] = stateProbabilities[2] + stateProbabilities[3];
        denialProbability = (double) deniedAppCount / (double) generatedAppCount;
        double sum = 0.;
        for (Double d : processingTimes)
            sum += d;
        averageTime = sum / (double) processingTimes.size();
    }

    public double[] getStateProbabilities() {
        return stateProbabilities;
    }

    public double[] getLoadCoefficients() {
        return loadCoefficients;
    }

    public double getDenialProbability() {
        return denialProbability;
    }

    public double getAverageTime() {
        return averageTime;
    }
}
