function appendAndDelete(s, t, k) {
    let getMin = Math.min.apply(Math,[s.length, t.length]);
    let firstDiffPosition = getMin;

    for (let i = 0; i < getMin; i++) {
        if(s[i] != t[i]){
            firstDiffPosition = i
            break;
        }
    }
    let steps = s.length + t.length - 2 * firstDiffPosition;
    
    if((k>=steps && (k-steps)%2==0) ||  (k>= s.length + t.length) || (k == steps)) {
        return "Yes";
    }
    else {
        return "No";
    }

}