import Jama.Matrix;

public class TheoreticalQS {
    private double[] stateProbabilities = new double[App.STATE_COUNT];
    private double[] loadCoefficients = new double[2];
    private double denialProbability;
    private double averageTime;


    public void calculateStateProbabilities() {

        double[][] weightCoefficients = {

                //0 - 00
                {
                        1. - App.l,     //0 - 00
                        1. + App.m1,     //1 - 10
                        1. + App.m2,     //2 - 01
                        1.      //3 - 11
                },

                //1 - 10
                {
                        App.l,     //0 - 00
                        -(App.l + App.m1),     //1 - 10
                        0.,     //2 - 01
                        App.m2      //3 - 11
                },

                //2 - 01
                {
                        0.,     //0 - 00
                        0.,     //1 - 10
                        -(App.l + App.m2),     //2 - 01
                        App.m1      //3 - 11
                },

                //3 - 11
                {
                        0.,     //0 - 00
                        App.l,     //1 - 10
                        App.l,     //2 - 01
                        -(App.m1 + App.m2)      //3 - 11
                }

        };

        double[] freeCoefficients = {1., 0., 0., 0.};

        Matrix weightCoefficientsMatrix = new Matrix(weightCoefficients);
        Matrix freeCoefficientsMatrix = new Matrix(freeCoefficients, App.STATE_COUNT);
        Matrix stateProbabilitiesMatrix = weightCoefficientsMatrix.solve(freeCoefficientsMatrix);

        for (int i = 0; i < App.STATE_COUNT; i++) {
            stateProbabilities[i] = stateProbabilitiesMatrix.getArray()[i][0];
        }
    }

    public void calculate() {
        calculateStateProbabilities();
        loadCoefficients[0] = stateProbabilities[1] + stateProbabilities[3];
        loadCoefficients[1] = stateProbabilities[2] + stateProbabilities[3];
        denialProbability = 1 - (loadCoefficients[0] * App.m1 + loadCoefficients[1] * App.m2) / (App.l);
        averageTime = (stateProbabilities[1] + stateProbabilities[2] + 2. * stateProbabilities[3]) / (loadCoefficients[0] * App.m1 + loadCoefficients[1] * App.m2);
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
