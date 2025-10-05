#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef struct {
    long comparisons;
    long swaps;
} Stats;

void bubbleSort(int arr[], int n, Stats *stats) {
    stats->comparisons = stats->swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            stats->comparisons++;
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                stats->swaps++;
            }
        }
    }
}

double simulateCPU(Stats stats, double baseTime, double factor) {
    double delay = (stats.comparisons + stats.swaps) * (1e-6 / factor);
    return baseTime + delay;
}

int main() {
    int n = 1000;
    int *arr = malloc(n * sizeof(int));
    srand(time(NULL));
    for (int i = 0; i < n; i++) arr[i] = rand() % 10000;

    Stats stats;
    clock_t start = clock();
    bubbleSort(arr, n, &stats);
    clock_t end = clock();

    double baseTime = (double)(end - start) / CLOCKS_PER_SEC;
    double basic = simulateCPU(stats, baseTime, 1.0);
    double pro = simulateCPU(stats, baseTime, 3.0);

    printf("Bubble Sort Basic CPU: %.4fs\\n", basic);
    printf("Bubble Sort Pro CPU: %.4fs\\n", pro);
    printf("Ops: %ld\\n", stats.comparisons + stats.swaps);

    free(arr);
    return 0;
}
