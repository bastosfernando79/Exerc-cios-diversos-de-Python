function romanToInt(s) {
  const su = s.toUpperCase();

  const romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

  function converToInt(su) {
    return romanValues[su];    
  }

  const values = Array.from(su).map(converToInt);
  let decimal = 0;

  for (let i = 0; i < values.length - 1; i++) {
    if (values[i] < values[i+1]) {
      decimal -= values[i];
    } else {
      decimal += values[i];
    }
  }

  decimal += values[values.length - 1];

  return decimal;
}

const result = romanToInt('XXVI');
console.log(result);
