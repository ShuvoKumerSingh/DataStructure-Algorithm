'''
Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.
'''
'''
Examples

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
 
collectStrings(obj) # ['foo', 'bar', 'baz']
'''
#Code
def collectStrings(obj):
    new_dic=[]
    for key in obj:
        if type(obj[key]) == dict:
            new_dic.extend(collectStrings(obj[key]))
        elif type(obj[key])is str:
            new_dic.append(obj[key])
    return new_dic