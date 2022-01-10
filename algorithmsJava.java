public class Algorithms {

    public static void main(String[] args) {
      
        int[] intArray = new int[]{2, 3, 4, 6, 7, 8, 9, 10};
        int result = secondLargestElement(intArray);
        System.out.println(result);

        double element = 1;
        double result2 = binarySearch(intArray, element);
        System.out.println(result2);

        double element2 = 5;
        double result3 = binarySearchIndex(intArray, element2);
        System.out.println(result3);

        //int[] intArray2 = new int[]{12, 1, 5, 0, 55, 8, 7, 10};
        //System.out.println(Arrays.toString(selectionSort(intArray2)));
    }

    public static int getMin(int[] array) {
      
        int currentMin = array[0];
      
        for (int i = 1; i < array.length; i++) {
            if (array[i] < currentMin) {
                currentMin = array[i];
            }
        }
        return currentMin;
    }

    public static int getMax(int[] array) {
      
        int currentMax = array[0];
      
        for (int i = 1; i < array.length; i++) {
            if (array[i] > currentMax) {
                currentMax = array[i];
            }
        }
        return currentMax;
    }

    public static int linearSearch(int[] array, int element) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == element) {
                return i;
            }
        }
        return -1;
    }

    public static int secondLargestElement(int[] array) {
      
        int largestElement = -1;
        int secondLargestElement = -1;
      
        if (array[0] < array[1]) {
            largestElement = array[1];
            secondLargestElement = array[0];
        }
      
        else {
            largestElement = array[0];
            secondLargestElement = array[1];
        }
      
        for (int i = 2; i < array.length; i++) {
          
            if (array[i] > secondLargestElement) {
                secondLargestElement = array[i];
              
                if (largestElement < secondLargestElement) {
                    int temp = secondLargestElement;
                    secondLargestElement = largestElement;
                    largestElement = temp;
                }
            }
        }
        return secondLargestElement;
    }

    public static double binarySearch(int[] array, double element) {

        double start = 0;
        double end = array.length;

        while (start <= end) {

            double mid = Math.floor((start+end)/2);
            int intMid = (int) mid;
            int intElement = (int) element;

            if (intElement == array[intMid]) {
                return intMid;
            }

            else if (intElement < array[intMid]) {
                end = mid - 1;
            }

            else {
                start = mid + 1;

            }
        }
        return -1;
    }

    public static double binarySearchIndex(int[] array, double element) {

        double start = 0;
        double end = array.length;

        while (start <= end) {

            double mid = Math.floor((start+end)/2);
            int intMid = (int) mid;
            int intElement = (int) element;

            if (intElement == array[intMid]) {
                return intMid;
            }

            else if (intElement < array[intMid]) {
                end = mid - 1;
            }

            else {
                start = mid + 1;

            }
        }
        return start;
    }

    public static int[] selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int[] newArray = Arrays.copyOfRange(array, i, array.length);
            int currentMin = getMin(newArray) + i;
            int temp = array[currentMin];
            array[currentMin] = array[i];
            array[i] = temp;
        }
        return array;
    }

    public static int[] insertionSortBinaryOptimized(int[] array) {
        return array;
    }


}
