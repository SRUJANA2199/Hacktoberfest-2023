def rotate_array(arr, n, k):
    # Rotate the array to the right by k positions
    k = k % n  # To handle cases where k is greater than n
    arr[:] = arr[-k:] + arr[:-k]

def main():
    # Input array elements from the user
    arr = list(map(int, input("Enter array elements separated by space: ").split()))

    # Input rotation count from the user
    k = int(input("Enter the rotation count: "))

    # Display the original array
    print("Original Array:", arr)

    # Rotate the array
    rotate_array(arr, len(arr), k)

    # Display the rotated array
    print("Rotated Array:", arr)

if __name__ == "__main__":
    main()
