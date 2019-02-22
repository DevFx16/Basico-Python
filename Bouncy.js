function Cre(Num){
    r = false;
    for (let index = 0; index < Num.length; index++) {
        if(Num[index] < Num[index + 1]){
            if(index + 1 == Num.length - 1){
                r = true;
                break;
            }
        }
    }
    return r;
}

console.log(Cre('123'))