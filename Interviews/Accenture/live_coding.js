
function createObject(stringToParse, valueToAssign) {
  const keys = stringToParse.split('.');
  const result = {};
  let current = result;
  console.log("Keys:", keys);
  console.log(`"Initial Result Object: ${JSON.stringify(result)}`);
  for (let i=0; i < keys.length; i++){
    const key = keys[i];
    console.log(`Current Key: ${key}`);
    if (i == keys.length -1){
      current[key] = valueToAssign;
    } else {
      current[key] = {};
      current = current[key];
    }
  }
  console.log(`Final Result Object: ${JSON.stringify(result)}`);
  return result;
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