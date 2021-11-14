

function bubble_sort(array) {

  let i = 0;
  let j = 0;

  while (i < array.length) {
      j = i;
      while (j < array.length) {
        if (array[j] < array[j-1]) {
          let temp = array[j];
          array[j] = array[j-1];
          array[j-1] = temp;
        }
        j +=1;
      }
    i +=1;
  }
  return array;
}


