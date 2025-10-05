abstract class Algorithm {
    protected long comparisons = 0;
    protected long swaps = 0;

    public abstract void sort(int[] arr);

    public long getOperations() {
        return comparisons + swaps;
    }
}

class BubbleSort extends Algorithm {
    @Override
    public void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                comparisons++;
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swaps++;
                }
            }
        }
    }
}

class CPUSimulator {
    private double clockFactor; // higher => faster CPU

    public CPUSimulator(double clockFactor) {
        this.clockFactor = clockFactor;
    }

    public double simulate(Algorithm algo, int[] data) {
        long start = System.nanoTime();
        algo.sort(data.clone());
        long end = System.nanoTime();

        double baseTime = (end - start) / 1e9;
        double simulatedDelay = algo.getOperations() * (1e-6 / clockFactor);
        return baseTime + simulatedDelay;
    }
}

public class Main {
    public static void main(String[] args) {
        int[] arr = new java.util.Random().ints(1000, 0, 10000).toArray();
        BubbleSort bubble = new BubbleSort();
        CPUSimulator basic = new CPUSimulator(1.0);
        CPUSimulator pro = new CPUSimulator(3.0);

        double t1 = basic.simulate(bubble, arr);
        double t2 = pro.simulate(bubble, arr);

        System.out.println("Basic CPU: " + t1 + "s");
        System.out.println("Pro CPU: " + t2 + "s");
    }
}
