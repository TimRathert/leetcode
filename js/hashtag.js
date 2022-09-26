function generateHashtag (str){
    if (str.length == 0) {return false;}
    else{
//capitalize first letter of each string
    let hashtag = str.replace(/\w\S*/g, function (txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    }).split(` `);
    hashtag.splice(0,0,`#`)
if(hashtag.join('').length > 140 || hashtag.length < 1){return false}
else {return hashtag.join('')}
    }
}




//.join(``)

    




generateHashtag("Codewars is nice")
generateHashtag("")