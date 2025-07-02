
function createObject(stringToParse, valueToAssign) {
  //to imlement
  // let finalObject = {};
  // let new_array = stringToParse.split(".");
  // console.log(new_array);
  // for (let i in new_array) {
  //   console.log("char:", new_array[i]);
  //   let char = new_array[i];
  //   finalObject[char] = {};
  // }
  // return finalObject;
}
console.log(createObject("a.b.c.d.e", 2));


//expected result below
/* {
  a: {
    b: {
      c: {
        d: {
          e: 2,
        }
      }
    }
  }
} */