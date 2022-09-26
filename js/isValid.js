/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let arr = [];
  const vars = { "(": ")", "{": "}", "[": "]" };
  const open = ["(", "{", "["];
  let last;

  for (let i = 0; i < s.length; i++) {
    if (open.includes(s[i])) {
      arr.push(s[i]);
    } else if (!open.includes(s[i])) {
      last = arr.pop();
      if (vars[last] !== s[i]) {
        return false;
      }
    } else {
      return true;
    }
  }
  return arr.length === 0;
};
