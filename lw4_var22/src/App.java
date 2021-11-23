public class App {
    public static final int STATE_COUNT = 4;
    public static final double l = 2.5;
    public static final double m = 2.0;
    public static final double m1 = 2.0 * m;
    public static final double m2 = m;

    public static void main(String[] args) {
        TheoreticalQS t = new TheoreticalQS();
        t.calculate();
        PracticalQS p = new PracticalQS();
        p.run();
        p.calculateValues();
        for (int i = 0; i < App.STATE_COUNT; i++) {
            System.out.println(
                    String.format("%6s", "P(" + (i % 2) + (i / 2) + ")") + "\t" +
                    String.format("%1.6f", t.getStateProbabilities()[i]) + "\t" +
                    String.format("%1.6f", p.getStateProbabilities()[i])
            );
        }
        for (int i = 0; i < 2; i++) {
            System.out.println(
                    String.format("%6s", "K(" + (i + 1) + ")") + "\t" +
                    String.format("%1.6f", t.getLoadCoefficients()[i]) + "\t" +
                    String.format("%1.6f", p.getLoadCoefficients()[i])
            );
        }
        System.out.println(
                String.format("%6s", "Potk") + "\t" +
                String.format("%1.6f", t.getDenialProbability()) + "\t" +
                String.format("%1.6f", p.getDenialProbability())
        );
        System.out.println(
                String.format("%6s", "Wc") + "\t" +
                String.format("%1.6f", t.getAverageTime()) + "\t" +
                String.format("%1.6f", p.getAverageTime())
        );
    }
}
