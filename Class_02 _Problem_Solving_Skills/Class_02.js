// Write a function which takes a string and returns counts of
// each character in the string


function charCount(str) {
    //object to return
    var output={}
    //loop through
    for (var iCount=0; iCount<str.length; iCount++) {
        //lowercase
        var char=str[i].toLowerCase()
        //check alphanumeric
        if(/[a-z0-9]/.test(char))
            if (XPathResult.hasOwnProperty(char) {
                output[char]+=1
            }
            // if in it, add count
            else {
                output[char]=1
            }
            // else add to object
            }   

            //result[char] ? result[char]+=1 :result[char]=1
    //return results
    return output
}

charCount('hello') //{h:1. e:1, l:2, o:1}
charCount('')  //{}
charCount('Hello') //{h:1. e:1, l:2, o:1}
charCount('Hello World!') //{h:1. e:1, l:3, o:2, w:1, r:1, d:1}