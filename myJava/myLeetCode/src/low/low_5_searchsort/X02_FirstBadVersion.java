package low.low_5_searchsort;

public class X02_FirstBadVersion {
    boolean isBadVersion(int version) {
        return false;
    }

    public int firstBadVersion(int n) {
        int l = 1;
        int r = n;
        while (l!=r){
//            n = (r+l)/2;   用这个时间超过限制
            n = l+(r-l)/2;
            if (isBadVersion(n)){
                r = n;
            }else {
                l = n+1;
            }
        }
        return l;
    }
}
