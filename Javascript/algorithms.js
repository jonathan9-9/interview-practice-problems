// Binary search
function binarySearch(items, target) {

  let start = 0;
  let end = items.length - 1;
  while (start <= end) {
    let half = Math.floor((start + end) / 2);
    let value = items[half];

    if (target === value) {
      return value;
    } else if (target < value) {
      end = half - 1;
    } else {
      start = half + 1;
    }
  }

  return null;
}

// Bubble sort

function bubbleSort(items) {
  // know you have to have nested loop
  // inner loop: if left is bigger than right, swap and move to next index
  // outer loop: facilitating the inner loop running n number of times

  for (let i = 0; i < items.length; i++) {
    let sortedCheck = true;
    for (let j = 0; j < items.length - 1 - i; j++) {
      if (items[j] > items[j + 1]) {
        let temp = items[j];
        items[j] = items[j + 1];
        items[j + 1] = temp;
        sortedCheck = false;
        //   [items[j], items[j + 1]] = [items[j + 1], items[j]];
      }
    }
    if (sortedCheck) {
      return items;
    }
  }
  return items;
}

// Selection sort

function selectionSort(items) {
  // outerloop: doing inner loop multiple times,
  // and swapping the smallest element found to the next smallest spot
  for (let i = 0; i < items.length; i++) {
    let minValue = items[i];
    let minIndex = i;

    // inner loop: finding the smallest element remaining
    for (let j = i + 1; j < items.length; j++) {
      // if we find a new smallest, track it
      if (items[j] < minValue) {
        minValue = items[j];
        minIndex = j;
      }
    }

    // swap the next smallest value (minIndex) to the right spot (i)
    let temp = items[i];
    items[i] = minValue;
    items[minIndex] = temp;
  }
  return items;
}

// QUICK SORT

function partition(values, left, right) {
  const pivot = values[right];
  let star = left;
  for (let i = left; i < right; i += 1){

      if (values[i] < pivot ){
          [values[star], values[i]] = [values[i], values[star]];
          star += 1;
      }

  }
  [values[star], values[right]] = [values[right], values[star]];
  return star;
}

function quicksort(values, left=null, right=null) {
  if (left === null && right === null ){

      left = 0;
      right = values.length - 1;
  }
  if (left >= right || values.length < 0){
      return;
  }
  const pivot = partition(values, left, right);
  quicksort(values, left, pivot - 1);
  quicksort(values, pivot + 1, right);
}

// MERGE SORT

function merge(left, right) {
  let leftIndex = 0;
  let rightIndex = 0;
  const sortedList = [];

  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      sortedList.push(left[leftIndex]);
      leftIndex++;
    } else {
      sortedList.push(right[rightIndex]);
      rightIndex++;
    }
  }

  // Append the remaining items into sortedList
  while (leftIndex < left.length) {
    sortedList.push(left[leftIndex]);
    leftIndex++;
  }

  while (rightIndex < right.length) {
    sortedList.push(right[rightIndex]);
    rightIndex++;
  }

  return sortedList;
}

function mergeSort(list) {
  if (list.length <= 1) {
    return list;
  }

  const mid = Math.floor(list.length / 2);
  const left = mergeSort(list.slice(0, mid));
  const right = mergeSort(list.slice(mid));

  // Returns the sorted merged left and right
  return merge(left, right);
}

console.log(mergeSort([4, 1, 5, 9, 2, 6, 7]));
console.log(mergeSort([3, 7, 1, 4, 2, 6]));
